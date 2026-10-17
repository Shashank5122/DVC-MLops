"""Application-scoped database wiring and the FastAPI session dependency."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from sqlalchemy.orm import Session

from app.core.config import Settings
from app.db.base import Database

_database: Database | None = None


def init_database(settings: Settings) -> Database:
    """Create (once) and return the process-wide Database holder."""
    global _database
    if _database is None:
        _database = Database(
            settings.database_url, echo=settings.db_echo, is_sqlite=settings.is_sqlite
        )
    return _database


def get_database() -> Database:
    if _database is None:  # pragma: no cover - guarded by app startup
        raise RuntimeError("database is not initialised; call init_database() first")
    return _database


def reset_database() -> None:
    """Dispose the engine. Used by tests between runs."""
    global _database
    if _database is not None:
        _database.dispose()
    _database = None


def session_dependency() -> Generator[Session, None, None]:
    """Yield a session that commits on success and rolls back on any exception."""
    database = get_database()
    yield from database.session()


def current_engine_options() -> dict[str, Any]:  # pragma: no cover - diagnostics helper
    database = get_database()
    return {"dialect": database.engine.dialect.name, "url_host": _safe_host(database)}


def _safe_host(database: Database) -> str:
    """Return the DB host without credentials, for health checks and logs."""
    url = database.engine.url
    return str(url.host or ("sqlite" if url.drivername.startswith("sqlite") else "unknown"))
