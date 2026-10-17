"""Application configuration.

All settings come from the environment (optionally a .env file) and are validated once at
import time. Secrets are never logged and never have defaults that work in production.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

Environment = Literal["development", "testing", "production"]


class Settings(BaseSettings):
    """Runtime configuration for the SignalGEO backend."""

    model_config = SettingsConfigDict(
        env_prefix="SIGNALGEO_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: Environment = "development"
    app_name: str = "SignalGEO"
    api_v1_prefix: str = "/api/v1"

    # --- database -----------------------------------------------------------
    # SQLite by default so `make test` works with no services running.
    # docker-compose sets this to a PostgreSQL URL.
    database_url: str = "sqlite:///./signalgeo.db"
    db_echo: bool = False
    db_pool_size: int = Field(default=5, ge=1, le=100)
    db_max_overflow: int = Field(default=10, ge=0, le=100)

    # --- security / tenancy -------------------------------------------------
    # Pilot-grade tenancy: a workspace key header. There is no user auth yet.
    workspace_header: str = "X-Workspace-Key"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    # --- observability ------------------------------------------------------
    log_level: str = "INFO"
    log_json: bool = True
    request_log_body: bool = False  # never log bodies by default: they may hold client data

    # --- provider policy (M1: no external calls are made anywhere) ----------
    # Hard kill-switch. Every adapter must consult this before issuing a request.
    provider_calls_enabled: bool = False
    provider_denylist: list[str] = Field(
        default_factory=lambda: [
            # Prohibited by the Gemini API Additional Terms for this use case
            # (docs/validation/08-compliance-decision-sheet.md section 1).
            "gemini-grounding-google-search",
            # Blocked pending written commercial clarification (gate W2).
            "perplexity-agent-api",
        ]
    )

    @field_validator("cors_origins", "provider_denylist", mode="before")
    @classmethod
    def _split_csv(cls, value: object) -> object:
        """Accept comma-separated strings from the environment as well as JSON lists."""
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    @field_validator("log_level")
    @classmethod
    def _upper_level(cls, value: str) -> str:
        level = value.upper()
        allowed = {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}
        if level not in allowed:
            raise ValueError(f"log_level must be one of {sorted(allowed)}")
        return level

    @model_validator(mode="after")
    def _guard_production(self) -> Settings:
        """Refuse obviously unsafe production configurations at startup."""
        if self.environment == "production":
            if self.database_url.startswith("sqlite"):
                raise ValueError("production must not use a SQLite database_url")
            if self.provider_calls_enabled:
                # M1 ships with every provider integration disabled; enabling it in
                # production requires a deliberate configuration change plus approval.
                raise ValueError(
                    "provider_calls_enabled=true is not permitted in production for M1; "
                    "provider integrations require separate authorization (gate M5)"
                )
        return self

    @property
    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")

    @property
    def dev_bootstrap_enabled(self) -> bool:
        """Workspace bootstrap over HTTP is a development convenience only."""
        return self.environment == "development"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the process-wide settings instance (cached)."""
    return Settings()
