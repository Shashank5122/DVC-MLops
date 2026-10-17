from __future__ import annotations

import pytest
from app.core.domain import normalise_domain, require_non_blank, slugify
from app.core.errors import ValidationError


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Acme Analytics", "acme-analytics"),
        ("  CloudSEK  ", "cloudsek"),
        ("Rockets & Jets", "rockets-jets"),
        ("Créatif Studio", "creatif-studio"),
        ("a" * 200, "a" * 120),
    ],
)
def test_slugify_is_deterministic_and_ascii(value: str, expected: str) -> None:
    assert slugify(value) == expected
    assert slugify(value) == slugify(value)


@pytest.mark.parametrize("value", ["", "   ", "!!!", "日本語のみ"])
def test_slugify_rejects_unusable_input(value: str) -> None:
    with pytest.raises(ValidationError):
        slugify(value)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("https://www.example.com/path?q=1", "example.com"),
        ("http://example.com", "example.com"),
        ("www.example.co.uk", "example.co.uk"),
        ("EXAMPLE.COM", "example.com"),
        ("app.example.com", "app.example.com"),
        (None, None),
        ("", None),
    ],
)
def test_normalise_domain(value: str | None, expected: str | None) -> None:
    assert normalise_domain(value) == expected


@pytest.mark.parametrize("value", ["https://", "not a domain", "https://example", "http://a..b"])
def test_normalise_domain_rejects_malformed(value: str) -> None:
    with pytest.raises(ValidationError):
        normalise_domain(value)


def test_require_non_blank_trims_and_limits() -> None:
    assert require_non_blank("  Acme  ", field="name") == "Acme"
    with pytest.raises(ValidationError):
        require_non_blank("   ", field="name")
    with pytest.raises(ValidationError):
        require_non_blank(None, field="name")
    with pytest.raises(ValidationError):
        require_non_blank("x" * 500, field="name", max_length=200)
