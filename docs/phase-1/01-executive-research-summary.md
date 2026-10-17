# Phase 1 — Executive research summary

**Date:** 2026-10-16 (v2) · **Author:** founding team (research + strategy) · **Status:** awaiting founder decision
**Companion files:** `02-evidence-register.md` (all sources, incl. new §13–§15) · `03-market-assessment.md` ·
`04-pain-point-map.md` · `05-icp-scoring-and-ranking.md` (incl. new §6.1 robustness re-score) ·
`06-assumptions-hypotheses-failures.md` · `07-discovery-interview-guide.md` ·
`08-validation-plan-v2.md` · `09-competitive-threats.md` · `10-tam-bottom-up.md` (§1 only; §2–§6 superseded) ·
`11-correction-log.md` · `12-economics-v2.md` · `13-measurement-reproducibility-protocol.md` ·
`00-decision-memo.md` (v2)

> **⚠ v2 CORRECTIONS — read before using §5–§9 of this file.** The founder withheld approval of v1 and
> required seven corrections; all are logged in `11-correction-log.md` (C-01…C-12). The three that change
> this summary:
> 1. **C-01 — "the mid-market execution layer is largely empty" was FALSE.** Official vendor documentation
>    retrieved 16 Oct 2026 shows Peec (Actions incl. *earned* actions, content optimizer, Peec Agent with
>    20+ MCP connectors, GA4 + GSC joins, ARR $15M, 19% market adoption), Profound (AI Marketer drafts work
>    and stages it for approval; FactCheck drafts publisher corrections; Agents write into WordPress/Sanity/
>    Contentful/Framer) and Scrunch/Sitecore (AEO opportunities with projected citation lift, apply-or-decline
>    in the CMS Page Builder) all ship approval-bound execution. §5 and §6 below are corrected in place.
> 2. **C-08 — the "citation-gateway dataset" is not a moat.** Every major platform already maps cited
>    third-party sources and recommends earned-media actions; agencies sell the execution from **$997/mo**.
>    §6's "compounding asset" bullet is withdrawn.
> 3. **C-02/C-03/C-09 — the economics were internally inconsistent** (13 client-hours in the capacity model
>    vs 21+ in COGS; no tooling line; break-even that paid the founder nothing). All numbers in §6 are
>    replaced by `12-economics-v2.md`.

---

## 1. Clear problem statement

Companies that sell to research-led B2B buyers are losing control of the first impression.
**51% of B2B software buyers now start their research in an AI chatbot more often than Google**
(29% a year earlier), chatbots are the **#1 influence on buyer shortlists at 54%** — ahead of review
sites (43%) and vendor websites (36%) — and **69% of buyers chose a different vendor than they
originally planned because of chatbot guidance**, with 33% buying from a vendor they had never heard
of (B3, B4). At the same time, when Google shows an AI Overview, users click an organic result
**8% of the time instead of 15%** (Pew browsing study, E3), position-1 organic CTR is **58% lower**
(Ahrefs, E2), and brand-level organic CTR on AI-Overview queries fell to **0.61% from 1.62%**
(Seer, E1).

The problem is not that these companies lack information. It is that:
1. They cannot see what AI says about them where it matters, in a form they can trust (P1, P9).
2. Even when they can see it, they have nobody to execute the fix (P3): **92% of marketers plan to
   optimize for AI search and only 40.6% are doing so** (P7).
3. The fixes that matter most are on websites they do not own (P4): **85% of commercial brand
   discovery in AI answers comes from third-party sources, brands are 6.5x more likely to be cited
   via third parties than via their own domain, and ~90% of those third-party mentions come from
   listicles, comparison pages and review roundups** (M8). The top 15 domains take ~68% of all AI
   citation share, and only ~11% of cited domains appear on more than one platform (C4).
4. They cannot prove any of it to a CFO (P5) — and, in the strong causal form, nobody can.

**SignalGEO's problem to solve:** make an India-origin, globally-selling software company *present,
accurate and recommended* in the AI answers its buyers read first — with evidence the client can
verify without us — at a price between a $95 dashboard and a $5,000/mo agency.

## 2. Evidence of demand (what is verified vs what is inferred)

**Verified, independent (T1):**
- Pew, n=5,119, fielded Feb 2026: 49% of U.S. adults use AI chatbots (33% in 2024), 24% daily, 42%
  use them to search for information, 60% read AI search summaries, ChatGPT reaches 44% (B1, B2).
- Pew browsing study, 68,879 searches: 8% vs 15% organic click rate with/without an AI Overview;
  26% end the session (E3).
- Employer-published compensation for dedicated AI-search roles: AWS AEO Manager $152,300–$216,090;
  Victoria's Secret Director AI & Organic Search $224,000–$318,000; Home Depot, Workday, Rippling
  and others hiring (H1). **Companies are putting six-figure salaries behind this problem.**
- Aggarwal et al., KDD 2024 (peer-reviewed): adding citations, quotations and statistics raised
  source visibility up to ~40% on their benchmark and ~22% on live Perplexity; keyword stuffing did
  not help; the lowest-ranked sources gained most (O1). **The lever exists and is documented.**
- RBI reference rate 95.032 INR/USD on 14 Oct 2026 (X1) — our FX basis.

**Verified, but vendor-interested (T2):**
- G2's buyer surveys (B3–B6); Conductor: AI referrals = 1.08% of traffic across 13,000+ domains and
  3.3B sessions, converting ~2x organic and closing in ~1/3 the sessions; enterprises allocate an
  average **12% of digital marketing budgets** to AEO/GEO with **94% planning to increase** and
  **~97% reporting positive funnel impact** (E7, P6).
- Published prices proving willingness to pay: GEO retainers **$1,500–$50,000+/mo** globally (P4);
  SEO agency retainers averaging **$3,209/mo** across 439 providers (P1); mid-market B2B SaaS SEO
  retainers **$5,000–$10,000/mo** (P3); Indian GEO retainers published at **₹19,999 – ₹2,80,000/mo**
  and self-serve AI-visibility tooling at **₹799 – ₹5,999/mo** (P9); 56.2% of SEO agencies raised
  prices in 2025–26 citing AI-search work (P2).
- Category capital and revenue: **Profound raised $180M at a $1.8B valuation on 15 Sept 2026**
  (~$335M total across five rounds since Aug 2024) and reports revenue tripling in six months (F1);
  **Peec reached ~$10M ARR 16 months after launch with 2,500+ customers (~$4,000 ARPU)**, with
  Sacra estimating $15M ARR by Aug 2026 and a new round discussed at ~$200M pre-money (F3);
  **Sitecore acquired Scrunch in June 2026** (~$225M reported, unconfirmed) and **HubSpot acquired
  XFunnel in Oct 2025** (~$30M reported) (F4, F5).

**Counter-evidence we must hold in view (integrity rule 5):**
- AI referral traffic is **~0.24% of global internet traffic** (Jan 2026), with organic search
  still moving ~345x more (E8). The behaviour shift is fast; the traffic shift is small.
- The conversion premium is **contradicted for transactional e-commerce**: a 973-site study found
  organic beat ChatGPT referrals by ~13% on transactional purchases (E11).
- AI answers are **volatile**: cited-source sets overlap only 34–42% between consecutive days (M9);
  ~30% of brands persist between consecutive runs and 1 in 5 across five runs (M8); ChatGPT's
  exact-repeat citation rate is 0.06% (M12); 82% of Perplexity answers in one large study contained
  no brand mention at all (M7). But within-minutes repeats are ~95% consistent (M10) — so the
  instability is driven by *time*, not sampling noise (M11).
- Practitioners are openly sceptical: "any tool purporting to track your visibility in LLMs like GPT
  is complete snake oil"; "no tool is reliable for now… a lot of people are tracking with custom
  prompts and manual checks rather than paying for a platform" (M14).
- Measurement is being **given away free**: Google's Search Console generative-AI report has been
  worldwide since 31 Aug 2026 (impressions, pages, countries, devices, dates — no clicks, no
  queries) (M1); HubSpot's AEO Grader is free; Semrush and Ahrefs bundle checkers into suites
  buyers already pay (F6).

**Demand verdict: real and growing at the top of the funnel (behaviour and budgets), unproven at the
bottom (attributable revenue), and contested in the middle (free/cheap measurement).** The
opportunity is in *execution*, not *information*.

## 3. Target customer ranking (full model in `05`)

| Rank | Segment | Weighted avg (1–5) | Verdict |
|---|---|---|---|
| **1** | **S1 India-origin B2B SaaS selling to US/UK/EU** | **3.94** | **Beachhead.** Wins under both survival-weighted and growth-weighted sensitivity |
| 2 | S4 US/EU mid-market B2B SaaS | 3.76 | Highest WTP, worst reachability; year-2 expansion |
| 3 | S2 Indian cybersecurity product vendors | 3.70 | Adjacent wedge: only ~400 firms (DSCI) but extreme severity |
| 4 | S5 Agencies (white-label channel) | 3.46 | Fastest revenue per unit of trust, worst retention |
| 5 | S3 Indian IT services / consulting exporters | 3.06 | Slow cycles, weak measurability |
| 6 | S6 India-origin D2C / export e-commerce | 3.00 | Low WTP, marketplace-mediated, conversion premium contradicted |
| 7 | S7 GCCs / MNC in-house teams | 2.96 | 3–9 month procurement we cannot survive pre-traction |
| 8 | S8 Indian domestic SMB services | 2.50 | Structurally unprofitable for us |

## 4. Willingness-to-pay hypotheses (to be tested, not assumed)

- **W1.** India-origin global software companies with a US/UK entity will pay **$1,000–$1,500/mo**
  for managed measurement + execution. *Basis:* global mid-market GEO retainers $1,500–$12,000/mo
  (P4); their existing SEO spend $2,500–$10,000/mo (P3). *Test:* H3, call ladder Q18–Q21.
- **W2.** The same company billing in INR anchors at **₹40,000–₹75,000/mo**. *Basis:* published
  Indian GEO tiers ₹19,999 / ₹24,000 / ₹39,999 / ₹40,000 / ₹50,000 (P9). *Test:* H3.
- **W3.** At ₹40,000/mo we can only afford ≤4 labour hours, so that price must buy **measurement +
  report + prioritized backlog** (≈80% gross margin), not execution (≈30% at best, negative in the
  conservative case). *Basis:* our own COGS model, `10` §3.
- **W4.** A **one-time audit at ₹75,000 (~$790)** will convert prospects who refuse recurring spend.
  *Basis:* one-time AI visibility audits sell at $500–$2,000 globally (P4) and ₹40,000 in India (P9).
- **W5.** Agencies would white-label at **$200–$400/mo per client workspace**. *Basis:* Profound
  agency $399/mo per client workspace (F2); Peec/Otterly unlimited seats at $95/$29 (F6).
- **W6.** Nobody will pay for a guarantee, and anybody who demands one is not our customer.
  *Basis:* integrity rule 7; category scepticism (M14).

## 5. Competitive threats (summary; full analysis in `09`)

1. **Funded platforms — and they now execute, not just measure** *(v2, C-01)*. Profound ($1.8B valuation,
   $335M raised), Peec (**ARR $15M**, market adoption **quadrupled to 19%**, 21% enterprise — Ramp Rate data
   via vendor press release 13 Oct 2026), Scrunch/Sitecore (acquired 3 Jun 2026). All three ship ranked
   actions **including earned-media actions**, in-product content optimisation with per-suggestion
   accept/reject/revert, approval-bound publishing into client CMSs, agent layers, and first-party analytics
   joins carrying conversions and revenue (register §13). **v1's mitigant — "Profound withdrew from the
   mid-market, so the middle was abandoned" — is withdrawn**: Profound withdrew its *self-serve brand tiers*
   but kept a $399/mo agency tier and shipped an execution agent, while Peec took the mid-market at
   €70–€360/mo *with* execution included on all plans. There is no empty middle.
2. **Suite bundling** — Semrush AI Visibility at $99/domain and included in $199 Semrush One;
   Ahrefs Brand Radar; SE Ranking. Threat: buyers won't add a fourth tool.
3. **Platform-given data** — free GSC generative-AI impressions; free HubSpot Grader; free Ahrefs
   checker. Threat: caps what a paid score can claim to add. **Response: never sell the number.**
4. **GEO agencies — and they already sell our v1 offer** *(v2, C-01)*. Published offers retrieved 16 Oct
   2026: **$997/mo** "GEO and AEO done for you, measurement included" (SourceRank, + $497 audit);
   **$2,000–$5,000/mo** "tool plus contractor"; **$2,500/mo per pillar or $5,500/mo fully managed** (MADX);
   **$3,000–$10,000/mo** digital-PR-for-GEO mid-market and $25,000–$30,000+/mo enterprise; **from
   $12,000/mo** PR-native (Crackle); global retainers $1,500–$50,000/mo; Indian ₹19,999–₹2,80,000/mo.
   Their published workstreams (prompt baseline, off-site publishing incl. review/listicle placements,
   source-gap analysis, reporting) match v1's differentiation thesis item for item. **White-label digital-PR
   suppliers let any agency resell the earned-media work tomorrow.** Still our WTP proof and our likeliest
   channel — now tested directly as option O2 (gate G-6).
5. **In-housing** — $65k–$318k roles at Amazon, Victoria's Secret, Home Depot, Workday, Rippling
   (H1). Caps the enterprise end; *helps* us in the mid-market that cannot justify a $171k hire.
6. **Provider restriction / drift** — OpenAI ToS prohibit programmatic extraction outside the API
   (M4); Perplexity's Sonar API was slated for deprecation on 27 Sept 2026 (M6). Demonstrated, not
   hypothetical.
7. **Category toxicity** — "snake oil" sentiment (M14) plus a documented pattern of unsourced
   statistics being published then retracted (O3).

## 6. Business viability assessment

**Viable as a services-led hybrid; not viable as a monitoring SaaS from our position.**

*(v2 — all figures from `12-economics-v2.md`; the v1 numbers in this section are superseded because the
capacity and COGS models used different hour definitions and omitted tooling.)*

- **One hour definition now governs everything.** `H_tier` = all client-facing hours per client per month:
  **Tier A 5 h** (measure/report/backlog, client executes), **Tier B 12 h** (managed on-site), **Tier C 21 h**
  (managed + earned media). Effective delivery hours per FTE 90/110/130 → **clients per FTE: A 18–26,
  B 7.5–10.8, C 4.3–6.2.** v1's "10 clients per FTE" was true only for Tier A and overstated managed
  capacity ~2×.
- **Variable cost per client/month (buy path, base tooling $100):** Tier A **$147** · Tier B **$198** ·
  Tier C **$264**. Gross margin: **82%** at $1,500 (Tier C), **75%** at ₹1,00,000, **65%** at ₹40,000
  (Tier A) — and **−6%** at ₹40,000 if tooling is $400/client/month. Labour is ~58% of cost; **tooling
  choice, not API price, is the margin risk at low price points.**
- **Buy, don't build.** Building our own measurement costs $22–$83/client/month in API spend **plus**
  ~40 h/month of engineering = $160/client at N=10, $80 at N=20, $53 at N=30 → **not cheaper than licensing
  until N ≈ 25–30**, and never cheaper during validation.
- **Two break-evens, not one.** Operating **cash** break-even at $600/mo fixed: **1 client** (Tier B/C USD),
  **3 clients** (Tier A ₹40,000). **Founder-compensated economic** break-even (+$4,000/mo market comp):
  **5 clients** at $1,500 · 8 at ₹1,00,000 · 11 at ₹75,000 · **~30 at ₹40,000**. Cash survival is trivial;
  founder compensation is the real constraint, and it is dominated by **price and billing domicile** (a USD
  buyer breaks even ~3.4× faster on identical COGS), not by cost control.
- **The ceiling is honest and modest.** Bootstrapped 24-month ARR: **$61k** conservative · **$162k** base ·
  **$375k** optimistic · **$70k** INR-Tier-A-only. Both INR-dominated variants are cash-positive by month 4
  and **never economically profitable within 24 months**; the base case reaches economic profit at month 13.
  **$2M ARR requires 12–21 delivery FTEs** — v1's "$2–4M ARR without external capital" implied a 12–40 person
  agency and is withdrawn as a small-team outcome.
- **There is no compounding asset.** *(withdrawn, C-08)* The citation-gateway map is sold by Peec, Profound,
  Scrunch, Ahrefs and Semrush; joined first-party data is sold by Peec (GA4 conversions + revenue) and given
  away by Google (GSC generative-AI report). Incumbents hold 2B+ prompts and 30M+ sources. What is left is
  delivery IP, India cost structure, and segment trust — none of which is a moat. **This is a finding, and
  the founder should decide deliberately whether a moat-less cash-generating service is the company they
  want (decision D-3).**
- **The strongest single risk is credibility, and the arithmetic is unforgiving.** Wilson 95% half-width at
  n = 5 runs is **±0.29–±0.33**; detecting a 0.30 → 0.60 lift needs **~42 runs per arm**. So we can sell
  **directional intelligence with disclosed uncertainty**, never proven lift — and v1's live "re-run it
  yourself" test is replaced by the interval-scored co-observation card in `13` §7.

## 7. Key assumptions and failure conditions

Sixteen critical assumptions (A1–A16), thirteen falsifiable hypotheses (H1–H12 + H3b), staged gates
G0/G1/G2 and four pivot branches are in `06` and `08-validation-plan-v2.md`. **v1's six numeric NO-GO
conditions are replaced by decision bands that trigger a written founder decision, never an automatic
company-wide kill** (C-07). The three that matter most:

- **A2/A3/H3b — buyers pay us rather than license a tool.** The decisive test. If **≥4 of 5** buyers
  choose the tool on the buy-vs-hire card, the service hypothesis is dead at our price and we route to
  O2 (agency channel) or O3 (a different problem) — **not** to Stage 2.
- **A5/H5 — our measurement survives co-observation.** Scored against a stated interval, not a point
  estimate. Systematic failure triggers the Red/Black band review in `13` §8 and a methodology change;
  it does not by itself kill the company.
- **A4/H7 — we can *act* on the off-site lever.** Identifying gateways is no longer differentiating
  (Peec and Profound both do it); the test is whether ≥50% of diagnostics yield ≥3 gateways we can
  ethically influence within a month.

## 8. Recommended next decision

*(v2)* **CONDITIONAL PROCEED to Stage 1 only; NO-GO on building any platform.**
Approve Stage 1 in `08-validation-plan-v2.md`: **14 days, 98 founder-hours, $408 cash (₹38,760)** —
5 diagnostics, 5 buyer conversations with the buy-vs-hire card and a 4-step price ladder, 2 agency
interviews, a written measurement protocol with a 200-response gold set, an hour-and-cost log, and ≥1
priced pilot proposal. **No application code.** Beachhead: **3 × S1, 1 × S2, 1 × S4** — `05` §6.1 shows the
post-correction ranking collapses to a 0.08 spread (S1 3.70 = S2 3.70 > S4 3.62), so the experiment must
discriminate rather than the spreadsheet. Differentiation: **thesis 4** in `09` §6 (the accountable operator
for a segment the platforms do not serve) with **thesis 1** as positioning, **thesis 3** as reporting
discipline, and **thesis 2 withdrawn as a moat**. Stage 2 (20 diagnostics) runs only if all three G2 tests
pass. Decision items D-1…D-6 are in `00` §I.

## 9. Closing four (required by the brief)

*(v2 — the full closing four is in `00-decision-memo.md`; this is the summary version, corrected.)*

- **Biggest uncertainty:** whether a buyer who can license a capable tool for ~$210/month will pay us
  $1,500/month to execute. Not market size, not technology, not churn — this one question decides whether
  SignalGEO is a business or a hobby.
- **What we may be overlooking:** that the buyer may be an **agency or a portfolio operator** rather than a
  brand; that **accountability** (a named human who verifies every claim and owns what gets published) may
  be the scarce product, not discovery; that value may be shifting from *being cited in an answer* to *being
  machine-readable and transactable by an agent*; that the founder's engineering skill is largely unused by
  an agency — a real cost beyond the $40/hour we model; and that **Indic-language and non-US surfaces are
  unmeasured by every vendor we checked**.
- **Strongest counterargument:** *"You have proven the market exists, that three funded vendors own the
  software layer, that agencies own the service layer from $997/month, and that you have no advantage in
  either. Peec shipped a complete execution layer in 90 days at $15M ARR — anything you do manually becomes
  a feature within two quarters. The rational move is not 98 hours confirming you would be a small agency;
  it is finding a problem where your engineering is the product."* This argument is strong and cannot be
  refuted with evidence — only tested cheaply, which is why `00` §I recommends running Stage 1 **and** a
  parallel problem search rather than either alone.
- **Best next experiment:** the buy-vs-hire card (`07` Q18a) on 5 named buyers **and 5 agencies**, alongside
  5 real diagnostics whose hours and API costs are logged line by line. Cost: **$408 cash, 98 hours.**
  Pre-registered falsification: ≥4 of 5 buyers choosing the tool, or a first "no" at or below ₹40,000 for
  ≥4 of 5 ⇒ the service hypothesis is dead at our price; go to O2 or O3, not to Stage 2.
