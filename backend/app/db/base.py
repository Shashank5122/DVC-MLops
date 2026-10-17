"""SQLAlchemy 2.0 declarative base, engine/session factories and shared column types.

Design notes (see docs/engineering/00-architecture-decisions.md):
* Synchronous SQLAlchemy. Async adds a second failure mode set for no pilot-stage benefit;
  FastAPI runs sync endpoints in a threadpool.
* `sa.Uuid` and `sa.JSON` are used deliberately: both are portable across PostgreSQL
  (native uuid / jsonb-ish) and SQLite (char(32) / text), so the same migration and the same
  test suite run against either.
* Every tenant-owned table carries `workspace_id` and a composite unique constraint, so
  isolation is enforced by the schema and not only by application code.
"""

from __future__ import annotations

import uuid
from collections.abc import Generator
from datetime import UTC, datetime

from sqlalchemy import DateTime, MetaData, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    DeclarativeMeta,
    Mapped,
    Session,
    mapped_column,
    sessionmaker,
)

# Deterministic constraint names make Alembic autogenerate and manual migrations stable.
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Declarative base with a shared naming convention."""

    metadata = MetaData(naming_convention=NAMING_CONVENTION)


def utcnow() -> datetime:
    """Timezone-aware UTC now. Used as the default for every timestamp column."""
    return datetime.now(UTC)


def new_uuid() -> uuid.UUID:
    return uuid.uuid4()


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False
    )


def build_engine(database_url: str, *, echo: bool = False, is_sqlite: bool = False):  # type: ignore[no-untyped-def]
    """Create an engine appropriate for the configured backend."""
    if is_sqlite:
        # check_same_thread=False lets FastAPI's threadpool reuse connections safely.
        return create_engine(
            database_url,
            echo=echo,
            future=True,
            connect_args={"check_same_thread": False},
        )
    return create_engine(
        database_url,
        echo=echo,
        future=True,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )


def build_session_factory(engine) -> sessionmaker[Session]:  # type: ignore[no-untyped-def]
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, future=True)


class Database:
    """Small holder so the app can own one engine and one session factory."""

    def __init__(self, database_url: str, *, echo: bool = False, is_sqlite: bool = False) -> None:
        self.engine = build_engine(database_url, echo=echo, is_sqlite=is_sqlite)
        self.SessionFactory = build_session_factory(self.engine)

    def session(self) -> Generator[Session, None, None]:
        session = self.SessionFactory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def dispose(self) -> None:
        self.engine.dispose()


# Re-exported for convenience in migrations and tests.
__all__ = [
    "Base",
    "Database",
    "DeclarativeMeta",
    "TimestampMixin",
    "new_uuid",
    "utcnow",
]
