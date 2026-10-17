"""Brand onboarding and competitor management (M1 vertical slice)."""

from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from app.core.tenancy import resolve_workspace
from app.db.models import Workspace
from app.db.session import session_dependency
from app.schemas.brand import BrandCreate, BrandDetail, BrandRead, BrandUpdate
from app.schemas.common import Page
from app.schemas.competitor import CompetitorCreate, CompetitorRead, CompetitorUpdate
from app.services import brand_service

router = APIRouter(prefix="/brands", tags=["brands"])


@router.post(
    "", response_model=BrandRead, status_code=status.HTTP_201_CREATED, summary="Onboard a brand"
)
def create_brand(
    payload: BrandCreate,
    response: Response,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> BrandRead:
    brand = brand_service.create_brand(session, workspace_id=workspace.id, payload=payload)
    response.headers["Location"] = f"/api/v1/brands/{brand.id}"
    return BrandRead.model_validate(brand)


@router.get("", response_model=Page[BrandRead], summary="List brands")
def list_brands(
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    search: str | None = Query(default=None, max_length=120),
) -> Page[BrandRead]:
    brands, total = brand_service.list_brands(
        session, workspace_id=workspace.id, limit=limit, offset=offset, search=search
    )
    return Page[BrandRead](
        items=[BrandRead.model_validate(brand) for brand in brands],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get("/{brand_id}", response_model=BrandDetail, summary="Brand detail with competitors")
def get_brand(
    brand_id: uuid.UUID,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> BrandDetail:
    brand = brand_service.get_brand(session, workspace_id=workspace.id, brand_id=brand_id)
    detail = BrandDetail.model_validate(brand)
    competitors = sorted(brand.competitors, key=lambda item: item.name)
    return detail.model_copy(
        update={
            "competitors": [CompetitorRead.model_validate(item) for item in competitors],
            "competitor_count": len(competitors),
        }
    )


@router.patch("/{brand_id}", response_model=BrandRead, summary="Update a brand")
def update_brand(
    brand_id: uuid.UUID,
    payload: BrandUpdate,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> BrandRead:
    brand = brand_service.update_brand(
        session, workspace_id=workspace.id, brand_id=brand_id, payload=payload
    )
    return BrandRead.model_validate(brand)


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Soft-delete a brand")
def delete_brand(
    brand_id: uuid.UUID,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> None:
    brand_service.soft_delete_brand(session, workspace_id=workspace.id, brand_id=brand_id)


# --- competitors (nested under a brand) ---------------------------------------

competitor_router = APIRouter(prefix="/brands/{brand_id}/competitors", tags=["competitors"])


@competitor_router.get("", response_model=list[CompetitorRead], summary="List competitors")
def list_competitors(
    brand_id: uuid.UUID,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> list[CompetitorRead]:
    rows = brand_service.list_competitors(session, workspace_id=workspace.id, brand_id=brand_id)
    return [CompetitorRead.model_validate(row) for row in rows]


@competitor_router.post(
    "",
    response_model=CompetitorRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a competitor",
)
def add_competitor(
    brand_id: uuid.UUID,
    payload: CompetitorCreate,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> CompetitorRead:
    competitor = brand_service.add_competitor(
        session, workspace_id=workspace.id, brand_id=brand_id, payload=payload
    )
    return CompetitorRead.model_validate(competitor)


@competitor_router.patch(
    "/{competitor_id}", response_model=CompetitorRead, summary="Update a competitor"
)
def update_competitor(
    brand_id: uuid.UUID,
    competitor_id: uuid.UUID,
    payload: CompetitorUpdate,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> CompetitorRead:
    competitor = brand_service.update_competitor(
        session,
        workspace_id=workspace.id,
        brand_id=brand_id,
        competitor_id=competitor_id,
        payload=payload,
    )
    return CompetitorRead.model_validate(competitor)


@competitor_router.delete(
    "/{competitor_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Remove a competitor"
)
def remove_competitor(
    brand_id: uuid.UUID,
    competitor_id: uuid.UUID,
    session: Session = Depends(session_dependency),
    workspace: Workspace = Depends(resolve_workspace),
) -> None:
    brand_service.remove_competitor(
        session, workspace_id=workspace.id, brand_id=brand_id, competitor_id=competitor_id
    )
