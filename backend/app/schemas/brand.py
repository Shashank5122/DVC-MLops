"""Brand request/response schemas (M1: brand onboarding)."""

from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.db.models import FactVerificationStatus
from app.schemas.common import ORMModel
from app.schemas.competitor import CompetitorCreate, CompetitorRead


class BrandCreate(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=200)
    website: str | None = Field(default=None, max_length=300)
    category: str | None = Field(default=None, max_length=200)
    description: str | None = Field(default=None, max_length=4000)
    primary_language: str = Field(default="en", min_length=2, max_length=16)
    primary_region: str = Field(default="US", min_length=2, max_length=16)
    competitors: list[CompetitorCreate] = Field(default_factory=list, max_length=25)

    @field_validator("primary_region")
    @classmethod
    def _region_upper(cls, value: str) -> str:
        return value.upper()

    @field_validator("competitors")
    @classmethod
    def _no_duplicate_competitors(cls, value: list[CompetitorCreate]) -> list[CompetitorCreate]:
        names = [item.name.casefold() for item in value]
        if len(names) != len(set(names)):
            raise ValueError("competitors contains duplicate names")
        return value


class BrandUpdate(BaseModel):
    """Partial update. `extra='forbid'` keeps typos from being silently ignored."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=2, max_length=200)
    website: str | None = Field(default=None, max_length=300)
    category: str | None = Field(default=None, max_length=200)
    description: str | None = Field(default=None, max_length=4000)
    primary_language: str | None = Field(default=None, min_length=2, max_length=16)
    primary_region: str | None = Field(default=None, min_length=2, max_length=16)
    fact_verification_status: FactVerificationStatus | None = None
    website_change_authorized: bool | None = None
    data_retention_permitted: bool | None = None


class BrandRead(ORMModel):
    id: UUID
    name: str
    slug: str
    website: str | None = None
    normalised_domain: str | None = None
    category: str | None = None
    description: str | None = None
    primary_language: str
    primary_region: str
    fact_verification_status: FactVerificationStatus
    website_change_authorized: bool
    data_retention_permitted: bool
    created_at: datetime
    updated_at: datetime


class BrandDetail(BrandRead):
    competitors: list[CompetitorRead] = Field(default_factory=list)
    competitor_count: int = 0


BrandCreate.model_rebuild()
BrandUpdate.model_rebuild()
BrandDetail.model_rebuild()
