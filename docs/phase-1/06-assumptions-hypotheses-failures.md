# Phase 1 — Critical assumptions, falsifiable hypotheses, failure conditions

Everything below is either an **assumption** (we believe it, have not tested it), a **hypothesis**
(a statement with a designed test that could prove it wrong), or an **[UNVERIFIED] claim** we found
in the wild and have not been able to confirm from a primary source.

> **v2 revision, 16 Oct 2026.** Labels used here: **[VERIFIED]** · **[ESTIMATED]** · **[HYPOTHESIS]** ·
> **[NOT YET VERIFIED]**. Three structural changes from v1 (see `11-correction-log.md`):
> (1) **"Kill thresholds" are now "falsification signals"** — a signal triggers a *written founder decision*,
> never an automatic company-wide kill (C-07);
> (2) every test is re-scoped to **Stage 1** of `08-validation-plan-v2.md` (5 diagnostics, 5 buyer
> conversations, 2 agency interviews, 14 days, $408 cash) rather than v1's impossible 20-diagnostic sprint
> (C-05);
> (3) **A4 and differentiation thesis 2 are withdrawn as moats** after official vendor documentation showed
> Peec, Profound and Scrunch/Sitecore all ship earned-media recommendation and approval-bound execution, and
> agencies sell the same workstream from $997/month (C-01, C-08).

---

## 1. Critical assumptions (with what breaks if wrong)

| ID | Assumption | Current support | If wrong |
|---|---|---|---|
| **A1** | AI-mediated shortlisting is now material for B2B software purchases, not a fad | G2: 51% start in AI chat (29% a year earlier), 54% shortlist influence, 69% vendor switching (B3, B4); Pew: 49% of adults use chatbots, 42% to search (B1) | The entire demand premise weakens. Note G2 is T2 with a commercial interest; Pew is T1 but measures *consumer* use, not B2B purchase behaviour |
| **A2** | Being absent from AI answers causes lost opportunities (not merely lost vanity metrics) | Exclusion mechanism (B4: 33% bought from a vendor they'd never heard of; B6: AI-sourced buyers stick to shortlists 80% vs 65%) | We are selling insurance against a risk buyers won't pay for. **This is the assumption our 14-day test most needs to attack** |
| **A3** | The mid-market will pay $1,000–$1,500/mo (₹95,000–₹1,42,500) for *managed execution*, not just measurement | **[HYPOTHESIS]**, better-supported than in v1: published done-for-you offers now include **$997/mo** ("GEO and AEO done for them, measurement included", SourceRank), **$2,000–$5,000/mo** ("tool plus contractor"), **$2,500/mo per pillar or $5,500/mo fully managed** (MADX), **$3,000–$10,000/mo** digital-PR-for-GEO mid-market (register §14) — plus GEO retainers $1,500–$50,000/mo (P4) and Indian ₹19,999–₹2,80,000/mo (P9). Counter-evidence: Peec sells the *software* half of this for €180/mo and 19% of the market has adopted a tool (X13-7) | If wrong we fall back to a ₹40,000/mo Tier A monitoring service which `12` §5 shows is **+65% gross margin, 3 clients to cash break-even, and ~30 clients before it pays a market-rate founder** — a lifestyle business, not a company. **This is the assumption Stage 1 exists to attack** |
| **A4** *(v2, corrected)* | Off-site third-party corroboration is the dominant **lever** — but not a **moat** | Lever: M8 (85% third-party discovery; 6.5x citation likelihood; ~90% from listicles/comparison/review roundups), C1–C4 (top 15 domains ≈68% of citation share), and **95% of AI-cited links come from non-paid sources** (Muck Rack via register X14-2 — [NOT YET VERIFIED] independently). Not a moat: Peec Actions already recommend "getting listed, pitching editorial, growing reviews" and surface third-party channels worth working with; Profound sells "earned media placements at highly cited sources"; digital-PR-for-GEO retainers are a published $3,000–$10,000/mo category with white-label suppliers (X13-1, X13-12, X14-2) | **Already happened.** Thesis 2 is withdrawn as a differentiator (`09` §6) and survives only as a required delivery capability. The ethical constraint tightened: because paid placement does not earn citations, the work must be genuine editorial and community value, and the syndication tactic claiming a 239% citation lift is one we will not sell without a written ethics ruling |
| **A5** *(v2, corrected)* | Repeated-sampling measurement is stable enough to report a **distribution** clients will accept — *not* a trend from a single run | M7 (Otterly 252k answers; 10 prompts insufficient), M9 (arXiv: source overlap 34–42% day-to-day, brand Jaccard 0.45–0.59), M10 (~95% consistency within minutes), M11 (instability is time-driven), EWR Digital (ChatGPT exact-repeat citation rate **0.06%** across 12,778 answers). New [ESTIMATED]: Wilson half-width **±0.29–±0.33 at n = 5**, and ~42 runs/arm to detect a 0.30→0.60 lift | We do not lose the business, we lose the *strong* claim. Fallback: report intervals, upper bounds and per-surface distributions; sell executed work rather than proven lift. Tested by protocol §5 (reproducibility study) and §7 (co-observation), **not** by v1's single-rerun experiment V4, which was invalid (C-07) |
| **A6** | Official APIs are a legitimate, affordable measurement surface | Perplexity Sonar $5–12/1,000 requests (M5); measured $5.27 per 1,000 answers | Measurement COGS blow up, or we are pushed toward ToS-violating automation (M4) — unacceptable |
| **A7** | We can acquire beachhead customers from India through founder networks and communities (SaaSBoomi 4,000+ startups; DSCI/Nasscom events; LinkedIn; Product Hunt) | A4, A5, A6 | CAC becomes cold-outbound CAC and the beachhead advantage evaporates → S4 economics without S4 prices |
| **A8** *(v2, grounded)* | India-based delivery at **$7/hr blended** ($4–$6 mid-level, $6–$12 senior) fully loaded is achievable at the quality this work requires | **[VERIFIED]** Indeed India: SEO specialist average **₹19,763/mo** (145 salaries, upd. 21 Aug 2026), senior ₹38,666, 75th pct ₹45,000–₹85,000, SaaS/product-company specialists ₹70,000–₹2,00,000/mo (register §15); +25–30% employer load ÷160 h at ₹95/$1 | Margins are *less* sensitive to this than v1 feared: `12` §9 shows a 3× rate change moves founder-compensated break-even by ±1 client. **The real cost risk is tooling ($30–$400/client/mo), not labour** |
| **A9** | Globally-selling India-origin companies can and will pay in USD through a foreign entity | Common structure; **[UNVERIFIED]** — depends on each company's setup | ARPU halves; ₹40,000 anchor dominates and the managed tier is unprofitable |
| **A10** | Clients will let us instrument their funnel (GA4, Search Console, CRM self-attribution field) | Required for our three-tier evidence stack | We cannot report commercial outcomes (P5) → we are back to selling a contested number |
| **A11** | Export-of-services invoicing (GST/LUT or zero-rated), USD receivables and transfer pricing are manageable for a 2-person company at this scale | **[UNVERIFIED — needs an accountant]** | Real cash-flow and compliance drag; could force INR-only pricing early |
| **A12** | Provider surfaces remain available and affordable for at least 12 months | **Already contradicted once**: Perplexity docs stated Sonar support ends 27 Sept 2026 with migration to the Agent API (M6) | We must design multi-provider adapters and cost caps from day 1, and disclose surface loss to clients rather than silently degrading |
| **A13** | The category does not become toxic before we establish a reputation | M14 (loud "snake oil" sentiment); R5 | Honest positioning becomes a liability rather than an asset; we would need to lead with outcomes-only language |
| **A14** *(new, v2)* | We can **license** measurement rather than build it, at $30–$400/client/month, without losing the ability to publish our own protocol | Published pricing (register §13, X13-15/16); `12` §4.1 shows building is not cheaper until N ≈ 25–30 | COGS rises (at $400 tooling a ₹40,000 Tier A client is **gross-margin negative**), and our numbers live in a vendor's platform. Mitigation: our protocol is tool-agnostic and our raw-response store is ours |
| **A15** *(new, v2)* | A moat-less but cash-generating niche service is a business the founder actually wants | **No evidence — a preference, not a fact.** `12` §8: $61k–$375k ARR bootstrapped in 24 months; $2M ARR needs 12–21 delivery FTEs | If the answer is "no", the correct move is O3 (a fresh problem search where engineering is the product), and Stage 1 becomes a cheap way to keep the option alive rather than a commitment |
| **A16** *(new, v2)* | Vendor capability claims in official documentation correspond to usable quality in practice | Peec/Profound/Scrunch docs [VERIFIED-VENDOR-CLAIM] | If their earned-media recommendations are vague or unusable, the *software-assisted vs managed-delivery* distinction becomes our strongest sales argument. Tested hands-on in Stage 1 (gap CG-6) |

## 2. Falsifiable hypotheses and the test that could disprove each

| ID | Hypothesis | Falsification test (all inside **Stage 1** of `08-validation-plan-v2.md` unless noted) | Falsification signal → triggers a written founder decision, **not** an automatic kill |
|---|---|---|---|
| **H1** | India-origin global B2B software companies will accept a meeting about AI-search visibility when shown a specific, verifiable finding about their own brand | 40 personalized outreaches (2 batches of 20) containing one true, checkable finding each | <20% reply rate **or** <5 conversations from 40 outreaches → the list or the message is wrong; re-target before concluding anything about demand (gate G1) |
| **H2** | When shown that AI recommends a named competitor and not them, ≥40% of prospects rate it a "serious problem" worth budget | 5 buyer conversations, scored on a fixed 1–5 severity scale, asked **before** any pitch | <40% rate it 4–5. At n = 5 this is 2 of 5 — weak evidence by construction, recorded as directional only |
| **H3** | Median stated willingness to pay for a managed measurement+optimization service is ≥₹75,000/mo (or ≥$1,000/mo for USD-billing entities) | Ascending price ladder on all 5 conversations (₹40,000 → ₹75,000 → ₹1,00,000/$1,500 → $3,000), recording the first "no", plus ≥1 real priced proposal | First "no" at or below ₹40,000 for ≥4 of 5, **and** no prospect accepts a $1,000+/mo quote |
| **H3b** *(new — the most dangerous test)* | A buyer who can license a capable tool for ~$210/mo will pay us $1,000–$1,500/mo to execute | **Buy-vs-hire card** on all 5 buyer conversations (`08` §7.1): Option 1 tool + in-house execution vs Option 2 us; choice and reasoning recorded verbatim | **≥4 of 5 choose the tool** → the service hypothesis is dead at our price; go to O2 (agency channel) or O3 (new problem), not to Stage 2 |
| **H4** | ≥1 company will commit to a paid pilot within Stage 1 | Real proposals, real signatures or verbal commitment with a named budget line, approver and start date | 0 commitments after 5 conversations and 5 delivered diagnostics → gate G2/T3 CONDITIONAL: 10 more conversations before any Stage 2 spend |
| **H5** *(v2, replaced)* | Prospects can **co-observe** our measurement: their own protocol-controlled runs fall inside our stated predictive interval | Protocol §7 co-observation card: exact prompt, surface, region, logged-out fresh session, **3 runs inside a named 6-hour window**, scored against the Wilson interval — never against a point estimate | ≥2 of 3 co-observations outside the interval, systematically, across ≥2 prospects → measurement premise review (band Red/Black, protocol §8). **v1's "single rerun, agreement <60% ⇒ kill the company" was invalid and is withdrawn** |
| **H6** | Prospects will authorize funnel instrumentation (GA4 + Search Console read access + a self-attribution field) | Ask on every call; count yeses | <30% agree |
| **H7** | The off-site lever is actionable *by us*: for a given query cluster we can identify the specific third-party URLs that get cited and at least one ethical route to influence each | 5 Stage 1 diagnostics: record whether a named, actionable gateway URL was found for ≥3 of the client's top query clusters. (Identification alone is **not** differentiating — Peec and Profound both do it; the test is whether *we can act on it*) | <50% of diagnostics yield ≥3 actionable gateways |
| **H8** *(v2, corrected)* | Delivery cost per diagnostic is **≤$110 cash and ≤9 hours** initially, falling to **≤6 hours** by unit 5 | Hour-by-step and API-spend logging on all 5 Stage 1 diagnostics (`08` §6) | >9 h or >$110 for #1, or no downward trend by #5 → **re-scope before expanding** (fewer prompts/surfaces, cheaper tooling) and re-run two diagnostics. v1's "≤$30 falling to $15" was withdrawn: it counted collection only and understated labour ~3× (C-04) |
| **H9** | Agencies would white-label or resell our measurement/QA layer, or refer execution work to us | 2 agency interviews in Stage 1 + 5 agency channel conversations (option O2 test, ~3 extra hours) | 0 of 7 express interest in a commercial arrangement. Note the counter-evidence: white-label **digital-PR** suppliers already exist, so agencies may need pitching capacity less than they need measurement credibility |
| **H10** | A "false statement audit" (P6) is a stronger door-opener than a "visibility score" | A/B the outreach angle: 20 messages each, identical list quality | Reply rate advantage <1.3x in either direction (i.e. no signal) |
| **H11** | Search-enabled API observations correlate with consumer-product observations well enough to report trends (but **never** to claim equivalence) | Stage 1: 25 prompts × 5 runs × 2 windows on one API surface vs the same on one human-captured consumer surface; report per-surface results, Jaccard on citation sets and agreement on mention status | Agreement <50% → report consumer captures only (cost model changes materially, since human capture cannot reach the ~42 runs/arm needed for lift claims) or API only (weaker claims about the surface buyers care about). Either way the limitation is disclosed, not hidden |
| **H12** | Retention is structurally supported by volatility (clients keep paying because answers keep changing) | Longitudinal; **not testable in Stage 1.** Interim proxy: window 2 vs window 1 (≥7 days apart) for the same 5 brands and prompts | If <20% of tracked items changed between windows, the "it keeps changing" retention argument is weaker than we assume — and `12` §7's churn range becomes the dominant financial unknown with no supporting story |

## 3. Failure conditions — what makes us abandon or pivot (brief question 10)

**v2 governance rule (replaces v1's automatic triggers — C-07):** no numeric signal below abandons the company
by itself. Each triggers a **written founder decision**, recorded with the evidence attached, in the Stage 1
memo. Thresholds are decision bands, and the same number can mean different things depending on *why* it
happened (wrong list, wrong message, wrong price, wrong segment, or genuinely no demand).

**Consider abandoning the *service* hypothesis if, at the end of Stage 1 (day 14 or day 21):**
- 0 pilot commitments after 5 buyer conversations and 5 delivered diagnostics (H4), **and**
- ≥4 of 5 buyers prefer licensing a tool to paying us (H3b), **and**
- the first "no" on the price ladder comes at or below ₹40,000 for ≥4 of 5 (H3), **and**
- co-observation fails systematically (H5, protocol band Black on every surface).
Even then the decision is between **O2** (white-label measurement/QA for agencies), **O3** (a new problem
search where engineering is the product) and **O4** (stop) — not a reflexive "the market does not exist",
because the demand evidence in §1 of `01` is T1 and independent of our offer.

**Pivot to a productized one-time audit (₹40,000–₹1,00,000 per engagement, no subscription) if:**
- interest is high but recurring commitment is refused, and ≥3 prospects say "I'd pay once for this
  report" — this is a real business with a churn problem we would be choosing deliberately. At 9 logged hours
  per audit and $7/h delivery labour, a ₹40,000 audit is ~$353 of labour cost against $421 of revenue
  **before** tooling — viable only once templated to ≤5 h (`12` §6), so this pivot inherits the same cost
  discipline Stage 1 is testing.

**Pivot to the agency channel (S5) if:**
- ≥3 of 5 agency interviews produce commercial interest (H9) while direct beachhead sales stall.
  Agencies buy faster, pay less, and churn more; that trade may still beat zero.

**Pivot to cybersecurity-only (S2) if:**
- severity scores and WTP are materially higher in the 58 Series A+ / 400-product-company universe
  than in general SaaS, and the DSCI/Nasscom network gives us warmer access (A7).

**Do NOT pivot to a self-serve monitoring SaaS** on the evidence in this phase (F1–F6, M1, `10` §5).
If the founder wants to build that company anyway, the honest framing is: it requires capital,
brand, and a data moat, and it competes with a free Google report and a $1.8B incumbent.

## 4. [UNVERIFIED] claims we found and must not repeat as fact

| Claim | Where it appears | Why we can't use it yet |
|---|---|---|
| Profound Enterprise contracts "typically $1,500–$5,000+/mo"; a "$499/mo Lite tier" | F2 (two conflicting third-party accounts) | Neither is confirmed on Profound's own page in our access; the two accounts contradict each other |
| Ahrefs Brand Radar at $398/mo vs $199/mo add-on | F6 | Two sources, one price each |
| Perplexity Agent API web_search at $0.0025 vs $0.005 per invocation | M6 | Two sources conflict; also the Sonar deprecation date must be re-checked |
| Mid-market spends $75k–$150k/yr on GEO (attributed to Forrester) | P5 | Second-hand via a vendor blog; the same article gives $75k–$200k and $400k+ elsewhere |
| ISB/Carnegie Mellon randomized field experiment: −38% organic clicks on AIO queries | E5 | Primary paper not located |
| "96% of B2B companies are invisible during early-stage AI-driven buyer discovery" (2X AI Visibility Index) | P7 | Vendor index, no disclosed method |
| "92% of marketers plan to optimize for AI search, only 40.6% are doing so" (ConvertMate GEO Benchmark) | P7 | Vendor benchmark, no disclosed sample |
| India digital advertising market: ₹71,621 Cr (2025) / ₹84,977 Cr (2026) vs ₹62,500 Cr vs ₹35,000 Cr | P10 | Three figures, three definitions; unreconciled |
| Indian digital-services exports ">$250B in FY2025-26" | A7 | Conflicts with Nasscom's $246B total exports (A1) |
| All GEO market-size forecasts ($1.09B/$2.70B/$1.25B/$848M for 2025–26, CAGRs 13.6%–50.5%) | S1–S3 | Report mills; mutually inconsistent; no disclosed methodology |
| Every vendor/agency case-study result (Ramp 7x, CRS +15% pipeline, Rough Country $22,700, Akamai +364%, Go Fish +43%/+83%, Ignite +458%/+20%) | O4 | Self-reported by the vendor or agency that sold the work. Usable only as "vendor claims" |
| India SEO budget increase "53% of Indian businesses increased SEO budget in 2026" | P8/P10 | Single weak aggregator source |
| Keyword volumes for "GEO optimization for exporters" (~880/mo) and "how to appear in ChatGPT as supplier" (~480/mo) | A8 | Single practitioner, no tool or date given |

## 5. Answers to the brief's fifteen challenge questions (Phase-1 depth; some are deferred)

1. **Why would a client pay monthly after their website is optimized?** Because the target moves:
   cited-source sets overlap only 34–42% day to day (M9); ~30% of brands persist between
   consecutive runs (M8); ChatGPT's exact-repeat citation rate is 0.06% (M12); pages not refreshed
   within 3 months are >3x more likely to lose citations (M8); competitors keep publishing; and
   providers change surfaces (Perplexity's Sonar deprecation, M6). **But this argument only supports
   a monitoring+refresh retainer, and only if we are honest that a stable client should step down.**
   Rule 24 in `INTEGRITY-RULES.md` exists to stop us manufacturing work.
2. **What can we measure reliably vs only estimate?** Reliably: our own repeated API observations
   with run counts and CIs; Search Console AI-feature impressions for the client's own property
   (M1); GA4 AI-referral sessions/conversions (M3); presence and content of specific third-party
   pages. Only estimated: consumer-experience visibility at scale (M4 blocks automation; APIs ≠
   consumer product); share of voice across a market; any causal revenue effect.
3. **Can we prove AI visibility improvements produce incremental revenue?** **No, not at
   mid-market scale, and we should say so.** We can report three tiers of evidence (leading /
   acquisition / commercial) and let the client draw the inference. E11 shows even the conversion
   premium is contradicted in transactional e-commerce.
4. **How do we distinguish consumer AI-search behaviour from API-generated answers?** Separate
   observation records by surface (consumer-captured vs API-captured), never blend them into one
   score, disclose the difference in every report, and validate correlation with H11.
5. **How will we compete with established GEO monitoring tools?** *(v2)* We won't compete with them — **we
   will buy them** (`12` §4.1: building is not cheaper than licensing until N ≈ 25–30). We compete with the
   *service* layer, and our leverage against tools is that they leave execution to the client's team: Peec's
   own reviewers summarise it as "It identifies the opportunity; your team still executes it" (`09` §3).
6. **Why wouldn't traditional SEO agencies simply offer the same service?** *(v2)* **They already do, and
   better-resourced than v1 assumed** — published offers from $997/mo to $30,000/mo, with digital PR as the
   core workstream and white-label suppliers behind it (register §14, `09` §4). Their remaining blocker is
   **disclosure**: an agency billing $5,000/mo has little incentive to publish confidence intervals showing
   its numbers are noisy, or to tell a client its own site is the smallest lever. That is a real but narrow
   opening, and it closes the moment a platform publishes a protocol (`09` §7).
7. **Can our agents safely optimize customer websites without introducing false claims?** Only with
   a client fact-verification workflow, typed evidence requirements per claim, human approval before
   publish, and rollback. Full design in Phases 6–8. **Phase 1 position: any claim we cannot source
   to a client-verified fact does not get written, regardless of its citation value** (O1's
   "add statistics and quotations" finding is a *temptation* to fabricate specificity; that is
   exactly the failure mode we must guard against).
8. **What is our real proprietary advantage?** *(v2)* **None identified — and two of v1's four candidates are
   now closed.** The citation-gateway dataset is sold by Peec, Profound, Scrunch, Ahrefs and Semrush, and
   incumbents hold 2B+ prompts and 30M+ sources; joined first-party data is sold by Peec (GA4 conversions and
   revenue) and is free from Google (GSC generative-AI report). What remains: delivery IP (replicable in a
   quarter), India cost structure applied to USD-priced work (real, also used by Indian agencies and
   white-label suppliers), and segment network/trust (the only one that compounds, and it compounds as
   reputation, not as data). `09` §6 states this plainly: **items 4 and 5 support a good small company, not a
   venture-scale one.**
9. **Which segment produces the strongest unit economics?** *(v2, `12` §5)* Domicile of the buying entity
   dominates segment choice: **$1,500/mo (Tier C) = 82% gross margin, 1 client to cash break-even, 5 clients
   to pay a market-rate founder.** ₹1,00,000/mo = 75% margin, 1 client cash, 8 clients economic. ₹40,000/mo
   (Tier A) = 65% margin, 3 clients cash, **~30 clients economic** — i.e. never, inside 24 months. Same COGS,
   ~3.4× the break-even speed for the USD buyer.
10. **What would make us abandon or pivot?** §3 above, with **decision bands and a written founder decision**
   rather than automatic numeric triggers (C-07), and the staged gates G0/G1/G2 in `08` §9.
11. **Which parts can become self-service SaaS, and which require human expertise?** Self-service:
    measurement scheduling, storage, scoring, CIs, dashboards, audit checks, alerting, report
    generation. Human: fact verification, proposal judgement, off-site outreach and relationships,
    client communication, approval decisions, and anything touching publishing. Design the seam now.
12. **How do we avoid generating unnecessary changes merely to justify a subscription?** Publish
    the evidence grade of every recommendation; require an expected-impact range and a measurement
    plan per proposal; allow "no change recommended this month" as a valid report; offer a
    maintenance tier that steps down automatically when volatility for that client is low; make
    the client's own verification path part of the report.
13. **How will model changes and provider restrictions affect our product?** Demonstrated already
    (M6, M4). Design: provider adapters with per-surface cost caps, fallback ordering, cached raw
    evidence, human-captured baselines that survive API loss, and client-facing disclosure when a
    surface degrades. Deferred to Phase 5.
14. **How can we validate demand before building the full platform?** *(v2)* Stage 1 in
    `08-validation-plan-v2.md`: 40 personalized outreaches, **5 delivered diagnostics** (not 20 — v1's sprint
    needed 160–240 founder-hours), 5 buyer conversations with a buy-vs-hire card and a 4-step price ladder,
    2 agency interviews, a written measurement protocol with a 200-response gold set, an hour-and-cost log on
    every unit, and ≥1 priced pilot proposal. **14 days, 98 founder-hours, $408 cash, zero platform code.**
    Stage 2 (20 diagnostics) runs only if all three G2 tests pass.
15. **What is the fastest path to the first paying customer?** The "false statement + missing
    recommendation" audit (P6 + P1) delivered free to a named founder in our network, followed by a
    90-day paid pilot at $1,500/mo (or ₹75,000/mo) with pre-registered success metrics. Target:
    **day 10–14**, from warm network contacts, not cold outreach. *(v2 addition: the free audit is delivered
    **with** the priced proposal attached and time-boxed, so it cannot be mistaken for the product — and it
    carries the interval disclosure from `13` §9, because the first client's expectations set the standard for
    every later one.)*
