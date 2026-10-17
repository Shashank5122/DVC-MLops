# Stage 2 — Competitor capability matrix (living document)

**Workstream B1/B2 of the founder's decision of 16 Oct 2026.** Agent-executed desk research; no spend, no
outreach, no code. Started 16 October 2026.

**Central question:** *what commercially valuable work can SignalGEO perform that existing platforms, agencies
and in-house teams do not already provide adequately?*

## Labelling rules (mandatory)

- **[VERIFIED]** — retrieved from official vendor documentation, changelog, pricing page, developer docs, or an
  official product doc, **with the URL and retrieval date recorded**.
- **[PARTIALLY VERIFIED]** — official source seen but incomplete (e.g. a feature named without detail, or a
  price shown without packaging), or two consistent credible secondary sources with no official page retrieved.
- **[NOT FOUND]** — we looked in the obvious official places on the stated date and did not find it. **This is
  never a claim that the capability is absent.**
- **[UNKNOWN]** — we have not yet looked, or the evidence conflicts.
- Capability descriptions from a vendor are additionally tagged **(vendor-claimed)**: we verified that the
  vendor documents it, not that it works as described.

**Rule from the v1 failure:** three reviews published 26 Aug – 26 Sep 2026 said Peec had "no content
generation"; Peec's changelog of 13 Oct 2026 disproves them. Every claim here carries a retrieval date and is
re-checked before external use (`11-correction-log.md` C-01).

## Priority targets (B1)

| # | Target | Type | Status today |
|---|---|---|---|
| 1 | **Peec AI** | Platform | **Verified 16 Oct 2026** — official pricing page + changelog + API docs |
| 2 | **Profound** | Platform | Verified 16 Oct 2026 — official site + blog (16 Oct 2026) |
| 3 | **Scrunch / Sitecore** | Platform (enterprise CMS) | Verified 16 Oct 2026 — scrunch.com + official Sitecore product docs |
| 4 | Otterly.AI | Platform (low-cost) | [UNKNOWN] — pricing/capabilities from register only; retrieval queued |
| 5 | Semrush (AI Visibility Toolkit) | Suite | [UNKNOWN] — retrieval queued |
| 6 | Ahrefs (Brand Radar) | Suite | [UNKNOWN] — price conflict unresolved ($398 vs $199); retrieval queued |
| 7 | Managed GEO agency #1 — **SourceRank AI** ($497 audit / $997/mo, "done for you, measurement included") | Agency | [PARTIALLY VERIFIED] — price via a third-party roundup (12 Oct 2026); own site not yet retrieved |
| 8 | Managed GEO agency #2 — **MADX Digital** ($2,500/mo per pillar, $5,500/mo fully managed) | Agency | [PARTIALLY VERIFIED] — price via roundup (30 Sep 2026); own site not yet retrieved |
| 9 | White-label provider — **DemandLocal** (digital PR for GEO, $3,000–$10,000/mo mid-market, explicit white-label programme) | White-label | [PARTIALLY VERIFIED] — own blog playbook retrieved; service page and rate card not yet retrieved |

---

## B2 capability matrix

Legend: ✔ VERIFIED · ◐ PARTIALLY VERIFIED · ? UNKNOWN · — NOT FOUND (≠ absent). All vendor entries are
(vendor-claimed) unless independently corroborated.

| # | Capability | **Peec AI** | **Profound** | **Scrunch / Sitecore** | Otterly | Semrush | Ahrefs | Agencies (7/8) | White-label (9) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Brand mention & citation monitoring | ✔ daily, multi-model, per-topic/geo/competitor | ✔ | ✔ | ? | ? | ? | ◐ via tools | ◐ via tools |
| 2 | AI answer & competitor tracking | ✔ visibility, position, sentiment, share of voice vs competitors | ✔ Answer Engine Insights | ✔ Monitoring & Citations | ? | ? | ? | ◐ | ◐ |
| 3 | Query / purchase-intent intelligence | ✔ **intent classification (informational / commercial / transactional)**, branded vs non-branded classification, prompt volume scored 1–5 | ◐ Prompt Volumes | ◐ AI Search Trends | ? | ? | ? | — | — |
| 4 | Citation-source discovery | ✔ **Source analytics**: domain & URL detail, subdomain tracking, fanout overview, retrievals, citation share, **source classification (competitor / editorial / reference / UGC)** | ✔ citation categories | ✔ citations | ? | ? | ? | ◐ | ◐ |
| 5 | Third-party content-gap detection | ✔ **Gap analysis**: "sources that appear often and name competitors but not you, by source, domain, subdomain, URL and host" | ◐ Opportunities | ✔ content-gap recommendations | ? | ? | ? | ◐ "source-gap work" | ◐ |
| 6 | Citation-gateway recommendations | ✔ **Recommended actions "grouped by earned and owned"**, ranked, with evidence; Sources surfaces "third-party channels worth working with" | ✔ "earned media placements at highly cited sources" | ✔ prioritised recommendations with **projected citation lift** | ? | ? | ? | ✔ human judgement | ✔ |
| 7 | Website technical audits | ✔ **crawlability audit across 40+ AI bots**, crawl insights (which bots hit which pages, status codes), sitemap/`llms.txt`/Organization-schema checks | ◐ | ✔ Site Optimization / site diagnostics | ? | ✔ AI Search Health | ? | ✔ | ◐ |
| 8 | Content generation & optimisation | ✔ **content optimizer** (accept/edit/reject/revert per suggestion; passage-level rework; feature pages, articles, listicles) + `POST /customer/v1/actions/optimize_content` returning text, URL, score /100 and suggestions | ✔ Agents/Sheets: draft, refresh, translate, FAQs, PDP optimisation; Agent Template Marketplace | ✔ Content Enrichment + Content Transformation applied in Page Builder | — | ? | — | ✔ human | ✔ human |
| 9 | Fact-checking & entity corrections | ✔ **Prompts fact-checked** against "facts you set"; Facts per brand; **Objections** traced to the pages behind them; fact-checking actions name contradicting source pages | ✔ FactCheck traces claims to publishers, **drafts a personalised correction per publisher, tracks which updated** | — | — | — | — | ◐ | ◐ |
| 10 | Human review & approval | ✔ "Nothing changes without your approval"; atomic edit API ("nothing is written unless every edit applies") | ✔ "pings you for approval"; "Stage everything, do not publish" → "all staged as drafts, nothing live" | ✔ apply or decline each recommendation | ? | ? | ? | ✔ | ✔ |
| 11 | CMS integrations & publishing | ◐ connected tools + MCP connectors (Notion, Linear, DataForSEO); no direct CMS write found | ✔ **WordPress, Sanity, Contentful, Framer** read/write; Google Suite; Gamma; Slack | ✔ **native — inside SitecoreAI CMS Page Builder**; AXP edge delivery | ? | — | — | ✔ | ✔ |
| 12 | Digital PR / earned-media **delivery** | — recommends, does not deliver ("your team still executes it") | ◐ drafts outreach; delivery not evidenced | — | — | — | ✔ **this is the retainer** (listicles, review platforms, community, editorial pitching) | ✔ wire releases, syndication, expert pitching, newsjacking |
| 13 | GA4 / GSC / CRM integration | ✔ **Google Analytics** (AI referrals: sessions, engaged sessions, conversions, **revenue**); **GSC in early access**; CDN/log providers (Vercel, Cloudflare, AWS CloudFront, WordPress) | ◐ Agent Analytics (server-side AI traffic) | ◐ Agent Traffic | ? | ◐ | ◐ | — (client shares) | ◐ |
| 14 | Pipeline & revenue reporting | ✔ AI referrals incl. conversions/revenue; **visibility lift analysis + visibility lift predictor**; Looker Studio / Data Studio connector; Power BI | ◐ reports; no revenue attribution found | ◐ | ? | ? | ? | ◐ | ◐ |
| 15 | Agency & white-label functionality | ✔ **separate agency pricing page**; unlimited users on every plan; 1/2/5 projects by tier; role-based permissions per project; API + MCP | ✔ agency self-serve **$399/mo per client workspace** | ✔ dedicated agencies section | ◐ unlimited team members | ? | ? | n/a | ✔ core offer |
| 16 | Pricing, implementation burden, ongoing labour | ✔ see below | ◐ brand plans custom-only since mid-Sep 2026 | ◐ enterprise/CMS-dependent | ? | ? | ? | ◐ published ranges | ◐ |

### Pricing verified today

**Peec AI — official pricing page, retrieved 16 Oct 2026** [VERIFIED]:

| Plan | Price | Prompts | Models | Projects | Other |
|---|---|---|---|---|---|
| Starter | **$95/mo** | 50 | choose 3 | **1** | unlimited users, daily tracking |
| Pro | **$245/mo** | 150 | choose 3 | 2 | + 3 countries |
| Advanced | **$495/mo** | 350 | choose 3 | **5** | + multi-country, Looker Studio |
| Enterprise | custom, annual | customisable | **up to 13** | unlimited | API, SSO, custom prompt setup, daily or weekly |

Unlimited users on every plan; separate **agency pricing page** exists (linked, not yet retrieved);
"Trusted by 3500+ brands and agencies" (vendor-claimed). Third-party reviews (Sep 2026) report a 15% annual
discount ($80/$205/$420) and extra tracked models at $30/$70/$140 per month — **[PARTIALLY VERIFIED]**, not on
the page retrieved today. Monthly AI answers are computed as prompts × active models × frequency
(4,500 / 13,500 / 31,500 per the same reviews).

**Implication for our COGS (A-9 in `12-economics-v2.md`):** the binding constraint is **projects**, not seats —
Starter covers 1 brand. Five Stage 1 diagnostics therefore need either Advanced ($495) or the hybrid path in
`00-integrated-plan.md` §9 (one brand in the tool + four via official APIs and human capture). Per-client
tooling at scale: **$99/client/month at Advanced's 5 projects, $95 at Starter-per-client.**

### Traction verified today

Peec: ARR **$15M**, market adoption **quadrupled to 19%**, second-highest enterprise adoption **21%**,
3,500+ brands and agencies (vendor press release 13 Oct 2026 citing Ramp Rate data + pricing page)
[VERIFIED as vendor-issued]. Profound: $180M Series D at $1.8B (15 Sep 2026), ~$335M total.
Scrunch: acquired by Sitecore 3 Jun 2026 (~$225M reported by Bloomberg, unconfirmed); "trusted by over 500
companies" (vendor-claimed).

---

## What this tranche already answers

**B4 question 1 — do competitors collect the same citation-gateway data?** **Yes, verified.** Peec's Source
analytics + Gap analysis enumerate the domains, subdomains, URLs and hosts that cite competitors and not the
client, classified as competitor / editorial / reference / UGC, with citation share and retrievals.

**B4 question 2 — can their customers access it?** **Yes, verified.** CSV export is listed on the pricing page
under Data access; API and MCP exist (API shown at Enterprise tier — **per-plan confirmation queued**); Looker
Studio / Data Studio connectors ship from Advanced.

**B4 question 8 — could a customer reproduce our gateway work with existing tools?** **Largely yes, verified** —
for $95–$495/month. **This closes the citation-gateway-as-moat thesis** (already withdrawn in `09` §6 C-08) and
moves the question to B4's questions 5–7: are the identified opportunities *actionable*, do actions produce
*measurable* improvement, and does anything *compound*. Those are Stage 1 empirical questions, not desk
research — they need diagnostics delivered and outcomes observed over months.

**B3 implication for H1 (managed execution specialisation):** capability rows 8–11 are occupied by software, but
**row 12 (digital PR / earned-media delivery) is not occupied by any platform we have verified.** Peec
recommends earned actions; Profound drafts corrections and outreach; neither pitches the editor, negotiates the
listicle, updates the G2 profile or produces the asset. That is the surviving gap — and it is labour, sold by
agencies from $997/month.

**B3 implication for H4 (agency infrastructure):** weaker than it looks. Peec has a dedicated agency pricing
page, unlimited users on every plan and per-project role-based permissions; Profound sells agency workspaces at
$399/month. So H4 cannot be "tooling for agencies" — it must be "**verified human delivery and measurement QA
that agencies cannot staff**", which is a services contract competing with white-label digital-PR suppliers
(target 9).

**B3 implication for H3 (commercial-outcome intelligence):** Peec already joins GA4 conversions and revenue to AI
referrals and ships a "visibility lift analysis" and "visibility lift predictor". Our differentiator cannot be
the join; it can only be **the honesty of the interval and the refusal to claim causality** — and note that a
vendor "lift predictor" is precisely the kind of claim our protocol forbids us from making. That asymmetry is a
trust position, not a feature.

---

## Tranche 2 — trials, agency economics and API rate cards (verified 16 Oct 2026)

Full evidence rows in `../phase-1/02-evidence-register.md` §16 (X16-1 … X16-12). Summary of what changed:

| Target | New verified fact | Label |
|---|---|---|
| **Peec (agency)** | **Free 7-day pitch projects on every agency plan, outside the client quota** — prospect visibility profile, competitor benchmarking, the prompts where they are invisible, across six channels; instant data; convert to paid in three clicks keeping 7 days of history. **MCP free on every paid plan.** Plans: Essential €205 (10,000 credits, ~111 prompts) · Growth €425 (~277) · Scale €675 (~722) · Comprehensive custom/unlimited. Consolidated billing across client projects; CSV export; per-project role-based permissions | **[VERIFIED]** peec.ai/pricing-agencies + peec.ai/for-agencies, 16 Oct 2026 |
| **Peec (brand)** | Starter $95 (50 prompts, **1 project**) · Pro $245 (150, 2) · Advanced $495 (350, **5**) · Enterprise custom (up to 13 models, API, SSO). Unlimited users on all plans. Data access: API, MCP, CSV. Integrations: GA4 + CDN/log providers | **[VERIFIED]** peec.ai/pricing, 16 Oct 2026 |
| **Profound** | Agency Growth **$99/mo includes 10 pitch workspaces** (25 prompts × 3 engines × 7 days, extendable); **full client workspace $399/mo each** ⇒ $498 for one client, ≈$4,089/mo for ten; free 7-day brand trial; one language/region on self-serve; no Google organic view | **[PARTIALLY VERIFIED]** — three consistent secondary sources (26 Aug, 30 Jul, 14 Oct 2026); official page not retrieved |
| **Scrunch** | Starter **$250/mo annual or $300 monthly**, Growth $417/$500, Enterprise custom; **7-day free trial, no credit card**; free 30-second AI visibility audit; extra seats $25/mo | **[PARTIALLY VERIFIED]** prices (secondary, citing scrunch.com/pricing 15 Sep 2026) + **[VERIFIED]** free audit/trial on scrunch.com |
| **Otterly** | Lite $29 (15 prompts fixed, 4 engines, 1,000 URL audits, unlimited team members) · Standard $189 (100 prompts, **API 2,000 req/mo, MCP, Agent Analytics**) · Premium $489 (400 prompts) · Enterprise from $1,000; 15% annual; **Claude and Gemini are paid add-ons**; free trial **7 days/50 prompts (one source) or 14 days (another)** — conflict recorded | **[PARTIALLY VERIFIED]** — three secondary sources citing otterly.ai/pricing |
| **SourceRank AI** (agency target 7) | **$497 one-time AI Visibility Audit; ongoing from $997/mo (Foundation)** — "GEO and AEO done for them, measurement included" | **[PARTIALLY VERIFIED]** — stated on **their own domain** (12 Oct 2026); own pricing page not retrieved |
| **Gemini grounding (API)** | Gemini 3+: billed **per query executed**, **5,000 free requests/month**, then $14/1,000; returns a grounded answer with citation annotations, **not a SERP**; Flash tokens $0.75/$3.75 per M through 31 Dec 2026, doubling 1 Jan 2027 | **[VERIFIED]** ai.google.dev official docs |
| **Perplexity (API)** | **Sonar Chat Completions ended 27 Sep 2026**; Sonar now Agent API presets: $1/M tokens + $5/$8/$12 per 1,000 by context, ≈$0.007 per answer; Search API flat $5/1,000, raw results, no answer; Pro subscribers get $5/mo API credits | **[PARTIALLY VERIFIED]** — three consistent Oct-2026 sources; official rate card not retrieved |

### Consequences for our own plan

1. **Five candidates can be measured on a vendor platform for $0** via Peec's free pitch projects — so the $95
   Starter purchase (S1) is **withdrawn**, and the hands-on capability test B1/CG-6 becomes free too.
2. **The binding constraint on licensed tooling is projects/workspaces, not seats** (Peec Starter = 1 project;
   Profound = $399 per real client). Per-client tooling at scale is therefore **$95–$99/client on Peec Advanced
   or agency Essential, $399 on Profound, $29–$189 on Otterly** — which is the range `12-economics-v2.md` A-9
   already assumes, now better sourced.
3. **L1 API measurement is far cheaper than budgeted**: 1,500 observations ≈ **$16** (Perplexity ≈$9, Gemini
   ≈$2.50 inside the free grounding allowance, plus ~25% for retries). The S2 cap is revised from $110 to **$40**.
4. **Agencies have a published floor at $497 one-time / $997 per month** and a candid public argument that
   *"most teams under $3,000/month do better with one tool plus in-house fixes"* — the objection our $1,500
   Option C must survive. Recorded as X16-12 and built into the buyer script.
5. **H4 (agency infrastructure) is weaker than it looked**: Peec's agency plans include free pitch projects,
   consolidated billing, per-project permissions, client dashboards and free MCP; Profound sells ten pitch
   workspaces for $99. Agencies do not need our tooling — they may need our **verified human delivery and
   measurement QA**, which is a services contract competing with white-label digital-PR suppliers.

## Retrieval queue (next tranche, agent-executed, no approval needed)

| # | Retrieve | Answers |
|---|---|---|
| 1 | peec.ai/pricing-agencies | B1 target 1, capability 15; white-label economics |
| 2 | docs.peec.ai — API availability per plan, data-export terms, retention | B5 portability/lock-in |
| 3 | Profound pricing page + agency page (post-Sep-2026 packaging) | Capability 16; gap CG-2 |
| 4 | Scrunch pricing page; Sitecore docs on whether AEO opportunities require a Sitecore CMS licence | Capability 16; gap CG-3 |
| 5 | Otterly.AI pricing + feature pages | Target 4; cheapest tooling option for COGS |
| 6 | Semrush AI Visibility Toolkit page + Ahrefs Brand Radar page (resolve the $398 vs $199 conflict) | Targets 5–6 |
| 7 | sourcerankai.com own service/pricing page | Target 7 — is $997/mo real, and what is included? |
| 8 | MADX Digital GEO page | Target 8 — $2,500/pillar vs $5,500 managed scope |
| 9 | DemandLocal digital-PR-for-GEO service + white-label rate card | Target 9 — H4's real competitor |
| 10 | Peec hands-on trial of Actions + gap analysis (requires G-Spend S1) | Gap CG-6; B4 questions 5–6 |
| 11 | Whether any vendor publishes a measurement-uncertainty methodology (run counts, CIs, per-surface separation) | Gap CG-5 — the last pillar of our honesty positioning |
| 12 | Independent source for "95% of AI-cited links are non-paid" (Muck Rack) and the Stacker+Scrunch "239% lift" claim | Gap CG-9; ethics ruling input |

Findings are appended to `02-evidence-register.md` §16 with URLs and retrieval dates; this matrix is updated in
place and the retrieval date on every changed cell is refreshed.
