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
| 3 | Business model & unit economics | Not started |
| 4 | Product definition & MVP | Not started |
| 5 | AI visibility measurement engine | Not started |
| 6 | AEO/GEO optimization intelligence | Not started |
| 7 | Agent architecture & orchestration | Not started |
| 8 | Production system architecture | Not started |
| 9 | Implementation | Not started |
| 10 | Customer acquisition & launch | Not started |

**No application code exists in this repository yet.** That is deliberate: Phase 1 of the brief forbids it,
the go/no-go decision has not been made, and the v2 recommendation (Stage 1) explicitly proposes **no
production platform and no application code** — validation runs on a licensed measurement tool, a hashed
prompt registry, an append-only file store and two human annotators.

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
commitments · Stage 2 engineering or later implementation phases. Each requires the matching gate in
`docs/validation/01-founder-decision-checklist.md`.

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
superseded rather than silently rewritten. **Repository note:** the workspace was re-cloned on 16 Oct 2026 and its history squashed, so the intermediate commits (e5a828b, c6cfc22, 34d7e11, d0538a3) no longer exist in git; all current content is in commit bae95ed and the working tree is the source of truth.

Two standing rules came out of it:
1. **Competitive claims decay in weeks.** Any statement about a competitor's capabilities must come from vendor
   documentation retrieved within ~30 days, and must be re-checked before external use.
2. **Log, don't estimate.** Unit costs and hours are measured on real work before they are used in a plan.

**Primary objective (from the brief):** not to build SignalGEO fast — to discover whether
SignalGEO deserves to be built, find the most profitable and defensible version of it,
and then build that version correctly.
