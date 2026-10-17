"""Tenant isolation is a security boundary, so it gets its own test module."""

from __future__ import annotations

import uuid

from fastapi.testclient import TestClient

HEADER = "X-Workspace-Key"


def _create_brand(client: TestClient, headers: dict[str, str], name: str) -> str:
    response = client.post("/api/v1/brands", json={"name": name}, headers=headers)
    assert response.status_code == 201, response.text
    return str(response.json()["id"])


def test_missing_workspace_key_is_unauthorized(client: TestClient) -> None:
    response = client.get("/api/v1/brands")
    assert response.status_code == 401
    body = response.json()["error"]
    assert body["code"] == "UNAUTHENTICATED"
    assert HEADER in body["message"]


def test_unknown_workspace_key_is_unauthorized_and_indistinguishable(
    client: TestClient, workspace_key: str
) -> None:
    wrong = client.get("/api/v1/brands", headers={HEADER: "sg_totally-wrong-key"})
    valid = client.get("/api/v1/brands", headers={HEADER: workspace_key})
    assert wrong.status_code == 401
    assert valid.status_code == 200
    # The message must not reveal whether a key exists.
    assert wrong.json()["error"]["message"] == "Invalid workspace key"


def test_workspace_cannot_read_another_workspaces_brand(
    client: TestClient, auth_headers: dict[str, str], second_workspace_key: str
) -> None:
    brand_id = _create_brand(client, auth_headers, "Acme Analytics")
    other_headers = {HEADER: second_workspace_key}

    assert client.get(f"/api/v1/brands/{brand_id}", headers=other_headers).status_code == 404
    assert (
        client.patch(
            f"/api/v1/brands/{brand_id}", json={"name": "Hijacked"}, headers=other_headers
        ).status_code
        == 404
    )
    assert client.delete(f"/api/v1/brands/{brand_id}", headers=other_headers).status_code == 404
    assert client.get("/api/v1/brands", headers=other_headers).json()["total"] == 0


def test_workspace_cannot_touch_another_workspaces_competitor(
    client: TestClient, auth_headers: dict[str, str], second_workspace_key: str
) -> None:
    brand_id = _create_brand(client, auth_headers, "Acme Analytics")
    added = client.post(
        f"/api/v1/brands/{brand_id}/competitors", json={"name": "Rival"}, headers=auth_headers
    )
    competitor_id = str(added.json()["id"])
    other = {HEADER: second_workspace_key}

    assert client.get(f"/api/v1/brands/{brand_id}/competitors", headers=other).status_code == 404
    assert (
        client.patch(
            f"/api/v1/brands/{brand_id}/competitors/{competitor_id}",
            json={"notes": "tampered"},
            headers=other,
        ).status_code
        == 404
    )
    assert (
        client.delete(
            f"/api/v1/brands/{brand_id}/competitors/{competitor_id}", headers=other
        ).status_code
        == 404
    )


def test_audit_events_are_scoped_to_the_workspace(
    client: TestClient, auth_headers: dict[str, str], second_workspace_key: str
) -> None:
    _create_brand(client, auth_headers, "Acme Analytics")
    other = {HEADER: second_workspace_key}

    own = client.get("/api/v1/audit-events", headers=auth_headers).json()
    theirs = client.get("/api/v1/audit-events", headers=other).json()
    assert own["total"] >= 1
    assert theirs["total"] == 0


def test_same_brand_name_is_allowed_in_two_workspaces(
    client: TestClient, auth_headers: dict[str, str], second_workspace_key: str
) -> None:
    other = {HEADER: second_workspace_key}
    assert (
        client.post("/api/v1/brands", json={"name": "Acme"}, headers=auth_headers).status_code
        == 201
    )
    assert client.post("/api/v1/brands", json={"name": "Acme"}, headers=other).status_code == 201


def test_invalid_uuid_path_parameter_is_422_not_500(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    response = client.get("/api/v1/brands/not-a-uuid", headers=auth_headers)
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_random_uuid_does_not_leak_existence(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    response = client.get(f"/api/v1/brands/{uuid.uuid4()}", headers=auth_headers)
    assert response.status_code == 404
