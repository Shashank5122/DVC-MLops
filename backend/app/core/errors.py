"""Domain errors and a single, consistent API error envelope.

Every error response carries a correlation_id so a client report and a server log line can be
matched without exposing stack traces or internals.
"""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.logging import correlation_id_var, get_logger

logger = get_logger(__name__)

# Starlette renamed this constant; resolve it once so we work on both and emit no warning.
HTTP_422 = getattr(status, "HTTP_422_UNPROCESSABLE_CONTENT", None) or 422


class AppError(Exception):
    """Base class for expected, client-facing failures."""

    status_code: int = status.HTTP_400_BAD_REQUEST
    code: str = "APP_ERROR"

    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}


class NotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    code = "NOT_FOUND"


class ConflictError(AppError):
    status_code = status.HTTP_409_CONFLICT
    code = "CONFLICT"


class ValidationError(AppError):
    status_code = HTTP_422
    code = "VALIDATION_ERROR"


class AuthenticationError(AppError):
    status_code = status.HTTP_401_UNAUTHORIZED
    code = "UNAUTHENTICATED"


class AuthorizationError(AppError):
    status_code = status.HTTP_403_FORBIDDEN
    code = "FORBIDDEN"


class ProviderDisabledError(AppError):
    """Raised if anything attempts an external provider call while disabled."""

    status_code = status.HTTP_403_FORBIDDEN
    code = "PROVIDER_CALLS_DISABLED"


def _envelope(code: str, message: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details or {},
            "correlation_id": correlation_id_var.get(),
        }
    }


def install_error_handlers(app: FastAPI) -> None:
    """Attach handlers so every failure path returns the same envelope shape."""

    @app.exception_handler(AppError)
    async def _app_error(_: Request, exc: AppError) -> JSONResponse:
        logger.warning("app_error", extra={"code": exc.code, "detail": exc.details})
        return JSONResponse(
            status_code=exc.status_code,
            content=_envelope(exc.code, exc.message, exc.details),
        )

    @app.exception_handler(StarletteHTTPException)
    async def _http_error(_: Request, exc: StarletteHTTPException) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content=_envelope(f"HTTP_{exc.status_code}", str(exc.detail)),
        )

    @app.exception_handler(RequestValidationError)
    async def _validation_error(_: Request, exc: RequestValidationError) -> JSONResponse:
        # `exc.errors()` can contain non-serialisable objects; normalise to str.
        details = [
            {"loc": [str(part) for part in err.get("loc", ())], "msg": str(err.get("msg", ""))}
            for err in exc.errors()
        ]
        logger.info("request_validation_error", extra={"errors": details})
        return JSONResponse(
            status_code=HTTP_422,
            content=_envelope("VALIDATION_ERROR", "Request validation failed", {"errors": details}),
        )

    @app.exception_handler(IntegrityError)
    async def _integrity_error(_: Request, exc: IntegrityError) -> JSONResponse:
        # Do not leak SQL or constraint internals to clients.
        logger.warning("integrity_error", extra={"statement": str(exc.orig)[:200]})
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=_envelope("CONFLICT", "The request conflicts with existing data"),
        )

    @app.exception_handler(SQLAlchemyError)
    async def _db_error(_: Request, exc: SQLAlchemyError) -> JSONResponse:
        logger.exception("database_error", exc_info=exc)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content=_envelope("DATABASE_UNAVAILABLE", "The database is temporarily unavailable"),
        )

    @app.exception_handler(Exception)
    async def _unhandled(_: Request, exc: Exception) -> JSONResponse:
        logger.exception("unhandled_error", exc_info=exc)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=_envelope("INTERNAL_ERROR", "An unexpected error occurred"),
        )
