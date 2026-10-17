"""Brand and competitor operations, always scoped to a single workspace.

Every public function takes `workspace_id` explicitly and filters by it. There is no code path
that reads a brand without a workspace predicate - that is the tenancy boundary, and it is
covered by tests/test_tenancy_isolation.py.
"""

from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy import Select, func, select
from sqlalchemy.orm import Session, selectinload

from app.core.domain import normalise_domain, require_non_blank, slugify
from app.core.errors import ConflictError, NotFoundError, ValidationError
from app.db.models import Brand, Competitor, CompetitorRelationship, FactVerificationStatus
from app.schemas.brand import BrandCreate, BrandUpdate
from app.schemas.competitor import CompetitorCreate, CompetitorUpdate
from app.services import audit


def _brand_query(workspace_id: uuid.UUID) -> Select[tuple[Brand]]:
    """Base query: workspace-scoped, excluding soft-deleted rows."""
    return select(Brand).where(Brand.workspace_id == workspace_id, Brand.deleted_at.is_(None))


def _get_brand_or_404(session: Session, workspace_id: uuid.UUID, brand_id: uuid.UUID) -> Brand:
    brand = session.scalar(_brand_query(workspace_id).where(Brand.id == brand_id))
    if brand is None:
        raise NotFoundError("Brand not found", details={"brand_id": str(brand_id)})
    return brand


def _unique_slug(
    session: Session, workspace_id: uuid.UUID, base: str, *, exclude_id: uuid.UUID | None = None
) -> str:
    """Return a slug unique within the workspace, suffixing on collision."""
    candidate = base
    suffix = 2
    while True:
        statement = _brand_query(workspace_id).where(Brand.slug == candidate)
        if exclude_id is not None:
            statement = statement.where(Brand.id != exclude_id)
        if session.scalar(statement) is None:
            return candidate
        candidate = f"{base}-{suffix}"
        suffix += 1
        if suffix > 500:  # pathological input guard
            raise ConflictError("Could not derive a unique brand slug")


def create_brand(
    session: Session, *, workspace_id: uuid.UUID, payload: BrandCreate, actor: str = "api"
) -> Brand:
    name = require_non_blank(payload.name, field="name")
    domain = normalise_domain(payload.website)

    duplicate = session.scalar(
        _brand_query(workspace_id).where(func.lower(Brand.name) == name.lower())
    )
    if duplicate is not None:
        raise ConflictError("A brand with this name already exists in the workspace")
    if domain is not None:
        existing_domain = session.scalar(
            _brand_query(workspace_id).where(Brand.normalised_domain == domain)
        )
        if existing_domain is not None:
            raise ConflictError(
                "A brand with this website domain already exists in the workspace",
                details={"domain": domain},
            )

    brand = Brand(
        workspace_id=workspace_id,
        name=name,
        slug=_unique_slug(session, workspace_id, slugify(name)),
        website=payload.website.strip() if payload.website else None,
        normalised_domain=domain,
        category=payload.category.strip() if payload.category else None,
        description=payload.description.strip() if payload.description else None,
        primary_language=payload.primary_language or "en",
        primary_region=payload.primary_region or "US",
        fact_verification_status=FactVerificationStatus.unverified,
    )
    session.add(brand)
    session.flush()  # populate brand.id before children and audit rows

    for item in payload.competitors:
        session.add(
            _build_competitor(session, workspace_id=workspace_id, brand_id=brand.id, payload=item)
        )

    audit.record(
        session,
        workspace_id=workspace_id,
        action="brand.created",
        entity_type="brand",
        entity_id=brand.id,
        actor=actor,
        changes={
            "name": brand.name,
            "slug": brand.slug,
            "normalised_domain": brand.normalised_domain,
            "competitors": [item.name for item in payload.competitors],
        },
    )
    session.flush()
    return brand


def list_brands(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    limit: int = 50,
    offset: int = 0,
    search: str | None = None,
) -> tuple[list[Brand], int]:
    statement = _brand_query(workspace_id)
    count_statement = (
        select(func.count())
        .select_from(Brand)
        .where(Brand.workspace_id == workspace_id, Brand.deleted_at.is_(None))
    )
    if search:
        pattern = f"%{search.strip().lower()}%"
        statement = statement.where(func.lower(Brand.name).like(pattern))
        count_statement = count_statement.where(func.lower(Brand.name).like(pattern))

    total = session.scalar(count_statement) or 0
    rows = session.scalars(
        statement.order_by(Brand.created_at.desc()).limit(limit).offset(offset)
    ).all()
    return list(rows), int(total)


def get_brand(session: Session, *, workspace_id: uuid.UUID, brand_id: uuid.UUID) -> Brand:
    brand = session.scalar(
        _brand_query(workspace_id)
        .options(selectinload(Brand.competitors))
        .where(Brand.id == brand_id)
    )
    if brand is None:
        raise NotFoundError("Brand not found", details={"brand_id": str(brand_id)})
    return brand


def count_brands(session: Session, *, workspace_id: uuid.UUID) -> int:
    return int(
        session.scalar(
            select(func.count())
            .select_from(Brand)
            .where(Brand.workspace_id == workspace_id, Brand.deleted_at.is_(None))
        )
        or 0
    )


def update_brand(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    brand_id: uuid.UUID,
    payload: BrandUpdate,
    actor: str = "api",
) -> Brand:
    brand = _get_brand_or_404(session, workspace_id, brand_id)
    changes: dict[str, Any] = {}
    # mode="json" so enum fields arrive as their string values, not enum instances.
    data = payload.model_dump(exclude_unset=True, mode="json")

    if not data:
        raise ValidationError("No fields to update")

    if "name" in data and data["name"] is not None:
        new_name = require_non_blank(data["name"], field="name")
        if new_name.lower() != brand.name.lower():
            clash = session.scalar(
                _brand_query(workspace_id).where(
                    func.lower(Brand.name) == new_name.lower(), Brand.id != brand.id
                )
            )
            if clash is not None:
                raise ConflictError("A brand with this name already exists in the workspace")
            changes["name"] = {"from": brand.name, "to": new_name}
            brand.name = new_name
            brand.slug = _unique_slug(session, workspace_id, slugify(new_name), exclude_id=brand.id)

    if "website" in data:
        domain = normalise_domain(data["website"])
        if domain != brand.normalised_domain:
            if domain is not None:
                clash = session.scalar(
                    _brand_query(workspace_id).where(
                        Brand.normalised_domain == domain, Brand.id != brand.id
                    )
                )
                if clash is not None:
                    raise ConflictError("Another brand in this workspace already uses that domain")
            changes["website"] = {"from": brand.website, "to": data["website"]}
            brand.website = data["website"].strip() if data["website"] else None
            brand.normalised_domain = domain

    for field in ("category", "description", "primary_language", "primary_region"):
        if field in data and data[field] is not None:
            new_value = data[field].strip() if isinstance(data[field], str) else data[field]
            if new_value != getattr(brand, field):
                changes[field] = {"from": getattr(brand, field), "to": new_value}
                setattr(brand, field, new_value)

    # Authorization and verification flags are the security-relevant ones: always audited.
    for field in (
        "fact_verification_status",
        "website_change_authorized",
        "data_retention_permitted",
    ):
        if field in data and data[field] is not None:
            new_value = data[field]
            if isinstance(new_value, str):
                new_value = FactVerificationStatus(new_value)
            if new_value != getattr(brand, field):
                changes[field] = {
                    "from": getattr(brand, field).value
                    if isinstance(getattr(brand, field), FactVerificationStatus)
                    else getattr(brand, field),
                    "to": new_value.value
                    if isinstance(new_value, FactVerificationStatus)
                    else new_value,
                }
                setattr(brand, field, new_value)

    if not changes:
        raise ValidationError("No effective changes supplied")

    audit.record(
        session,
        workspace_id=workspace_id,
        action="brand.updated",
        entity_type="brand",
        entity_id=brand.id,
        actor=actor,
        changes=changes,
    )
    session.flush()
    return brand


def soft_delete_brand(
    session: Session, *, workspace_id: uuid.UUID, brand_id: uuid.UUID, actor: str = "api"
) -> None:
    """Soft delete: measurement history must remain auditable, so rows are never hard-deleted."""
    from app.db.base import utcnow

    brand = _get_brand_or_404(session, workspace_id, brand_id)
    brand.deleted_at = utcnow()
    audit.record(
        session,
        workspace_id=workspace_id,
        action="brand.deleted",
        entity_type="brand",
        entity_id=brand.id,
        actor=actor,
        changes={"name": brand.name, "mode": "soft"},
    )
    session.flush()


# --- competitors -------------------------------------------------------------


def _build_competitor(
    session: Session, *, workspace_id: uuid.UUID, brand_id: uuid.UUID, payload: CompetitorCreate
) -> Competitor:
    name = require_non_blank(payload.name, field="competitor name")
    domain = normalise_domain(payload.website)
    relationship_type = (
        payload.relationship_type
        if isinstance(payload.relationship_type, CompetitorRelationship)
        else CompetitorRelationship(str(payload.relationship_type))
    )
    return Competitor(
        workspace_id=workspace_id,
        brand_id=brand_id,
        name=name,
        slug=slugify(name),
        website=payload.website.strip() if payload.website else None,
        normalised_domain=domain,
        relationship_type=relationship_type,
        notes=payload.notes.strip() if payload.notes else None,
    )


def list_competitors(
    session: Session, *, workspace_id: uuid.UUID, brand_id: uuid.UUID
) -> list[Competitor]:
    _get_brand_or_404(session, workspace_id, brand_id)
    rows = session.scalars(
        select(Competitor)
        .where(Competitor.workspace_id == workspace_id, Competitor.brand_id == brand_id)
        .order_by(Competitor.name)
    ).all()
    return list(rows)


def add_competitor(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    brand_id: uuid.UUID,
    payload: CompetitorCreate,
    actor: str = "api",
) -> Competitor:
    _get_brand_or_404(session, workspace_id, brand_id)
    name = require_non_blank(payload.name, field="competitor name")
    clash = session.scalar(
        select(Competitor).where(
            Competitor.brand_id == brand_id,
            Competitor.workspace_id == workspace_id,
            func.lower(Competitor.name) == name.lower(),
        )
    )
    if clash is not None:
        raise ConflictError("That competitor is already tracked for this brand")
    competitor = _build_competitor(
        session, workspace_id=workspace_id, brand_id=brand_id, payload=payload
    )
    session.add(competitor)
    session.flush()
    audit.record(
        session,
        workspace_id=workspace_id,
        action="competitor.added",
        entity_type="competitor",
        entity_id=competitor.id,
        actor=actor,
        changes={"brand_id": str(brand_id), "name": competitor.name},
    )
    session.flush()
    return competitor


def update_competitor(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    brand_id: uuid.UUID,
    competitor_id: uuid.UUID,
    payload: CompetitorUpdate,
    actor: str = "api",
) -> Competitor:
    competitor = session.scalar(
        select(Competitor).where(
            Competitor.id == competitor_id,
            Competitor.brand_id == brand_id,
            Competitor.workspace_id == workspace_id,
        )
    )
    if competitor is None:
        raise NotFoundError("Competitor not found", details={"competitor_id": str(competitor_id)})

    # mode="json" so enum fields arrive as their string values, not enum instances.
    data = payload.model_dump(exclude_unset=True, mode="json")
    if not data:
        raise ValidationError("No fields to update")
    changes: dict[str, Any] = {}

    if data.get("name"):
        new_name = require_non_blank(data["name"], field="competitor name")
        if new_name.lower() != competitor.name.lower():
            changes["name"] = {"from": competitor.name, "to": new_name}
            competitor.name = new_name
            competitor.slug = slugify(new_name)
    if "website" in data:
        domain = normalise_domain(data["website"])
        if domain != competitor.normalised_domain:
            changes["website"] = {"from": competitor.website, "to": data["website"]}
            competitor.website = data["website"].strip() if data["website"] else None
            competitor.normalised_domain = domain
    if data.get("relationship_type"):
        new_rel = CompetitorRelationship(str(data["relationship_type"]))
        if new_rel != competitor.relationship_type:
            changes["relationship_type"] = {
                "from": competitor.relationship_type.value,
                "to": new_rel.value,
            }
            competitor.relationship_type = new_rel
    if "notes" in data and data["notes"] is not None:
        changes["notes"] = {"changed": True}
        competitor.notes = data["notes"].strip()

    if not changes:
        raise ValidationError("No effective changes supplied")

    audit.record(
        session,
        workspace_id=workspace_id,
        action="competitor.updated",
        entity_type="competitor",
        entity_id=competitor.id,
        actor=actor,
        changes=changes,
    )
    session.flush()
    return competitor


def remove_competitor(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    brand_id: uuid.UUID,
    competitor_id: uuid.UUID,
    actor: str = "api",
) -> None:
    competitor = session.scalar(
        select(Competitor).where(
            Competitor.id == competitor_id,
            Competitor.brand_id == brand_id,
            Competitor.workspace_id == workspace_id,
        )
    )
    if competitor is None:
        raise NotFoundError("Competitor not found", details={"competitor_id": str(competitor_id)})
    name = competitor.name
    session.delete(competitor)
    audit.record(
        session,
        workspace_id=workspace_id,
        action="competitor.removed",
        entity_type="competitor",
        entity_id=competitor_id,
        actor=actor,
        changes={"brand_id": str(brand_id), "name": name},
    )
    session.flush()
