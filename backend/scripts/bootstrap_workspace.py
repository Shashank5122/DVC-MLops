"""Create a workspace and print its key exactly once.

Usage:  python -m scripts.bootstrap_workspace "Acme Analytics" [slug]

This is the production-safe path: no HTTP endpoint, no plaintext key stored, key printed to
stdout for an operator to place in a secret store.
"""

from __future__ import annotations

import sys

from app.core.config import get_settings
from app.core.domain import slugify
from app.db.base import Database
from app.db.models import Workspace, WorkspaceStatus, generate_workspace_key, hash_workspace_key
from app.services import audit
from sqlalchemy import select


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: python -m scripts.bootstrap_workspace <name> [slug]", file=sys.stderr)
        return 2
    name = argv[0].strip()
    settings = get_settings()
    database = Database(settings.database_url, is_sqlite=settings.is_sqlite)
    slug = argv[1].strip().lower() if len(argv) > 1 and argv[1] else slugify(name, max_length=80)

    with database.SessionFactory() as session:
        existing = session.scalar(select(Workspace).where(Workspace.slug == slug))
        if existing is not None:
            print(f"error: workspace slug '{slug}' already exists", file=sys.stderr)
            return 1
        plain_key = generate_workspace_key()
        workspace = Workspace(
            name=name,
            slug=slug,
            key_hash=hash_workspace_key(plain_key),
            key_last4=plain_key[-4:],
            status=WorkspaceStatus.active,
        )
        session.add(workspace)
        session.flush()
        audit.record(
            session,
            workspace_id=workspace.id,
            action="workspace.created",
            entity_type="workspace",
            entity_id=workspace.id,
            actor="bootstrap-script",
            changes={"slug": slug},
        )
        session.commit()
        workspace_id = workspace.id

    database.dispose()
    # Printed once. Not logged, not stored, not retrievable again.
    print(f"workspace_id={workspace_id}")
    print(f"slug={slug}")
    print(f"workspace_key={plain_key}")
    print("Store this key in a secret manager. It cannot be recovered.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
