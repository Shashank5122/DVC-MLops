# SignalGEO backend (M1)

FastAPI + SQLAlchemy 2.0 + Alembic. PostgreSQL in Docker, SQLite for a zero-setup local run.

**M1 makes no external provider calls.** `SIGNALGEO_PROVIDER_CALLS_ENABLED` defaults to `false`, and
`gemini-grounding-google-search` + `perplexity-agent-api` are denied in configuration regardless of
that switch. See `../docs/validation/08-compliance-decision-sheet.md` and
`../docs/engineering/00-architecture-decisions.md` (ADR-05).

## Run

```bash
python3 -m venv .venv && ./.venv/bin/pip install -r requirements-dev.txt

# zero-setup (SQLite)
SIGNALGEO_DATABASE_URL="sqlite:///./signalgeo.db" ./.venv/bin/python -m alembic upgrade head
SIGNALGEO_DATABASE_URL="sqlite:///./signalgeo.db" ./.venv/bin/python -m scripts.bootstrap_workspace "Acme Analytics"
SIGNALGEO_DATABASE_URL="sqlite:///./signalgeo.db" ./.venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The bootstrap script prints a workspace key **exactly once**; only its SHA-256 hash is stored. Send it
as `X-Workspace-Key` on every tenant-scoped request.

* Health: `GET /api/v1/health` (no key needed)
* Docs: `http://localhost:8000/docs` (disabled in production)
* Provider inventory + permission state: `GET /api/v1/providers`

## Gates

```bash
./.venv/bin/python -m pytest -q              # 66 passed, 1 skipped (postgres) in this repo's M1 run
./.venv/bin/python -m ruff check .           # lint
./.venv/bin/python -m ruff format --check .  # format
./.venv/bin/python -m mypy                   # strict, 41 files
```

Tests run on SQLite. `@pytest.mark.postgres` tests are **skipped** unless
`SIGNALGEO_TEST_POSTGRES_URL` points at a live server; CI runs them against `postgres:16-alpine`.

## Layout

```
app/core/       config (kill-switch, denylist) · logging · errors (one envelope) · domain helpers · tenancy
app/db/         Base · models (Workspace, Brand, Competitor, AuditEvent) · session
app/schemas/    typed request/response models, extra="forbid"
app/services/   brand_service (all queries workspace-scoped) · audit (append-only)
app/api/        health · workspaces · brands · competitors · providers · audit routes
app/providers/  adapter contract · permission registry · deterministic mock (no I/O)
alembic/        env.py + 0001_initial_schema.py
scripts/        bootstrap_workspace.py
tests/          67 tests, including a dedicated tenancy-isolation module
```
