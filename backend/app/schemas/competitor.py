"""Competitor schemas."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.db.models import CompetitorRelationship
from app.schemas.common import ORMModel


class CompetitorCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=200)
    website: str | None = Field(default=None, max_length=300)
    relationship_type: CompetitorRelationship = CompetitorRelationship.direct
    notes: str | None = Field(default=None, max_length=2000)


class CompetitorUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=2, max_length=200)
    website: str | None = Field(default=None, max_length=300)
    relationship_type: CompetitorRelationship | None = None
    notes: str | None = Field(default=None, max_length=2000)


class CompetitorRead(ORMModel):
    id: UUID
    brand_id: UUID
    name: str
    slug: str
    website: str | None = None
    normalised_domain: str | None = None
    relationship_type: CompetitorRelationship
    notes: str | None = None
    created_at: datetime
    updated_at: datetime
