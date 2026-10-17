# 08 — Validation plan v2 (staged, gated)

**Status: authoritative.** Replaces `08-validation-plan-14-day.md` (removed; the workspace was re-cloned and its history squashed on 16 Oct 2026, so v1 text is **no longer retrievable from git**; every v1 claim that matters is quoted verbatim in `11-correction-log.md`). Created in response to corrections **C-03, C-04, C-05, C-06, C-07** (`11-correction-log.md`).

Depends on: `13-measurement-reproducibility-protocol.md` (how we measure) and `12-economics-v2.md` (what it
must cost and earn).

---

## 1. Principle

v1 tried to validate a company in 14 days with 20 diagnostics, 15 prospect calls, 5 agency interviews and four
written deliverables. The arithmetic did not close: 20 diagnostics at full protocol is **7,500 observations**
and **100–180 delivery hours**, which with everything else totals **160–240 founder-hours — 12–17 hours a day
for two weeks**. It also assumed a cost per diagnostic ($15) that counted data collection only.

v2 is staged. **Stage 1 is deliberately small enough to be completed by one person at a sustainable pace, and
deliberately instrumented so that its own costs become the evidence Stage 2 needs.** No stage expands because
the previous stage was *busy*; each expands only on stated, pre-registered evidence.

**Standing constraints on all stages:**
- **No production platform. No application code.** Spreadsheets, a prompt registry, an immutable raw-response
  store (files), a scripted API client only if it can be written in an afternoon and thrown away, and a document
  template. If a step seems to need a database, a queue, a dashboard or a login, Stage 1 is out of scope for it.
- No consumer-UI scraping. Collection is official search-enabled APIs plus human capture on consumer surfaces.
- No named-brand findings published without written permission.
- Every quantitative claim carries n, surface, runs, window and interval (protocol §9).

---

## 2. Stage map

| Stage | Window | Scope | Cost (cash / founder hours) | Entry condition |
|---|---|---|---|---|
| **0 — Setup** | Day 1 | Protocol freeze, tool seat, raw store, 5 target accounts with named buyers | included in Stage 1 | Phase 1 memo approved |
| **1 — Feasibility & demand** | Days 1–14 | **5 diagnostics · 5 buyer conversations · 2 agency interviews · written protocol · hour+API cost log · ≥1 concrete paid-pilot proposal** | **$408 / 98 h** | G0 passed |
| **2 — Scale test** | Days 15–45 | 20 diagnostics total, 2 measurement windows, findings article at n = 20, 5 agency/channel conversations, 2–3 signed pilots | ~$900–$1,500 / ~150 h | **All three G2 tests passed** |
| **3 — Paid delivery** | Days 46–90 | 3 paying clients under contract, real churn signals, build-vs-buy revisited at N ≥ 10 | revenue-funded | ≥2 signed pilots from Stage 2 |

If the founder cannot commit ~7 h/day, **Stage 1 runs over 21 days at ~4.7 h/day.** That is an allowed change,
logged in `13` §11, and gate dates shift accordingly. Compressing below 98 hours is not allowed — that is how
v1 produced fictional numbers.

---

## 3. Stage 1 scope

**In:** 5 full diagnostics for 5 different companies, deliberately mixed across the top-ranked segments so the
experiment can discriminate between them (`05` §6.1 shows the ranking collapses to a 0.08 spread after
post-correction re-scoring): **3 × S1** (India-origin B2B SaaS selling to US/UK/EU), **1 × S2** (Indian
cybersecurity product vendor selling globally), **1 × S4** (US/EU mid-market B2B SaaS, sold remotely from
India); 5 buyer conversations (the diagnostic recipient counts as a buyer conversation);
2 agency/channel interviews; the written measurement protocol and gold set; a logged hour-and-cost record for
every unit; at least one written paid-pilot proposal with a real price; one methodology article draft
(**not** a findings article).

**Out:** any 6th–20th diagnostic; any paid advertising; any hiring; any platform build; any public claim about
brand counts; any promise of ranking or placement; any conclusion about churn, LTV or scaled CAC.

**Sample size honesty:** 5 diagnostics × 25 prompts × 5 runs × 2 windows × 2 surfaces = **2,500 observations**,
**5 brands**. That supports statements about *method, cost and buyer reaction*. It does **not** support
statements about *category-level visibility patterns*, and no Stage 1 output may imply otherwise.

---

## 4. Stage 1 schedule (98 founder-hours over 14 days)

| Day | Hours | Work | Output |
|---|---|---|---|
| 1 | 7 | Freeze protocol: 25 prompts × 5 diagnostics hashed into the registry; controls documented; buy one month of a measurement tool seat; create append-only raw store; set up hour/cost log | G0 evidence pack |
| 2 | 7 | Build 40-account target list with fit evidence (India-origin, global-selling, research-led category, named buyer); write outreach; **send batch 1 (20)** | list + 20 sends |
| 3 | 7 | **Diagnostic #1** (7 of 9 h) | raw observations |
| 4 | 7 | Diagnostic #1 finish (2 h) · onboard + calibrate annotators on codebook (2 h) · **buyer conversation 1** (1.5 h) · notes/QA (1.5 h) | deliverable #1, call notes |
| 5 | 7 | **Diagnostic #2** (7 of 9 h) | raw observations |
| 6 | 5 | Diagnostic #2 finish (2 h) · extractor QA and per-label F1 against gold batch 1 (3 h) | extraction report |
| 7 | 7 | **Send batch 2 (20)** (3 h) · buyer conversations 2–3 (3 h) · notes (1 h) | **G1 checkpoint** |
| 8 | 7 | **Diagnostic #3** (7 of 9 h) | raw observations |
| 9 | 7 | Diagnostic #3 finish (2 h) · reproducibility statistics for #1–#3 (3 h) · agency interview #1 (1.5 h) · notes (0.5 h) | κ/Wilson/Jaccard/RBO/ICC report |
| 10 | 7 | **Diagnostic #4** (7 of 9 h) | raw observations |
| 11 | 6 | Diagnostic #4 finish (2 h) · buyer conversations 4–5 (3 h) · notes (1 h) | deliverable #4, all 5 conversations done |
| 12 | 7 | **Diagnostic #5** (7 of 9 h) | raw observations |
| 13 | 7 | Diagnostic #5 finish (2 h) · reproducibility statistics, all five (3 h) · agency interview #2 (1.5 h) · decision-band assessment (0.5 h) | full measurement report |
| 14 | 6 | **≥1 written paid-pilot proposal with price** (4 h) · methodology article draft (2 h) · reconcile hour/cost log · write Stage 1 memo | G2 evidence pack |

Day 6 is deliberately light (5 h) as slippage buffer. Outreach is front-loaded so replies land mid-plan; if batch
1 produces fewer than 3 replies by Day 7, the messaging — not the product — is the problem (see G1).

---

## 5. Budget

| Line | Low | Base | High |
|---|---|---|---|
| API/inference (2,500 observations, 2 surfaces, 2 windows) | $60 | $110 | $200 |
| Measurement tool seat, 1 month (Otterly $29 tier or Peec Starter €70) | $30 | $100 | $210 |
| Gold-set annotation, 200 responses × 2 annotators (~27 h @ $4/h) | $50 | $108 | $220 |
| Domain, email, landing page, contract template | $50 | $90 | $150 |
| **Out-of-pocket cash** | **$190 (₹18,050)** | **$408 (₹38,760)** | **$780 (₹74,100)** |
| **Founder hours** | | **98 h** | |
| **Economic cost @ $40/h founder opportunity cost** | **$3,230** | **$4,328** | **$5,480** |
| *Optional: hire diagnostic labour (5 × 9 h @ $7) to cut ~45 founder hours* | *+$315* | *+$315* | *+$315* |

v1's "total ≤ ₹1,30,000" for a 20-diagnostic 14-day sprint is withdrawn: it understated labour by ~3× and the
workload by ~4×.

---

## 6. Logging requirements (this is the point of Stage 1)

Every diagnostic gets a log row, filled in **the same day**:

| Field | Purpose |
|---|---|
| Hours by step (research / prompt design / collection / extraction QA / reproducibility analysis / gateway classification / report / call) | tests the `H_tier` budgets in `12` §3.1 and the 9 h → 5 h templating hypothesis |
| API calls, tokens, cost by surface | tests the $22–$83/client/month API estimate |
| Tool-seat cost actually invoiced | tests A-9 and closes verification gap on live pricing |
| Observations collected / observations usable (retrieval present) | tests F3 retrieval-on rates |
| κ, F1, Wilson half-width achieved | tests protocol acceptance bands |
| Prospect reaction, verbatim, to the interval disclosure | tests whether honest uncertainty sells or repels |
| Any deviation from the frozen protocol, with reason | audit trail (`13` §11) |

**Tolerance tests at G2:** hours per diagnostic ≤ 9 h for #1 and showing a downward trend to ≤ 6 h by #5;
cash cost per diagnostic ≤ $110. If either fails, Stage 2 is re-scoped (fewer prompts, fewer surfaces, cheaper
tooling) and two diagnostics are re-run **before** any expansion — we do not scale a cost structure we have not
made work once.

---

## 7. The five buyer conversations

Same structure each time, ~75 minutes, notes within 24 h. Full script in `07-discovery-interview-guide.md`
(D1), with two mandatory additions:

### 7.1 The most dangerous question (buy-vs-hire test) — new, replaces "would you pay ₹40,000?"

Present both options on one card, in this order, without recommending either:

> **Option 1 — Do it yourself with a tool.** A measurement platform (e.g. Peec Pro ≈ $210/month, Otterly
> ≈ $189/month) tells you where you appear, ranks the opportunities, drafts content changes and names the
> third-party pages worth pitching. Your team executes. Estimated internal effort: 6–10 hours/month.
>
> **Option 2 — We do it.** Same measurement discipline, plus we execute: on-site optimisation staged for your
> approval, and the off-site work — pitching editors and listicles, updating G2/Capterra/TrustRadius profiles,
> producing the comparison and video assets that get cited. $1,500/month (₹1,00,000) or ₹75,000/month for
> on-site only. Estimated internal effort: 1–2 hours/month.

Record, verbatim: which they would choose; why; what they believe their internal staff hour costs; whether they
already use a tool in this category (and which); what would make Option 2 worth it; what would make them cancel
Option 2 in month 4.

**Interpretation rule:** if 4 or 5 of the buyers choose Option 1, the service has no demand at our price and
Phase 1's central recommendation is wrong. That is the outcome this experiment exists to detect, and it must be
reported plainly in the Stage 1 memo, not softened.

### 7.2 Price ladder (willingness to pay, not interest)

Ask in ascending order and record the first "no": ₹40,000 (monitor + report only) → ₹75,000 (managed on-site) →
₹1,00,000 / $1,500 (managed + earned media) → $3,000 (dedicated, weekly cadence). Then ask what they pay today
for SEO/content/PR retainers and who approves it. A "yes" without a named budget line, approver and start date
counts as **interest, not willingness to pay** and is recorded in a separate column.

### 7.3 Co-observation card

Per protocol §7: exact prompt, surface, region, logged-out fresh session, 3 runs inside a named 6-hour window.
Scored against our predictive interval, never against a point estimate. Record their reaction to the intervals
verbatim — including "these numbers move around, so I wouldn't pay for them", which is the most valuable
negative signal available.

---

## 8. Deliverables (Stage 1)

1. Frozen prompt registry + protocol document (`13`, updated with any deviations).
2. Gold set (200 responses), κ per label, extractor precision/recall/F1 report.
3. Five diagnostic reports, each with per-surface intervals, decision band, verified-fact sourcing for every
   recommendation, and an explicit statement of what the report cannot tell the client.
4. Reproducibility report across 5 diagnostics × 2 windows × 2 surfaces.
5. Hour-and-cost log with variance analysis against `12` §3.1/§6.
6. Ten conversation records (5 buyers + 2 agencies + 3 informal), each with the buy-vs-hire choice, price-ladder
   first "no", and verbatim objections.
7. ≥1 written paid-pilot proposal with price, scope, term, authorisation-to-touch-the-site clause, exit clause
   and the measurement disclosure.
8. Methodology article draft (public, no brand counts) — the asset that best tests technical credibility.
9. Stage 1 memo: gate assessment, what we learned, what we would do differently, and a recommendation to
   proceed / re-scope / stop.

**Publishing rules (C-06):** titles may state only counts actually measured; no findings article before
n ≥ 20 brands across two windows; no named-brand deficits without written permission; intervals published
alongside point estimates. At n = 5 we publish **methodology only**.

---

## 9. Gates

### G0 — entry (Day 1)
Protocol frozen and prompts hashed · tool seat purchased and invoiced · raw store append-only · 5 target
accounts identified with a named buyer contact each. **Fail → do not start; fix first.**

### G1 — mid-point (Day 7)
≥2 diagnostics delivered · extractor F1 measured against gold batch 1 · ≥8 replies from the first 20
outreaches · ≥2 buyer conversations completed.
- Replies < 3 → the positioning or the list is wrong, not the product. Rewrite the outreach, re-send to a fresh
  20, and extend Stage 1 by 7 days. Do **not** proceed to G2 on untested messaging.
- Extractor below acceptance → fix before continuing; measurements taken with a bad extractor are worthless.

### G2 — Stage 1 exit (Day 14): three tests, all pre-registered

| Test | Pass criterion | Source |
|---|---|---|
| **T1 Technical credibility** | gold-set κ ≥ 0.80 · extractor F1 ≥ 0.90 (mentions) / ≥ 0.85 (citations) · at least one surface in the Green or Amber band of `13` §8 · every deliverable carried intervals and decision bands | protocol §4–§8 |
| **T2 Cost control** | measured hours ≤ 9 h for diagnostic #1 and ≤ 6 h trend by #5 · cash cost ≤ $110/diagnostic · no undisclosed spend | log §6 |
| **T3 Commercial interest** | ≥1 signed **or verbally committed** paid pilot at ≥₹75,000/mo or ≥$1,000/mo, **or** ≥3 prospects who asked for a priced proposal. "Interesting, keep me posted" = 0 | conversations §7 |

**Outcomes:**

- **GO (all three pass)** → Stage 2: expand to 20 diagnostics with two windows, publish the findings article at
  n = 20 with exact counts in the title, run 5 agency/channel conversations, sign 2–3 pilots. Budget
  ~$900–$1,500 cash and ~150 founder-hours, justified by measured Stage 1 unit costs.
- **CONDITIONAL (T1 + T2 pass, T3 fails)** → the measurement works and is affordable, and nobody is buying.
  **Do not expand.** Run 10 more buyer conversations and re-test the price ladder and the buy-vs-hire card
  before spending anything on Stage 2. Two consecutive failures of T3 = the service hypothesis is dead at this
  price/scope, and the honest options are (a) reposition as a pure measurement/reporting service at Tier A
  pricing (which `12` §5 shows cannot pay a market-rate founder), (b) become a channel for an existing
  platform, or (c) stop.
- **NO-GO on measurement (T1 fails)** → we cannot measure reliably enough to sell honesty as the product.
  Stop the measurement-led positioning; revisit whether a pure execution service (no measurement claims) has
  demand — a materially different, less defensible business.
- **RE-SCOPE (T2 fails)** → the unit economics do not work at current scope. Cut prompts/surfaces or switch
  tooling, re-run 2 diagnostics, and re-gate. Expanding a broken cost structure is how services businesses die.

**No gate outcome is an automatic company kill.** Each triggers a written founder decision recorded in the
Stage 1 memo with the evidence attached — this is the governance rule that replaces v1's threshold-triggered
kill conditions (C-07).

---

## 10. Stage 2 (conditional, days 15–45)

- Diagnostics 6–20 (15 × ≤5 h = ≤75 h), each with two windows ≥7 days apart.
- Reproducibility study extended to 3 surfaces and to the geo factor (IN vs US-East) on one prompt subset.
- Findings article at n = 20 (title states 20 brands, prompt count, observation count, window) — only if the
  publishing rules in §8 are satisfied.
- 5 agency/channel conversations (do agencies resell measurement? what margin do they want? what do their
  clients ask for that they cannot deliver?).
- 2–3 signed paid pilots with 3-month minimum terms, written site-authorisation and rollback clauses.
- Re-test build-vs-buy at N ≈ 5–10 with real invoices in hand (`12` §4.1).

**Stage 2 does not run if G2 is anything other than GO.**

## 11. Stage 3 (days 46–90)

Three paying clients under contract; measure actual delivery hours against `H_tier`; record the first real
churn/renewal signals; decide whether to hire the first delivery analyst (only when contribution covers three
months of loaded cost — `12` §8); revisit the build decision at N ≥ 10.

---

## 12. What we will not do in validation

- Build a platform, dashboard, database, scheduler or multi-tenant anything.
- Scrape consumer AI interfaces, or use any method that violates a provider's terms.
- Publish brand counts we did not measure, or name a brand's deficit without permission.
- Promise placement, ranking, guaranteed citations, or proven revenue lift.
- Optimise anything on a client's site without written authorisation; every change staged, diffed, approved
  item-by-item, reversible.
- Recommend an optimisation not grounded in a verified business fact with a named verifier.
- Treat a vendor's marketing claim, case study or self-reported metric as independent evidence.
- Accept a pilot priced below Tier A economics (a ₹20,000 pilot teaches us nothing and may be
  gross-margin negative).

---

## 13. Risks to the validation itself

| # | Risk | Mitigation |
|---|---|---|
| VR-1 | Cannot get 5 companies to accept a free diagnostic | Free + written permission + no publication without consent; fall back to our own portfolio/affiliate sites and label them as such (weaker evidence, disclosed) |
| VR-2 | Consumer-UI capture is slow and inconsistent between two people | Inter-observer dry run before any prospect test (protocol §7); if agreement is poor, drop the consumer surface and say so |
| VR-3 | Model/version changes mid-window (this category changes weekly — Peec's own changelog logs new models and a renamed search API in a single month) | Record model id per observation; treat a mid-window change as a window break and restart that window |
| VR-4 | Outreach replies come from the wrong persona (agencies, job seekers, tool vendors) | Named-buyer requirement in G0; disqualify and log |
| VR-5 | Founder under-logs hours, reproducing v1's optimism | Log same-day; reconcile on Day 14; variance reported, not smoothed |
| VR-6 | A free diagnostic is treated as the product and no pilot follows | Free diagnostic is explicitly time-boxed and delivered with the priced proposal attached |
| VR-7 | We talk ourselves into GO because we did the work | G2 criteria are pre-registered here, before Day 1, and the Stage 1 memo must quote them verbatim |
| VR-8 | Vendor tool changes pricing/packaging mid-Stage 1 (Profound removed self-serve brand tiers in Sep 2026) | Record the invoice; keep a second tool as fallback; never assume a published price survives 30 days |

---

## 14. Which assumption each activity tests

| Activity | Assumption under test | Result that falsifies it |
|---|---|---|
| 5 diagnostics with full protocol | Measurement can be produced reliably at ≤9 h and ≤$110 | T2 fails |
| Gold set + extractor QA | We read answers accurately (protocol E) | F1 < 0.90 mentions after one fix cycle |
| 2 windows × 5 runs | Observations are stable enough to report (protocol R) | Fleiss' κ < 0.20 on all surfaces |
| Co-observation cards | A buyer can corroborate our numbers | Their observations fall outside our intervals on ≥2 of 3 runs, systematically |
| Buy-vs-hire card | Buyers pay for managed delivery on top of tools they can license | ≥4 of 5 choose Option 1 |
| Price ladder | Willingness to pay exists at ≥₹75,000 or ≥$1,000 | First "no" at or below ₹40,000 for ≥4 of 5 |
| Agency interviews | Agencies are a channel, not just competitors | All 5 say they already deliver this in-house and would not resell |
| Pilot proposals | Interest converts to signed commitment | 0 commitments from ≥3 priced proposals |
| Hour/cost log | `H_tier` and tooling assumptions in `12` | Variance > 40% on any line |
