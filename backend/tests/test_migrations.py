"""Migrations must produce exactly the schema the models declare, and must reverse cleanly."""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from app.db import models  # noqa: F401  - registers tables
from app.db.base import Base
from sqlalchemy import create_engine, inspect

BACKEND_ROOT = Path(__file__).resolve().parents[1]


def _alembic_config(database_url: str) -> Config:
    from app.core.config import get_settings

    get_settings.cache_clear()  # env.py builds settings from the environment we just set
    config = Config(str(BACKEND_ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(BACKEND_ROOT / "alembic"))
    config.set_main_option("sqlalchemy.url", database_url)
    # env.py builds settings from the environment; keep it consistent with this test DB.
    os.environ["SIGNALGEO_DATABASE_URL"] = database_url
    return config


def test_upgrade_head_creates_every_model_table(tmp_path: Path) -> None:
    url = f"sqlite:///{tmp_path / 'migrated.db'}"
    command.upgrade(_alembic_config(url), "head")

    engine = create_engine(url, future=True)
    inspector = inspect(engine)
    created = set(inspector.get_table_names()) - {"alembic_version"}
    declared = set(Base.metadata.tables)
    assert declared == {"workspaces", "brands", "competitors", "audit_events"}
    assert created == declared, f"migration/model drift: {created ^ declared}"

    # Columns must match too, not just table names.
    for table in declared:
        migrated_columns = {column["name"] for column in inspector.get_columns(table)}
        model_columns = {column.name for column in Base.metadata.tables[table].columns}
        assert migrated_columns == model_columns, f"column drift in {table}"

    # The isolation constraints are part of the migration, not just the models.
    brand_uniques = {
        frozenset(constraint["column_names"])
        for constraint in inspector.get_unique_constraints("brands")
    }
    # These two constraints ARE the tenant isolation guarantee for brand identity.
    assert frozenset({"workspace_id", "slug"}) in brand_uniques
    assert frozenset({"workspace_id", "normalised_domain"}) in brand_uniques
    # No global uniqueness on name/domain: two workspaces may track the same company.
    assert frozenset({"slug"}) not in brand_uniques
    assert frozenset({"normalised_domain"}) not in brand_uniques

    competitor_uniques = {
        frozenset(c["column_names"]) for c in inspector.get_unique_constraints("competitors")
    }
    assert frozenset({"brand_id", "slug"}) in competitor_uniques

    # Every tenant-owned table must carry an index on workspace_id.
    for table in ("brands", "competitors", "audit_events"):
        indexed = {
            column for index in inspector.get_indexes(table) for column in index["column_names"]
        }
        foreign_keys = {fk["constrained_columns"][0] for fk in inspector.get_foreign_keys(table)}
        assert "workspace_id" in indexed | foreign_keys, table
    engine.dispose()


def test_downgrade_to_base_removes_everything(tmp_path: Path) -> None:
    url = f"sqlite:///{tmp_path / 'downgraded.db'}"
    config = _alembic_config(url)
    command.upgrade(config, "head")
    command.downgrade(config, "base")

    engine = create_engine(url, future=True)
    remaining = set(inspect(engine).get_table_names()) - {"alembic_version"}
    assert remaining == set()
    engine.dispose()


def test_only_one_head(tmp_path: Path) -> None:
    url = f"sqlite:///{tmp_path / 'heads.db'}"
    config = _alembic_config(url)
    from alembic.script import ScriptDirectory

    script = ScriptDirectory.from_config(config)
    heads = script.get_heads()
    assert len(heads) == 1
    assert heads[0] == "0001"


@pytest.mark.postgres
def test_migration_applies_to_postgres(
    database_url: str,
) -> None:  # pragma: no cover - needs a server
    """Runs only with SIGNALGEO_TEST_POSTGRES_URL set and a live server (see CI/compose)."""
    command.upgrade(_alembic_config(database_url), "head")
    engine = create_engine(database_url, future=True)
    assert "brands" in set(inspect(engine).get_table_names())
    engine.dispose()
