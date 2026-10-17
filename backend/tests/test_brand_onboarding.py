"""M1 vertical slice: onboard a brand with competitors through the HTTP API."""

from __future__ import annotations

from typing import Any

from fastapi.testclient import TestClient

BRAND = {
    "name": "Acme Analytics",
    "website": "https://www.acme-analytics.com/product",
    "category": "Marketing analytics",
    "description": "Attribution and marketing-mix modelling for mid-market SaaS.",
    "primary_language": "en",
    "primary_region": "us",
    "competitors": [
        {"name": "Northbeam", "website": "northbeam.io", "relationship_type": "direct"},
        {"name": "Triple Whale", "relationship_type": "alternative"},
    ],
}


def _create(client: TestClient, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
    response = client.post("/api/v1/brands", json=payload, headers=headers)
    assert response.status_code == 201, response.text
    result: dict[str, Any] = response.json()
    return result


def test_create_brand_normalises_region_domain_and_slug(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    body = _create(client, auth_headers, BRAND)
    assert body["slug"] == "acme-analytics"
    assert body["normalised_domain"] == "acme-analytics.com"
    assert body["primary_region"] == "US"
    assert body["fact_verification_status"] == "unverified"
    # Security-relevant defaults must start closed.
    assert body["website_change_authorized"] is False
    assert body["data_retention_permitted"] is False


def test_create_brand_sets_location_header(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    response = client.post("/api/v1/brands", json=BRAND, headers=auth_headers)
    assert response.headers["Location"].startswith("/api/v1/brands/")


def test_brand_detail_includes_competitors(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    created = _create(client, auth_headers, BRAND)
    detail = client.get(f"/api/v1/brands/{created['id']}", headers=auth_headers).json()
    assert detail["competitor_count"] == 2
    names = [item["name"] for item in detail["competitors"]]
    assert names == ["Northbeam", "Triple Whale"]  # ordered by name
    assert detail["competitors"][0]["normalised_domain"] == "northbeam.io"


def test_list_brands_paginates_and_searches(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    _create(client, auth_headers, BRAND)
    _create(client, auth_headers, {"name": "Zeta Robotics", "website": "zeta.dev"})

    listing = client.get("/api/v1/brands", headers=auth_headers).json()
    assert listing["total"] == 2
    assert listing["limit"] == 50

    found = client.get("/api/v1/brands?search=zeta", headers=auth_headers).json()
    assert found["total"] == 1
    assert found["items"][0]["name"] == "Zeta Robotics"

    paged = client.get("/api/v1/brands?limit=1&offset=1", headers=auth_headers).json()
    assert len(paged["items"]) == 1
    assert paged["total"] == 2


def test_update_brand_records_changed_fields(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    created = _create(client, auth_headers, BRAND)
    response = client.patch(
        f"/api/v1/brands/{created['id']}",
        json={"category": "Measurement platform", "website_change_authorized": True},
        headers=auth_headers,
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["category"] == "Measurement platform"
    assert body["website_change_authorized"] is True

    events = client.get(
        f"/api/v1/audit-events?entity_type=brand&entity_id={created['id']}", headers=auth_headers
    ).json()
    actions = {item["action"] for item in events["items"]}
    assert {"brand.created", "brand.updated"} <= actions
    updated = next(item for item in events["items"] if item["action"] == "brand.updated")
    assert updated["changes"]["website_change_authorized"] == {"from": False, "to": True}


def test_update_with_no_effective_change_is_rejected(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    created = _create(client, auth_headers, BRAND)
    response = client.patch(
        f"/api/v1/brands/{created['id']}", json={"name": "Acme Analytics"}, headers=auth_headers
    )
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_soft_delete_hides_brand_but_keeps_audit_trail(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    created = _create(client, auth_headers, BRAND)
    assert client.delete(f"/api/v1/brands/{created['id']}", headers=auth_headers).status_code == 204
    assert client.get(f"/api/v1/brands/{created['id']}", headers=auth_headers).status_code == 404
    assert client.get("/api/v1/brands", headers=auth_headers).json()["total"] == 0

    events = client.get("/api/v1/audit-events", headers=auth_headers).json()
    assert any(item["action"] == "brand.deleted" for item in events["items"])


def test_duplicate_brand_name_conflicts(client: TestClient, auth_headers: dict[str, str]) -> None:
    _create(client, auth_headers, BRAND)
    response = client.post("/api/v1/brands", json={"name": "acme analytics"}, headers=auth_headers)
    assert response.status_code == 409
    assert response.json()["error"]["code"] == "CONFLICT"


def test_duplicate_domain_conflicts(client: TestClient, auth_headers: dict[str, str]) -> None:
    _create(client, auth_headers, BRAND)
    response = client.post(
        "/api/v1/brands",
        json={"name": "Different Name", "website": "www.acme-analytics.com"},
        headers=auth_headers,
    )
    assert response.status_code == 409


def test_invalid_payloads_are_rejected(client: TestClient, auth_headers: dict[str, str]) -> None:
    # Blank name
    assert (
        client.post("/api/v1/brands", json={"name": "  "}, headers=auth_headers).status_code == 422
    )
    # Malformed domain reaches the domain validator
    response = client.post(
        "/api/v1/brands", json={"name": "Bad Site", "website": "https://"}, headers=auth_headers
    )
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"
    # Unknown fields are refused rather than ignored
    response = client.post(
        "/api/v1/brands", json={"name": "Ok", "sneaky": True}, headers=auth_headers
    )
    assert response.status_code == 422
    # Duplicate competitors in one payload
    response = client.post(
        "/api/v1/brands",
        json={"name": "Dupes", "competitors": [{"name": "Same"}, {"name": "same"}]},
        headers=auth_headers,
    )
    assert response.status_code == 422


def test_competitor_crud(client: TestClient, auth_headers: dict[str, str]) -> None:
    created = _create(client, auth_headers, {"name": "Solo Brand"})
    brand_id = created["id"]
    base = f"/api/v1/brands/{brand_id}/competitors"

    added = client.post(
        base, json={"name": "Rival One", "website": "rivalone.com"}, headers=auth_headers
    )
    assert added.status_code == 201, added.text
    competitor_id = added.json()["id"]
    assert added.json()["relationship_type"] == "direct"

    # Duplicate competitor name for the same brand
    assert client.post(base, json={"name": "rival one"}, headers=auth_headers).status_code == 409

    patched = client.patch(
        f"{base}/{competitor_id}",
        json={"relationship_type": "incumbent", "notes": "Series C, US-focused"},
        headers=auth_headers,
    )
    assert patched.status_code == 200
    assert patched.json()["relationship_type"] == "incumbent"

    listing = client.get(base, headers=auth_headers).json()
    assert len(listing) == 1

    assert client.delete(f"{base}/{competitor_id}", headers=auth_headers).status_code == 204
    assert client.get(base, headers=auth_headers).json() == []


def test_unknown_brand_returns_404_with_envelope(
    client: TestClient, auth_headers: dict[str, str]
) -> None:
    response = client.get(
        "/api/v1/brands/00000000-0000-0000-0000-000000000000", headers=auth_headers
    )
    assert response.status_code == 404
    body = response.json()["error"]
    assert body["code"] == "NOT_FOUND"
    assert body["correlation_id"]
