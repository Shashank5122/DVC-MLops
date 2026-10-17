"""Deterministic mock provider.

Produces the same output for the same input, always, with no I/O. This is what makes M2
ingestion and evaluation testable before any real provider is permitted, and it is the fixture
source for the demo workspace.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from typing import Any

from app.providers.base import (
    Capability,
    CollectionMethod,
    ProviderAdapter,
    ProviderMetadata,
    SurfaceKind,
)

PROVIDER_ID = "mock-deterministic-v1"


class MockProvider(ProviderAdapter):
    """A fixture-backed adapter: hash(prompt) selects a canned, stable response."""

    def __init__(self, fixtures: dict[str, dict[str, Any]] | None = None) -> None:
        self._fixtures = fixtures or _default_fixtures()

    @property
    def metadata(self) -> ProviderMetadata:
        return ProviderMetadata(
            provider_id=PROVIDER_ID,
            display_name="Deterministic mock provider",
            surface=SurfaceKind.mock_fixture,
            collection_method=CollectionMethod.deterministic_fixture,
            model_identifier="mock-model-1.0.0",
            capability=Capability(
                returns_citations=True,
                returns_raw_text=True,
                supports_region=True,
                supports_language=True,
                supports_repeat_runs=True,
                notes="No network I/O. Output is a pure function of the input.",
            ),
            compliance_status="permitted",
            compliance_notes="Fixtures only; contains no real provider output.",
        )

    def collect(self, request: dict[str, Any]) -> dict[str, Any]:
        prompt = str(request.get("prompt_text", ""))
        if not prompt.strip():
            raise ValueError("prompt_text is required")
        digest = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
        fixture = (
            self._fixtures[digest[:4]] if digest[:4] in self._fixtures else _generic(prompt, digest)
        )
        return {
            "provider_id": PROVIDER_ID,
            "model_identifier": self.metadata.model_identifier,
            "surface": SurfaceKind.mock_fixture.value,
            "collection_method": CollectionMethod.deterministic_fixture.value,
            "prompt_hash": digest,
            "response_text": fixture["response_text"],
            "citations": fixture["citations"],
            "mentions": fixture["mentions"],
            "grounding_used": None,  # unknown by construction for a fixture; never guessed
            "cost_usd": 0.0,
            "observed_at": datetime.now(UTC).isoformat(),
        }

    def estimate_cost_usd(self, request: dict[str, Any]) -> float:
        return 0.0


def _default_fixtures() -> dict[str, dict[str, Any]]:
    """A tiny, stable fixture set keyed by the first 4 hex chars of the prompt hash."""
    return {
        "0000": {
            "response_text": "Fixture response A.",
            "citations": [{"url": "https://example.com/a", "title": "Example A"}],
            "mentions": ["example-brand"],
        }
    }


def _generic(prompt: str, digest: str) -> dict[str, Any]:
    """Deterministic fallback so any prompt yields a stable, obviously-synthetic response."""
    bucket = int(digest[:8], 16) % 3
    templates: list[dict[str, Any]] = [
        {
            "response_text": f"Synthetic answer for: {prompt[:80]}",
            "citations": [
                {"url": "https://example.com/one", "title": "Synthetic source one"},
                {"url": "https://example.com/two", "title": "Synthetic source two"},
            ],
            "mentions": [],
        },
        {
            "response_text": f"Synthetic answer mentioning a brand for: {prompt[:80]}",
            "citations": [{"url": "https://example.com/three", "title": "Synthetic source three"}],
            "mentions": ["synthetic-brand"],
        },
        {
            "response_text": f"Synthetic answer with no citations for: {prompt[:80]}",
            "citations": [],
            "mentions": [],
        },
    ]
    return templates[bucket]


def fixture_fingerprint() -> str:
    """Stable hash of the fixture set, so a report can state which fixtures produced it."""
    return hashlib.sha256(
        json.dumps(_default_fixtures(), sort_keys=True).encode("utf-8")
    ).hexdigest()[:16]
