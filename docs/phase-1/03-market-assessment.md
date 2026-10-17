# Phase 1 — Evidence-backed market assessment

Answers the brief's ten Phase-1 questions in order. Every claim carries an evidence-register ID
(`02-evidence-register.md`), which holds the URL, date and credibility tier. Our own estimates are
marked **[ESTIMATE]**; unverified claims are marked **[UNVERIFIED]**.

---

## Q1. How are customers using AI-powered search for product discovery?

Three distinct behaviours, and they must not be conflated:

1. **Assisted search inside a traditional SERP.** 60% of U.S. adults read AI-generated search
   summaries (B1, Pew, n=5,119, fielded Feb 2026). When an AI Overview appears, users click an
   organic result 8% of the time versus 15% when it does not, and 26% end the session (E3, Pew
   browsing study, 68,879 searches). This is the largest-volume surface and the one with the most
   reliable measurement (M1: Search Console now reports AI-feature impressions worldwide).
2. **Conversational discovery.** 49% of U.S. adults use AI chatbots, 24% daily, 42% use them to
   search for information (B1). ChatGPT reaches 44% of adults, Gemini 24%, Copilot 17% (B2).
3. **Delegated shortlisting (the new behaviour).** Buyers do not ask AI to point them at sources;
   they ask it to synthesize a ranked vendor list. 51% of B2B software buyers now start research in
   an AI chatbot more often than Google (29% a year earlier); 71% use chatbots somewhere in
   research; chatbots are the #1 shortlist influence at 54%, ahead of review sites (43%) and vendor
   websites (36%); 33% of a buyer's first prompts are category questions and 31% are head-to-head
   competitor comparisons (B3, B4, B5 — all G2, tier T2, with a commercial interest in the narrative
   but the only large-sample B2B dataset we found).

**Volume reality check (the number most vendors omit):** AI referrals are **1.08%** of website
traffic across 13,000+ domains and 3.3B sessions (E7), and all AI platforms combined were ~**0.24%**
of global internet traffic in Jan 2026 (E8). Organic search still moves ~345x more traffic (E8).
So: **the behaviour shift is real and fast; the traffic shift is small and slow.** Both are true,
and any honest business case must hold both. The commercial argument rests on conversion quality
(~2x organic and ~1/3 the sessions to close, E7; 4.4x per Semrush, 23x per Ahrefs on its own
signups, E10) and on *exclusion risk* — 69% of buyers chose a different vendor than planned because
of chatbot guidance and 33% bought from a vendor they had never heard of (B4).

## Q2. Which buyer journeys are changing most?

Ranked by evidence strength:

1. **B2B software / technology purchases, research-led, practitioner-driven.** Strongest evidence
   (B3–B6), highest AI-conversion premiums (E10), and the shortest measurable funnel. G2's buyers
   who sourced recommendations from AI chatbots bought from their initial shortlist in ≥3 of their
   last 5 purchases 80% of the time vs 65% for those who did not (B6) — i.e. **AI narrows the set
   before a human is involved.**
2. **Informational and consideration-stage queries in every vertical.** Where AI Overviews compress
   clicks hardest: organic CTR 0.61% vs 1.62% (E1), position-1 CTR −58% (E2). Gartner's 25%
   search-volume-decline-by-2026 forecast is proceeding unevenly and is concentrated on
   informational queries, with B2B SaaS and research-heavy queries most affected (B7).
3. **High-trust / high-stakes categories where third-party validation dominates** — cybersecurity,
   healthcare, financial services. Buyers consult analyst reports and peer reviews heavily (90% of
   enterprise buyers consult analyst reports; Gartner Peer Insights and G2 are explicitly used for
   unfiltered validation), and Perplexity leans on Reddit, LinkedIn and G2 for B2B queries (C1).
4. **NOT transactional e-commerce.** The one place with a *contradicted* premium: a 973-site study
   found organic beat ChatGPT referrals by ~13% for transactional purchases (E11). Marketplace
   mediation (Amazon/Flipkart own the query) compounds this in India (P12, A7).

## Q3. Which industries are most exposed to AI-mediated discovery?

Exposure = (share of journey that starts in AI) × (revenue dependence on that journey) × (how
concentrated the citation set is).

| Industry | Exposure | Why (evidence) |
|---|---|---|
| B2B software / SaaS | **Very high** | B3–B6; citation gateways are G2, comparison pages, listicles (C1, M8) |
| Cybersecurity products & services | **Very high** | analyst-report + peer-review dependence; Perplexity leans Reddit/LinkedIn/G2 for B2B (C1); legal/high-stakes queries are the *most stable* (M12), so being wrong or absent is persistent, not noisy |
| Financial services / fintech | High | B4-style shortlisting; regulated claims make misrepresentation (P6) costly |
| Professional services, agencies, consulting | High | "best X for Y" queries; personal-brand/expert-recommendation queries are the *least* stable (0.118, M12) — meaning share can be taken quickly |
| Healthcare / medical devices | High | 20% of U.S. adults use chatbots for medical advice (B1); Perplexity over-indexes NIH/PubMed (C3) |
| Travel / hospitality | High but adverse to independents | academic note that third-party authority signals are concentrated among large brands, disproportionately exposing independent/boutique operators (C6) |
| E-commerce (transactional) | Medium | E11 contradiction; marketplace mediation |
| Industrial / manufacturing B2B | Medium | long RFP cycles dilute AI influence; but exporter sites have basic technical gaps (A8) |

## Q4. What problems do businesses experience today?

See `04-pain-point-map.md` for the full map. In one line each: no visibility into AI answers (P1);
falling organic clicks (P2); no capacity to execute (P3); the effective levers are on sites they
don't own (P4); no provable ROI (P5); AI states falsehoods about them (P6); crawlability gaps (P7);
invisible in the markets they export to (P8); and vendor numbers that don't match what they see
themselves (P9).

The three that generate budget are **P3, P4, P6**. The one that blocks the sale is **P9**.

## Q5. How do they currently measure AI search visibility?

Four methods in practice, in ascending order of rigour:

1. **Manual spot-checks.** Ask ChatGPT/Perplexity/Gemini a few prompts, read the answer. Free,
   immediate, and — per M11/M12 — a single response carries almost no brand-discriminating signal
   (brand identity explains ~1.5% of variance in one response; ChatGPT's exact-repeat citation rate
   is 0.06%). Yet this is what most practitioners report doing (M14: "a lot of people are tracking
   with custom prompts and manual checks rather than paying for a platform").
2. **Free first-party data.** Search Console's generative-AI report (impressions, pages, countries,
   devices, dates; data from 18 May 2026; **no clicks, no queries**; absent tab ≠ absent presence)
   (M1); GA4 referral sessions from chatgpt.com / perplexity.ai / gemini.google.com (M3); Ahrefs'
   free AI-crawler-traffic tier and free visibility checkers; HubSpot's free AEO Grader (F6).
3. **Paid prompt-sampling platforms.** $29–$500/mo self-serve, $1,500–$5,000+/mo enterprise (F2, F6).
   They sample prompts across engines and report mention/citation/sentiment/share-of-voice.
   Accuracy and stability are the weak points: mention-detection accuracy averaged 81% across 12
   platforms (M13); day-to-day source overlap is only 34–42% (M9); ~30% brand persistence between
   consecutive runs (M8).
4. **Nothing.** The most common answer. 92% plan to optimize for AI search, 40.6% are doing so (P7).

**Critical distinction we must respect (integrity rule 8):** search-enabled LLM APIs are **not** the
consumer experience. Perplexity's API returns different retrieval and formatting than perplexity.ai;
OpenAI's API with a web-search tool is not ChatGPT with memory, personalization, plan tier and UI;
and OpenAI's ToS prohibit programmatic extraction from the consumer product except via the API (M4).
Every report we publish must separate "API surface observation" from "consumer experience
observation", and the latter must come from human-run captures.

## Q6. Which problems are already solved by existing products?

- Measuring brand mention/citation frequency across engines at a portfolio level: **solved** (F2, F6).
- Free baseline checks and AI-crawler visibility: **solved and free** (M1, F6).
- Detecting sentiment and misrepresentation: **partially solved** as a detection feature (P6).
- Serving machine-readable versions of owned pages to AI agents: **one productized attempt**
  (Scrunch AXP; vendor-claimed +364% brand presence / +218% citations for Akamai — T2, single case,
  unverified) (F4, O4).
- Enterprise workflow and BI export: **solved** (Profound, Scrunch Enterprise) (F1, F4).
- Traditional SEO fundamentals: **solved** by a 20-year-old industry at $3,209/mo average agency
  retainer (P1).

## Q7. Which problems remain underserved?

> **⚠ v2 correction (16 Oct 2026, C-01/C-08).** v1's answer to this question was **wrong** and rested on
> T3 review content that vendor documentation contradicts. Corrected answer below; the v1 text is quoted
> only so the error is auditable. Full capability matrix with sources and retrieval dates: `09` §2.

1. ~~**Execution in the mid-market price band** — between a $99/mo dashboard and a $5,000/mo agency.
   Verified gap: Peec "reports and recommends" with "no content generation, no changes to your site";
   Scrunch "shows you the gap and leaves the closing to you".~~ **RETRACTED.** Peec's changelog of
   **13 Oct 2026** ships *Actions* (site fixes, owned actions, and **earned actions such as getting
   listed, pitching editorial and growing reviews**), a **content optimizer** with per-suggestion
   accept/edit/reject/revert, a **Peec Agent** with 30 skills and 20+ MCP connectors, **Google
   Analytics** joins carrying conversions and revenue, and **Google Search Console** in early access —
   on plans from €70/mo, with "Nothing changes without your approval" (register X13-1…X13-6). Profound's
   AI Marketer drafts work and stages it for approval, and its Agents write into WordPress, Sanity,
   Contentful and Framer (X13-9…X13-11). Scrunch/Sitecore surfaces AEO opportunities with a projected
   citation lift that you **apply or decline inside the CMS Page Builder** (X13-13). The reviews v1 relied
   on were published 26 Aug – 26 Sep 2026 and were already stale.
   **What actually remains underserved [HYPOTHESIS]:** *managed human delivery* — the software drafts and
   stages, but a human still has to pitch the editor, update the G2/Capterra/TrustRadius profile, produce
   the asset and run the monthly cadence. That work is sold by agencies from **$997/mo** (register §14), so
   the gap is not capability or price band but **segment focus, accountability and disclosed measurement
   uncertainty** — which is exactly what Stage 1's buy-vs-hire card tests (`07` Q18a).
2. ~~**The off-site lever** — systematically identifying and earning placement in the third-party surfaces
   AI actually cites. No product does this; agencies do it by hand.~~ **RETRACTED as a differentiator.**
   The lever is real — 85% of commercial brand discovery is third-party (M8), the top 15 domains take ~68%
   of citation share (C4), ~90% of third-party mentions come from listicles/comparison/review roundups
   (M8), and **95% of AI-cited links come from non-paid sources** (X14-2) — but *identifying* gateways is
   table stakes (Peec Sources and Actions, Profound "earned media placements at highly cited sources",
   Scrunch Insights, Ahrefs/Semrush citation reports) and *earning* them is a published
   $3,000–$10,000/mo agency category with white-label suppliers behind it (X14-2/X14-3). **What is left is
   [HYPOTHESIS]:** measured, ethical, segment-specialised delivery at the bottom of that price band.
3. **Statistically honest measurement** — run counts, confidence intervals, per-surface separation,
   and a documented protocol (P9). The literature says single-prompt assessment is unreliable (M9)
   and that 10 prompts is insufficient (M7), yet tools publish single blended scores.
4. **Mid-market pricing for globally-selling companies in cost-advantaged geographies** (P8).
   Indian agencies publish ₹19,999–₹2,80,000/mo (P9) but mostly on-page only, without measurement.
5. **Remediation of false AI statements** (P6) — detection exists, correction workflows do not.
6. **A CFO-facing evidence stack that refuses to claim causation** (P5).

## Q8. How much do businesses currently spend on related services?

**Global (verified anchors):**
- SEO agency retainers average **$3,209/mo**; consultants $3,250; freelancers $1,349; 78.2% bill
  monthly retainers; most common band $501–$2,000 (P1). Clutch: $3,199/mo average, $37,158 average
  project (P2). Surveys disagree by >3x because they sample different slices (SE Ranking: 64% of
  agencies charge under $1,000/mo) (P2).
- B2B-specific: small B2B $1,500–$5,000/mo; **mid-market B2B SaaS $5,000–$10,000/mo**; enterprise
  $10,000–$50,000+/mo (P3). In-house senior hire $110k–$180k fully loaded (P3).
- GEO/AEO services: typical retainers **$1,500–$10,000/mo**; mid-market $3,000–$12,000; enterprise
  $10,000–$50,000+; one-time audits $500–$2,000 up to $5,000–$25,000; monitoring-only $500–$1,500/mo
  (P4).
- GEO tooling: self-serve $29–$500/mo, industry average ~$337/mo; enterprise custom-quoted,
  reported $1,500–$5,000+/mo [UNVERIFIED] (F6, F2).
- Budget share: enterprises allocated an average **12% of digital marketing budgets** to AEO/GEO in
  2025, 94% plan to increase, ~97% report positive funnel impact (P6, Conductor T2 survey of 250+
  enterprise leaders). Similarweb cites Forrester for **mid-market $75k–$150k/yr, enterprise
  $250k+/yr** — second-hand and internally inconsistent, so **[UNVERIFIED]** (P5).
- Revealed budget via hiring: dedicated roles at **$65k–$318k** base (H1, H2).

**India (verified anchors, published prices):**
- SEO: ₹8,000–15,000/mo local; ₹15,000–30,000 standard; ₹30,000–80,000 competitive national;
  one-time audit ₹15,000–40,000; full-service digital retainers ₹15,000–1,50,000/mo (P8).
- GEO/AEO: **₹19,999/mo** (Adexorb SEO+GEO), self-serve AI-visibility tooling **₹799 / ₹2,499 /
  ₹5,999 per month** (IndexGraph.ai); **₹20,000–45,000/mo** (Vikilinks); **₹24,000–₹2,80,000/mo**
  published tiers (Raasis — its ₹40,000 tier = 40 tracked commercial queries, 20 answer briefs,
  5 page upgrades, 1 entity cluster); **₹39,999/mo** retainer and **₹40,000** one-time audit
  (Digimark); **₹50,000 / ₹75,000 / ₹1,25,000 / ₹2,00,000 + GST** (DigiStreet) (P9).
- India digital advertising: ₹71,621 Cr in 2025 (+19%), projected ₹84,977 Cr in 2026 (Dentsu via
  T3); conflicting figures of ₹62,500 Cr and ₹35,000 Cr circulate for 2026 with different
  definitions — **do not quote any single India market-size number without reconciling
  definitions** (P10).

## Q9. Which customer segments have the strongest willingness to pay?

By *demonstrated* willingness (published prices and observed spend), not by stated interest:

1. **US/EU mid-market B2B SaaS and enterprise brands** — $5,000–$10,000/mo SEO retainers are
   normal (P3), $75k–$250k+/yr GEO spend is cited (P5), and they hire $152k–$318k roles (H1).
   Highest WTP, lowest reachability for us.
2. **India-origin companies billing a US/UK entity** — the same buyer, the same work, ~3.4× the
   break-even speed (see **`12-economics-v2.md` §5**, which supersedes `10` §3: a $1,500/mo Tier C client
   reaches founder-compensated break-even at **5 clients** vs **~30 clients** at ₹40,000/mo on identical
   COGS). **[ESTIMATE — tested by Q21 and the price ladder in Stage 1]**
3. **Indian cybersecurity product vendors with global ambition** — $4.46B segment revenue growing
   25%/yr, 400+ firms, 55% global (A5). Small universe, high severity, real budgets.
4. **India-origin global B2B SaaS billing in India** — anchored at ₹40,000–₹1,20,000/mo by
   published competitor prices (P9). Real, but at the low end it cannot support managed-service
   margins (§3 of `10`).
5. **Agencies** — pay $99–$500/mo for tooling and resell at 3–5x; high volume, low loyalty (F6, P2).
6. **Indian domestic SMBs** — ₹8,000–30,000/mo ceiling (P8). Structurally unprofitable for us.

## Q10. Standalone SaaS, agency, or hybrid?

**Hybrid, services-first, with software extracted only from demonstrated repetition.** The
reasoning, in order of evidential weight:

1. **The SaaS layer is being commoditized from three directions at once.** Free first-party data
   from Google (M1), free/cheap bundled checkers from HubSpot/Semrush/Ahrefs (F6), and a funded
   leader that withdrew self-serve pricing to chase enterprise (F2). Meanwhile the fastest-growing
   independent (Peec: $0→$10M ARR in 16 months, 2,500 customers, ~$4,000 ARPU, $29M raised, talking
   at ~$200M pre-money — F3) has already occupied the low-price/high-volume position we would need.
   Two independents were acquired within 12 months (F4, F5): the exits exist, but for companies
   that raised first.
2. **The money is in execution, and execution is labour.** GEO retainers are $1,500–$50,000/mo (P4)
   versus $29–$500/mo tooling (F6). The adoption gap (92% plan / 40.6% act, P7) and the off-site
   lever (85% third-party, M8) are both *work* problems, not *information* problems.
3. **A pure agency has no compounding asset and caps at founder energy.** So the hybrid must extract
   software from the two parts of delivery that are genuinely repeatable: (a) the measurement
   pipeline (sampling, repeats, extraction, scoring, CIs) and (b) the third-party citation-gateway
   dataset. Everything else stays human.
4. **Break-even is ~2 clients** (`10` §4), so the services-first path carries almost no capital risk
   and produces the case studies needed to sell into the higher-WTP segments later.
5. **Reversibility check (per the brief's decision framework):** services-first → software is
   reversible (we can stop delivering and sell the tool); software-first → services is expensive
   (a dashboard brand does not convert into a trusted operator, and the build cost is sunk).
   Choose the reversible direction.

**Verdict: hybrid, sequenced as service → productized service → software where repetition is
proven.** Not "SaaS with a services wrapper," which is the version that dies.
