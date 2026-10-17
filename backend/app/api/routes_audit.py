"""Audit trail reads, always workspace-scoped."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.tenancy import resolve_workspace
from app.db.models import Workspace
from app.db.session import session_dependency
from app.schemas.common import AuditEventRead, Page
from app.services import audit

router = APIRouter(prefix="/audit-events", tags=["audit"])


@router.get("", response_model=Page[AuditEventRead], summary="List audit events")
def list_audit_events(
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
    entity_type: str | None = Query(default=None, max_length=60),
    entity_id: uuid.UUID | None = None,
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
) -> Page[AuditEventRead]:
    rows, total = audit.list_events(
        session,
        workspace_id=workspace.id,
        entity_type=entity_type,
        entity_id=entity_id,
        limit=limit,
        offset=offset,
    )
    return Page[AuditEventRead](
        items=[AuditEventRead.model_validate(row) for row in rows],
        total=total,
        limit=limit,
        offset=offset,
    )
