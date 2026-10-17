"""The provider permission gate. M1 must make no external calls, ever."""

from __future__ import annotations

import pytest
from app.core.config import Settings
from app.core.errors import ProviderDisabledError
from app.providers.base import CollectionMethod, ProviderRegistry, SurfaceKind
from app.providers.mock import MockProvider
from fastapi.testclient import TestClient


def test_mock_provider_is_deterministic_and_io_free() -> None:
    provider = MockProvider()
    request = {"prompt_text": "Best marketing attribution tools for mid-market SaaS?"}
    first = provider.collect(request)
    second = provider.collect(request)
    assert first["response_text"] == second["response_text"]
    assert first["citations"] == second["citations"]
    assert first["prompt_hash"] == second["prompt_hash"]
    assert first["cost_usd"] == 0.0
    # Grounding status is unknown by construction and must never be guessed.
    assert first["grounding_used"] is None
    assert first["surface"] == SurfaceKind.mock_fixture.value
    assert first["collection_method"] == CollectionMethod.deterministic_fixture.value


def test_mock_provider_rejects_blank_prompt() -> None:
    with pytest.raises(ValueError, match="prompt_text is required"):
        MockProvider().collect({"prompt_text": "   "})


def test_different_prompts_get_different_fixtures() -> None:
    provider = MockProvider()
    a = provider.collect({"prompt_text": "prompt alpha"})
    b = provider.collect({"prompt_text": "prompt beta that is clearly different"})
    assert a["prompt_hash"] != b["prompt_hash"]


def test_registry_blocks_every_call_while_switch_is_off() -> None:
    settings = Settings(environment="development")
    assert settings.provider_calls_enabled is False
    registry = ProviderRegistry(settings)
    registry.register(MockProvider())

    allowed, reason = registry.is_permitted("mock-deterministic-v1")
    assert allowed is False
    assert "provider_calls_enabled" in reason
    with pytest.raises(ProviderDisabledError):
        registry.assert_permitted("mock-deterministic-v1")


def test_denied_providers_stay_denied_even_with_the_switch_on() -> None:
    settings = Settings(environment="development", provider_calls_enabled=True)
    registry = ProviderRegistry(settings)
    registry.register(MockProvider())

    for denied in ("gemini-grounding-google-search", "perplexity-agent-api"):
        allowed, reason = registry.is_permitted(denied)
        assert allowed is False
        assert "denylist" in reason
        with pytest.raises(ProviderDisabledError):
            registry.assert_permitted(denied)

    # With the switch on and no denylist hit, the registered mock is allowed.
    allowed, _ = registry.is_permitted("mock-deterministic-v1")
    assert allowed is True


def test_production_settings_refuse_the_switch_and_sqlite() -> None:
    with pytest.raises(ValueError):
        Settings(
            environment="production",
            provider_calls_enabled=True,
            database_url="postgresql+psycopg://u:p@localhost/db",
        )
    with pytest.raises(ValueError):
        Settings(environment="production", database_url="sqlite:///./prod.db")


def test_providers_endpoint_is_read_only(client: TestClient) -> None:
    body = client.get("/api/v1/providers").json()
    assert body["provider_calls_enabled"] is False
    assert "gemini-grounding-google-search" in body["denied_pending_authorization"]
    assert "perplexity-agent-api" in body["denied_pending_authorization"]
    adapter = body["adapters"][0]
    assert adapter["provider_id"] == "mock-deterministic-v1"
    assert adapter["permitted_now"] is False
    assert adapter["surface"] == "mock_fixture"


def test_no_route_can_trigger_a_provider_call(client: TestClient) -> None:
    """The provider surface is inventory-only: GET, nothing that could invoke an adapter."""
    schema = client.get("/openapi.json").json()
    paths: dict[str, dict[str, object]] = schema["paths"]

    assert "/api/v1/providers" in paths
    assert set(paths["/api/v1/providers"]) == {"get"}
    assert not any("collect" in path for path in paths)
    assert not any("ingest" in path or "run" in path for path in paths)
    # No provider path accepts a body-bearing method anywhere in the API.
    provider_paths = [path for path in paths if "provider" in path]
    for path in provider_paths:
        assert set(paths[path]) <= {"get"}, path
