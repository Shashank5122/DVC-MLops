"""Workspace (tenant) endpoints.

Bootstrap over HTTP is a development convenience and is disabled unless
SIGNALGEO_ENVIRONMENT=development. In production, workspaces are created by an operator via
`python -m scripts.bootstrap_workspace`.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.domain import slugify
from app.core.errors import AuthorizationError, ConflictError
from app.core.logging import get_logger
from app.core.tenancy import resolve_workspace
from app.db.models import (
    Brand,
    Workspace,
    WorkspaceStatus,
    generate_workspace_key,
    hash_workspace_key,
)
from app.db.session import session_dependency
from app.schemas.workspace import WorkspaceCreate, WorkspaceCreated, WorkspaceRead
from app.services import audit

logger = get_logger(__name__)
router = APIRouter(tags=["workspaces"])


@router.get("/workspaces/me", response_model=WorkspaceRead, summary="Current workspace")
def read_current_workspace(
    workspace: Workspace = Depends(resolve_workspace),
) -> Workspace:
    return workspace


@router.post(
    "/dev/workspaces",
    response_model=WorkspaceCreated,
    status_code=201,
    summary="Create a workspace (development only)",
)
def bootstrap_workspace(
    payload: WorkspaceCreate,
    session: Session = Depends(session_dependency),
    settings: Settings = Depends(get_settings),
) -> WorkspaceCreated:
    if not settings.dev_bootstrap_enabled:
        raise AuthorizationError(
            "Workspace bootstrap over HTTP is disabled outside development",
            details={"environment": settings.environment},
        )

    slug = payload.slug.strip().lower() if payload.slug else slugify(payload.name, max_length=80)
    if session.scalar(select(Workspace).where(Workspace.slug == slug)) is not None:
        raise ConflictError("A workspace with this slug already exists")

    plain_key = generate_workspace_key()
    workspace = Workspace(
        name=payload.name.strip(),
        slug=slug,
        key_hash=hash_workspace_key(plain_key),
        key_last4=plain_key[-4:],
        status=WorkspaceStatus.active,
        notes=payload.notes,
    )
    session.add(workspace)
    session.flush()
    audit.record(
        session,
        workspace_id=workspace.id,
        action="workspace.created",
        entity_type="workspace",
        entity_id=workspace.id,
        actor="dev-bootstrap",
        changes={"slug": workspace.slug},
    )
    session.flush()
    logger.info("workspace_created", extra={"workspace_slug": workspace.slug})
    # The plaintext key is returned exactly once and is never stored.
    return WorkspaceCreated(
        workspace=WorkspaceRead.model_validate(workspace), workspace_key=plain_key
    )


@router.get("/workspaces/me/stats", summary="Counts for the current workspace")
def workspace_stats(
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> dict[str, int | str]:
    brand_count = session.scalar(
        select(func.count())
        .select_from(Brand)
        .where(Brand.workspace_id == workspace.id, Brand.deleted_at.is_(None))
    )
    return {"workspace": workspace.slug, "brands": int(brand_count or 0)}
