# Integrated execution plan — Stage 1 (customer validation) + Stage 2 (focused competitive intelligence)

**Version:** 1.0 · 16 October 2026 · Issued under the founder's revised decision ("APPROVE WITH CHANGES").
**Owner:** founder. **Prepared by:** research/strategy agent.
**Authority:** Part F of the founder's decision. See `01-founder-decision-checklist.md` for the authorization
gates — **nothing in this plan may touch money, prospects, publishing, client sites or code until the matching
gate is cleared.**

Labels: **[VERIFIED]** · **[PARTIALLY VERIFIED]** · **[ESTIMATED]** · **[HYPOTHESIS]** · **[NOT YET VERIFIED]** ·
**[NOT FOUND]** · **[UNKNOWN]**. FX: ₹95 = $1 (RBI reference rate 95.032, 14 Oct 2026) [VERIFIED].

---

## 1. What changed from the v2 plan, and why

| v2 plan (`08-validation-plan-v2.md`) | Revised under A1–A5 | Reason |
|---|---|---|
| 98 founder-hours / 14 days | **52 founder-hours planned, 60 ceiling** | A2: 98 h was too demanding; do not assume founder availability |
| Document-heavy deliverables | **Agent drafts everything; founder reviews, verifies facts, talks to buyers** | A2: prioritise commercial validation over document production |
| 25 prompts × 5 runs × 2 windows × 2 surfaces = 500 obs/diagnostic (2,500 total) | **15 prompts × 5 runs × 2 windows × 2 API providers = 1,500 controlled observations**, plus a vendor cross-check layer and 60 manual consumer captures. Full arithmetic, the feasibility correction and the three-layer design are in **`03-operational-readiness-memo.md` §2** | Breadth reduced, **not** statistical quality: runs per prompt (5), windows (2) and surface separation are unchanged. **Correction C-13:** the original "2 surfaces" wording hid 750 human captures = 19–38 h, which no founder-hour scenario can absorb |
| 200-response gold set, 2 annotators, κ ≥ 0.80 | **50–100 adjudicated responses now; expand to 200 before any paid client-facing automated extraction** (A3) | A3; and κ needs a second human annotator, which needs spend approval (§5) |
| 2-option buy-vs-hire card | **3-option card: software+internal / agency-or-freelancer / SignalGEO managed** (`02-three-option-card.md`) | A4: commercially realistic comparison |
| "≥4 of 5 choose the tool ⇒ hypothesis dead" | **Withdrawn as an automatic trigger.** Small-sample interpretation rule in §4.4 | A4: no 4-of-5 kill threshold |
| Stage 2 deferred until Stage 1 passed a gate | **Stage 2 desk research runs in parallel, agent-executed** | Part B |

**Protected without exception** (these are the "evidence quality" items A2 says not to trade away):
two measurement windows ≥7 days apart · per-surface separation, never blended · raw evidence + all 14 metadata
factors stored · an adjudication set of ≥50 responses · Wilson intervals on every reported rate · line-by-line
hour and cost logging · at least one formal priced pilot proposal · all five buyer conversations.

---

> **SUPERSEDED for scheduling purposes (16 Oct 2026).** The authoritative Stage 1 schedule is now
> **`../validation/05-stage1-30-hour-plan.md`** (30 founder-hours, provisional baseline; 3 diagnostics;
> 36 manual captures; 25-response adjudication set; vendor-trial layer excluded while NO-GO stands).
> The content below remains valid for scope rationale, gates, economics and Stage 2 workstreams.

## 2. Task-by-task allocation (founder-hours are the binding constraint)

**F** = founder hours · **A** = agent hours (no founder time consumed; founder review is counted separately as F).

### Days 1–3 — Competitive and measurement foundations · **F 9.0 h**

| # | Task | Owner | F | A | Output |
|---|---|---|---|---|---|
| 1.1 | Confirm current features and prices of the 8 priority competitors (B1) | A | 1.5 (review) | 8 | `phase-2/01-competitor-capability-matrix.md` tranche 1 |
| 1.2 | Finalise measurement protocol at reduced scope (A3) | A drafts / F approves | 1.5 | 3 | protocol v1.1 + deviation log entry |
| 1.3 | Build 20-account longlist → **F selects 5 diagnostic candidates** (3 × S1, 1 × S2, 1 × S4) with a named buyer contact each | A builds / F selects | 2.0 | 4 | candidate list + selection rationale |
| 1.4 | Create the 50-response adjudication set (positives, negatives, ambiguous) and label it | F labels / A formats | 3.0 | 3 | adjudication set + per-label precision/recall |
| 1.5 | Define the three-option card + discovery question set | A drafts / F approves | 1.0 | 2 | `02-three-option-card.md` |
| — | *Stage 2 started in parallel:* capability matrix, pricing verification | A | — | (in 1.1) | — |

### Days 4–7 — Customer evidence · **F 17.0 h**

| # | Task | Owner | F | A | Output |
|---|---|---|---|---|---|
| 2.1 | Diagnostics #1–#3: collection, extraction, statistics, draft report | A | — | 18 | 3 draft reports + reproducibility stats |
| 2.2 | Per diagnostic: verify every business fact, QA the report, deliver, log hours/cost | F | 9.0 (3 h each) | — | 3 delivered diagnostics + 3 log rows |
| 2.3 | Buyer conversations #1–#3 (75 min + notes within 24 h) | F | 4.5 | 1.5 (prep briefs) | 3 scored conversation records |
| 2.4 | Outreach batch 2 + follow-ups (batch 1 sent only after gate **G-Spend/G-Outreach**) | F | 1.5 | 2 | send log, reply log |
| 2.5 | Review matrix tranche 1; compare buyer needs against competitor capabilities | F | 2.0 | 3 | gap list v1 |

### Days 8–11 — Commercial testing · **F 17.0 h**

| # | Task | Owner | F | A | Output |
|---|---|---|---|---|---|
| 3.1 | Diagnostics #4–#5 (as 2.1/2.2) | F 6.0 / A | 6.0 | 12 | 2 delivered diagnostics + logs |
| 3.2 | Buyer conversations #4–#5 | F | 3.0 | 1 | 2 scored records |
| 3.3 | Agency interviews ×2 (D2 script, incl. white-label questions 8/8a) | F | 2.0 | 1 | 2 agency records |
| 3.4 | Present the three options; test price rungs and who does the work; ask for a pilot or deposit | F | 3.0 | — | option choices, first "no" rung, commitments |
| 3.5 | Update unit economics with **actual** delivery cost (Part C) | A | 1.5 (review) | 4 | `12-economics-v2.md` addendum |
| 3.6 | Differentiation hypotheses H1–H4 assessment (B3) | A | 1.5 (review) | 6 | `phase-2/02-differentiation-hypotheses.md` |

### Days 12–14 — Integrated decision · **F 9.0 h**

| # | Task | Owner | F | A | Output |
|---|---|---|---|---|---|
| 4.1 | ≥1 formal paid-pilot proposal (personalise, price, term, site-authorisation + rollback + exit clauses) | F | 2.5 | 3 | proposal, sent only after gate **G-Outreach** |
| 4.2 | Finalise competitive gaps, citation-gateway assessment (B4), build-vs-buy (B5), recurring value (B6) | A | 3.0 (review) | 10 | `phase-2/03…05` |
| 4.3 | Determine most promising ICP from actual responses; recommend service vs software vs agency-channel | F+A | 2.0 | 3 | positioning recommendation |
| 4.4 | Integrated decision pack + **GO / MODIFY / STOP** memo | A drafts / F decides | 1.5 | 5 | `validation/03-decision-pack.md` |

**Founder total: 9 + 17 + 17 + 9 = 52 h** (ceiling 60 h; 8 h held as contingency). **Agent total ≈ 90 h**,
which is why the plan fits at all — and why §7.4 costs agent work explicitly rather than treating it as free.

### 2.1 Degradation ladder (A2: "recommend the smallest credible scope rather than reducing evidence quality")

If founder hours run short, cut in this order and record the cut in the deviation log:

| Level | Change | Observations | Founder hours | Evidence lost |
|---|---|---|---|---|
| **L0** planned | 5 diagnostics × 15 prompts | 1,500 | 52 | — |
| L1 | prompts 15 → 10 | 1,000 | ~47 | prompt-set breadth only; per-prompt precision unchanged |
| L2 | diagnostics 5 → 4, **keep all 5 buyer conversations** | 800 | ~44 | one segment data point (drop S4 or the second S1) |
| **L3 floor** | 3 diagnostics + 5 conversations + 2 agency interviews | 600 | ~38 | segment discrimination between S1/S2/S4 |
| Below L3 | **Do not cut further — extend to 21 days instead** | — | — | cutting here would degrade evidence quality, which A2 forbids |

Never cut, at any level: the second window, surface separation, the ≥50 adjudication set, intervals in every
deliverable, hour/cost logging, the priced proposal, or the number of buyer conversations.

---

## 3. Measurement reliability at reduced scope (A3)

| Element | Stage 1 (now) | Before paid client-facing automated extraction |
|---|---|---|
| Adjudication set | **50–100 responses**: positives, negatives, ambiguous, stratified across surfaces | **200 responses** |
| Annotators | Founder only (single-annotator) → **κ is NOT MEASURED**; extraction precision/recall are reported against founder labels with that limitation disclosed in every deliverable | 2 independent annotators + adjudicator → **Cohen's κ ≥ 0.80** required. Needs spend approval (§5, item 3) |
| Runs per prompt | 5 | 5 (10+ for any comparison claim) |
| Windows | 2, ≥7 days apart | 2 minimum; 3 for trend claims |
| Surfaces | 1 official search-enabled API + 1 human-captured consumer surface, **never blended** | same, plus per-surface sample sizes stated |
| Uncertainty | Wilson 95% interval on every rate; rule-of-three upper bound (3/n) for absence; Fleiss' κ across runs; Jaccard on citation sets; RBO on ordering | same + power statement for any lift claim (≈42 runs/arm for 0.30→0.60) |
| Metadata | All 14 factors per observation (surface, model id, retrieval evidence, geo, session state, plan tier, device, time, date, prompt hash, run index, answer shape, capture method, cost) | same, immutable append-only |
| Ground truth | **No such thing for reproducibility.** Prospects use the co-observation card, scored against the interval | same |

**A3 compliance notes.** Single-answer disagreement is never treated as measurement failure — it is one draw
from a distribution, and the band assessment in `13` §8 requires a *systematic* pattern across prospects and
surfaces before any methodology review is triggered. No confidence is invented: where n is too small for a
claim, the deliverable says "not observed in n = 5; 95% upper bound 60%" rather than "invisible". No placement
is guaranteed, ever.

---

## 4. Commercial experiments (A4, A5)

### 4.1 The three-option card
Full card, wording and scoring in **`02-three-option-card.md`**. Summary:

| | Option A — software + internal execution | Option B — agency or freelancer | Option C — SignalGEO managed |
|---|---|---|---|
| What they buy | Peec $95–$495/mo [VERIFIED today], Otterly $29–$489, Semrush $99/domain | Retainer $997–$20,000/mo (published offers) | ~$1,500/mo (₹1,00,000) or ₹75,000/mo on-site only — **price under test, not asserted** |
| Who does the work | Their team, 6–10 h/mo | Agency team | Us, with their approval on every change |
| Their internal effort | 6–10 h/mo | 2–5 h/mo (briefing, approvals) | 1–2 h/mo |
| Measurement | Vendor dashboard | Agency report (tool-derived) | Our protocol: intervals, per-surface, disclosed extraction error |
| Earned media | Vendor names the opportunities; they pitch | Agency pitches (often white-labelled) | We pitch, with verified facts only |
| Main risk | Nobody acts on the readings | Volume drops after month 3; disclosure quality unknown | Capacity-capped; we are unproven |

### 4.2 Buyer investigation set (asked of every buyer)
Budget owner and approver · tools and agencies already used and what they pay · current monthly spend on
SEO/content/PR · **what work is identified but not done** · internal execution capacity (hours/month, whose) ·
the **specific result that would justify payment** · what would make them switch vendors · which of A/B/C they
would buy and why · would they sign a paid pilot or pay a deposit.

### 4.3 Evidence hierarchy for commercial commitment (A5)

| Tier | Evidence | Weight |
|---|---|---|
| **T1 — commitment** | Signed paid pilot, or advance payment / deposit received | Decisive |
| **T2 — procurement signal** | Formal proposal requested with a price **plus** written budget confirmation, or a named procurement process with a date | Strong |
| **T3 — next action** | Calendar commitment to a decision meeting, or introduction to the economic buyer | Moderate |
| **T4 — not evidence** | "GEO is important", "interesting", "keep me posted", "send me more info" | **Zero** — logged separately, never counted toward a pass |

### 4.4 Small-sample interpretation rule (replaces the 4-of-5 trigger)
At n = 5, every count is directional. Rules: (1) report **counts and verbatim reasons**, never percentages, in
the decision pack; (2) a pattern only becomes a conclusion when it is **consistent across segments and
explained** — e.g. 3 of 5 choose Option A *and* all three give the same reason (no internal capacity to act is
different from preferring a dashboard); (3) any signal that would have triggered a kill in v1 instead triggers
a **written reasoning note** from the founder plus a named next test; (4) the strongest single observation
(a deposit, or a refusal with a stated price) outweighs the vote count.

---

## 5. Budget — cap ₹38,760 ($408), **not** mandatory spend. Every line needs gate **G-Spend**.

| # | Item | Low | Base | High | Needed for | Gate |
|---|---|---|---|---|---|---|
| 1 | ~~Peec Starter $95~~ → **S1a: free-trial vendor accounts** — Peec agency trial gives **5 free 7-day pitch projects outside the client quota** [VERIFIED peec.ai/for-agencies + /pricing-agencies, 16 Oct 2026]; Otterly free trial (50 prompts) or Scrunch 7-day trial (no card) as cross-check | **$0** | **$0** | $0 (S1/S5 withdrawn; Starter covers only 1 project so it cannot serve 5 candidates) | Measurement cross-check **and** hands-on verification of Peec Actions/gap analysis (gap CG-6) | G-Spend + new account-creation approval |
| 2 | Provider API spend — **Perplexity Sonar (Agent API) ≈$9 + Gemini 3 Flash grounding ≈$2.50 + ~25% retries ≈$4 = ≈$16 expected** for 1,500 observations (rate card: `03-operational-readiness-memo.md` §3.3) | $16 | **$20** | **$40 cap** (was $110) | L1 controlled repetitions | G-Spend |
| 3 | ~~Second annotator $56–$110~~ — **DEFERRED by founder decision**: κ reported as **NOT MEASURED**; extraction precision/recall is founder-referenced only, and automated extraction may not be used for paid client-facing reporting in Stage 1 | $0 | **$0** | $0 | Inter-annotator agreement | — |
| 4 | ~~Domain, email, one-page site, contract template~~ — **DEFERRED**: not essential for any approved interaction (diagnostics deliver as PDF; the proposal is a plain document). Re-request only if a prospect asks for a site or a countersigned contract | $0 | **$0** | $0 | — | — |
| 5 | **Total proposed cash** | **$16 (₹1,520)** | **$20 (₹1,900)** | **$40 cap (₹3,800)** | **90% below the ₹38,760 ceiling, which is unchanged** | |

**Revised 16 Oct 2026 under condition 4 of the founder's decision — this table's v1.0 request is superseded by
`03-operational-readiness-memo.md` §3–§4.** The binding constraint on licensed tooling is **projects and
workspaces, not seats** [VERIFIED]: Peec Starter = 1 project, Pro = 2, Advanced = 5; Peec **agency** plans
(Essential €205 / Growth €425 / Scale €675 per month) include live client accounts **plus free 7-day pitch
projects that sit outside the client quota**; Profound Agency Growth is $99/month with 10 pitch workspaces and
then **$399 per real client workspace**; Scrunch Starter is $250/$300 with a 7-day no-card trial; Otterly Lite
is $29 with a free trial. Five candidates are therefore coverable for **$0** through Peec's free pitch projects,
which is why **S1 ($95) and S5 ($495) are withdrawn** rather than deferred, and why the proposed cash total falls
from $321 to **$20 (cap $40)** — 90% below the unchanged ₹38,760 ceiling. S3 (annotator) and S4 (domain/contract)
are **deferred by decision**: κ is reported as NOT MEASURED, and no website or contract spend occurs unless a
prospect requires it.

---

## 6. Stage 2 — parallel competitive intelligence (Part B)

**Central question:** *what commercially valuable work can SignalGEO perform that platforms, agencies and
in-house teams do not already provide adequately?*

Execution: agent-led desk research from official documentation, changelogs, pricing pages, developer docs,
verified case studies and credible customer evidence. **No broad Phase 1 market research is repeated.**
Founder review hours are already budgeted (1.5 + 2.0 + 1.5 + 3.0 = 8 h).

| Ref | Workstream | File | Status |
|---|---|---|---|
| B1 | Verify 8 priority targets: Peec, Profound, Scrunch/Sitecore, Otterly, Semrush, Ahrefs, 2 managed GEO agencies, 1 white-label provider. Confirm the Oct-2026 execution-layer developments. Label every capability **VERIFIED / PARTIALLY VERIFIED / NOT FOUND / UNKNOWN**; an undocumented capability is **never** described as absent | `phase-2/01-competitor-capability-matrix.md` | **Started today** — Peec column verified from the official pricing page and changelog |
| B2 | Capability matrix across the 16 dimensions listed in Part B2, with links, verification dates, limitations | same file | tranche 1 drafted |
| B3 | Test differentiation hypotheses **H1 managed execution · H2 vertical specialisation · H3 commercial-outcome intelligence · H4 agency infrastructure** on 10 criteria each, with explicit invalidating evidence | `phase-2/02-differentiation-hypotheses.md` | Days 8–11 |
| B4 | Critical evaluation of the citation-gateway thesis on the 8 questions in Part B4 | `phase-2/03-citation-gateway-assessment.md` | Days 12–14 |
| B5 | Build-vs-buy economic validation (§9 below is the interim answer) | `phase-2/04-build-vs-buy.md` | Days 12–14 |
| B6 | Recurring-value business-model test (§8 below is the interim answer) | `phase-2/05-recurring-value.md` | Days 12–14 |

Verification discipline: capability claims must come from vendor documentation retrieved within ~30 days, carry
a retrieval date, and be re-checked before any external use. Three reviews published 26 Aug – 26 Sep 2026 said
Peec had no content generation; Peec's 13 Oct 2026 changelog disproves them. **That error is the reason this
discipline exists** (`11-correction-log.md` C-01).

---

## 7. Unit economics (Part C) — three commercially feasible offerings

Baseline is `12-economics-v2.md` with Tier A 5 h / B 12 h / C 21 h per client-month, blended delivery rate
$7/h [ESTIMATED, grounded in register §15], founder opportunity cost $40/h, fixed cash $600/mo.

### 7.1 Offering 1 — paid diagnostic / implementation project (one-time)

| Price | V (9 h founder-led) | V (6 h agent-assisted) | Contribution | GM |
|---|---|---|---|---|
| $497 (market reference: SourceRank audit) | $88 | $67 | $409–$430 | **82–87%** |
| ₹40,000 ($421) | $88 | $67 | $333–$354 | 79–84% |
| ₹75,000 ($789) | $88 | $67 | $701–$722 | **89–92%** |
| ₹1,00,000 ($1,053) | $88 | $67 | $965–$986 | 92–94% |

V = hours × $7 + $25 API/tool per engagement [ESTIMATED]. **Verdict:** excellent margin, zero recurrence, and
CAC is never amortised — a project business must re-sell every month. Use it as the **entry wedge** with a
measured conversion rate into Offering 2, never as the business. Stage 1 cannot measure that conversion (it
needs months); it can only measure whether the project sells at all.

### 7.2 Offering 2 — managed monthly execution (from `12`)

| Tier | H | V (base tooling) | GM @ ₹40,000 | GM @ ₹75,000 | GM @ ₹1,00,000 | GM @ $1,500 | Cash BE | **Economic BE** |
|---|---|---|---|---|---|---|---|---|
| A measure & advise | 5 | $147 | +65% | — | — | — | 3 clients | ~30 clients |
| B managed on-site | 12 | $198 | — | +75% | — | — | 1 | 11 |
| C managed + earned | 21 | $264 | — | — | +75% | **+82%** | **1** | **5** |

Capacity: 4.3–6.2 clients per delivery FTE at Tier C; 7.5–10.8 at Tier B; 18–26 at Tier A.

### 7.3 Offering 3 — agency white-label (per agency client workspace / month)

| Price | Hours | V (tooling $30 / $100) | GM | Contribution |
|---|---|---|---|---|
| $250 | 3–6 | $57–$79 / $127–$149 | 68–77% / 40–49% | $171–$193 / $101–$123 |
| **$350** | 3–6 | $57–$79 / $127–$149 | **77–84% / 57–64%** | **$271–$293 / $201–$223** |
| $500 | 3–6 | $57–$79 / $127–$149 | 84–89% / 70–75% | $421–$443 / $351–$373 |

Clients per FTE at 3–6 h: **18–37** — the best capacity ratio of the three offerings, because the agency owns
client communication and reporting. **But:** one agency with 8 clients puts $2,800/mo at risk in a single
relationship; and Peec already sells **agency plans** (official pricing page links a separate agency pricing
page; a T3 source reports $245/$495/$795 on credits — **[PARTIALLY VERIFIED]**), and Profound sells agency
workspaces at $399/mo. So H4 cannot be "we give agencies tooling" — it must be **"we give agencies verified
human delivery + measurement QA they cannot staff"**, which is a services contract, not a platform.

### 7.4 Agent-labour costing rule (new, and it matters)

Agent hours are **not free** and must not be allowed to inflate margin silently. Rule: for every task the agent
performs, log (a) agent hours, (b) actual AI/API spend, and (c) the founder's review/QA hours. For COGS, charge
the **higher of** actual AI spend **or** the analyst-rate proxy ($7/h) for the portion a hired analyst would have
done — **plus 100% of the human verification time, which does not shrink.** Rationale: fact verification,
approval decisions and client accountability are irreducibly human (integrity rules 9, 15, 16), so the binding
constraint on agent-assisted delivery is review capacity, not drafting capacity. **Whether agent-assisted
delivery genuinely beats a $7/h analyst is a [HYPOTHESIS] that Stage 1's log will answer**; if it does, it is the
first real cost advantage we have found — and it is an operational one, not a moat.

### 7.5 Headcount reconciliation (no ARR claim without it)

`FTEs = ARR / (12 × P) × H_tier / H_eff`, `H_eff` = 110. $2M ARR at $1,500/mo = 111 clients = **21.2 Tier-C
FTEs** or 12.1 Tier-B FTEs. Any projection presented later must carry this line, plus churn, sales throughput
and capital requirement (Part C).

---

## 8. B6 — Recurring value: the mandatory business-model test

**Why would a customer keep paying after the first audit and optimisation?**

| Recurring driver | Evidence | Monthly hours (Tier C) |
|---|---|---|
| The measured distribution genuinely moves | Exact-repeat citation rate **0.06%** (12,778 ChatGPT answers); source overlap **34–42%** day-to-day; brand Jaccard 0.45–0.59; ~30% brand persistence run-to-run; content >3 months stale loses **>3×** citations | 1.0 (re-measure, 2 windows) |
| Models and surfaces churn | Peec's changelog logs new models monthly and a renamed search API ("OpenAI Search API" → **OpenAI Luna**) within a single quarter [VERIFIED] | 0.5 (prompt-set + surface refresh) |
| Competitors act | New listicles, reviews, comparison pages and vendor content enter the cited set continuously | 1.0 (gateway refresh, new targets) |
| The client's own facts change | New features, pricing, claims, certifications → the verified-fact base must be re-verified before anything is published | 1.0–2.0 |
| Earned media is a cadence, not a project | Pitch → place → re-measure → next target; placements decay and need replacing; 95% of AI-cited links are non-paid, so this cannot be bought once | 2.0–4.0 |
| Profiles and review platforms drift | G2/Capterra/TrustRadius/analyst-profile accuracy, Q&A, listing data | 0.5–1.0 |
| Reporting, QA, accountability | Interval-based report, verification of every claim, approval trail, rollback readiness | 2.5 |

**The honest limit — stated here so it is never hidden from a client:** at Tier A (5 h/month) the recurring
deliverable is mostly **labour substitution and cadence**, not new information. With ±0.33 intervals at n = 5,
much of the month-to-month informational delta sits inside the noise. **Recurring value must therefore be sold
as capacity, cadence and accountability — not as "fresh intelligence every month."** Selling the latter would
be manufacturing work, which integrity rule 21 forbids.

**When a customer should reasonably downgrade or cancel** — to be published in the contract, not negotiated
later. Step down to quarterly monitoring when all four hold: (i) mention probability for the core prompt
cluster is stable across **3 consecutive windows**; (ii) the top-5 gateways are actioned and placements are
live; (iii) no material product, competitor or model change; (iv) the client has internal capacity to maintain.
Cancel is appropriate when the client in-houses the work or when their query cluster stops moving.

**Is SignalGEO naturally recurring, project, software or hybrid?** **Hybrid, with a project-shaped entry and a
cadence-shaped core:** paid diagnostic (Offering 1) → 90-day managed sprint (Tier B/C) → maintenance retainer
(Tier A or quarterly) → optional agency white-label (Offering 3) for distribution. Software only where §9 says
build.

**What honesty about step-down costs us** [ESTIMATED]: if Tier C clients step down to a $400/mo maintenance
tier after month 6, LTV falls **−36% at a 12-month life, −54% at 24 months, −60% at 36 months**
($29,656 → $13,719 at 24 months). LTV:CAC on economic CAC ($4,328) is then **3.2× at 24 months, 2.2× at 12** —
still viable, and these are the numbers we should plan with. **We plan for step-down rather than resist it**,
because resisting it is exactly how agencies invent work.

---

## 9. B5 — Build vs buy: interim economic validation

Founder's provisional decision (**buy or integrate rather than build a competing monitoring platform**) is
**supported by the arithmetic** [ESTIMATED]:

| Path | Per-client cash cost | Plus | Verdict |
|---|---|---|---|
| License one tool | Peec $95/project/mo (1 project) → **$99/client at Advanced's 5 projects**; Otterly $29–$489; Profound agency $399/workspace | zero build time; vendor absorbs model churn; **project-count limits bind** (Starter = 1 project) | **Use now** |
| Official provider APIs + small internal scripts | $22–$83/client/mo | ~40 h/mo engineering = **$160/client at N=10**, $80 at N=20, $53 at N=30, $40 at N=40 | Not cheaper until **N ≈ 25–30** |
| Manual measurement (human capture) | 1.5–3 min/observation → 300 obs = **7.5–15 h = $52–$105** per diagnostic in capture alone | the only ToS-safe route to consumer surfaces; cannot reach ~42 runs/arm for lift claims | Use for a **small consumer baseline only** (e.g. 10 prompts × 3 runs) |
| **Hybrid (recommended)** | APIs for volume + human capture for a consumer baseline + one licensed seat for cross-check and client-facing views | ~$120–$190/client/mo at N=5, falling with scale | **Best at validation scale; revisit at N ≥ 25** |

**Licensing restrictions / portability / lock-in:** Peec's official pricing page lists **CSV export**, **API**
and **MCP** under Data access, with API/SSO shown at the Enterprise tier **[PARTIALLY VERIFIED — needs
per-plan confirmation]**. Lock-in is **low if and only if we keep our own raw-evidence store**, which protocol
§3 already requires: prompt registry, raw responses and all 14 metadata factors are ours, so a vendor change
costs re-analysis, not re-collection.

**What, if anything, should eventually be built internally:**
1. **Raw-evidence store + factor metadata** (protocol §3) — cheap, ours, and no vendor records retrieval
   evidence, session state and prompt hash the way our protocol requires. *Build, eventually.*
2. **Gold-set / extractor validation harness** — a QA asset that produces the F1 and κ numbers we publish.
   *Build, eventually; it is the credibility mechanism.*
3. **Interval-based client report template** — a document, not software. *Never build.*
4. Sampling collectors, dashboards, scoring, prompt discovery, citation-source mapping, gap analysis, action
   ranking — **all commoditised and all shipped by incumbents.** *Never build.*

**Do not assume proprietary development is cheaper or creates a moat:** confirmed on both counts. Licensing is
cheaper until N ≈ 25–30, and neither path creates a moat — the moat question is answered in B3/B4, not here.

---

## 10. Deliverable map (Part E) — where each of the nine will live

| # | Required deliverable | File | When |
|---|---|---|---|
| 1 | Stage 1 customer validation report (what buyers said; evidence vs assumption) | `validation/03-decision-pack.md` §1 | Day 14 |
| 2 | Stage 2 competitor matrix (verified features, pricing, positioning, gaps) | `phase-2/01-competitor-capability-matrix.md` | Days 1–3, 12 |
| 3 | Differentiation assessment (which claims survive verification) | `phase-2/02-differentiation-hypotheses.md` | Day 11 |
| 4 | Commercial experiment results (option choices, budget ownership, WTP, commitments) | `validation/03-decision-pack.md` §4 | Day 14 |
| 5 | Updated economics (delivery costs, price sensitivity, margins, founder-compensated break-even) | `12-economics-v2.md` addendum | Day 11 |
| 6 | Recommended business model (services / software / agency channel / hybrid) | `validation/03-decision-pack.md` §6 | Day 14 |
| 7 | Build-vs-buy recommendation (integrate / build / manual / defer per capability) | `phase-2/04-build-vs-buy.md` | Day 13 |
| 8 | Next-stage roadmap (smallest commercially justified milestone) | `validation/03-decision-pack.md` §8 | Day 14 |
| 9 | Decision memo — **GO / MODIFY / STOP** with unresolved risks and alternatives | `validation/03-decision-pack.md` §9 | Day 14 |

Supporting research stays in `02-evidence-register.md` (new §16 for Stage 2 retrievals) and the `phase-2/`
files. **No duplication of the long Phase 1 reports**: Stage 2 cites them rather than restating them.

---

## 11. Gates and stop rules

| Gate | Cleared by | Blocks |
|---|---|---|
| **G-Plan** | Founder approves this plan | All work |
| **G-Spend** | Founder approves each budget line in §5 by item number | Any money leaving the account (tool seat, API credits, annotator, domain) |
| **G-Outreach** | Founder approves the target list **and** the message text | Sending anything to any prospect or agency |
| **G-Deliver** | Founder approves the diagnostic template and disclosure language | Sending a diagnostic to a candidate company |
| **G-Proposal** | Founder approves price, scope, term, liability and exit clauses | Sending a paid-pilot proposal |
| **G-Publish** | *Not requested in Stage 1* | Any public article, post or promotional content |
| **G-Site** | *Not requested in Stage 1* | Any change to any client website |

**Stop rules (Part F).** Work stops immediately and reports if: any unapproved spend is about to occur; a
prospect asks us to change their website; a prospect offers payment before a proposal is approved; a provider's
terms would require scraping a consumer UI; a recommendation cannot be traced to a verified business fact; or
founder hours pass 60 before Day 12 (→ invoke the degradation ladder, §2.1).

**GO / MODIFY / STOP at Day 14** is decided on the §4.3 evidence hierarchy and the §4.4 interpretation rule —
**not** on a numeric threshold, and **not** automatically advancing to a larger sprint.

---

## 12. Explicitly not authorised (restated so it cannot be misread)

Spending money · sending outreach or contacting customers · publishing research, articles or promotional
content · building or deploying a production SaaS platform · changing client websites · signing agreements or
making financial commitments · Stage 2 engineering or any later implementation phase.

**Authorised now:** reviewing and revising existing research, and the focused Stage 2 desk research in §6 —
which is why `phase-2/01-competitor-capability-matrix.md` already exists with today's verified retrievals.
