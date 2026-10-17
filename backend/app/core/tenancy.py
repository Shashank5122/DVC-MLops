"""Workspace (tenant) resolution.

Pilot-grade by design and documented as such: a workspace key in a header identifies the
tenant. There are no user accounts, roles, sessions or SSO. What IS enforced here, and tested,
is the boundary that matters most: a request can only ever read or write rows belonging to the
workspace its key resolves to.
"""

from __future__ import annotations

import uuid

from fastapi import Depends, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.errors import AuthenticationError, AuthorizationError
from app.db.models import Workspace, WorkspaceStatus, hash_workspace_key
from app.db.session import session_dependency


def resolve_workspace(
    request: Request,
    session: Session = Depends(session_dependency),
    settings: Settings = Depends(get_settings),
) -> Workspace:
    """Resolve and validate the workspace for this request.

    Raises:
        AuthenticationError: header missing or key unknown.
        AuthorizationError: workspace suspended.
    """
    raw_key = request.headers.get(settings.workspace_header)
    if not raw_key or not raw_key.strip():
        raise AuthenticationError(
            f"Missing {settings.workspace_header} header",
            details={"hint": "create a workspace with `make bootstrap` or the dev endpoint"},
        )
    statement = select(Workspace).where(Workspace.key_hash == hash_workspace_key(raw_key.strip()))
    workspace = session.scalar(statement)
    if workspace is None:
        # Do not reveal whether the key exists or is merely wrong.
        raise AuthenticationError("Invalid workspace key")
    if workspace.status is not WorkspaceStatus.active:
        raise AuthorizationError(
            "Workspace is not active", details={"status": workspace.status.value}
        )
    return workspace


WorkspaceDep = Depends(resolve_workspace)


def workspace_id_of(workspace: Workspace) -> uuid.UUID:
    return workspace.id
