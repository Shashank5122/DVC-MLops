"""M1 data model: workspaces (tenants), brands, competitors and audit events.

The measurement model required by the founder's brief (observations, query registry,
evidence, extraction metadata, grounding status, costs) lands in M2. It is intentionally NOT
stubbed here: half-built tables are worse than no tables.

Isolation rules enforced at the schema level:
* every tenant-owned row carries workspace_id (NOT NULL, indexed, FK -> workspaces.id)
* uniqueness is per workspace, never global (a brand name may exist in two workspaces)
"""

from __future__ import annotations

import enum
import hashlib
import secrets
import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import JSON, Uuid

from app.db.base import Base, TimestampMixin, new_uuid, utcnow

# Variant keeps JSONB on PostgreSQL and JSON elsewhere, without branching in every model.
JSONType = JSON().with_variant(JSONB(), "postgresql")


class WorkspaceStatus(enum.StrEnum):
    active = "active"
    suspended = "suspended"


class FactVerificationStatus(enum.StrEnum):
    """Whether the business facts behind a brand's claims have been verified.

    Integrity rule 9: no published claim without a traced, verified business fact. The status
    lives on the record so a report can never be generated for an unverified brand by accident.
    """

    unverified = "unverified"
    in_progress = "in_progress"
    verified = "verified"


class CompetitorRelationship(enum.StrEnum):
    direct = "direct"
    indirect = "indirect"
    alternative = "alternative"
    incumbent = "incumbent"


def hash_workspace_key(plain_key: str) -> str:
    """Workspace keys are stored only as SHA-256 hashes."""
    return hashlib.sha256(plain_key.encode("utf-8")).hexdigest()


def generate_workspace_key() -> str:
    """Return a new URL-safe workspace key. Shown exactly once, at creation."""
    return f"sg_{secrets.token_urlsafe(32)}"


class Workspace(Base, TimestampMixin):
    """A tenant. For the pilot a workspace is a client company (or our own test workspace)."""

    __tablename__ = "workspaces"

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), primary_key=True, default=new_uuid)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(80), nullable=False, unique=True, index=True)
    # Only the hash is persisted; the plaintext key is returned once at bootstrap.
    key_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True)
    key_last4: Mapped[str] = mapped_column(String(4), nullable=False, default="")
    status: Mapped[WorkspaceStatus] = mapped_column(
        Enum(WorkspaceStatus, native_enum=False, length=20),
        default=WorkspaceStatus.active,
        nullable=False,
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    brands: Mapped[list[Brand]] = relationship(
        back_populates="workspace", cascade="all, delete-orphan", passive_deletes=True
    )

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"<Workspace {self.slug} id={self.id}>"


class Brand(Base, TimestampMixin):
    """The company whose AI-search visibility is being measured."""

    __tablename__ = "brands"
    __table_args__ = (
        UniqueConstraint("workspace_id", "slug", name="brand_workspace_slug"),
        UniqueConstraint("workspace_id", "normalised_domain", name="brand_workspace_domain"),
        Index("ix_brand_workspace_active", "workspace_id", "deleted_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), primary_key=True, default=new_uuid)
    workspace_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), nullable=False)
    website: Mapped[str | None] = mapped_column(String(300), nullable=True)
    normalised_domain: Mapped[str | None] = mapped_column(String(255), nullable=True)
    category: Mapped[str | None] = mapped_column(String(200), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    primary_language: Mapped[str] = mapped_column(String(16), nullable=False, default="en")
    primary_region: Mapped[str] = mapped_column(String(16), nullable=False, default="US")

    # Integrity scaffolding, present from the first table rather than bolted on later.
    fact_verification_status: Mapped[FactVerificationStatus] = mapped_column(
        Enum(FactVerificationStatus, native_enum=False, length=20),
        default=FactVerificationStatus.unverified,
        nullable=False,
    )
    # Explicit, revocable authorization is required before anything touches a client website
    # (integrity rule 15). M1 records the flag; M3 workflow enforces it.
    website_change_authorized: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    data_retention_permitted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None
    )

    workspace: Mapped[Workspace] = relationship(back_populates="brands")
    competitors: Mapped[list[Competitor]] = relationship(
        back_populates="brand", cascade="all, delete-orphan", passive_deletes=True
    )


class Competitor(Base, TimestampMixin):
    """A competitor tracked for a brand, used as the comparison set in measurement."""

    __tablename__ = "competitors"
    __table_args__ = (
        UniqueConstraint("brand_id", "slug", name="competitor_brand_slug"),
        Index("ix_competitor_workspace", "workspace_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), primary_key=True, default=new_uuid)
    workspace_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
    )
    brand_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        ForeignKey("brands.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), nullable=False)
    website: Mapped[str | None] = mapped_column(String(300), nullable=True)
    normalised_domain: Mapped[str | None] = mapped_column(String(255), nullable=True)
    relationship_type: Mapped[CompetitorRelationship] = mapped_column(
        Enum(CompetitorRelationship, native_enum=False, length=20),
        default=CompetitorRelationship.direct,
        nullable=False,
    )
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    brand: Mapped[Brand] = relationship(back_populates="competitors")


class AuditEvent(Base):
    """Append-only record of who changed what. Never updated, never deleted by the app."""

    __tablename__ = "audit_events"
    __table_args__ = (Index("ix_audit_workspace_created", "workspace_id", "created_at"),)

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), primary_key=True, default=new_uuid)
    workspace_id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        ForeignKey("workspaces.id", ondelete="CASCADE"),
        nullable=False,
    )
    actor: Mapped[str] = mapped_column(String(120), nullable=False, default="system")
    action: Mapped[str] = mapped_column(String(80), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(60), nullable=False)
    entity_id: Mapped[uuid.UUID | None] = mapped_column(Uuid(), nullable=True)
    changes: Mapped[dict[str, Any]] = mapped_column(JSONType, nullable=False, default=dict)
    correlation_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=utcnow, index=False
    )
