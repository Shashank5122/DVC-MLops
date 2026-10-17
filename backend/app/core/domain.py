"""Pure helpers for identity normalisation and input validation.

Kept free of framework and database imports so they are trivially unit-testable and reusable
by ingestion jobs in later milestones.
"""

from __future__ import annotations

import re
import unicodedata
from urllib.parse import urlparse

from app.core.errors import ValidationError

_SLUG_RE = re.compile(r"[^a-z0-9]+")
_DOMAIN_RE = re.compile(r"^(?!-)[a-z0-9-]{1,63}(?<!-)(\.(?!-)[a-z0-9-]{1,63}(?<!-))+$")
_MAX_DOMAIN_LEN = 253


def slugify(value: str, *, max_length: int = 120) -> str:
    """Deterministic, ASCII-safe slug. Raises rather than silently returning ''."""
    normalised = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = _SLUG_RE.sub("-", normalised.lower()).strip("-")
    slug = slug[:max_length].rstrip("-")
    if not slug:
        raise ValidationError(
            "Value cannot be converted to a slug", details={"value_length": len(value)}
        )
    return slug


def normalise_domain(website: str | None) -> str | None:
    """Extract a lower-case registrable host from a URL or bare domain.

    Accepts 'https://www.example.com/path', 'www.example.com' and 'example.com'.
    Returns None for empty input; raises ValidationError for malformed input. We do NOT
    attempt to resolve DNS or verify ownership here - that is a separate, logged step.
    """
    if website is None:
        return None
    candidate = website.strip()
    if not candidate:
        return None
    if "://" not in candidate:
        candidate = f"https://{candidate}"
    try:
        host = (urlparse(candidate).hostname or "").lower().strip(".")
    except ValueError as exc:  # malformed URL
        raise ValidationError("Website is not a valid URL", details={"reason": str(exc)}) from exc
    if not host:
        raise ValidationError("Website does not contain a hostname")
    if host.startswith("www."):
        host = host[4:]
    if len(host) > _MAX_DOMAIN_LEN or not _DOMAIN_RE.match(host):
        raise ValidationError(
            "Website hostname is not a valid domain", details={"hostname": host[:120]}
        )
    return host


def require_non_blank(value: str | None, *, field: str, max_length: int = 200) -> str:
    """Trim and length-check a required string field."""
    if value is None:
        raise ValidationError(f"{field} is required")
    trimmed = value.strip()
    if not trimmed:
        raise ValidationError(f"{field} must not be blank")
    if len(trimmed) > max_length:
        raise ValidationError(
            f"{field} exceeds {max_length} characters", details={"length": len(trimmed)}
        )
    return trimmed
