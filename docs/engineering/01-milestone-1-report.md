# Milestone 1 report — app + database + backend + frontend + brand onboarding

**Date:** 17 Oct 2026
**Branch:** `arena/135d041a-dvc-mlops` (pushed to `origin`; CI run `39019593970` green)
**Status:** implemented, gates run, results recorded below. **Stopped here for founder review** —
M2 has not been started, per instruction.
**Compliance status:** unchanged. No external provider call was made, no money was spent, no
outreach occurred, nothing was published, no trial was registered.

> Integrity rule 18 governs this document: every result below was actually executed in this
> environment. Where something could not be executed here, it says so explicitly instead of
> implying success.

---

## 1. What was built

A working local application: Next.js console → FastAPI API → database, with brand onboarding as
the single vertical slice, tenant isolation, an append-only audit trail, database migrations, and a
provider permission gate that currently blocks everything.

### 1.1 Files created (43 Python files / 3,511 lines; 18 TS/TSX files / 2,206 lines; 749 lines CSS)

**Backend — configuration and cross-cutting (`backend/app/core/`)**
| File | Purpose |
| --- | --- |
| `config.py` | Typed settings from env/`.env`; provider kill-switch + denylist; production validator that refuses SQLite and refuses `provider_calls_enabled=true` |
| `logging.py` | Single-line JSON formatter, `correlation_id` ContextVar, third-party noise suppressed |
| `errors.py` | `AppError` hierarchy → one error envelope; handlers for AppError / HTTPException / RequestValidationError / IntegrityError / SQLAlchemyError / Exception |
| `domain.py` | Pure helpers: `slugify`, `normalise_domain`, `require_non_blank` — no framework or DB imports |
| `tenancy.py` | Resolves `X-Workspace-Key` → workspace row; rejects missing, unknown and suspended keys |

**Backend — data layer (`backend/app/db/`, `backend/alembic/`)**
| File | Purpose |
| --- | --- |
| `base.py` | Declarative base, deterministic constraint naming, engine/session factories, `Database` holder |
| `models.py` | `Workspace`, `Brand`, `Competitor`, `AuditEvent`; key hashing/generation; enum definitions |
| `session.py` | App-scoped engine init/dispose, commit-on-success session dependency |
| `alembic/env.py` | Reads the URL from settings; honours an explicitly configured URL; `render_as_batch`, `compare_type` |
| `alembic/versions/0001_initial_schema.py` | Hand-written initial migration: 4 tables, indexes, composite uniques, FKs with `ON DELETE CASCADE` |

**Backend — API contracts (`backend/app/schemas/`)** — `common.py` (`Page[T]`, `HealthResponse`,
`AuditEventRead`, ORM base), `workspace.py` (create/read/created-with-key), `brand.py`
(create/update/read/detail, duplicate-competitor validator, region upper-casing),
`competitor.py`. All input models use `extra="forbid"`, so a typo'd field is rejected rather than
silently dropped.

**Backend — services (`backend/app/services/`)** — `brand_service.py` (create with nested
competitors, list with search + pagination, get with eager-loaded competitors, update with
before/after change capture, soft delete; competitor add/update/remove; per-workspace duplicate
name and domain checks), `audit.py` (`record`, `list_events` — no update or delete function
exists).

**Backend — HTTP surface (`backend/app/api/`)** — `routes_health.py` (`GET /api/v1/health`),
`routes_workspaces.py` (`GET /workspaces/me`, `GET /workspaces/me/stats`,
`POST /dev/workspaces` — development only), `routes_brands.py` (brand CRUD + nested competitor
CRUD), `routes_providers.py` (`GET /providers` — inventory and permission state, read-only),
`routes_audit.py` (`GET /audit-events` with entity filters and pagination), `main.py` (app factory,
lifespan, correlation-id/request-log middleware, CORS, per-app settings override).

**Backend — provider contract (`backend/app/providers/`)** — `base.py` (`ProviderAdapter` ABC,
`ProviderRegistry` with `is_permitted`/`assert_permitted`, `SurfaceKind`, `CollectionMethod`,
`Capability`, `ProviderMetadata`, `ObservationRequest`), `mock.py` (deterministic fixture adapter,
`fixture_fingerprint()`). **No Gemini adapter. No Perplexity adapter. No HTTP client anywhere.**

**Backend — operations** — `scripts/bootstrap_workspace.py` (creates a workspace, prints the key
once, stores only the hash), `Dockerfile` (python:3.11-slim, non-root UID 10001, healthcheck,
runs `alembic upgrade head` before serving), `.dockerignore`, `requirements.txt`,
`requirements-dev.txt`, `pyproject.toml` (pytest/ruff/mypy-strict configuration), `alembic.ini`.

**Backend — tests (`backend/tests/`, 10 files, 865 lines, 67 tests)** — `conftest.py` (per-test
SQLite DB, app factory, two independent workspace fixtures, postgres skip hook),
`test_health.py`, `test_domain_helpers.py`, `test_brand_onboarding.py`,
`test_tenancy_isolation.py`, `test_workspace_bootstrap.py`, `test_providers.py`,
`test_error_handling.py`, `test_migrations.py`.

**Frontend (`frontend/`)**
| File | Purpose |
| --- | --- |
| `next.config.ts` | Rewrites `/api/backend/:path*` → `BACKEND_ORIGIN/api/v1/:path*`; security headers; standalone output; `allowedDevOrigins` |
| `lib/types.ts` | Hand-written types mirroring the Pydantic schemas, with literal-union enums |
| `lib/api.ts` | Typed client: relative paths only, correlation id per request, `ApiError` exposing `code`/`message`/`details`/`correlationId` and flattened 422 field messages |
| `lib/workspace.ts` | localStorage read/write/clear for the pilot workspace key |
| `app/layout.tsx`, `app/globals.css` | Shell + 749 lines of token-based, responsive CSS (no framework) |
| `app/page.tsx` | Overview: workspace stats, API health, provider switch state, searchable brand grid, recent audit trail |
| `app/setup/page.tsx` | Create a workspace (dev bootstrap) or connect an existing key; shows the key once; states the pilot-auth limitation in the UI |
| `app/onboard/page.tsx` | Brand onboarding: identity, domain, category, language/region, competitor set builder, and the three authorization/verification flags shown as read-only and closed |
| `app/brands/[id]/page.tsx` | Brand record, authorization/verification editing with audit-trail refresh, competitor CRUD, per-brand audit trail, soft delete |
| `app/providers/page.tsx` | Provider inventory + the two compliance denials and their reasons |
| `components/` | `TopBar`, `PageHeader`, `ErrorNotice`, `Pill` (+ verification / relationship / authorization pills), `BrandTile`, `CompetitorTable`, `AuditTrail`, `ProviderTable` |
| `app/not-found.tsx`, `public/robots.txt`, `Dockerfile`, `.dockerignore`, `.env.example`, `package.json` (exact pins), `tsconfig.json` (strict + `noUncheckedIndexedAccess`) | |

**Repository root** — `docker-compose.yml` (PostgreSQL 16 + backend + frontend, healthchecks,
dependency ordering, named volume), `Makefile` (13 targets), `.env.example` (documented, with the
provider policy block), `.gitignore`, `.github/workflows/ci.yml` (3 jobs),
`docs/engineering/00-architecture-decisions.md` (13 ADRs), this report.

### 1.2 Working functionality — verified by hand against the running servers

Backend on `0.0.0.0:8000`, frontend dev server on `0.0.0.0:3000`, SQLite at `backend/signalgeo.db`
(gitignored). Actual observed responses:

| Check | Result |
| --- | --- |
| `GET /api/v1/health` | `{"status":"ok","version":"0.1.0","environment":"development","database":"ok","provider_calls_enabled":false}` |
| `GET /api/v1/providers` | `provider_calls_enabled: false`; denied list `['gemini-grounding-google-search','perplexity-agent-api']`; `mock-deterministic-v1` → `permitted_now: false`, reason `"provider_calls_enabled is false (M1 default: no external calls)"` |
| `POST /api/v1/brands` with a valid key | `201`, `normalised_domain: "demo-brand.example.com"` (from `https://www.demo-brand.example.com`), `slug: "demo-brand"`, `fact_verification_status: "unverified"`, `website_change_authorized: false`, `data_retention_permitted: false`, 2 competitors created |
| `GET /api/v1/brands` with no key | `401` |
| `GET /api/v1/brands` with a wrong key | `401 {"error":{"code":"UNAUTHENTICATED","message":"Invalid workspace key","details":{},"correlation_id":"11dcbc…"}}` |
| `alembic upgrade head` on a real SQLite file | Applied `0001` cleanly; `bootstrap_workspace` then created workspace `demo` (`workspace_id=5240b157-…`) and printed the key once |
| Frontend `GET /api/backend/health` (through the Next proxy) | Returned the backend JSON — the browser path works without CORS and without any localhost reference in client code |
| Frontend pages `/`, `/setup`, `/onboard`, `/providers` | All `200` |
| Frontend security headers | `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin` |
| `GET /api/backend/brands` with no key (through the proxy) | `401` — the envelope passes through unchanged |
| Backend startup log | One JSON line: `{"level":"INFO","logger":"app.main","message":"startup","environment":"development","database_dialect":"sqlite","provider_calls_enabled":false,"version":"0.1.0"}` |

---

## 2. Commands to run locally

**Zero-setup path (no Docker, SQLite).**
```bash
make install                 # backend venv + python deps, frontend npm deps
cd backend
./.venv/bin/python -m alembic upgrade head
./.venv/bin/python -m scripts.bootstrap_workspace "Acme Analytics"   # prints the key ONCE
./.venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# second terminal
cd frontend && BACKEND_ORIGIN=http://127.0.0.1:8000 npm run dev
# open http://localhost:3000 → /setup → paste the key (or create a dev workspace in the UI)
```

**Docker path (PostgreSQL 16).**
```bash
cp .env.example .env         # edit if desired; defaults work as-is
docker compose up --build    # frontend :3000, backend :8000/docs, postgres :5432
docker compose exec backend python -m scripts.bootstrap_workspace "Acme Analytics"
```
The backend container runs `alembic upgrade head` before serving, so schema state has one source of
truth.

**Quality gates.**
```bash
make test        # pytest (SQLite)
make lint        # ruff check + ruff format --check
make typecheck   # mypy --strict (backend) + tsc --noEmit (frontend)
make migrate     # alembic upgrade head
```

---

## 3. Tests and gates actually executed, with results

Environment: Python 3.11.2, Node v22.22.3, npm 10.9.8, Linux sandbox. **No Docker daemon and no
PostgreSQL server exist in this sandbox** — see §4.1.

| Gate | Command | Result |
| --- | --- | --- |
| Backend tests | `pytest -q` | **66 passed, 1 skipped** in 2.45 s (67 collected). The skip is `test_migration_applies_to_postgres`, skipped because `SIGNALGEO_TEST_POSTGRES_URL` is not set. It was **not** passed. |
| Backend lint | `ruff check .` | **All checks passed** (0 errors; rule set `E,F,I,UP,B,S,C4,SIM,RUF`, line length 100) |
| Backend format | `ruff format --check .` | **43 files already formatted** |
| Backend types | `mypy` (strict, pydantic plugin) | **Success: no issues found in 41 source files** |
| Frontend types | `tsc --noEmit` (strict, `noUncheckedIndexedAccess`) | **No type errors** |
| Frontend build | `next build` | **Compiled successfully**; 6 routes: `/` ○, `/_not-found` ○, `/onboard` ○, `/providers` ○, `/setup` ○, `/brands/[id]` ƒ |
| Migration on a real DB | `alembic upgrade head` (SQLite file) | Applied `0001` → 4 tables created; verified again by `test_upgrade_head_creates_every_model_table` (table + column parity with the models, both composite uniques present, no global unique on slug/domain, `workspace_id` indexed on all three tenant tables) and `test_downgrade_to_base_removes_everything` (clean reverse to zero tables) |
| Dependency install | `pip install -r requirements-dev.txt`; `npm install` | 41 Python packages (FastAPI 0.143.3, SQLAlchemy 2.0.55, Pydantic 2.14.1, Alembic 1.20.0); 30 npm packages (Next 16.4.2, React 19.3.1) |
| Live HTTP checks | `curl` against both running servers | All 11 rows in §1.2 |
| CI on GitHub Actions | push → run `39019593970` (commit `7a03639`) | **completed / success**, 3 jobs, 39 s. All steps `success`, including `Alembic upgrade head` and `Tests against PostgreSQL` on a `postgres:16-alpine` service. Raw logs not retrievable from this sandbox — see §4.1. |
| Production config guard | `Settings(environment="production", provider_calls_enabled=True)` | **Refused** with `ValueError` locally, and asserted again by the CI step `Verify production config refuses provider calls` |

**Security-boundary tests that ran (not just feature tests):**
* `test_tenancy_isolation.py` — missing key → 401; wrong key → 401 with a message identical to the
  unknown-key case; workspace B gets **404** (not 403) on workspace A's brand via GET, PATCH and
  DELETE; same for A's competitor via GET, PATCH and DELETE; B's brand list is empty; B's audit
  total is 0; the same brand name is allowed in both workspaces; a malformed UUID path is 422, not
  500; a random UUID does not leak existence.
* `test_workspace_bootstrap.py` — the plaintext key appears exactly once and never again on
  `GET /workspaces/me`; the stored value is a 64-char hash and the plaintext appears nowhere in the
  row; duplicate slug → 409; bootstrap outside development → **403**.
* `test_providers.py` — the registry blocks every call while the switch is off; both denied
  providers stay denied **even with the switch on**; `assert_permitted` raises
  `ProviderDisabledError`; production settings refuse `provider_calls_enabled=true` and refuse
  SQLite; `/providers` is GET-only and no route in the entire OpenAPI schema can trigger a
  collection call.
* `test_error_handling.py` — the envelope shape; a deliberately raised `RuntimeError("synthetic
  failure with secret=abc123")` becomes `500 INTERNAL_ERROR` and the string `secret=abc123`,
  `Traceback`, `RuntimeError` and `brand_service` appear **nowhere** in the response body.
* `test_domain_helpers.py` — 22 parametrised cases over slug and domain normalisation, including
  rejection of `https://`, `not a domain`, `https://example` and `http://a..b`.

**Three real defects were found by these tests during M1 and fixed** — recorded because "tests
passed" is only meaningful if the tests were capable of failing:
1. Enum coercion: `model_dump()` returned enum *instances*, so `CompetitorRelationship(str(...))`
   produced `'CompetitorRelationship.incumbent'` → `ValueError` → HTTP 500 on competitor update.
   Fixed by dumping in `mode="json"`.
2. Alembic `env.py` overwrote an explicitly configured URL with the cached application settings, so
   migrations could target a different database than the caller asked for. Fixed with an explicit
   fallback rule.
3. The migration used a `JSON` *instance* as a callable (`JSONType()`), so `upgrade` failed with
   `TypeError: 'JSON' object is not callable`. Fixed.

---

## 4. Remaining limitations

### 4.1 Environment limits — what could not run here, and what CI has since closed

This sandbox has **no Docker daemon and no PostgreSQL server**. Three limitations were recorded when
the milestone was built; the branch was then pushed to `origin` and CI ran.

| # | Limitation at build time | Status now |
| --- | --- | --- |
| 4.1.1 | **Docker was never run.** `docker-compose.yml`, both `Dockerfile`s and the migrate-before-serve command are written and YAML-validated, but no image was built and no container started here. | **STILL OPEN.** CI does not build the images either. `docker compose up --build` must be run once on a machine with Docker before the container path is treated as verified. |
| 4.1.2 | **PostgreSQL was never queried.** The postgres-marked migration test is skipped locally. | **CLOSED by CI.** Job `backend (migrations on PostgreSQL 16)` ran against a `postgres:16-alpine` service container: `Initialize containers=success`, `Alembic upgrade head=success`, `Tests against PostgreSQL=success`. The full suite (including `test_migration_applies_to_postgres`) therefore passed on PostgreSQL, not just SQLite. |
| 4.1.3 | **CI had not executed.** | **CLOSED.** Run `39019593970` on commit `7a03639`, push to `arena/135d041a-dvc-mlops`: **completed / success**, 39 s, all three jobs green. Every step reported `success`, including `Ruff lint`, `Ruff format check`, `Mypy (strict)`, `Tests (SQLite)`, `Verify production config refuses provider calls`, `TypeScript (strict)`, `Next build`, `npm ci`. |

**Precision about the CI evidence.** Step-level conclusions were read from the GitHub API. The raw
log text could **not** be retrieved from this sandbox (the Actions log host
`results-receiver.actions.githubusercontent.com` is outside the permitted egress list), so this report
does **not** quote CI's pytest counts. The claim is exactly: every step in all three jobs returned
`success`. The quoted counts in §3 are from local execution here.

### 4.2 Scope limitations (deliberate, M1)
4. **No measurement capability at all.** No observations, query registry, evidence, extraction
   metadata, citation analysis, visibility scoring or reports. The console says so on the brand
   page. Nothing in M1 can answer "how visible is this brand?" — it can only record *who* the brand
   is and *what we are allowed to do*.
5. **No user authentication.** One workspace key per tenant, held in `localStorage` on the device,
   not rotated, not revocable per person, readable by any script on the origin. Acceptable for a
   pilot with trusted operators; **not acceptable before real client data is entered**.
6. **No frontend automated tests.** Verification is type-check + build + manual exercise. No
   Playwright/Vitest. The UI's error paths (401 → redirect to `/setup`, 409 messaging, 422 field
   list) are implemented but not machine-tested.
7. **One Alembic revision, hand-written.** Autogenerate parity is asserted by tests, but there is no
   migration linting, no downgrade drill beyond `base`, and no seeded fixture data in migrations.
8. **No rate limiting, no request size limits, no TLS, no CSP, no audit log export, no retention
   policy, no backup procedure.** No observability beyond JSON logs (no metrics, no tracing).
9. **Search is `LIKE` on brand name only** — no full-text search, no filtering by category, region
   or verification status, no cursor pagination beyond `limit`/`offset`.
10. **Enum typing is application-level**, not database-level (`native_enum=False`, ADR-03), so a
    raw SQL write could insert an out-of-range string on PostgreSQL.
11. **Soft-deleted brands still occupy their slug and domain** within a workspace (ADR-08), so
    re-onboarding a deleted brand needs an explicit step.
12. **Version choices differ from the original plan:** Next.js **16.4.2** (not 15) and TypeScript
    **5.9.3** (not 7.0.2 — the new native-port major was not adopted three weeks after release, to
    avoid being an early adopter on a build-critical tool). Both are recorded here rather than
    silently shipped.
13. **Single-process, single-host.** No horizontal scaling story, no background work, no queue.

### 4.3 Known unknowns carried forward
14. Whether `web_search` tool output inside the Perplexity Agent API counts as a "Search Service"
    under Schedule 1 of the Search Addendum (which would deny Output ownership) — **unresolved**,
    gate W2.
15. The full text of Perplexity API ToS §2.1 and the Acceptable Use Policy — **not read**.
16. Perplexity's post-migration Sonar request-fee applicability — **D-b: NOT YET VERIFIED**.
17. Gemini grounding metadata field names — **not verified**, and irrelevant unless gate W1 ever
    produces a permission, which the compliance sheet assesses as unlikely.

---

## 5. Security and cost implications

### 5.1 Security
| Area | Position in M1 |
| --- | --- |
| Tenant isolation | Enforced in schema (composite uniques, non-null `workspace_id`, cascade FKs), in every service query, and by 8 dedicated tests. Cross-tenant access returns 404, not 403. |
| Secrets | Workspace keys stored only as SHA-256 hashes; plaintext printed once by the bootstrap script or dev endpoint; no key or hash in any response model after creation; `.env` gitignored; `.env.example` contains only local defaults. No provider API keys exist anywhere in the repo. |
| Injection | SQLAlchemy Core/ORM expressions throughout; no string-built SQL anywhere; all inputs pass through Pydantic with `extra="forbid"` and length bounds. |
| Information disclosure | One error envelope; generic 500s; no tracebacks, SQL, file paths or stack frames returned; tested with a planted secret string. |
| Tracing | Per-request `X-Correlation-ID` (client-supplied or generated), echoed in headers, present in every log line and every audit event. |
| Authorization flags | `website_change_authorized` and `data_retention_permitted` default **false**, are per-brand, and every change is audited with before/after values — the hooks integrity rules 15 and 9 require before M3 touches a client site or M2 stores raw evidence. |
| Provider policy | Two-layer block (global switch + denylist) plus a production startup refusal. No HTTP client is installed in the backend runtime dependencies, so an accidental provider call is not merely disallowed — it has no library to use. |
| Container | Non-root user (UID 10001) in both images; `python:3.11-slim` and `node:22-alpine`; `.dockerignore` excludes tests, venvs, caches and `.env`. |
| Transport | TLS is out of scope locally and is **not** configured; a real deployment must terminate TLS at a proxy. The frontend sends no cookies, so no CSRF surface exists in M1 (the workspace key is a header, not ambient credentials). |
| **Weakest point** | **The workspace key is a bearer secret held in `localStorage` with no rotation and no per-user attribution.** Any operator with the key has full read/write on that tenant, and the audit trail records `actor="api"` rather than a person. Fix before real client data (ADR-04 revisit condition). |

### 5.2 Cost
| Item | M1 cost |
| --- | --- |
| External API calls | **$0.00 — structurally impossible.** No adapter performs I/O; the only registered adapter returns fixtures with `cost_usd = 0.0`. |
| Spend controls | No spend counter is needed yet because nothing can spend. When M2/M5 add real calls, the compliance sheet's controls K1–K11 (counter, $40 ceiling, $35 abort, per-surface budgets) must be implemented *before* the first billable request, not after. |
| Licensing | All runtime dependencies are MIT/BSD/Apache-2.0 (FastAPI, Starlette, SQLAlchemy, Alembic, Pydantic, psycopg, uvicorn, Next.js, React). **$0 licence cost, no copyleft obligations.** No dependency was added whose licence was not checked. |
| Infrastructure to run this | One small container host: Postgres + API + web. Estimated $5–20/month on a low-end VPS or free tiers for a pilot. **No spend was incurred or authorized in this session.** |
| Engineering cost of the dependency floor | 41 Python packages and 30 npm packages total. Small enough to audit by hand, which is the point (ADR-12). |
| Cost of the compliance block | The two denied providers are also the two cheapest paths to data. Blocking them removes ~$3.65–$8.56 of planned S2 spend from the near-term budget and leaves measurement with **no permitted automated source** until gate W2 resolves. That is a real commercial constraint, not a technical one, and it is the reason M2 must be built on manual/authorized imports first. |

---

## 6. Next smallest step

**Not** "start M2". The smallest useful next step, in order:

1. **Founder review of M1 (this stop).** Specifically: (a) is pilot tenancy via a shared workspace
   key acceptable for the first real pilot workspace, or must per-user auth move into M2? (b) Is the
   ADR-12 dependency floor right, or do you want ESLint and Playwright added before more UI exists?
   (c) Confirm the two provider denials stay hard-coded in the denylist.
2. **Run the Docker path once on a machine with Docker** (`cp .env.example .env && docker compose up
   --build`). CI and the PostgreSQL migration path are now verified (run `39019593970`), so this is
   the **only** remaining unverified claim in this report — limitation 4.1.1. ~20 minutes, $0.
3. **Then, and only then, the first M2 slice:** the query registry alone — one table for commercial
   queries (query text, intent, language, region, hash, registry version, frozen with a SHA-256
   manifest), its migration, its CRUD, and its UI. Deterministic ingestion from the mock provider
   comes after that, then observation storage, then evaluation. One vertical slice at a time, each
   with tests before it is called done.

Nothing in step 3 requires a provider decision, so it can proceed while gates W1/W2 remain open —
but **no observation may be recorded from a real provider until the relevant authorization exists**.
