"""Initial schema: workspaces, brands, competitors, audit_events.

Revision ID: 0001
Revises:
Create Date: 2026-10-17
"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision: str = "0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

JSONType = sa.JSON().with_variant(JSONB(), "postgresql")


def upgrade() -> None:
    op.create_table(
        "workspaces",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=80), nullable=False),
        sa.Column("key_hash", sa.String(length=64), nullable=False),
        sa.Column("key_last4", sa.String(length=4), nullable=False),
        sa.Column(
            "status",
            sa.Enum("active", "suspended", name="workspacestatus", native_enum=False, length=20),
            nullable=False,
        ),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_workspaces")),
    )
    op.create_index(op.f("ix_workspaces_slug"), "workspaces", ["slug"], unique=True)
    op.create_index(op.f("ix_workspaces_key_hash"), "workspaces", ["key_hash"], unique=True)

    op.create_table(
        "brands",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("workspace_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("website", sa.String(length=300), nullable=True),
        sa.Column("normalised_domain", sa.String(length=255), nullable=True),
        sa.Column("category", sa.String(length=200), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("primary_language", sa.String(length=16), nullable=False),
        sa.Column("primary_region", sa.String(length=16), nullable=False),
        sa.Column(
            "fact_verification_status",
            sa.Enum(
                "unverified",
                "in_progress",
                "verified",
                name="factverificationstatus",
                native_enum=False,
                length=20,
            ),
            nullable=False,
        ),
        sa.Column("website_change_authorized", sa.Boolean(), nullable=False),
        sa.Column("data_retention_permitted", sa.Boolean(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspaces.id"],
            name=op.f("fk_brands_workspace_id_workspaces"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_brands")),
        sa.UniqueConstraint("workspace_id", "slug", name="brand_workspace_slug"),
        sa.UniqueConstraint("workspace_id", "normalised_domain", name="brand_workspace_domain"),
    )
    op.create_index(op.f("ix_brands_workspace_id"), "brands", ["workspace_id"], unique=False)
    op.create_index(
        "ix_brand_workspace_active", "brands", ["workspace_id", "deleted_at"], unique=False
    )

    op.create_table(
        "competitors",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("workspace_id", sa.Uuid(), nullable=False),
        sa.Column("brand_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("slug", sa.String(length=120), nullable=False),
        sa.Column("website", sa.String(length=300), nullable=True),
        sa.Column("normalised_domain", sa.String(length=255), nullable=True),
        sa.Column(
            "relationship_type",
            sa.Enum(
                "direct",
                "indirect",
                "alternative",
                "incumbent",
                name="competitorrelationship",
                native_enum=False,
                length=20,
            ),
            nullable=False,
        ),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspaces.id"],
            name=op.f("fk_competitors_workspace_id_workspaces"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["brand_id"],
            ["brands.id"],
            name=op.f("fk_competitors_brand_id_brands"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competitors")),
        sa.UniqueConstraint("brand_id", "slug", name="competitor_brand_slug"),
    )
    op.create_index(op.f("ix_competitors_brand_id"), "competitors", ["brand_id"], unique=False)
    op.create_index("ix_competitor_workspace", "competitors", ["workspace_id"], unique=False)

    op.create_table(
        "audit_events",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("workspace_id", sa.Uuid(), nullable=False),
        sa.Column("actor", sa.String(length=120), nullable=False),
        sa.Column("action", sa.String(length=80), nullable=False),
        sa.Column("entity_type", sa.String(length=60), nullable=False),
        sa.Column("entity_id", sa.Uuid(), nullable=True),
        sa.Column("changes", JSONType, nullable=False),
        sa.Column("correlation_id", sa.String(length=64), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["workspace_id"],
            ["workspaces.id"],
            name=op.f("fk_audit_events_workspace_id_workspaces"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_audit_events")),
    )
    op.create_index(
        "ix_audit_workspace_created", "audit_events", ["workspace_id", "created_at"], unique=False
    )


def downgrade() -> None:
    op.drop_index("ix_audit_workspace_created", table_name="audit_events")
    op.drop_table("audit_events")
    op.drop_index("ix_competitor_workspace", table_name="competitors")
    op.drop_index(op.f("ix_competitors_brand_id"), table_name="competitors")
    op.drop_table("competitors")
    op.drop_index("ix_brand_workspace_active", table_name="brands")
    op.drop_index(op.f("ix_brands_workspace_id"), table_name="brands")
    op.drop_table("brands")
    op.drop_index(op.f("ix_workspaces_key_hash"), table_name="workspaces")
    op.drop_index(op.f("ix_workspaces_slug"), table_name="workspaces")
    op.drop_table("workspaces")
