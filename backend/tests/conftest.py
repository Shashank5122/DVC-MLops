"""Shared fixtures. Every test gets an isolated SQLite database and its own app instance."""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from app.core.config import Settings
from app.db.base import Base
from app.db.models import Workspace, WorkspaceStatus, generate_workspace_key, hash_workspace_key
from app.db.session import reset_database
from app.main import create_app
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

HEADER = "X-Workspace-Key"


def _test_settings(tmp_path: Path) -> Settings:
    """Settings that mirror the default (production-safe) configuration but use SQLite."""
    os.environ["SIGNALGEO_DATABASE_URL"] = f"sqlite:///{tmp_path / 'test.db'}"
    os.environ["SIGNALGEO_ENVIRONMENT"] = "development"
    os.environ["SIGNALGEO_LOG_JSON"] = "false"
    for var in ("SIGNALGEO_PROVIDER_CALLS_ENABLED",):
        os.environ.pop(var, None)
    return Settings()


@pytest.fixture
def settings(tmp_path: Path) -> Iterator[Settings]:
    yield _test_settings(tmp_path)
    reset_database()
    os.environ.pop("SIGNALGEO_DATABASE_URL", None)


@pytest.fixture
def db_engine(settings: Settings) -> Iterator[Engine]:
    """A bare engine with the schema created, for direct row-level assertions."""
    engine = create_engine(
        settings.database_url, future=True, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest.fixture
def client(settings: Settings, db_engine: Engine) -> Iterator[TestClient]:
    app = create_app(settings)
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def workspace_key(db_engine: Engine) -> str:
    """Create a tenant directly so tests do not depend on the dev bootstrap endpoint."""
    plain = generate_workspace_key()
    with Session(db_engine) as session:
        session.add(
            Workspace(
                name="Test Workspace",
                slug="test-workspace",
                key_hash=hash_workspace_key(plain),
                key_last4=plain[-4:],
                status=WorkspaceStatus.active,
            )
        )
        session.commit()
    return plain


@pytest.fixture
def second_workspace_key(db_engine: Engine) -> str:
    plain = generate_workspace_key()
    with Session(db_engine) as session:
        session.add(
            Workspace(
                name="Other Workspace",
                slug="other-workspace",
                key_hash=hash_workspace_key(plain),
                key_last4=plain[-4:],
                status=WorkspaceStatus.active,
            )
        )
        session.commit()
    return plain


@pytest.fixture
def auth_headers(workspace_key: str) -> dict[str, str]:
    return {HEADER: workspace_key}


@pytest.fixture
def database_url() -> str:
    """Live PostgreSQL URL for @pytest.mark.postgres tests; empty skips them."""
    import os

    return os.environ.get("SIGNALGEO_TEST_POSTGRES_URL", "")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Skip postgres-marked tests unless a live server URL is provided.

    These are reported as SKIPPED, never as passed: there is no PostgreSQL server in this
    sandbox, and claiming otherwise would breach integrity rule 18.
    """
    import os

    if os.environ.get("SIGNALGEO_TEST_POSTGRES_URL"):
        return
    skip = pytest.mark.skip(reason="SIGNALGEO_TEST_POSTGRES_URL not set; no live PostgreSQL server")
    for item in items:
        if "postgres" in item.keywords:
            item.add_marker(skip)
