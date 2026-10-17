"""Liveness and readiness endpoints. Unauthenticated by design."""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import __version__
from app.core.config import Settings, get_settings
from app.db.session import session_dependency
from app.schemas.common import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, summary="Liveness and build metadata")
def health(
    settings: Settings = Depends(get_settings), session: Session = Depends(session_dependency)
) -> HealthResponse:
    try:
        session.execute(text("SELECT 1"))
        database = "ok"
    except Exception:
        database = "unavailable"
    return HealthResponse(
        status="ok" if database == "ok" else "degraded",
        version=__version__,
        environment=settings.environment,
        database=database,
        provider_calls_enabled=settings.provider_calls_enabled,
    )
