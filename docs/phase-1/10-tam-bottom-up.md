# Phase 1 — Bottom-up market sizing and the unit-economics reality check

> **⚠ PARTLY SUPERSEDED (16 Oct 2026).** **§1 (account-universe construction) remains valid** and is still
> cited elsewhere. **§2–§6 are superseded by `12-economics-v2.md` and must not be used.** Defects found in v1:
> the capacity model assumed 13 client-hours/client/month while the COGS model assumed 21+ (C-02); measurement
> tooling was omitted from COGS entirely (C-03); break-even did not distinguish operating cash break-even from
> founder-compensated economic break-even (C-09); the labour rate was asserted rather than grounded (C-10); and
> the "revenue ceilings" implied a 12–40 person delivery organisation that was never stated. See
> `11-correction-log.md`.

**All figures in this file are our own estimates unless tagged with an evidence-register ID.**
We deliberately do not use the published GEO market-size numbers: Dimension Market Research says
$1.09B for 2026 at 40.6% CAGR, Coherent Market Insights says $2.70B (platform) / $1.25B (services)
at 13.6–14% CAGR, and a third citation of the same firm's numbers gives $848M (2025) → $33.7B
(2034) at 50.5% (S1–S3). They cannot be reconciled, they are sold as press releases, and building
a strategy on them would violate our own research-integrity rule. Bottom-up only.

**FX assumption: ₹95 = $1** (RBI reference rate 95.032 on 14 Oct 2026; X1). All INR figures use
this rate and are rounded.

---

## 1. Universe construction (beachhead S1 + wedge S2)

| Layer | Count | Basis | Our adjustment |
|---|---|---|---|
| SaaS companies in India | 32,028 (24,243 active) | Tracxn (A3) | Database counts include dormant/shell entities; use "active" |
| …of which funded | 3,808 | Tracxn (A3) | — |
| …of which Series A+ | **1,049** | Tracxn (A3) | Our working universe of companies with a real marketing budget |
| …selling primarily outside India | ~700 | **our estimate**; SaaSBoomi/McKinsey-era claim was "90% of Indian SaaS cater to global customers" (A4, 2023) — we discount to ~65–70% because that quote predates the India-first SaaS wave | [ESTIMATE] |
| …in research-led categories with AI-mediated shortlisting | **~350** | **our estimate**: half of 700, filtering out India-only vertical SaaS, hardware-adjacent, and services-disguised-as-SaaS | [ESTIMATE] |
| Indian cybersecurity product companies | 400+ | DSCI Report 3.0 (A5) | — |
| …expanded globally | 220 | 55% of 400 (A5) | — |
| …with a marketing function and budget | **~130** | **our estimate**: 60% of 220 | [ESTIMATE] |
| **Beachhead universe (S1+S2)** | **≈480** (range 400–600) | 350 + 130 | [ESTIMATE built on T2 counts] |

Ring 2 (24–36 months): add funded Indian cybersecurity (253 companies, A6), India-origin ER&D /
product-engineering exporters and mid-size IT-services firms with a productized offer. Reachable
universe ≈ **3,000–3,500 firms** [ESTIMATE].

Ring 3 (post-proof): global mid-market B2B SaaS. Tracxn counts 298,610 SaaS companies worldwide,
30,231 at Series A+ (A3). Ring 3 universe ≈ **30,000 firms**, with the caveat that our acquisition
cost there is a multiple of Ring 1 and the competitive intensity is at its maximum (S4 scores 1/5
on competitive intensity).

## 2. What a services-led business can actually serve

This is the constraint that market-size reports never mention: **delivery capacity.**

| Parameter | Conservative | Base | Optimistic | Basis |
|---|---|---|---|---|
| Client-hours per client per month (managed GEO/AEO service) | 18 | 13 | 9 | Our own scope model: monitoring analysis, proposal generation, fact-verification with client, publishing coordination, reporting, plus third-party corroboration outreach |
| Effective delivery hours per FTE per month | 110 | 130 | 150 | After internal tooling, sales support, and non-billable learning |
| Clients per delivery FTE | 6 | 10 | 16 | = hours ÷ client-hours |
| Delivery FTEs at month 24 | 2 | 4 | 6 | Founder + hires; we do not assume capital |
| **Servable clients at month 24** | **12** | **40** | **96** | — |

## 3. Cost per client per month (base scenario, managed service at pilot scope)

Scope: 60 tracked buyer prompts × 3 measurement surfaces × 5 repeats × 4 evaluation runs/month
(= 3,600 provider requests/month), monthly technical + content audit, 8–12 optimization proposals
with diffs, third-party corroboration work, one monthly business-impact report, one 45-minute call.

| Cost line | Conservative | Base | Optimistic | Notes |
|---|---|---|---|---|
| Provider API requests | $45 | $22 | $12 | Perplexity Sonar $5–12/1,000 requests (M5); 3,600 requests ≈ $18 at $5/1,000 plus tokens. OpenAI search-enabled pricing is **[UNVERIFIED]** and is the single biggest cost uncertainty; we budget $5–15/1,000 |
| Extraction / classification LLM passes | $20 | $11 | $5 | 3,600 responses × ~1.5k tokens in / 200 out; mid-tier model $1/$5 per M ≈ $8; premium model ≈ $20 |
| Crawl + audit infrastructure | $8 | $5 | $3 | Fetching, rendering, storage of raw evidence |
| Shared platform + storage + observability | $10 | $6 | $4 | Allocated per client |
| **Total API/infra COGS** | **$83** | **$44** | **$24** | — |
| Delivery labour (India, $8–12/hr fully loaded) | $216 | $130 | $72 | 18/13/9 hrs × $12/$10/$8 |
| Third-party corroboration labour | $144 | $96 | $48 | 12/8/4 hrs — the workstream the evidence says matters most (M8) |
| Support + client comms | $40 | $25 | $15 | — |
| **Total COGS per client per month** | **$483** | **$295** | **$159** | — |

**This table is the most important output in Phase 1.** Compare it to price points:

| Price point | INR (at ₹95/$) | Gross margin @ conservative COGS $483 | @ base $295 | @ optimistic $159 |
|---|---|---|---|---|
| ₹20,000/mo | $211 | **−129%** | −40% | +24% |
| **₹40,000/mo** | **$421** | **−15%** | **+30%** | **+62%** |
| ₹75,000/mo | $789 | **+39%** | **+63%** | **+80%** |
| ₹1,20,000/mo | $1,263 | **+62%** | **+77%** | **+87%** |
| $1,500/mo (USD-billed) | ₹1,42,500 | **+68%** | **+80%** | **+89%** |
| $3,000/mo (USD-billed) | ₹2,85,000 | **+84%** | **+90%** | **+95%** |

*(All cells computed as (price − COGS) ÷ price at ₹95 = $1. Example, the ₹75,000 conservative cell:
(789 − 483) / 789 = +38.8%. The pattern is the point: the conservative COGS case only clears a
healthy margin at ≥₹75,000/mo, and the optimistic case is the only one where ₹40,000/mo works for
the managed scope.)*

### Direct answer to the brief's instruction: do not assume ₹40,000/month is correct

**₹40,000/month is a real, published market price in India** — Raasis publishes a ₹40,000/mo
"Startup" GEO tier (40 tracked commercial queries, 20 answer briefs, 5 priority page upgrades,
1 entity cluster), Digimark publishes a ₹39,999/mo GEO/AEO retainer, and Adexorb starts at
₹19,999/mo (P9). So it is *sellable*.

**But at ₹40,000 the full managed service is at best a 30% gross margin business and at worst
margin-negative**, because labour — not AI — is 70–75% of COGS. Three conclusions follow:

1. **₹40,000/mo must buy a narrower product**: measurement + monthly report + a prioritized
   opportunity backlog, with the client's own team executing. Cap our labour at ≤4 hrs/client/month.
   At 4 hrs ($40) + $44 API/infra = $84 COGS → **80% gross margin at ₹40,000**. This is a real,
   healthy product — it is simply not the managed service.
2. **The managed optimization service must be priced ≥₹75,000/mo for India-domiciled budgets, or
   ≥$1,000–1,500/mo for globally-selling clients** to clear a 60% gross-margin bar.
3. **Price by domicile of the buying entity, not by cost of delivery.** Many India-origin SaaS
   companies have a US/UK entity (a fact we can verify in discovery). Billing $1,500/mo to the US
   entity for the same work that would be haggled to ₹40,000 in India is a ~3.4x revenue difference
   on identical COGS. This is the single largest lever on our unit economics and it is a
   positioning/legal question, not a technical one. *(Flag: transfer-pricing and GST/LUT treatment
   of export services needs an accountant's review before we commit — see `06`, assumption A11.)*

## 4. Break-even (why the validation risk is genuinely low)

Fixed cash costs for a 1–2 person operation before any founder draw:

| Line | Monthly |
|---|---|
| Cloud (compute, Postgres, Redis, object storage, egress) | $80–$250 |
| Third-party tooling (one Ahrefs *or* Semrush seat; GSC and GA4 are free) | $100–$400 |
| Legal/accounting/compliance baseline | $100–$250 |
| Domain, email, landing page, analytics | $30–$80 |
| **Total fixed cash cost** | **$310–$980** (base ≈ $600) |

Contribution per client at $1,500/mo with base COGS $295 = **$1,205**.

Break-even clients at the base fixed cost of $600/mo:
- $1,500/mo managed: 600 ÷ 1,205 = **0.5 → 1 client** (0.8 clients even at the $980 fixed case).
- ₹75,000/mo managed: contribution $789 − $295 = $494 → 600 ÷ 494 = **1.2 → 2 clients** (2.0 at $980 fixed).
- ₹40,000/mo monitoring tier (≤4 labour hours, COGS $84): contribution $421 − $84 = $337 →
  600 ÷ 337 = **1.8 → 2 clients** (2.9 at $980 fixed).

**Strategic consequence:** we do not need to raise money or build a platform to learn whether this
business is real. **One to three clients make the operation cash-flow positive at every price point
we would actually quote.** That materially changes the correct Phase 1 recommendation: **validate
with a service, and only build software against the parts of delivery that are provably repeatable.**

## 5. Revenue ceilings under three strategies (our estimates)

| Strategy | Clients at month 24 | ARPU | ARR | Gross margin | What it takes |
|---|---|---|---|---|---|
| **A. Services-led, beachhead only (S1+S2)** | 12–40 | $9,000–$18,000/yr | **$0.1M–$0.7M** | 60–80% | Founder selling + delivering; no capital |
| **B. Services + productized measurement (Ring 2)** | 40–100 | $12,000–$18,000/yr | **$0.5M–$1.8M** | 55–75% | 4–6 delivery FTEs, internal tooling, 5+ case studies |
| **C. B + agency white-label channel (S5)** | 100–250 (via 20–50 agencies × 5 clients) | $6,000–$12,000/yr net of agency margin | **$0.6M–$3.0M** | 65–85% | Multi-tenant workspaces, agency pricing, channel support — i.e. real software |
| **D. Self-serve monitoring SaaS** | 500–2,500 | $1,140–$5,940/yr | **$0.6M–$15M** | 80–90% | Competing head-on with Peec ($29M raised, $10–15M ARR in 16 months), Semrush ($99/domain), HubSpot (free Grader), GSC (free impressions) and Profound ($335M). Requires capital, brand and a data moat we do not have |

Honest read: **Strategy D has the only venture-scale ceiling and the worst odds for us.** Peec's
trajectory ($0 → $10M ARR in 16 months at ~$4,000 ARPU, 2,500 customers, $29M raised, now talking
at ~$200M pre-money — F3) proves the model works *and* proves the window we would need has already
been taken by better-capitalized players, while Google gives away AI-impression data (M1) and
HubSpot/Semrush/Ahrefs bundle the rest at $0–$199 (F6).

Strategy A→B→C is the path that reaches **$2M–$4M ARR with 60–80% gross margins and no external
capital**, and — critically — it accumulates the one asset that could later justify software:
a continuously refreshed dataset of *which third-party URLs get cited for which commercial query
clusters, across engines, over time* (see `09-competitive-threats.md`, differentiation thesis 2).

## 6. What would have to be true for this to be a venture-scale company

Not a forecast — a list of conditions we should hold ourselves to:

1. The third-party-citation dataset must become a **proprietary, compounding asset** that clients
   cannot assemble themselves and incumbents will not sell (they sell brand-level scores, not
   "which listicle on which domain is the citation gateway for this query cluster").
2. Delivery labour per client must fall **≥50% within 12 months** through tooling, or the business
   is an agency with a nice dashboard and will cap out at founder energy.
3. At least one measurement surface must be **first-party and defensible** — e.g. a client-authorized
   Search Console + GA4 integration that joins AI-feature impressions (M1) to AI-referral conversions
   (M3) — because third-party prompt sampling is reproducible by anyone with $50 of API credit.
4. A revenue-attribution story must exist that survives a sceptical CFO **without claiming
   causation** (leading indicators + self-attribution + AI-referral conversions, presented as three
   separate tiers of evidence).
5. Churn must stay below ~2%/month at the managed tier. The retention mechanism is the volatility
   itself (M7–M9, M12): AI answers change weekly, citations decay without refresh (M8: pages not
   updated in 3 months are >3x more likely to lose citations), and competitors keep publishing.
   If clients reach a stable state, we must be willing to step them down — rule 24 in
   `docs/INTEGRITY-RULES.md`.
