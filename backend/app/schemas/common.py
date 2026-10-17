"""Shared API response schemas."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ORMModel(BaseModel):
    """Base for response models read from SQLAlchemy objects."""

    model_config = ConfigDict(from_attributes=True, frozen=True)


class Page(BaseModel, Generic[T]):
    """A simple, explicit pagination envelope (no cursor tricks in M1)."""

    items: list[T]
    total: int = Field(ge=0)
    limit: int = Field(ge=1, le=200)
    offset: int = Field(ge=0)


class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    database: str
    provider_calls_enabled: bool = Field(
        description="Hard kill-switch. False in M1: no external provider calls are made anywhere."
    )


class AuditEventRead(ORMModel):
    id: UUID
    action: str
    entity_type: str
    entity_id: UUID | None = None
    actor: str
    changes: dict[str, Any] = Field(default_factory=dict)
    correlation_id: str | None = None
    created_at: datetime
