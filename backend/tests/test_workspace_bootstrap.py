from __future__ import annotations

from pathlib import Path

from app.core.config import Settings
from app.db.models import Workspace
from fastapi.testclient import TestClient
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session


def test_dev_bootstrap_returns_plaintext_key_once(client: TestClient) -> None:
    response = client.post("/api/v1/dev/workspaces", json={"name": "Acme Analytics"})
    assert response.status_code == 201, response.text
    body = response.json()
    key = body["workspace_key"]
    assert key.startswith("sg_")
    assert body["workspace"]["slug"] == "acme-analytics"
    assert body["workspace"]["key_last4"] == key[-4:]
    # The response model must never include the hash or the key on subsequent reads.
    assert "workspace_key" not in body["workspace"]

    me = client.get("/api/v1/workspaces/me", headers={"X-Workspace-Key": key})
    assert me.status_code == 200
    assert me.json()["slug"] == "acme-analytics"
    assert "workspace_key" not in me.json()


def test_key_is_stored_only_as_a_hash(db_engine: Engine, client: TestClient) -> None:
    response = client.post("/api/v1/dev/workspaces", json={"name": "Hash Check"})
    key = response.json()["workspace_key"]
    with Session(db_engine) as session:
        row = session.scalar(select(Workspace).where(Workspace.slug == "hash-check"))
        assert row is not None
        assert row.key_hash != key
        assert key not in (row.key_hash, row.key_last4, row.name, row.slug, row.notes or "")
        assert len(row.key_hash) == 64


def test_duplicate_slug_conflicts(client: TestClient) -> None:
    assert client.post("/api/v1/dev/workspaces", json={"name": "Same Name"}).status_code == 201
    assert client.post("/api/v1/dev/workspaces", json={"name": "Same Name"}).status_code == 409


def test_bootstrap_is_rejected_outside_development(tmp_path: Path) -> None:
    settings = Settings(
        database_url=f"sqlite:///{tmp_path / 'other.db'}",
        environment="testing",
    )
    assert settings.dev_bootstrap_enabled is False
    from app.main import create_app

    app = create_app(settings)
    with TestClient(app) as non_dev_client:
        response = non_dev_client.post("/api/v1/dev/workspaces", json={"name": "Nope"})
    assert response.status_code == 403
    assert response.json()["error"]["code"] == "FORBIDDEN"


def test_workspace_stats(client: TestClient, auth_headers: dict[str, str]) -> None:
    client.post("/api/v1/brands", json={"name": "Brand One"}, headers=auth_headers)
    body = client.get("/api/v1/workspaces/me/stats", headers=auth_headers).json()
    assert body == {"workspace": "test-workspace", "brands": 1}
