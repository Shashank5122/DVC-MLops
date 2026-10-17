"""Provider adapter contract and the permission gate every adapter must pass.

The contract is deliberately narrow and measurement-shaped: an adapter reports what surface it
observes, how it collects, and what it costs. It never decides policy, never blends surfaces and
never publishes. Those are separate concerns with separate permissions (integrity rule 14).
"""

from __future__ import annotations

import enum
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Protocol

from app.core.config import Settings
from app.core.errors import ProviderDisabledError


class SurfaceKind(enum.StrEnum):
    """Where an observation came from. Never blend these into one score."""

    api_search_enabled = "api_search_enabled"
    consumer_interface_human = "consumer_interface_human"
    vendor_platform = "vendor_platform"
    ungrounded_model = "ungrounded_model"
    mock_fixture = "mock_fixture"


class CollectionMethod(enum.StrEnum):
    """How the bytes were obtained. Provenance is part of the measurement."""

    official_api = "official_api"
    human_transcription = "human_transcription"
    vendor_export = "vendor_export"
    deterministic_fixture = "deterministic_fixture"


@dataclass(frozen=True, slots=True)
class Capability:
    """What an adapter can and cannot do, stated explicitly rather than inferred."""

    returns_citations: bool
    returns_raw_text: bool
    supports_region: bool
    supports_language: bool
    supports_repeat_runs: bool
    notes: str = ""


@dataclass(frozen=True, slots=True)
class ProviderMetadata:
    """Identity of a provider/surface. `model_identifier` is the exact string reported back."""

    provider_id: str
    display_name: str
    surface: SurfaceKind
    collection_method: CollectionMethod
    model_identifier: str
    capability: Capability
    compliance_status: str = "permitted"
    compliance_notes: str = ""


class ProviderError(Exception):
    """Base class for adapter failures."""


class ProviderUnavailable(ProviderError):
    """Adapter is present but cannot be used right now."""


class ProviderAdapter(ABC):
    """Interface every provider adapter implements.

    M1 adapters perform NO network I/O. `collect` exists so M2 ingestion has one typed shape to
    target, and so the permission gate is exercised by tests before any real integration exists.
    """

    @property
    @abstractmethod
    def metadata(self) -> ProviderMetadata: ...

    @abstractmethod
    def collect(self, request: dict[str, Any]) -> dict[str, Any]:
        """Return one observation payload. Must raise, never fabricate, on failure."""

    @abstractmethod
    def estimate_cost_usd(self, request: dict[str, Any]) -> float:
        """Estimated USD cost of one request. 0.0 for fixtures and human capture."""


class PermissionGate(Protocol):
    def is_permitted(self, provider_id: str) -> tuple[bool, str]: ...


class ProviderRegistry:
    """Holds adapters and enforces the kill-switch before any collection can happen."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._adapters: dict[str, ProviderAdapter] = {}

    def register(self, adapter: ProviderAdapter) -> None:
        self._adapters[adapter.metadata.provider_id] = adapter

    def get(self, provider_id: str) -> ProviderAdapter:
        try:
            return self._adapters[provider_id]
        except KeyError as exc:
            raise ProviderUnavailable(f"unknown provider: {provider_id}") from exc

    def list_metadata(self) -> list[ProviderMetadata]:
        return [adapter.metadata for adapter in self._adapters.values()]

    def is_permitted(self, provider_id: str) -> tuple[bool, str]:
        """Return (allowed, reason). Deny by default when the global switch is off."""
        if not self._settings.provider_calls_enabled:
            return False, "provider_calls_enabled is false (M1 default: no external calls)"
        if provider_id in self._settings.provider_denylist:
            return False, f"{provider_id} is on the provider denylist"
        adapter = self._adapters.get(provider_id)
        if adapter is None:
            return False, f"no adapter registered for {provider_id}"
        if adapter.metadata.compliance_status != "permitted":
            return False, f"compliance status is {adapter.metadata.compliance_status}"
        return True, "permitted"

    def assert_permitted(self, provider_id: str) -> None:
        allowed, reason = self.is_permitted(provider_id)
        if not allowed:
            raise ProviderDisabledError(
                "Provider calls are disabled for this integration",
                details={"provider_id": provider_id, "reason": reason},
            )


@dataclass(slots=True)
class ObservationRequest:
    """The typed shape M2 ingestion will use. Defined now so adapters cannot drift."""

    prompt_text: str
    prompt_hash: str
    language: str = "en"
    region: str = "US"
    run_index: int = 0
    window_id: str | None = None
    options: dict[str, Any] = field(default_factory=dict)
