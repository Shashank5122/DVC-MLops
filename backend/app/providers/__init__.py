"""Provider adapters.

M1 ships interface definitions and a deterministic mock only. No adapter in this package
performs a network request, and `ProviderRegistry.assert_permitted` blocks any attempt while
`provider_calls_enabled` is false or the provider is on the denylist.

Compliance context (docs/validation/08-compliance-decision-sheet.md):
* `gemini-grounding-google-search` is denied: the official Gemini API Additional Terms prohibit
  analysing, collecting, monitoring or storing Grounded Results and Links for this purpose.
* `perplexity-agent-api` is denied pending written commercial clarification (gate W2).
Adding either later requires a code change AND a separate authorization (gate M5).
"""

from __future__ import annotations

from app.providers.base import (
    Capability,
    CollectionMethod,
    ProviderAdapter,
    ProviderError,
    ProviderMetadata,
    ProviderRegistry,
    ProviderUnavailable,
    SurfaceKind,
)
from app.providers.mock import MockProvider

__all__ = [
    "Capability",
    "CollectionMethod",
    "MockProvider",
    "ProviderAdapter",
    "ProviderError",
    "ProviderMetadata",
    "ProviderRegistry",
    "ProviderUnavailable",
    "SurfaceKind",
]
