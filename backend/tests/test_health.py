from __future__ import annotations

from fastapi.testclient import TestClient


def test_root_reports_service_metadata(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["service"] == "SignalGEO API"
    assert body["provider_calls_enabled"] is False


def test_health_reports_database_ok(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["database"] == "ok"
    # The kill-switch must be visible in the health payload so an operator can see it at a glance.
    assert body["provider_calls_enabled"] is False


def test_health_requires_no_workspace_key(client: TestClient) -> None:
    assert client.get("/api/v1/health").status_code == 200


def test_correlation_id_is_generated_and_echoed(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.headers.get("X-Correlation-ID")


def test_supplied_correlation_id_is_preserved(client: TestClient) -> None:
    response = client.get("/api/v1/health", headers={"X-Correlation-ID": "trace-abc-123"})
    assert response.headers["X-Correlation-ID"] == "trace-abc-123"
