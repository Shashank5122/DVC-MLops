"""Workspace schemas. The plaintext key is returned only on creation."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.db.models import WorkspaceStatus
from app.schemas.common import ORMModel


class WorkspaceCreate(BaseModel):
    """Development bootstrap payload. Disabled unless environment == development."""

    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=2, max_length=200, examples=["Acme Analytics"])
    slug: str | None = Field(
        default=None, max_length=80, description="Auto-derived from name when omitted"
    )
    notes: str | None = Field(default=None, max_length=2000)


class WorkspaceRead(ORMModel):
    id: UUID
    name: str
    slug: str
    status: WorkspaceStatus
    key_last4: str
    notes: str | None = None
    created_at: datetime


class WorkspaceCreated(BaseModel):
    """Returned once, at creation. The plaintext key is never stored or retrievable again."""

    workspace: WorkspaceRead
    workspace_key: str = Field(
        description="Send as the X-Workspace-Key header. Shown exactly once."
    )
