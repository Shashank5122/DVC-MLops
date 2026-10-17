"""Read-only provider inventory. No endpoint here can trigger a provider call."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings
from app.providers.base import ProviderRegistry
from app.providers.mock import MockProvider

router = APIRouter(prefix="/providers", tags=["providers"])


def _registry(settings: Settings) -> ProviderRegistry:
    registry = ProviderRegistry(settings)
    registry.register(MockProvider())
    return registry


@router.get("", summary="Registered adapters and their permission status")
def list_providers(settings: Settings = Depends(get_settings)) -> dict[str, Any]:
    registry = _registry(settings)
    items: list[dict[str, Any]] = []
    for metadata in registry.list_metadata():
        allowed, reason = registry.is_permitted(metadata.provider_id)
        items.append(
            {
                **asdict(metadata),
                "permitted_now": allowed,
                "permission_reason": reason,
            }
        )
    denied = list(settings.provider_denylist)
    return {
        "provider_calls_enabled": settings.provider_calls_enabled,
        "adapters": items,
        "denied_pending_authorization": denied,
        "note": (
            "M1 makes no external provider calls. Additions require a code change and separate "
            "authorization (gate M5)."
        ),
    }
