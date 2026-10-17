# SignalGEO console (M1)

Next.js 16 App Router + React 19 + TypeScript (strict). Hand-written CSS — no Tailwind, no component
library, no state library (see ADR-11/ADR-12 in `../docs/engineering/00-architecture-decisions.md`).

## Run

```bash
npm install
BACKEND_ORIGIN=http://127.0.0.1:8000 npm run dev    # http://localhost:3000
npm run typecheck                                   # tsc --noEmit (strict)
npm run build                                       # production build
```

## How the browser reaches the API

The browser only ever calls **relative** `/api/backend/*` paths. `next.config.ts` rewrites them to
`${BACKEND_ORIGIN}/api/v1/*` on the server, so:

* no backend origin is baked into a client bundle,
* no CORS preflight is needed for UI traffic,
* the app works behind any host, reverse proxy or preview domain.

`BACKEND_ORIGIN` is server-side only (default `http://127.0.0.1:8000`).

## Pages

| Route | What it does |
| --- | --- |
| `/setup` | Create a workspace (dev bootstrap only) or connect an existing key. Shows the key once. |
| `/` | Overview: brand count, API health, provider-switch state, searchable brand grid, recent audit trail. |
| `/onboard` | Brand onboarding: identity, website → normalised domain, category, language/region, competitor set builder, and the three authorization/verification flags shown as **closed and read-only**. |
| `/brands/[id]` | Brand record, authorization/verification editing (audited with before/after values), competitor CRUD, per-brand audit trail, soft delete. |
| `/providers` | Provider inventory and the two configuration-level denials with their reasons. |

## Pilot limitation, stated in the UI

The workspace key is stored in `localStorage` on the device. This is **not** user authentication: no
accounts, roles, sessions, rotation or per-person attribution. It matches the backend's pilot tenancy
posture (ADR-04) and must be replaced before real client data is entered.

## Not covered

There is no frontend test framework in M1. Verification is `tsc --noEmit`, `next build`, and manual
exercise against the running backend. Adding Playwright is proposed as an M4 QA step.
