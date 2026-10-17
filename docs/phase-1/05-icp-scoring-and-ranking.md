# Phase 1 — ICP comparison matrix, weighted scoring model and ranked segments

## 1. Model construction

Nine criteria, as required by the brief. Weights sum to 100. Scores are 1 (worst) to 5 (best).
Weighted score = Σ(weight × score), maximum 500; we report the weighted average on the 1–5 scale
(weighted score ÷ 100) so the number is interpretable.

**The weights are an explicit statement of who we are in the next 12 months:** a 1–2 person,
low-capital, founder-led team in India that must reach cash-flow positivity before it runs out of
patience. That is why willingness to pay (18) and problem severity (14) and measurability (14)
carry the most weight, and why market accessibility (6) carries the least — a huge market we
cannot reach is worthless to us, and a small market we can reach by name is not.

| # | Criterion | Weight | What a 5 means | What a 1 means |
|---|---|---|---|---|
| C1 | Problem severity | 14 | The buyer already feels revenue pain from AI-mediated discovery and has said so publicly | Nice-to-know curiosity, no budget line |
| C2 | Willingness to pay (verified price anchors) | 18 | Segment already pays ≥$3,000/mo for adjacent search services (documented prices) | Segment pays ≤₹20,000/mo and haggles |
| C3 | Sales cycle | 8 | Economic buyer can say yes in ≤4 weeks, pilot-friendly | Procurement + security review, 3–9 months |
| C4 | Customer acquisition difficulty | 12 | We can name and reach the accounts from India through communities we can actually enter | Cold outbound into saturated inboxes with an offshore-trust penalty |
| C5 | Measurability of results | 14 | A number moves within 90 days that the client can verify independently (signups, demos, AI referral conversions, citations) | Revenue lands 9–18 months later through RFPs; nothing attributable |
| C6 | Competitive intensity | 10 | No funded player targets this segment specifically | Profound/Peec/Semrush/Ahrefs/HubSpot + hundreds of agencies already sell here |
| C7 | Implementation complexity | 8 | English, docs/marketing-site changes, low regulatory risk, fast approvals | Huge gated enterprise estates, legal review on every sentence, compliance claims |
| C8 | Recurring value / churn resistance | 10 | The problem regenerates monthly (model drift, competitor publishing, 3-month content-freshness effect) | One-time fix, then the client cancels |
| C9 | Market accessibility & size | 6 | A few thousand reachable, nameable accounts | Hundreds of millions of accounts we can never reach, or fewer than 100 |

## 2. Segments evaluated (eight)

**S1 — India-headquartered B2B SaaS selling to US/UK/EU buyers** (Series A–C, roughly $1M–$50M ARR;
dev tools, data/AI infrastructure, martech, sales tech, HR tech, fintech infrastructure).
**S2 — Indian cybersecurity product vendors selling globally** (DSCI counts 400+ product companies;
55% have expanded globally but only 17% have overseas offices).
**S3 — Indian IT services / cloud & AI consulting exporters** (mid-size, roughly $2M–$100M revenue).
**S4 — US/EU mid-market B2B SaaS**, sold remotely from India.
**S5 — Digital/SEO agencies** as a white-label or done-with-you channel.
**S6 — India-origin D2C and export e-commerce brands** (Amazon Global Selling + own storefront).
**S7 — GCCs and in-house global marketing teams of multinationals in India.**
**S8 — Indian domestic SMB services** (healthcare, education, real estate, local services).

## 3. Scored matrix with rationale

Scores are ours; the justification cites the evidence register (`02-evidence-register.md`).

| Criterion (weight) | S1 India SaaS→global | S2 India cyber product | S3 India IT services | S4 US/EU mid-mkt SaaS | S5 Agencies | S6 India D2C export | S7 GCCs/MNC | S8 India domestic SMB |
|---|---|---|---|---|---|---|---|---|
| C1 Problem severity (14) | **5** | **5** | 4 | **5** | 4 | 3 | 4 | 3 |
| C2 Willingness to pay (18) | 4 | 4 | 3 | **5** | 3 | 2 | 4 | **1** |
| C3 Sales cycle (8) | 4 | 3 | 3 | 3 | 4 | 4 | **1** | 4 |
| C4 Acquisition difficulty (12) | 4 | 4 | 3 | 2 | 4 | 4 | 2 | 3 |
| C5 Measurability (14) | 4 | 3 | **2** | 4 | 3 | 3 | 3 | **2** |
| C6 Competitive intensity (10) | **2** | 3 | 3 | **1** | **2** | 3 | **2** | **2** |
| C7 Implementation complexity (8) | 4 | 4 | 3 | 4 | **5** | **2** | **2** | 3 |
| C8 Recurring value (10) | 4 | 4 | 3 | 4 | 3 | 3 | 4 | **2** |
| C9 Market accessibility (6) | 4 | **2** | 4 | **5** | 4 | 4 | 3 | **5** |
| **Weighted score (max 500)** | **394** | **370** | **306** | **376** | **346** | **300** | **296** | **250** |
| **Weighted average (1–5)** | **3.94** | **3.70** | **3.06** | **3.76** | **3.46** | **3.00** | **2.96** | **2.50** |

### Arithmetic shown (weight × score, summed)

- **S1** = 14·5 + 18·4 + 8·4 + 12·4 + 14·4 + 10·2 + 8·4 + 10·4 + 6·4 = 70+72+32+48+56+20+32+40+24 = **394**
- **S2** = 70+72+24+48+42+30+32+40+12 = **370**
- **S3** = 56+54+24+36+28+30+24+30+24 = **306**
- **S4** = 70+90+24+24+56+10+32+40+30 = **376**
- **S5** = 56+54+32+48+42+20+40+30+24 = **346**
- **S6** = 42+36+32+48+42+30+16+30+24 = **300**
- **S7** = 56+72+8+24+42+20+16+40+18 = **296**
- **S8** = 42+18+32+36+28+20+24+20+30 = **250**

### Rationale for the load-bearing scores

- **S1 problem severity = 5.** Its buyers *are* the G2 population: 51% of B2B software buyers now
  start research in an AI chatbot, chatbots are the #1 shortlist influence (54%), and 69% switch
  vendors because of chatbot guidance (B3, B4). An India-origin SaaS company that is absent from
  those answers is excluded before a human ever sees its site.
- **S1 competitive intensity = 2.** This is the single worst cell in the winning row. Profound
  ($1.8B), Peec ($10–15M ARR at 2,500 customers), Scrunch/Sitecore, Semrush ($99/domain),
  Ahrefs Brand Radar, HubSpot (free Grader, $45–50/mo) and dozens of GEO agencies all sell to
  exactly this buyer. We win here only on delivery model and price/geography arbitrage, never on
  a monitoring feature (F1–F6).
- **S1 WTP = 4, not 5.** These companies already pay for Ahrefs/Semrush seats and for SEO
  retainers; mid-market B2B SaaS SEO retainers run $5,000–$10,000/mo globally (P3) and Indian
  agencies publish GEO retainers at ₹19,999–₹2,80,000/mo (P9). But India-domiciled CFOs apply
  local price anchors, so the *same* company may pay $1,500/mo through a US entity and haggle at
  ₹40,000/mo through the Indian one. This is a pricing-architecture problem, not a demand problem
  — see §6.
- **S2 market accessibility = 2.** Only ~400 product companies exist (A5), and Tracxn counts just
  58 Indian cybersecurity startups at Series A+ (A6). Excellent beachhead *quality*, poor
  beachhead *quantity* — it is a wedge, not a market.
- **S3 measurability = 2.** IT-services deals are $50k–$250k with 3–9 month cycles and
  referral/RFP-driven sourcing (A9). We would be selling an unmeasurable promise to a
  margin-pressured buyer in a segment Nasscom itself describes as undergoing revenue compression (A1).
- **S4 acquisition difficulty = 2, competitive intensity = 1.** Highest WTP, largest universe, and
  the two worst cells we have: no network, cold outreach into the most-pitched-inbox segment on
  earth, and an offshore-vendor trust penalty. This is the right segment for year 2–3 with proof,
  not month 1 with none.
- **S5 implementation complexity = 5, recurring value = 3.** Agencies need no publishing rights and
  no credentials (lowest risk work we could do), and 56.2% of SEO agencies raised prices in
  2025–26 citing AI-search work (P2) — real demand for a deliverable. But agencies churn tools
  aggressively, buy on price, and become competitors. Channel, not beachhead.
- **S6 WTP = 2 and measurability = 3.** Thin margins, marketplace-mediated discovery (Amazon/
  Flipkart own the queries), and the one place where the AI conversion premium is *contradicted*:
  a 973-site e-commerce study found organic beat ChatGPT referrals by ~13% on transactional
  purchases (E11). Wrong first customer.
- **S7 sales cycle = 1.** GCC procurement, security review and vendor onboarding run 3–9 months
  and demand SOC 2 and references we do not have. Also the exact segment Profound Enterprise and
  Sitecore/Scrunch are built for.
- **S8 WTP = 1.** Indian local SEO retainers are ₹8,000–30,000/mo (P8) against thousands of local
  agencies. Our cost structure cannot beat that price and our measurement sophistication is wasted.

## 4. Ranked segments

| Rank | Segment | Weighted avg | One-line verdict |
|---|---|---|---|
| 1 | **S1 India-origin global B2B SaaS** | **3.94** | Best fit for who we are now; contested, so win on delivery model and evidence quality, not features |
| 2 | S4 US/EU mid-market B2B SaaS | 3.76 | Highest money, worst reachability; the expansion target once S1 produces references |
| 3 | S2 Indian cybersecurity product vendors | 3.70 | Small, nameable, high-severity; the ideal *second* wedge, sharing S1's playbook |
| 4 | S5 Agencies (white-label channel) | 3.46 | Fastest revenue per unit of trust, worst retention; use as leverage, not as identity |
| 5 | S3 Indian IT services / consulting exporters | 3.06 | Large, reachable, but slow cycles and weak measurability |
| 6 | S6 India-origin D2C/export e-commerce | 3.00 | High volume, low WTP, and the conversion premium is contradicted for transactional queries |
| 7 | S7 GCCs / MNC in-house teams | 2.96 | Enterprise sales motion we cannot run pre-traction |
| 8 | S8 Indian domestic SMB services | 2.50 | Structurally unprofitable for us |

## 5. Sensitivity analysis (the ranking is not weight-invariant, and we should know where it flips)

**Scenario A — "bootstrapped survivors"** (acquisition difficulty and competitive intensity
doubled to 24 and 20; WTP cut to 14; market size cut to 3; total weight 115, divide by 115):

| Segment | Weighted score | Average |
|---|---|---|
| S1 | 70+56+32+96+56+40+32+40+12 = **434** | **3.77** |
| S2 | 70+56+24+96+42+60+32+40+6 = **426** | **3.70** |
| S5 | 56+42+32+96+42+40+40+30+12 = **390** | **3.39** |
| S4 | 70+70+24+48+56+20+32+40+15 = **375** | **3.26** |

→ Under survival weighting, **S1 still wins, S2 closes to within 0.07, and S4 drops from #2 to #4.**
This is the decisive argument for S1: it is the only segment that wins under both weightings.

**Scenario B — "venture-scale ambition"** (WTP doubled to 36, market size doubled to 12,
acquisition difficulty halved to 6, competitive intensity halved to 5; total weight 113):

| Segment | Weighted score | Average |
|---|---|---|
| S4 | 70+180+24+12+56+5+32+40+60 = **479** | **4.24** |
| S1 | 70+144+32+24+56+10+32+40+48 = **456** | **4.04** |
| S2 | 70+144+24+24+42+15+32+40+24 = **415** | **3.67** |
| S5 | 56+108+32+24+42+10+40+30+48 = **390** | **3.45** |

→ If we weight money and market size, **S4 wins**. Honest reading: the beachhead choice is really
a choice of risk profile. S1 is the survivable path that *earns the right* to sell into S4 with
references and case data; S4 first is the path that needs capital and a brand we do not have.

**Which single score would change our mind?** C5 (measurability) for S1. If the 14-day validation
shows that India-origin SaaS prospects cannot or will not instrument AI-referral conversion and
self-attribution in GA4/their CRM, S1's advantage collapses to a dashboard sale — which is the
crowded, commoditizing market we should not enter. This is why the validation plan (§08) makes
"will you let us instrument your funnel?" a screening question rather than an onboarding step.

## 6. Recommended beachhead market

**Beachhead: India-headquartered B2B software companies (SaaS and cybersecurity product vendors)
whose primary buyers are US/UK/EU practitioners, and whose funnel has a short, instrumented
conversion event (free trial, demo request, signup, or a self-serve purchase).**

Narrowing filters, all four required:
1. **Origin/domicile:** India-headquartered, English-language, selling outside India. (Reason:
   we can reach the founder/head-of-growth directly, in our time zone, through communities that
   exist — SaaSBoomi's 4,000+ startup community, DSCI/Nasscom events, LinkedIn, Product Hunt.)
2. **Category:** research-led purchase, not RFP-led. Dev tools, data/AI infrastructure, martech,
   sales tech, HR tech, developer-facing security, fintech infrastructure. (Reason: G2's data shows
   AI-mediated shortlisting is strongest for software bought by practitioners, and 31% of buyers'
   first prompt is a head-to-head competitor comparison — B5.)
3. **Stage/revenue:** Series A+ or $1M–$50M ARR, with at least one full-time growth/marketing
   owner. (Reason: Tracxn counts 1,049 Series A+ SaaS companies in India and 58 Series A+ Indian
   cybersecurity startups — a nameable universe — and these companies have a marketing budget but
   not a $171k in-house GEO hire, H1/H2.)
4. **Instrumentability:** willing to connect GA4 + Search Console and add a "how did you hear
   about us" field. Non-negotiable, because it is the only honest path from visibility to revenue.

**Explicitly excluded from the beachhead:** GCCs/enterprise procurement (S7), domestic Indian SMB
(S8), transactional e-commerce (S6), and pure IT-services/consulting (S3) — for the reasons scored
above, not because they are bad businesses.

**Why S2 (cybersecurity) is the adjacent wedge rather than the beachhead:** the universe is only
~400 product companies (A5) and 58 Series A+ (A6) — too small to build a company on, but the
severity is extreme (buyers research security tools heavily in AI, misrepresentation of a
security product's compliance posture is a sales-blocker, and 55% have global ambition with only
17% having overseas offices). Same playbook, same tooling, ~15% of the effort to reach a nameable
list. Sequence: S1 first, S2 as the second vertical once we have 5 S1 case studies.

## 6.1 Post-correction robustness re-score (added 16 Oct 2026, corrections C-01 / C-08)

Two columns of the §3 matrix were scored on evidence that official vendor documentation has since
contradicted. Rather than silently re-score, both adjustments are shown here with the arithmetic.

**Adjustment 1 — C6 competitive intensity, −1 for segments squarely inside the funded platforms' ICP.**
v1 scored S1 at 2 partly because "the mid-market execution layer is empty." It is not: Peec Actions +
content optimizer + Peec Agent (€70–€360/mo), Profound AI Marketer/Agents with CMS write access
($399/mo per agency workspace, custom for brands), Scrunch/Sitecore apply-or-decline in-CMS
recommendations. Global B2B SaaS (S1) is exactly these vendors' target customer, and agencies (S5) now have
dedicated vendor programs, so **S1: 2 → 1** and **S5: 2 → 1**. S4 is already at the floor (1). S2
(Indian cybersecurity *product* vendors) stays at 3 — no funded platform specialises in that vertical, though
all of them can serve it.

**Adjustment 2 — C5 measurability, −1 where it was scored 4.** `13-measurement-reproducibility-protocol.md`
§6 shows that honest intervals are ±0.29–±0.33 at n = 5 runs, and that demonstrating a 0.30 → 0.60 lift needs
~42 runs per arm (~81 for 0.20 → 0.40). Measurement remains a differentiator — no vendor publishes an
uncertainty protocol (gap CG-5) — but it supports weaker claims than v1 assumed, so **S1: 4 → 3** and
**S4: 4 → 3**. Segments already at ≤3 are unchanged.

| Segment | Base (§4) | After adjustment 1 | After adjustments 1 + 2 |
|---|---|---|---|
| **S1** India-origin global B2B SaaS | **3.94** (394) | **3.84** (394−10) | **3.70** (384−14) |
| **S2** Indian cybersecurity product vendors | 3.70 (370) | 3.70 | **3.70** |
| **S4** US/EU mid-market B2B SaaS | 3.76 (376) | 3.76 | **3.62** (376−14) |
| S5 Agencies | 3.46 (346) | 3.36 (346−10) | 3.36 |
| S3 India IT services | 3.06 | 3.06 | 3.06 |
| S6 India D2C export | 3.00 | 3.00 | 3.00 |
| S7 GCCs / MNC | 2.96 | 2.96 | 2.96 |
| S8 India domestic SMB | 2.50 | 2.50 | 2.50 |

**Reading:** the beachhead ranking is **fragile and no longer discriminating**. S1 leads by 0.18 in the base
model, by 0.08 after adjustment 1, and **ties exactly with S2 at 3.70 after both adjustments**, with S4 at
3.62 — a spread of 0.08 across the top three, which is well inside the noise of a subjective 1–5 scoring
exercise. A model that collapses to a tie on two defensible re-scores is not evidence; it is a structured
statement of priors.

**Consequence for Stage 1 (design change, applied in `08-validation-plan-v2.md` §3):** the five diagnostics
must not all come from one segment. Target **3 × S1, 1 × S2 (cybersecurity), 1 × S4 (US/EU mid-market SaaS
sold remotely from India)** so that real buyer responses — not re-argued weights — decide the beachhead. If
S4 or S2 responds materially better on the buy-vs-hire card and the price ladder, the beachhead changes. That
is a cheap and reversible decision, which is exactly the kind the brief tells us to prefer.

## 7. What we are NOT claiming

- We are not claiming the weighted model is objective. It is a structured way to make our
  trade-offs explicit and falsifiable; the weights encode our constraints, and §5 shows where the
  answer flips.
- We are not claiming S1 is large enough to support a venture-scale outcome on services alone.
  `12-economics-v2.md` §8 shows the honest bootstrapped 24-month band (**$61k–$375k ARR**) and §8.1 shows
  that $2M ARR requires **12–21 delivery FTEs**. v1's "$2M–$4M ARR" ceiling implied a 12–40 person agency
  and is withdrawn as a small-team outcome.
- We are not claiming any of these companies will buy. That is what Stage 1 in `08-validation-plan-v2.md`
  is for. Its gates are **decision bands that trigger a written founder decision**, not automatic kill
  switches (correction C-07).
