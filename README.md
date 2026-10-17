# SignalGEO — founding repository

Working name: **SignalGEO**. Hybrid SaaS + AI-powered managed service for discoverability across
search engines and AI answer systems (SEO / AEO / GEO / AI-search visibility intelligence).

> This repository was cleared of its previous contents (a DVC/MLOps tutorial project) on
> 2026-10-16 at the founder's instruction and restarted as the SignalGEO working repo.
> The prior history remains in git (`34a2d98` and ancestors).

## Current status

| Phase | Name | Status |
|---|---|---|
| 1 | Market research & problem validation | **v2 complete** — 7 founder-required corrections actioned; **APPROVED WITH CHANGES 16 Oct 2026** |
| 1a | Stage 1 — customer & business validation | **CONDITIONALLY APPROVED 16 Oct 2026.** Operational readiness memo issued: 3 founder-time scenarios (20/30/40 h + 52 h), corrected measurement arithmetic, $0-tooling stack, revised cash request **$40** (cap ₹38,760 unchanged). **30-founder-hour baseline adopted provisionally** (`validation/05-stage1-30-hour-plan.md`): 3 diagnostics, 36 manual captures, 25-response adjudication set, vendor-trial layer excluded. **NO-GO maintained on external activity, purchases, trial registrations, publishing and implementation** — pending S2 (API cap $40), O1/O2/O5 (list, message text, conversations), D1/G-Deliver, D5/G-Proposal |
| 2 | Stage 2 — focused competitive intelligence | **Running (desk research only, authorised).** Matrix tranches 1–2 live: Peec agency pitch projects, Profound agency economics, Scrunch/Otterly pricing and trials, Gemini + Perplexity rate cards all verified 16 Oct 2026 |
| 2b | Provider-use compliance review | **COMPLETE 16 Oct 2026** — `docs/validation/08-compliance-decision-sheet.md`. Gemini Grounding with Google Search **PROHIBITED** for visibility monitoring on 5 independent grounds in the official Gemini API Additional Terms. Perplexity Agent API **BLOCKED** pending written clarification (gate W2). Gates W1/W2 opened; S2 spend **NOT granted** |
| 3 | **MVP implementation — Milestone 1** | **COMPLETE 17 Oct 2026, STOPPED FOR FOUNDER REVIEW.** Working Next.js 16 + FastAPI + database app with brand onboarding, tenant isolation, append-only audit trail, migrations, provider permission gate. Gates run: **pytest 66 passed / 1 skipped** (postgres skip), **ruff clean**, **mypy --strict clean (41 files)**, **tsc --noEmit clean**, **next build clean (6 routes)**. `docs/engineering/01-milestone-1-report.md`. **Docker and PostgreSQL could NOT be executed in this sandbox** — see report §4.1 |
| 3 | Business model & unit economics | **Complete** — `docs/phase-1/12-economics-v2.md` (authoritative) |
| 4 | Product definition & MVP | **M1 implemented** — see Phase 3 row below |
| 5 | AI visibility measurement engine | Not started (M2) — blocked on provider authorization for any automated source |
| 6 | AEO/GEO optimization intelligence | Not started (M3) |
| 7 | Agent architecture & orchestration | **Deliberately not built** — ADR-01/ADR-06: no agent framework; the workflow that needs one ends at a human approval gate |
| 8 | Production system architecture | **M1 slice done** — `docs/engineering/00-architecture-decisions.md` (13 ADRs) |
| 9 | Implementation | **Phase 3 started 17 Oct 2026 — Milestone 1 COMPLETE, awaiting founder review** |
| 10 | Customer acquisition & launch | Not started — O2-b remains gated |

**Application code now exists (Milestone 1, 17 Oct 2026).** The founder authorized provider-independent
software development on 17 Oct 2026 and instructed that M1 be built and then stopped for review. M1 is a
working local app — `frontend/` (Next.js 16 + TypeScript), `backend/` (FastAPI + SQLAlchemy + Alembic),
`docker-compose.yml` (PostgreSQL 16) — covering **brand onboarding only**. It contains **no measurement,
no scoring, no reporting and no provider integration**: `SIGNALGEO_PROVIDER_CALLS_ENABLED=false` is a hard
kill-switch, and `gemini-grounding-google-search` plus `perplexity-agent-api` are denied in configuration
regardless of that switch. No external provider call was made and no money was spent.

Commercial validation remains a **separate workstream** and is not advanced by M1. A working product is not
evidence that anyone will pay for it; the Stage 1 gates in `docs/validation/01-founder-decision-checklist.md`
are unchanged, and the compliance hold in `docs/validation/08-compliance-decision-sheet.md` still governs
provider use.

## Repository layout

```
README.md                                  <- this file
docs/00-master-prompt.md                   <- the operating brief (working copy)
docs/INTEGRITY-RULES.md                    <- research/product/engineering/business integrity rules
docs/validation/                           <- STAGE 1 + STAGE 2 EXECUTION (approved with changes)
  00-integrated-plan.md                    <- START HERE: task-by-task hours, gates, economics, B5/B6
  01-founder-decision-checklist.md         <- what needs approval before money, outreach, delivery
  02-three-option-card.md                  <- software vs agency vs SignalGEO + buyer investigation set
  03-operational-readiness-memo.md         <- REQUIRED DELIVERABLE: 20/30/40/52-hour scenarios, corrected
                                              measurement arithmetic, $0-tooling comparison, revised purchase
                                              approvals, prospect criteria, 14-day schedule, explicit go/no-go
  04-prospect-selection-criteria.md        <- R1-R10 requirements, 8-criterion scoring, cold-outreach fallback
  05-stage1-30-hour-plan.md                <- AUTHORITATIVE Stage 1 schedule: 30 founder-hours
                                              (PROVISIONAL baseline, not confirmed availability),
                                              3 diagnostics, smallest credible measurement design,
                                              14-day dependencies, limitations, $0 contingency
  06-s2-provider-cost-sheet.md             <- S2 sign-off: Perplexity Agent API adapter spec, Gemini
                                              grounding verification, 720-observation cost model
                                              ($5.66 expected / $21.44 worst / $40 cap), controls K1-K11
  07-o1-o2-prospect-shortlist.md           <- O1/O2 sign-off: longlist, recommended candidates, outreach
  08-compliance-decision-sheet.md          <- PROVIDER-USE COMPLIANCE: Gemini grounding PROHIBITED by
                                              official terms (5 grounds); Perplexity API ToS assessed;
                                              written permissions W1/W2; alternatives A-F; rebuilt cost
                                              model ($3.65 expected vs $40 cap); S4 prospects; templates
                                              templates, binding rules (no contact made)
docs/phase-2/                              <- focused competitive intelligence (desk research, authorised)
  01-competitor-capability-matrix.md       <- 16 capabilities x 9 targets, VERIFIED/NOT FOUND labels
docs/engineering/                          <- PHASE 3 IMPLEMENTATION (M1 complete, under review)
  00-architecture-decisions.md             <- 13 ADRs: single service, sync SQLAlchemy, PG+SQLite
                                              strategy, pilot tenancy, provider kill-switch, adapter
                                              contract, audit trail, error envelope, dependency floor
  01-milestone-1-report.md                 <- M1 deliverable: files, verified behaviour, commands,
                                              test/gate results AS EXECUTED, 17 limitations, security
                                              and cost implications, next smallest step
backend/                                   <- FastAPI + SQLAlchemy + Alembic (29 app files, 67 tests)
  app/core/                                <- config (kill-switch, denylist), logging, errors, domain
                                              helpers, tenancy resolution
  app/db/                                  <- Base, models (Workspace/Brand/Competitor/AuditEvent),
                                              session wiring
  app/schemas/                             <- typed request/response models (extra="forbid")
  app/services/                            <- brand + competitor operations, append-only audit
  app/api/                                 <- health, workspaces, brands, competitors, providers,
                                              audit routes
  app/providers/                           <- adapter contract + permission registry + deterministic
                                              mock. NO network I/O, NO Gemini/Perplexity adapter
  alembic/versions/0001_initial_schema.py  <- initial migration (4 tables, composite uniques, FKs)
  scripts/bootstrap_workspace.py           <- creates a workspace, prints its key exactly once
  tests/                                   <- 67 tests incl. dedicated tenancy-isolation module
frontend/                                  <- Next.js 16 App Router + TypeScript (strict)
  app/                                     <- overview, setup, onboard, brand detail, providers, 404
  components/                              <- TopBar, BrandTile, CompetitorTable, AuditTrail,
                                              ProviderTable, ErrorNotice, Pill, PageHeader
  lib/                                     <- typed API client (relative paths only), types,
                                              workspace-key storage
docker-compose.yml                         <- PostgreSQL 16 + backend + frontend, healthchecks
Makefile                                   <- install / test / lint / typecheck / migrate / bootstrap
                                              / dev-backend / dev-frontend / up / down
.env.example                               <- documented local config incl. the provider policy block
.github/workflows/ci.yml                   <- 3 jobs: backend gates, postgres migrations, frontend
docs/phase-1/
  00-decision-memo.md                      <- START HERE (v2): A-I format + decisions D-1...D-6
  01-executive-research-summary.md         <- v2: correction banner + corrected sections 5-9
  02-evidence-register.md                  <- ~90 sources; S13 execution-layer capability (official
                                              vendor docs), S14 managed-service market prices,
                                              S15 Indian labour rates; 20 verification gaps
  03-market-assessment.md
  04-pain-point-map.md                     <- v2: P3/P4 status corrected
  05-icp-scoring-and-ranking.md            <- weighted model + S6.1 post-correction robustness re-score
  06-assumptions-hypotheses-failures.md    <- v2: A1-A16, H1-H12+H3b, decision bands replace auto-kills
  07-discovery-interview-guide.md          <- v2: buy-vs-hire card Q18a, 4-step price ladder,
                                              co-observation card replaces the single-rerun test
  08-validation-plan-v2.md                 <- staged, gated plan: Stage 1 = 5 diagnostics, 5 buyer
                                              conversations, 98 founder-hours, $408 cash, no code
  09-competitive-threats.md                <- v2: four-layer map, verified capability matrix, theses v2
  10-tam-bottom-up.md                      <- S1 valid; S2-S6 SUPERSEDED by 12
  11-correction-log.md                     <- NEW: C-01...C-12, claim as written / correction / evidence
  12-economics-v2.md                       <- NEW, AUTHORITATIVE: formulas, capacity, COGS (buy vs build),
                                              cash vs economic break-even, CAC/LTV, 24-month scenarios
  13-measurement-reproducibility-protocol.md <- NEW, AUTHORITATIVE: extraction vs reproducibility,
                                              gold set, statistics, co-observation, decision bands
```

## How to read this work

Every material claim in `docs/phase-1/` carries a **claim label** — `[VERIFIED]` (primary/official source
retrieved), `[ESTIMATED]` (computed by us from stated assumptions), `[HYPOTHESIS]` (plausible, untested),
`[NOT YET VERIFIED]` (needs a source or experiment we have not run) — plus a source and one of three
credibility tiers. Vendor capability statements are marked `[VERIFIED-VENDOR-CLAIM]`: we verified that the
vendor *documents* the capability, not that it works as described.

- **T1 — Primary/independent**: platform documentation, regulator or peer-reviewed output,
  probability-based survey research (e.g. Pew), official filings.
- **T2 — Vendor research / vendor pricing**: company-published studies, pricing pages, funding
  announcements. Usable, but the publisher has a commercial interest in the narrative.
- **T3 — Secondary aggregator / SEO content farm**: review roundups, stat lists, market-report
  press releases. Used only for directional signal or when it is the only trace of a primary source.

Unverified claims are listed in `docs/phase-1/06-assumptions-hypotheses-failures.md` §4, and the 20 open
verification gaps are at the end of `docs/phase-1/02-evidence-register.md`.

## Current operating authority (16 Oct 2026)

**Approved in principle:** the Stage 1 customer-validation design as revised; parallel focused Stage 2 desk
research; buy-before-build for monitoring; evidence-based measurement with no placement guarantees.

**Not authorised:** spending money · sending outreach or contacting customers · publishing anything · building
or deploying a production platform · changing client websites · signing agreements or making financial
commitments · any external provider API call. Each requires the matching gate in
`docs/validation/01-founder-decision-checklist.md`.

**Added 17 Oct 2026 — implementation authority (provider-independent scope only):** Milestone-based software
development is authorised: M1 app + database + backend + frontend + brand onboarding → M2 query registry,
deterministic ingestion, observation storage, evaluation → M3 recommendations + human approval → M4 client-ready
report, QA, docs, security review. **M5 provider integrations require separate permission.** Binding
restrictions: do not use Gemini Grounding with Google Search for visibility monitoring; do not call the
Perplexity API until written commercial permission is received; do not scrape or automate consumer AI
interfaces; do not register trials, purchase software, incur API charges, contact prospects or publish
anything. **M1 is complete and work has STOPPED for founder review — M2 must not start until M1 is reviewed.**

**Founder hours are NOT yet confirmed** (condition 2): scenarios for **20 / 30 / 40 / 52 h** are prepared in
`docs/validation/03-operational-readiness-memo.md` §1, with 30 h recommended as the defensible floor. Cash cap
**₹38,760** unchanged; **proposed spend is now $40 (₹3,800)** because Peec's free agency pitch projects and the
Gemini free grounding allowance removed almost all cost. **The next milestone is commercial validation, not code completion.**

## Correction discipline (added 2026-10-16)

v1 of this phase contained a material overclaim: it asserted that the mid-market "execution layer" was empty.
Official vendor documentation proved otherwise (Peec Actions incl. earned-media actions + content optimizer +
Peec Agent; Profound AI Marketer/Agents writing into client CMSs; Scrunch/Sitecore apply-or-decline AEO
recommendations in-CMS), and GEO agencies were found to sell the same workstream from $997/month. v1 also used
two inconsistent hour definitions in its economics and treated a single consumer-interface rerun as ground
truth. Every defect, its evidence and its fix is recorded in **`docs/phase-1/11-correction-log.md`**, and v1 is
superseded rather than silently rewritten. **Repository note:** the sandbox has re-cloned this workspace repeatedly and its history has been reset more
than once (commits e5a828b, c6cfc22, 34d7e11, d0538a3, ba95ed/be95ed, d2abb7c, 98a0fda and 76903d6 have each
vanished at some point while the working tree survived). **Nothing in this repository should be described as
"preserved in git history".** The working tree is the source of truth; superseded content is kept as a labelled
file (see `docs/phase-1/11-correction-log.md`), not as a commit reference. As of 17 Oct 2026 the tree is
branched from `34a2d98` with all Phase 1/2 documentation restored and the M1 codebase added.

Two standing rules came out of it:
1. **Competitive claims decay in weeks.** Any statement about a competitor's capabilities must come from vendor
   documentation retrieved within ~30 days, and must be re-checked before external use.
2. **Log, don't estimate.** Unit costs and hours are measured on real work before they are used in a plan.

**Primary objective (from the brief):** not to build SignalGEO fast — to discover whether
SignalGEO deserves to be built, find the most profitable and defensible version of it,
and then build that version correctly.
