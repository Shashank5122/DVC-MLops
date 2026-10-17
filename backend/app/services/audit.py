"""Audit trail. Append-only: the service exposes record(), never update() or delete()."""

from __future__ import annotations

import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.logging import correlation_id_var
from app.db.models import AuditEvent


def record(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    action: str,
    entity_type: str,
    entity_id: uuid.UUID | None = None,
    actor: str = "api",
    changes: dict[str, Any] | None = None,
) -> AuditEvent:
    """Append an audit event. The caller's transaction commits it (single unit of work)."""
    event = AuditEvent(
        workspace_id=workspace_id,
        actor=actor,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        changes=changes or {},
        correlation_id=correlation_id_var.get(),
    )
    session.add(event)
    return event


def list_events(
    session: Session,
    *,
    workspace_id: uuid.UUID,
    entity_type: str | None = None,
    entity_id: uuid.UUID | None = None,
    limit: int = 50,
    offset: int = 0,
) -> tuple[list[AuditEvent], int]:
    """Read the audit trail, always scoped to one workspace."""
    conditions = [AuditEvent.workspace_id == workspace_id]
    if entity_type is not None:
        conditions.append(AuditEvent.entity_type == entity_type)
    if entity_id is not None:
        conditions.append(AuditEvent.entity_id == entity_id)

    from sqlalchemy import func

    total = session.scalar(select(func.count()).select_from(AuditEvent).where(*conditions)) or 0
    rows = session.scalars(
        select(AuditEvent)
        .where(*conditions)
        .order_by(AuditEvent.created_at.desc(), AuditEvent.id.desc())
        .limit(limit)
        .offset(offset)
    ).all()
    return list(rows), int(total)
