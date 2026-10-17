from __future__ import annotations

import pytest
from app.core.config import Settings
from fastapi.testclient import TestClient


def test_error_envelope_shape(client: TestClient) -> None:
    response = client.get("/api/v1/brands", headers={"X-Workspace-Key": "sg_bad"})
    assert response.status_code == 401
    body = response.json()
    assert set(body) == {"error"}
    error = body["error"]
    assert {"code", "message", "details", "correlation_id"} <= set(error)
    # No stack traces, no SQL, no internal paths leak to the client.
    text = response.text
    for forbidden in ("Traceback", "sqlalchemy", "/home/", "app/services"):
        assert forbidden not in text


def test_validation_error_lists_offending_fields(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    response = client.post("/api/v1/brands", json={"name": ""}, headers=auth_headers)
    assert response.status_code == 422
    error = response.json()["error"]
    assert error["code"] == "VALIDATION_ERROR"
    assert error["details"]


def test_unknown_route_returns_envelope(client: TestClient) -> None:
    response = client.get("/api/v1/does-not-exist")
    assert response.status_code == 404


def test_unhandled_exception_becomes_500_envelope(
    settings: Settings,
    monkeypatch: pytest.MonkeyPatch,
    workspace_key: str,
) -> None:
    """A crash inside a service must become the generic envelope, never a leaked traceback."""
    from app.main import create_app
    from app.services import brand_service

    def boom(*args: object, **kwargs: object) -> object:
        raise RuntimeError("synthetic failure with secret=abc123")

    monkeypatch.setattr(brand_service, "list_brands", boom)
    app = create_app(settings)
    with TestClient(app, raise_server_exceptions=False) as raising_client:
        response = raising_client.get("/api/v1/brands", headers={"X-Workspace-Key": workspace_key})

    assert response.status_code == 500
    body = response.json()["error"]
    assert body["code"] == "INTERNAL_ERROR"
    assert body["correlation_id"]
    text = response.text
    for forbidden in ("secret=abc123", "Traceback", "RuntimeError", "brand_service"):
        assert forbidden not in text
