"""Application factory and ASGI entrypoint.

Run locally:  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""

from __future__ import annotations

import time
import uuid
from collections.abc import Awaitable, Callable
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app import __version__
from app.api import routes_audit, routes_brands, routes_health, routes_providers, routes_workspaces
from app.core.config import Settings, get_settings
from app.core.errors import install_error_handlers
from app.core.logging import configure_logging, correlation_id_var, get_logger
from app.db.session import init_database, reset_database

logger = get_logger(__name__)

CORRELATION_HEADER = "X-Correlation-ID"


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Assign a correlation id, log one structured line per request, add timing."""

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        correlation_id = request.headers.get(CORRELATION_HEADER) or uuid.uuid4().hex
        token = correlation_id_var.set(correlation_id)
        started = time.perf_counter()
        try:
            response = await call_next(request)
        except Exception:
            duration_ms = round((time.perf_counter() - started) * 1000, 2)
            logger.exception(
                "request_failed",
                extra={
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": duration_ms,
                },
            )
            raise
        finally:
            correlation_id_var.reset(token)

        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        response.headers[CORRELATION_HEADER] = correlation_id
        logger.info(
            "request",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        return response


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore[no-untyped-def]
    settings: Settings = app.state.settings
    configure_logging(settings.log_level, settings.log_json)
    app.state.database = init_database(settings)
    logger.info(
        "startup",
        extra={
            "environment": settings.environment,
            "database_dialect": app.state.database.engine.dialect.name,
            "provider_calls_enabled": settings.provider_calls_enabled,
            "version": __version__,
        },
    )
    if settings.provider_calls_enabled:
        logger.warning("provider_calls_enabled is TRUE - external calls are possible")
    try:
        yield
    finally:
        reset_database()
        logger.info("shutdown")


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build the FastAPI application. Tests call this with overridden settings."""
    settings = settings or get_settings()

    app = FastAPI(
        title="SignalGEO API",
        version=__version__,
        summary=(
            "Provider-independent AI-search visibility measurement and managed-optimisation "
            "backend. M1: brand onboarding. No external provider calls are made."
        ),
        lifespan=lifespan,
        docs_url="/docs" if settings.environment != "production" else None,
        redoc_url=None,
    )
    app.state.settings = settings
    # Dependencies must see THIS app's settings, not a process-wide cached instance.
    app.dependency_overrides[get_settings] = lambda: settings

    app.add_middleware(RequestContextMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=False,  # pilot uses a workspace key header, not cookies
        allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", settings.workspace_header, CORRELATION_HEADER],
        expose_headers=[CORRELATION_HEADER],
    )

    install_error_handlers(app)

    prefix = settings.api_v1_prefix
    app.include_router(routes_health.router, prefix=prefix)
    app.include_router(routes_workspaces.router, prefix=prefix)
    app.include_router(routes_brands.router, prefix=prefix)
    app.include_router(routes_brands.competitor_router, prefix=prefix)
    app.include_router(routes_providers.router, prefix=prefix)
    app.include_router(routes_audit.router, prefix=prefix)

    @app.get("/", include_in_schema=False)
    def root() -> dict[str, Any]:
        return {
            "service": "SignalGEO API",
            "version": __version__,
            "environment": settings.environment,
            "health": f"{prefix}/health",
            "docs": "/docs" if settings.environment != "production" else "disabled",
            "provider_calls_enabled": settings.provider_calls_enabled,
        }

    return app


app = create_app()
