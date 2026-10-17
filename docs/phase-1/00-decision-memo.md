# PHASE 1 DECISION MEMO — v2 (corrected)

**Company:** SignalGEO (working name) — hybrid SaaS + AI-powered managed service for SEO / AEO / GEO / AI-search
visibility.
**Phase:** 1 — Market research & problem validation.
**Version:** v2, 16 October 2026. **Supersedes v1** (the workspace was re-cloned and its history squashed on 16 Oct 2026, so v1 text is **no longer retrievable from git**; every v1 claim that matters is quoted verbatim in `11-correction-log.md`).
**Reason for v2:** the founder withheld approval and required seven corrections. All seven are actioned;
each is logged item-by-item in **`11-correction-log.md`** (C-01 … C-12).
**Application code written in this phase: none. Application code proposed by this memo: none.**

Claim labels: **[VERIFIED]** primary or official source retrieved · **[ESTIMATED]** computed by us from stated
assumptions · **[HYPOTHESIS]** plausible, untested · **[NOT YET VERIFIED]** needs a source or experiment we have
not run. FX: **₹95 = $1** (RBI reference rate 95.032, 14 Oct 2026) [VERIFIED].

---

## A. Executive conclusion

**v1's core differentiation premise is false, and I was wrong to assert it.**

v1 claimed the mid-market execution layer was "largely empty" and that no competitor closed the
measure → recommend → approve → publish → re-measure loop or mapped third-party citation gateways. Official
vendor documentation retrieved on 16 October 2026 contradicts this at every point:

- **Peec AI** ships *Actions* — ranked, evidence-backed opportunities covering site fixes, owned actions and
  "**earned actions such as getting listed, pitching editorial, and growing reviews**" — a **content optimizer**
  with per-suggestion accept/edit/reject/revert, a **Peec Agent** with 30 skills and 20+ MCP connectors,
  fact-checking actions that name the source pages contradicting a brand's facts, **Google Analytics** joins
  carrying conversions and revenue, **Google Search Console** in early access, and a Customer API that writes
  optimised content atomically. "Nothing changes without your approval." ARR **$15M**, market adoption
  **quadrupled to 19%** [VERIFIED, vendor changelog 13 Oct 2026 + vendor press release citing Ramp Rate data].
- **Profound**'s AI Marketer "identifies the work worth doing, **drafts it, and pings you for approval**",
  traces inaccurate claims to the publishers repeating them and drafts a correction per publisher, writes
  sponsored-answer creative, and **rewrites and republishes** owned content; its Agents read and write
  WordPress, Sanity, Contentful and Framer, staging drafts rather than publishing [VERIFIED, vendor site and
  vendor blog, 16 Oct 2026].
- **Scrunch / Sitecore** surfaces AEO opportunities with a **projected citation lift** and per-item
  **apply or decline** inside the CMS Page Builder, plus AXP edge delivery of agent-optimised content
  [VERIFIED, official Sitecore product documentation].
- **GEO agencies already sell the exact workstream v1 proposed as our differentiator**, at published prices:
  "$997/mo, GEO and AEO done for you, measurement included"; "tool plus contractor $2,000–$5,000/mo";
  "$2,500/mo per pillar or $5,500/mo fully managed"; digital-PR-for-GEO retainers "$3,000–$10,000/mo
  mid-market" — with **white-label suppliers who will let any agency resell the earned-media work tomorrow**
  [VERIFIED as published offers; not verified as delivered].

So the honest position is: **the closed loop is closed, by three funded vendors, in software, at €70–€360/month;
and the human execution of that loop is sold by agencies from $997/month.** SignalGEO has **no identified moat**.
That is a finding of this phase, not a gap in it.

**What survives:** real, documented buyer behaviour change (51% of B2B software buyers now start research in an
AI chatbot more often than Google, up from 29% a year earlier; AI referrals convert at roughly 2× organic);
a real, documented willingness-to-pay band for managed delivery ($997–$20,000/month published); a real cost
advantage from India-based delivery; and a real credibility opening in **measurement honesty** — no vendor we
checked publishes run counts, confidence intervals, per-surface separation or extraction error rates.

**What that adds up to:** a viable **niche managed service** with no software leverage, capacity-capped at
**~5 clients per delivery FTE at full managed scope**, cash-positive at **one client**, and requiring **5 clients
at USD pricing — or ~30 clients at ₹40,000/month — to pay the founder a market salary**. Bootstrapped 24-month
ARR band: **$61k (conservative) → $162k (base) → $375k (optimistic)**. $2M ARR requires **12–21 delivery FTEs**:
that is an agency, and it should be chosen deliberately or not at all.

**Recommendation: CONDITIONAL PROCEED to Stage 1 only** — a 14-day, **$408 cash / 98 founder-hour** experiment
(`08-validation-plan-v2.md`) whose primary job is to answer one question with evidence rather than argument:
**will a buyer who can license Peec for ~$210/month pay us $1,500/month to do the work?** Stage 1 delivers
**5 real diagnostics, 5 buyer conversations, 2 agency/channel interviews, a written measurement protocol, a
logged hour-and-cost record, and at least one priced paid-pilot proposal.** It builds no platform and writes no
production code. Expansion to 20 diagnostics is gated on three pre-registered tests (technical credibility,
cost control, commercial interest) and does not happen automatically.

If Stage 1's buy-vs-hire test fails, the correct responses are (a) reposition as a measurement/QA layer sold to
agencies, (b) search for a different problem where our engineering skill is the product, or (c) stop. All three
are legitimate; none of them is "build it anyway."

---

## B. Verified findings

### B1. Demand is real and shifting (unchanged from v1; all [VERIFIED])

| Finding | Source | Tier |
|---|---|---|
| 49% of US adults use AI chatbots (33% in 2024); 24% daily; 42% use them to search; ChatGPT reach 44% | Pew Research, *Americans and AI 2026*, n=5,119, fielded Feb 2026 | T1 |
| **51% of B2B software buyers start research in an AI chatbot more often than Google** (29% in Apr 2025); chatbots are the #1 shortlist influence at 54% vs review sites 43% and vendor sites 36%; 69% switched vendors because of chatbot guidance; 33% bought a vendor they had never heard of | G2, *The Answer Economy*, n=1,076, Mar 2026 | T2 |
| Organic CTR 0.61% with an AI answer vs 1.62% without; cited URLs get +120% clicks/impression; position-1 CTR −58% YoY | Seer (53 brands, 5.47M queries, 2.43B impressions); Ahrefs Feb 2026 | T2 |
| AI referrals ≈1.08% of traffic across 13,000+ domains and 3.3B sessions, converting at ~2× organic; 12% of enterprise digital budgets now go to AEO/GEO and 94% are increasing | Conductor | T2 |
| **Employer-published** roles: AWS AEO Manager $152,300–$216,090; Victoria's Secret Director AI & Organic Search $224,000–$318,000; Home Depot Sr Manager SEO/GEO $127,200–$165,000 | Employer job postings | **T1** |
| Contradiction retained: a 973-site e-commerce study found organic out-converted ChatGPT referrals by ~13% on transactional purchases | register §2 | T2 |

### B2. The competitive layer is more capable than v1 believed (new, corrects C-01)

See §A and `09-competitive-threats.md` §2 for the full matrix with sources and retrieval dates. Three findings
deserve restating here because they change strategy:

1. **Software-assisted execution is now table stakes at €70–€360/month.** The loop we proposed to build exists,
   with approval controls, staged edits and CMS writes.
2. **Earned-media recommendation is table stakes too.** Peec names "getting listed, pitching editorial, growing
   reviews"; Profound sells "earned media placements at highly cited sources" and drafts publisher corrections.
   The **85% off-site lever** (AirOps) is real — and it is *why the work exists*, not *why we would win it*.
3. **Human execution is table stakes at $997–$20,000/month.** Published agency offers match our v1 proposal
   workstream for workstream, and white-label digital-PR suppliers remove any scarcity of pitching capacity.

**Intelligence-discipline finding [VERIFIED]:** three independent reviews published 26 Aug – 26 Sep 2026 stated
Peec had "no built-in content generations" and "does little to fix it." Peec's changelog of 13 Oct 2026 proves
them wrong. **In this category, any competitive claim older than ~30 days is unusable** — a rule now written into
our process (`09` §5 R10).

### B3. Measurement is harder than v1 assumed, and the arithmetic is unforgiving (new, corrects C-04/C-07)

| Finding | Value | Source |
|---|---|---|
| Day-to-day source overlap; brand Jaccard; RBO | 34–42%; 0.45–0.59; 0.19–0.30 | arXiv 2604.07585 |
| Brand persistence run-to-run | ~30%; 1-in-5 across five runs | AirOps |
| Exact-repeat citation rate, ChatGPT (12,778 answers) | **0.06%** | EWR Digital |
| Perplexity answers with no brand mention (252,407 answers, 520 prompts × 7 engines) | 82% | Otterly |
| ChatGPT/Gemini/Copilot top-10 citation overlap; ChatGPT-vs-Google overlap | ~12%; 76.1% → 37.9% (Jul 2025 → Mar 2026) | Ahrefs |
| **Wilson 95% interval half-width at n = 5 runs** | **±0.29 to ±0.33** | computed, `13` §6 [ESTIMATED] |
| **Runs per arm to detect a 0.30 → 0.60 lift at 80% power** | **42** (0.20 → 0.40 needs 81) | computed, `13` §6 [ESTIMATED] |
| 95% upper bound on a true rate when 0 of 5 observed (rule of three) | **60%** | `13` §6 |

**Consequence, stated plainly:** at any n we can afford on consumer surfaces, we cannot honestly promise
"proven lift." What we can sell is **directional intelligence with disclosed uncertainty**, measured rigorously
where APIs allow and reported as wide intervals where they do not. The surfaces we can measure best are not the
surfaces buyers care most about, and we must say so in writing every time.

### B4. Cost inputs, now grounded (new, corrects C-10)

- Indian SEO specialist salaries: average **₹19,763/month** (Indeed, 145 salaries, updated 21 Aug 2026); senior
  ₹38,666; 75th percentile ₹45,000–₹85,000; SaaS/product-company specialists ₹70,000–₹2,00,000/month
  [VERIFIED T2]. Loaded, that is **$3–6/hour mid-level, $6–12/hour senior**; the model uses **$7/hour blended**
  and a **$40/hour founder opportunity cost** [ESTIMATED].
- Tooling: Otterly $29–$489/mo; Peec €70/€180/€360/mo billed annually for 1/2/5 projects (+€25–€115 per extra
  engine); Profound agency self-serve $399/mo per client workspace; Scrunch $300/$500+ [VERIFIED as published;
  live pricing conflicts unresolved — gaps CG-1/CG-2].
- **Building our own measurement is not cheaper than licensing until N ≈ 25–30 clients** [ESTIMATED, `12` §4.1].

---

## C. Assumptions and uncertainties

| # | Assumption | Value | Label | If wrong |
|---|---|---|---|---|
| U-1 | **Willingness to pay for managed delivery on top of licensable tools** | $1,000–$1,500/mo | **[NOT YET VERIFIED] — the whole company rests on this** | Stage 1 T3 fails → reposition or stop |
| U-2 | Churn | 2% / 3% / 5% per month | **[HYPOTHESIS]** — zero observations | LTV moves ±75%; acquisition economics unpriceable |
| U-3 | Pipeline additions, founder-led | 0.6 / 0.9 / 1.2 net new clients per month | **[HYPOTHESIS]** | 24-month scenarios move proportionally |
| U-4 | Delivery hours per client per month | A 5 h · B 12 h · C 21 h | **[ESTIMATED]** — itemised, never measured | Capacity and margin move directly; Stage 1 logs actuals |
| U-5 | First diagnostic 9 h, templated 5 h | — | **[HYPOTHESIS]** (v1's 1.5 h was wrong by ~3×) | Stage 1 unaffordable → re-scope before expanding |
| U-6 | Tooling per client per month | $30 / $100 / $400 | **[VERIFIED as published]** but packaging changes monthly | At $400 and ₹40,000 pricing we are **gross-margin negative** |
| U-7 | Founder opportunity cost | $40/h (band $25–$75) | **[ESTIMATED]** | Economic break-even moves 4 → 6 clients (Tier C) |
| U-8 | Extraction accuracy achievable | F1 ≥ 0.90 mentions, ≥ 0.85 citations; κ ≥ 0.80 | **[HYPOTHESIS]** until the gold set exists | We cannot sell measurement at all |
| U-9 | Reproducibility achievable | Fleiss' κ ≥ 0.40 within surface/window | **[HYPOTHESIS]**; published studies suggest 0.19–0.59 | Trend claims withdrawn; only distributions reported |
| U-10 | Beachhead universe | ≈480 accounts (≈350 India-origin global SaaS + ≈130 cybersecurity vendors) | **[ESTIMATED]** bottom-up from Tracxn/Nasscom/DSCI | Target list too small to support a channel strategy |
| U-11 | Agencies are a channel, not just competitors | — | **[HYPOTHESIS]**; white-label evidence cuts both ways | We lose our most realistic route to 20+ clients |
| U-12 | No L2 vendor publishes a measurement-uncertainty protocol | — | **[NOT YET VERIFIED]** (gap CG-5) | Thesis 1's last pillar falls |
| U-13 | Peec collects by scraping consumer UIs | — | **[NOT YET VERIFIED]** — third-party claim attributed to Peec support | Do not use in any external document until verified |
| U-14 | Published agency prices reflect delivered scope | — | **[NOT YET VERIFIED]** (gap CG-7) | The $997/mo end may be under-delivered (opportunity) or under-priced (trap) |

**Deliberately not assumed:** that ₹40,000/month is the right price (the brief is explicit; §F shows it is
probably *too low* for managed scope and *economically hopeless* for the founder), that AI-search APIs reproduce
consumer search, that any placement can be guaranteed, or that we have proprietary data.

---

## D. Options and tradeoffs

Scored on the brief's criteria. 1 = poor, 5 = strong.

| Criterion | **O1 — Niche managed service (buy tooling, sell delivery + honesty)** | **O2 — White-label measurement/QA layer for agencies** | **O3 — New problem search (engineering-led)** | **O4 — Stop** |
|---|---|---|---|---|
| Customer value | 4 — real capacity + accountability gap | 3 — agencies' own gap is unproven | ? — unknown by definition | — |
| Revenue potential | 2 — $61k–$375k ARR in 24 mo bootstrapped; $2M needs 12–21 FTEs | 3 — could scale further but needs a product | ? | — |
| Development effort | **5 — none required; license and deliver** | 2 — needs a real product | 1–3 | 5 |
| Operating cost | 3 — $408 to validate, $600/mo fixed | 2 | 3 | 5 |
| Time to market | **5 — first pilot possible inside 30 days** | 2 | 1 | — |
| Scalability | 2 — capacity-capped at 5 clients/FTE (Tier C) | 4 | ? | — |
| Security/ethics risk | 3 — managed by protocol + approval + verified facts | 3 | ? | 5 |
| Defensibility | **1 — no moat identified** | 2 | ? | — |
| Evidence quality today | 3 — demand verified, WTP not | 1 | 0 | — |
| Reversibility | **5 — fully reversible; sunk cost $408 + 98 h** | 3 | 4 | 5 |

**Tradeoff in one sentence:** O1 buys certainty and cash at the price of ambition; O3 buys ambition at the price
of everything we just learned; O2 is a product company wearing a services disguise and needs evidence we do not
have; O4 is the honest default if the founder does not want to run an agency.

---

## E. Recommended approach

**Run Stage 1 of `08-validation-plan-v2.md` exactly as scoped, and make no other commitments.**

1. **Buy, do not build.** License one month of a measurement tool (Otterly $29 tier or Peec Starter) as our
   Stage 1 substrate; run our own protocol on top of it. Revisit building only at N ≥ 25 clients and only for a
   capability we have proven clients pay for (`12` §4.1).
2. **Sell managed human delivery + measurement honesty to India-origin B2B software companies selling to
   US/UK/EU** (beachhead S1, wedge S2 cybersecurity — ICP ranking unchanged, with a post-correction robustness
   check in `05` §6). Positioning is **Thesis 4** in `09` §6: an accountable operator for a segment the
   platforms do not serve, at the bottom of the published L3 price band.
3. **Test willingness to pay against the real alternative.** Every buyer conversation includes the buy-vs-hire
   card (Option 1: license a tool at ~$210/mo and execute in-house; Option 2: us at $1,500/mo or ₹75,000/mo) and
   an ascending price ladder, recording the first "no" (`08` §7).
4. **Measure honestly or not at all.** Adopt `13-measurement-reproducibility-protocol.md` as a pre-registration:
   separate extraction accuracy from reproducibility, gold-set-validate the extractor, report Wilson intervals
   and per-surface results, use decision bands instead of kill thresholds, and never promise placement.
5. **Log everything.** Hours by step, API cost by surface, tool invoice, deviations. Stage 1's own cost record is
   the evidence Stage 2 needs; v1 failed precisely because it estimated instead of logging.
6. **Add a channel test at near-zero marginal cost:** run the same buy-vs-hire conversation with **5 agencies**
   (white-label measurement/QA, Option O2) inside the same 14 days — ~3 extra hours, and it answers a second
   strategic question with the same effort.

**Explicit non-goals for Stage 1:** no platform, dashboard, database, scheduler or multi-tenant anything; no
production application code; no consumer-UI scraping; no paid acquisition; no hiring; no public brand-count
claims; no 6th–20th diagnostic; no conclusion about churn, LTV or scaled CAC.

---

## F. Financial and technical implications

Full model, formulas and sensitivity in **`12-economics-v2.md`**. Headlines:

| Question | Answer | Label |
|---|---|---|
| Clients per delivery FTE | Tier A **18–26** · Tier B **7.5–10.8** · Tier C **4.3–6.2** (v1's "10" was Tier A only) | [ESTIMATED] |
| Variable cost per client/month (buy path, base tooling) | Tier A **$147** · Tier B **$198** · Tier C **$264** | [ESTIMATED] |
| Gross margin at Tier C | **82%** at $1,500 · **75%** at ₹1,00,000 · 62% if tooling is $400 | [ESTIMATED] |
| Gross margin at ₹40,000 (Tier A) | **+65%** at $100 tooling · **+82%** at $30 · **−6%** at $400 | [ESTIMATED] |
| **Operating cash break-even** ($600/mo fixed) | **1 client** (Tier B/C, USD) · **3 clients** (Tier A, ₹40,000) | [ESTIMATED] |
| **Founder-compensated break-even** (+$4,000/mo market comp) | **5 clients** at $1,500 · 8 at ₹1,00,000 · 11 at ₹75,000 · **30 at ₹40,000** | [ESTIMATED] |
| CAC (founder-led Stage 1) | **$408 cash / $4,328 economic** per pilot won; payback 0.33 mo cash, 3.5 mo economic (Tier C) | [ESTIMATED] |
| LTV:CAC | **6.9× at 3%/mo churn, 3.6× at 8%** — on economic CAC; churn is invented | [HYPOTHESIS] |
| 24-month ARR, bootstrapped | **$61k** conservative · **$162k** base · **$375k** optimistic · **$70k** INR-Tier-A-only | [ESTIMATED scenarios] |
| First economic-profit month | **5** (optimistic) · **13** (base) · **never within 24 mo** (both INR-dominated variants) | [ESTIMATED] |
| FTEs required for $2M ARR | **12–21** delivery staff | [ESTIMATED] |
| Stage 1 cost | **$408 cash (₹38,760)** + **98 founder-hours** ≈ **$4,328 economic** | [ESTIMATED] |
| What moves the answer most | **Price and billing domicile** (6× effect on founder break-even), then scope discipline. Delivery labour rate is nearly irrelevant (±1 client across a 3× rate range) | [ESTIMATED] |

**Technical implications:** none requiring engineering. The measurement protocol is executable with an
official search-enabled API, a spreadsheet prompt registry, an append-only file store and two human annotators.
**No application code is proposed in Phase 1 or Stage 1**, consistent with the brief and with the finding that
building measurement is more expensive than licensing until ~25–30 clients.

---

## G. Validation experiments (Stage 1, 14 days, gated)

| # | Experiment | Falsifies | Pass criterion |
|---|---|---|---|
| G-1 | **5 real diagnostics**, full protocol (25 prompts × 5 runs × 2 windows × 2 surfaces = 2,500 observations) | U-4, U-5, U-6 | ≤9 h for #1 with a downward trend to ≤6 h by #5; ≤$110 cash each |
| G-2 | **Gold set + extractor validation** (200 responses, 2 annotators) | U-8 | κ ≥ 0.80; F1 ≥ 0.90 mentions, ≥ 0.85 citations |
| G-3 | **Reproducibility study** across windows and surfaces | U-9 | at least one surface in the Green/Amber band of `13` §8 |
| G-4 | **5 buyer conversations with the buy-vs-hire card and price ladder** | **U-1** | ≥1 signed or verbally committed pilot at ≥₹75,000 or ≥$1,000/mo, **or** ≥3 priced-proposal requests. **≥4 of 5 choosing "buy the tool" kills the service hypothesis** |
| G-5 | **Prospect co-observation cards** (3 runs, same window, interval-scored) | the v1 "single rerun = ground truth" error | observations inside our stated interval; reaction logged verbatim |
| G-6 | **2 agency interviews + 5 agency channel conversations (O2 test)** | U-11 | ≥2 agencies willing to trial a white-label measurement/QA layer, or a clear "we do this in-house" |
| G-7 | **Hour-and-cost log reconciliation** | v1's estimating habit | variance explained line by line, not smoothed |
| G-8 | **≥1 written priced paid-pilot proposal** | interest-vs-willingness conflation | proposal sent with price, term, site-authorisation and exit clauses |

**Gate logic (`08` §9):** GO on all three of T1 technical credibility + T2 cost control + T3 commercial
interest → Stage 2 (20 diagnostics, findings article at n = 20, 2–3 signed pilots). CONDITIONAL (T1+T2 pass, T3
fails) → **no expansion**; 10 more buyer conversations first. NO-GO on measurement (T1 fails) → abandon the
measurement-led positioning. RE-SCOPE (T2 fails) → cut scope and re-run two diagnostics before expanding.
**No gate triggers an automatic company kill**; each produces a written founder decision (this replaces v1's
threshold-triggered kill conditions — C-07).

---

## H. Deliverables produced in this phase

| File | Status | Contents |
|---|---|---|
| `00-decision-memo.md` | **v2 (this file)** | A–I + closing four + decision items |
| `01-executive-research-summary.md` | v1 + v2 correction header | Problem, demand evidence, ranking, WTP hypotheses, threats, viability |
| `02-evidence-register.md` | **extended** | ~90 sourced findings; **new §13 execution-layer capability (official sources), §14 managed-service market prices, §15 Indian labour rates**; 20 verification gaps |
| `03-market-assessment.md` | v1 | Answers the brief's Q1–Q10 |
| `04-pain-point-map.md` | v1 + P3 correction | Pains P1–P9 |
| `05-icp-scoring-and-ranking.md` | v1 + **new §6 post-correction robustness re-score** | 9 weighted criteria, 8 segments, sensitivity A/B |
| `06-assumptions-hypotheses-failures.md` | **revised** | Labels, decision bands replacing automatic kills, 15 questions |
| `07-discovery-interview-guide.md` | **revised** | D1 script incl. buy-vs-hire card and price ladder; Q23 replaced by co-observation |
| `08-validation-plan-v2.md` | **new (replaces the 14-day plan)** | Staged, gated, 98-hour Stage 1 with day-by-day schedule, budget, gates, publishing rules |
| `09-competitive-threats.md` | **rewritten v2** | Four-layer map, verified capability matrix, published L3 prices, R1–R10, theses v2, 10 gaps |
| `10-tam-bottom-up.md` | **§2–§6 superseded** (banner added); §1 universe still valid | Bottom-up account counts |
| `11-correction-log.md` | **new** | C-01 … C-12: claim as written, correction, evidence, files affected |
| `12-economics-v2.md` | **new, authoritative** | Definitions, formulas, capacity, COGS (buy vs build), margins, cash vs economic break-even, CAC/LTV, 24-month scenarios, sensitivity, pricing verdict, 8 financial risks |
| `13-measurement-reproducibility-protocol.md` | **new, authoritative** | Extraction vs reproducibility, 14 recorded factors, gold-set protocol, statistics, co-observation, decision bands, reporting and publishing rules |

---

## I. Decision required

I am stopping here. Nothing proceeds — not Stage 1, not tooling purchase, not outreach — until you answer these.

**D-1. Approve Stage 1 as scoped?** 14 days, 98 founder-hours (~7 h/day; or 21 days at ~4.7 h/day), **$408 cash**,
5 diagnostics, 5 buyer conversations, 2 agency interviews, protocol, cost log, ≥1 priced pilot proposal, no
platform, no application code. **Yes / no / modify.**

**D-2. Accept "buy, don't build" for measurement?** One month of a licensed tool (~$30–$210) as the Stage 1
substrate, with our own protocol layered on top, and no build decision revisited before N ≈ 25 clients.
**Yes / no / prefer a specific tool.**

**D-3. Accept that no moat was identified — and what that means.** The realistic best case for O1 is a
cash-generating niche agency ($61k–$375k ARR in 24 months bootstrapped; 12–21 FTEs for $2M). Choose one:
**(a)** proceed with O1 anyway, deliberately, as a services business; **(b)** run Stage 1 but treat it as a
cheap test while commissioning a parallel problem search (O3) for something where our engineering skill is the
product; **(c)** skip to O3 now; **(d)** stop. **My recommendation is (b)** — Stage 1 costs $408 and 98 hours and
answers a question worth having answered, while (c) discards verified demand evidence for nothing.

**D-4. Approve the price ladder to test, and the floor.** Test ₹40,000 (Tier A) → ₹75,000 (Tier B) →
₹1,00,000 / $1,500 (Tier C) → $3,000 (dedicated). Rule: **no pilot below Tier A economics**, because a ₹20,000
pilot may be gross-margin negative and teaches us nothing about viable willingness to pay. **Approve / change.**

**D-5. Approve the measurement protocol and the language ban.** `13` becomes binding: gold-set-validated
extraction, per-surface Wilson intervals, rule-of-three upper bounds for absence, decision bands instead of
automatic kills, co-observation instead of "rerun it yourself", no guarantees of placement or ranking, and
publishing rules that forbid headlines stating counts we did not measure. **Approve / amend.**

**D-6. Confirm the founder time commitment.** Stage 1 requires ~7 hours a day for 14 days as the *only* focus. If
that is not available, say so and I will re-plan for 21 days rather than let the schedule produce fictional
numbers the way v1's did. **14 days / 21 days / other.**

---

## Closing four

### 1. The biggest unresolved uncertainty

**Whether a buyer who can license a capable tool for ~$210/month will pay us $1,500/month to execute.** Not the
market size, not the technology, not the churn rate — this one question decides whether SignalGEO is a business
or a hobby. Published agency prices ($997–$20,000/month) say *somebody* pays it; our register says the buyers
are mostly US/EU mid-market brands, not India-origin vendors; and nothing we have found tells us what an
India-origin SaaS or cybersecurity company with a ₹40,000–₹1,50,000 marketing line will actually sign. Stage 1
exists to answer it, and its most likely useful outcome is a clean "no" that saves us a year.

### 2. What we may be overlooking

- **The buyer may not be the brand.** It may be the agency (white-label measurement/QA), or a PE/VC operating
  partner managing a portfolio of brands, or a fractional CMO. G-6 tests the agency route at ~3 hours of cost;
  the portfolio-operator route is untested and might be the better wedge — one contract, many brands, higher
  ARPU, no per-client acquisition cost.
- **Accountability may be the product, not discovery.** Every vendor stops at drafting; Peec's own reviewers say
  "your team still executes it." The scarce thing may be a **named human who verifies every claim against the
  client's real product facts and accepts responsibility for what gets published** — most valuable exactly where
  a false claim is expensive (cybersecurity compliance posture, fintech, health). That is a *professional
  services* moat of reputation, and it may be worth more than any dataset.
- **The problem may be moving.** Agentic procurement — AI agents researching and buying, not humans reading
  answers — is already visible in Scrunch's AXP positioning and Profound's sponsored answers. If the next 18
  months shift value from "being cited in an answer" to "being machine-readable and transactable by an agent,"
  then visibility measurement is a shrinking problem and agent-readiness is a growing one.
- **Our own skill may be misallocated.** The founder's comparative advantage is MLOps/engineering. An agency
  uses almost none of it. That is a real cost of O1 beyond the $40/hour opportunity rate we modelled.
- **India-specific surfaces are unmeasured.** Indic-language AI search, and India-origin buyers researching in
  non-English markets, appear nowhere in the vendor coverage we checked — a possible niche where the incumbents'
  data is genuinely thin.

### 3. The strongest counterargument to my recommendation

**"You have just proven that the market exists, that three funded vendors own the software layer, that agencies
own the service layer from $997/month, and that you have no advantage in either. The rational response is not to
spend 98 hours confirming you would be a small agency — it is to stop now and find a problem where your
engineering is the product. Peec shipped a complete execution layer in 90 days at $15M ARR; anything you can do
manually, they will ship as a feature within two quarters, and your 5-clients-per-FTE ceiling means you cannot
outrun them on price either. Stage 1 is not cheap: its real cost is $4,328 of founder time plus a month of
attention that could go into a search for a defensible problem."**

That argument is strong and I cannot refute it with evidence — only with a cheaper way to test it. Which is why
D-3(b) is my recommendation rather than D-3(a): run the 98 hours, and run the problem search in parallel. If
Stage 1's buy-vs-hire test fails, we will have lost a month and gained a definitive answer; if it passes, we will
have a revenue line to fund the search. What I will not do is pretend the counterargument is weak.

### 4. The best next experiment

**The buy-vs-hire card, run on five named buyers and five agencies inside 14 days, alongside five real
diagnostics whose hours and API costs are logged line by line** (`08` §4, §6, §7). It is the only experiment that
simultaneously tests willingness to pay against a real substitute, produces a deliverable good enough to be
mistaken for the product, measures our own unit economics, and generates the protocol evidence that our one
surviving credibility claim depends on. Cost: **$408 cash, 98 hours.** Pre-registered falsification: **if ≥4 of
5 buyers choose the tool, or the first "no" on the price ladder comes at or below ₹40,000 for ≥4 of 5, the
service hypothesis is dead at our price and we go to O2 or O3 — not to Stage 2.**

---

**Waiting for D-1 … D-6. No further work will be done on this phase, and none on Phase 2, until you respond.**
