# Correction log — Phase 1 v1 → v2

Date: 16 October 2026. Raised by: founder (review of the v1 decision memo). Actioned by: research agent.
Every item below is a defect in **our own** work, not a change in the market. Each entry records the claim as
originally written, the correction, the evidence used, and the files affected.

Claim labels used throughout v2: **[VERIFIED]** primary/official source retrieved; **[ESTIMATED]** derived by us
from stated assumptions, no direct measurement; **[HYPOTHESIS]** plausible, untested; **[NOT YET VERIFIED]**
needs a source or an experiment we have not run.

---

## C-01 — "The mid-market execution layer is largely empty" — **RETRACTED**

**Claim as written (v1, `00-decision-memo.md` §A/E, `01` §4, `04` P3, `09` §3/§5):** the market separates into
measurement SaaS (no execution) and full-service agencies (expensive), and "the mid-market execution layer is
largely empty"; no competitor closes measure → recommend → approve → publish → re-measure.

**Correction:** the claim is **false as of October 2026** and was built on T2/T3 review content, not official
documentation. All three leading platforms ship approval-bound execution, earned-media recommendation, and
first-party analytics integration. The surviving distinction is narrower: **software-assisted execution
(the tool drafts and stages; the customer's team still does the work) vs managed human service delivery
(someone else pitches the editor, updates the G2 profile, produces the asset, and runs the monthly cadence).**

**Evidence [VERIFIED, official, retrieved 16 Oct 2026]:**

- **Peec AI** — `https://peec.ai/changelog`, entry 13 Oct 2026 "Get more done with actions and Peec Agent":
  - **Actions**, "a ranked list of opportunities with evidence… Site fixes come first, followed by owned
    actions on your own pages and **earned actions such as getting listed, pitching editorial, and growing
    reviews**." "Work on an action yourself, with the agent, or in a connected tool." "**Nothing changes
    without your approval.**" Included on all plans at no extra cost.
  - **Fact-checking actions** "point to source pages that contradict your brand facts."
  - **Content optimizer**: in-app editor with suggested changes; "accept, edit, or reject each one, and revert
    as you go"; select a passage and describe the rework; works on feature pages, articles and listicles.
  - **Peec Agent**: user/project/company context, file attachments (pdf/docx/pptx/xlsx/csv/txt/md),
    **20+ MCP connectors (Notion, Linear, DataForSEO)**, 30 built-in skills (model-gaps, **prompt auditor that
    flags prompts worded in favour of your own brand**, competitor analysis, weekly check-in), intelligence
    tiers and usage controls.
  - **Sources**: performance of social channels (YouTube, Reddit, LinkedIn, TikTok), channel movers, filter
    URLs by owner, "**find third-party channels worth working with**."
  - **AI referrals** (11 Sep 2026): "**Connect Peec to Google Analytics**" — traffic by assistant, landing
    page, country, device; engaged sessions, conversions and **revenue**.
  - **"My website" with Google Search Console** (early access, 13 Oct 2026); page-level crawl, citations and
    traffic; site checks for missing/invalid sitemaps, `llms.txt`, broken links in Organization schema.
  - **Customer API + MCP** expose actions, content optimisation, fact-check claim sources, social channels,
    project creation and member invites. `POST /customer/v1/actions/optimize_content` returns article text,
    URL, optimisation score /100 and suggestions with states pending/accepted/rejected;
    `.../optimize_content/edit` rewrites up to 50 passages and is atomic ("Nothing is written unless every
    edit applies"). Source: `https://docs.peec.ai/api/changelog`.
  - Traction: Ramp Rate data via press release 13 Oct 2026 — adoption **quadrupled to 19%**, **ARR $15M**,
    second-highest enterprise adoption (**21%**); integrations with Google Analytics and Vercel, Cloudflare,
    AWS CloudFront (EventBridge) and WordPress logs; Power BI and Looker Studio dashboards.
- **Profound** — `https://www.tryprofound.com/` (retrieved 16 Oct 2026) and
  `https://www.tryprofound.com/blog/introducing-the-next-generation-of-marketing-agents` (16 Oct 2026):
  - "**Your AI Marketer**… identifies the work worth doing, **drafts it, and pings you for approval**."
  - "**Chases down the wrong story at the source**: traces inaccurate claims back to the publishers repeating
    them, **drafts a personalized correction for each one, and tracks which ones actually updated**."
  - "Captures the AI search demand you cannot earn organically": finds high-volume prompts where the brand
    never shows up, writes **sponsored answer creative**, and stages the campaign for approval.
  - "Keeps the brand consistent everywhere it appears": scans owned surfaces for retired names/off-brand
    claims/stale creative, "then **rewrites and republishes** what it finds."
  - Product example: *"Find the pages we are losing in AI answers and rewrite them. Stage everything, do not
    publish."* → "Rewrote 9 pages… **All staged as drafts, nothing live.**"
  - Agents now run on schedules or triggers, show reasoning on every run, "keep you in control of what gets
    sent or published"; earlier node-based Agents renamed **Workflows**. Prior Agents shipped integrations that
    **read and write** to WordPress, Sanity, Contentful, Framer CMS, Google Suite, Slack, Gamma, Notion,
    Google Drive (Profound blog, Mar–Jun 2026).
  - Customer reviews page [T2]: "Opportunities to secure **earned media placements at highly cited sources**";
    agent templates for drafting/optimising content; a MongoDB-attributed example reducing content briefing
    from "6+ hours to under 60 seconds".
- **Scrunch / Sitecore** — `https://scrunch.com/` (retrieved 16 Oct 2026) and official product documentation
  `https://doc.sitecore.com/sai/en/users/sitecoreai/ai-discoverability-powered-by-scrunch/aeo-opportunities/aeo-opportunities.html`:
  - Scrunch analyses content and surfaces **AEO opportunities** with a **projected lift** ("estimated
    percentage-point improvement in citation rates") and a **recommendation** describing "the specific content
    change to make"; **Signals** (brand-level change vs competitors) vs **Channels** (all opportunities);
    **Page Builder** AEO optimisation where you "**apply or decline each recommended AEO optimization**" —
    i.e. execution inside the CMS with per-item approval.
  - Opportunity types are prescribed: **Content Enrichment** (add statistics/benchmarks/research findings,
    named experts, author credentials, attributed quotes, references to specific products/companies/people/
    dates/locations, links to authoritative sources) and **Content Transformation** (H2/H3 structure, numbered
    steps, comparison tables, FAQs, question-form headings).
  - **AXP (Agent Experience Platform)** serves AI-optimised content to agents at the edge/CDN "without
    disrupting the human experience"; product lines include Agent Pages, Agent Traffic, Site Optimization
    ("prioritized recommendations… turn pages into answers for the prompts you need to win"), Monitoring &
    Citations, Insights, Shopping, AI Search Trends; "Trusted by over 500 companies".
  - Scrunch's own enterprise buying guide enumerates the 14 capabilities it claims the category needs —
    including site auditing, content optimisation, **content generation** and **content delivery**
    (`https://scrunch.com/blog/best-answer-engine-optimization-aeo-generative-engine-optimization-geo-enterprise-platforms-2026`).

**Method lesson (the real failure):** v1 relied on T3 review content. Three independent reviews dated
**26 Aug – 26 Sep 2026** stated Peec has "No built-in content generations" and "does little to fix it" — and
were already wrong when published on **13 Oct 2026**. Category capability claims decay in weeks. Any
competitor statement we make must be sourced from vendor documentation dated within ~30 days, and re-checked
before it is used in a sales or investment document.

**Files affected:** `00-decision-memo.md` (rewritten), `01` §4, `02` (+§13), `04` P3, `06` A4/A5/C2,
`09` (rewritten), `10` (superseded by `12`).

---

## C-02 — Capacity model and COGS model used different hour definitions — **CORRECTED**

**Claim as written (v1, `10-tam-bottom-up.md` §2 vs §3):** the capacity model assumed **13 client-hours per
client per month** (10 clients per FTE), while the COGS model listed 13 delivery hours **plus** 8 third-party
corroboration hours **plus** support — 21+ hours. The two models could not both be true, so clients-per-FTE,
servable clients, gross margin, break-even and the 24-month scenarios were all internally inconsistent.

**Correction:** one hour definition now governs both models —
`H_tier` = **all** client-facing hours per client per month (collection/QA + analysis + proposal drafting +
third-party corroboration + reporting + calls + fact-verification + ticket handling). Tiers:
**A = 5 h** (monitor/report/backlog, client executes), **B = 12 h** (managed on-site optimisation),
**C = 21 h** (managed on-site + third-party corroboration). Effective delivery hours per FTE
`H_eff` = **90 / 110 / 130** (conservative/base/optimistic) out of ~160 gross, after sales, marketing,
internal tooling, learning, admin and leave. Clients per FTE = `H_eff / H_tier` →
**Tier A 18–26, Tier B 7.5–10.8, Tier C 4.3–6.2.** v1's "10 clients per FTE" was only true for Tier A; at the
managed scope we actually proposed it was **overstated by ~2×**.

**Files affected:** `10` superseded by **`12-economics-v2.md`** (all downstream numbers recomputed there).

---

## C-03 — COGS omitted the measurement tooling line — **CORRECTED**

**Claim as written (v1, `10` §3):** COGS = API + infra + labour, $159–$483/client/month, implicitly assuming we
build our own sampling and pay only inference.

**Correction:** if we do not build, we **license** measurement per client: Otterly $29–$489/mo (prompt-count
based, unlimited team members), Peec €70/€180/€360 per month billed annually with 1/2/5 projects
(approx. $82/$210/$420; extra engine €25/€55/€115), Profound agency self-serve $399/mo per client workspace.
Per-client tooling therefore runs **$30–$400/mo**. If we do build, we must amortise engineering time:
~40 h/month maintaining a sampling + extraction + reporting pipeline is **$160/client/mo at 10 clients**,
$80 at 20, $53 at 30, $40 at 40 — so **building is not cheaper than licensing until roughly 25–30 clients**,
and it is never cheaper during validation. v2 models both paths and recommends **buy for Stage 1–2, revisit
build only at scale**.

**Files affected:** `12-economics-v2.md` §2–§4, `08-validation-plan-v2.md` (tooling now a budget line).

---

## C-04 — Diagnostic cost understated ~3×; "cost falls to $15" was an assumption — **CORRECTED**

**Claim as written (v1, `08`, `10`):** $15–$31 per diagnostic initially, falling to $5–$15 once templated, based
on 90–120 minutes of labour for the first run and 25–40 minutes thereafter.

**Correction:** those labour figures covered data collection only. A complete diagnostic includes
client-specific research (product, ICP, competitors, category facts), prompt design, collection setup and
monitoring, extraction QA against a gold sample, reproducibility analysis with confidence intervals,
gateway identification and classification, report writing and QA, and a delivery call. Itemised:
**~9 h initially, ~5 h once templated** — so **$68/diagnostic at hired rates ($7/h) or $365 at founder
opportunity cost ($40/h)** initially, falling to **$40 / $205**. The "falls to $15" figure is withdrawn; the
templated-time claim is now an explicit **[HYPOTHESIS]** that Stage 1 must measure, not assume.

**Files affected:** `08-validation-plan-v2.md` §5, `12-economics-v2.md` §6.

---

## C-05 — 20 diagnostics = 7,500 observations did not fit a 14-day, one-person sprint — **CORRECTED**

**Claim as written (v1, `08`):** 20 diagnostics + 15 prospect calls + 5 agency interviews + 4 deliverables in
14 days, "no code".

**Correction:** the arithmetic does not close. 20 diagnostics × 25 prompts × 5 runs × 3 surfaces =
**7,500 observations** (v1 said 3,750 in one place and 20×25×5×3 elsewhere — both were wrong for the
20-diagnostic plan). Itemised hours: 20 × 5–9 h = **100–180 h** of delivery, + 15 calls × 1.5 h = 22 h,
+ 5 agency interviews × 1.5 h = 7.5 h, + sales/proposals 20 h, + protocol and deliverables 12 h
= **~160–240 founder-hours**, i.e. **12–17 h/day for 14 days**. Not feasible.

**Replaced by a staged plan** (`08-validation-plan-v2.md`): **Stage 1 = 14 days, 5 diagnostics
(1,875 observations), 5 buyer conversations, one written measurement protocol, hour-and-cost logging on every
unit, and at least one concrete paid-pilot proposal — total ~75–85 founder-hours (5.5–6 h/day), explicitly
requiring that this be the founder's only focus.** Stage 2 (20 diagnostics) is **gated** on Stage 1 evidence:
technical credibility (gold-set agreement, reproducibility bands), measured unit cost within tolerance, and
genuine commercial interest (≥1 signed or verbally committed paid pilot, or ≥3 "send a proposal" responses).
If Stage 1 shows costs above tolerance or no willingness to pay, Stage 2 does not run.

**Files affected:** `08` (rewritten as v2, old file removed), `00`, `01`, `06`.

---

## C-06 — Publishing plan would have overstated n in the headline — **CORRECTED**

**Claim as written (v1, `08` Day 12–14):** publish "We measured 40 India-origin B2B software brands" while the
plan scheduled 20 diagnostics, and the draft was to be written after the first 10.

**Correction:** the headline would have overstated the sample by 2–4×. New standing rules for any public
quantitative claim:

1. A headline may state **only** counts we actually measured; the title itself carries n, the number of
   prompts, the surfaces and the measurement window.
2. Every quantitative claim states n, surfaces, runs per prompt, geo, logged-in/out state, date range and the
   confidence band.
3. **No findings article before n ≥ 20 brands with two measurement windows.** At n = 5 we publish a
   **methodology** piece only ("how we measure, and why a single run is not evidence") — which is also the
   asset that best tests technical credibility.
4. No named-brand deficits published without written permission; otherwise aggregate and anonymise.
5. Pre-registration: prompts, run counts and thresholds are written down **before** collection and not edited
   afterwards; any deviation is logged in the article.

**Files affected:** `08-validation-plan-v2.md` §7, `13-measurement-reproducibility-protocol.md` §6.

---

## C-07 — A single consumer-interface rerun treated as ground truth — **CORRECTED**

**Claim as written (v1, `07` D1-Q23, `08` V4, `06` N-3):** ask the prospect to re-run one prompt in ChatGPT and
compare; if agreement < 60%, the measurement premise is dead and the company is killed.

**Correction:** a single rerun is **one sample from a distribution**, not ground truth. It varies with time of
day, region/exit node, logged-in state, memory/custom-instructions, plan tier, whether the surface actually
retrieved, and the model version. It also conflates two different questions: **extraction accuracy** (given a
stored response, did we label it correctly?) and **measurement reproducibility** (does the same prompt yield
the same observation over time and context?). v1 also wired an arbitrary threshold to an automatic
company-wide kill.

**Replaced by** `13-measurement-reproducibility-protocol.md`: separate gold-set validation for extraction
(≥200 double-labelled responses, per-label precision/recall, Cohen's κ ≥ 0.80 before use), a controlled
reproducibility design (surface, model id, geo, session state, retrieval evidence, time window, run index all
recorded; Wilson intervals; Fleiss' κ; Jaccard for citation sets; RBO for ordering; rule-of-three upper bound
for absence), and a **co-observation** protocol for prospects (exact prompt, surface, region, logged-out fresh
session, 3 runs inside a stated window; the test is whether their observations fall inside our predictive
interval, not whether they match a point estimate). Thresholds are now **decision bands** that trigger a
methodology review, never an automatic kill; the founder decides with the evidence in front of them and the
reasoning is recorded.

**Files affected:** `07` D1-Q23 and D3 scoring (to be updated), `06` N-3 (replaced), `08`, new `13`.

---

## C-08 — "Citation-gateway intelligence" presented as a moat — **DOWNGRADED TO HYPOTHESIS, then largely falsified**

**Claim as written (v1, `00` §E, `09` §3):** mapping the third-party pages that gate AI citations (Reddit,
YouTube, LinkedIn, G2, Wikipedia, listicles) is proprietary, compounds with each client, and is the main lever
because ~85% of discovery happens on third-party pages.

**Correction:** the **85% figure stands** (AirOps study, T2 — it is about where discovery happens, and it is a
reason the work exists, not a reason the work is defensible). The **moat claim does not**: Peec already
clusters owned vs earned actions, names the third-party channels worth working with, tracks YouTube/Reddit/
LinkedIn/TikTok performance and scores opportunities 1–3; Profound sells "opportunities to secure earned media
placements at highly cited sources" plus citation categories; Scrunch publishes prioritised recommendations
with projected citation lift; Ahrefs Brand Radar and Semrush's AI Visibility Toolkit report citation sources.
The dataset is **not** ours and cannot be. What is not automated anywhere we have verified is the **human
delivery** of that work: pitching editors, negotiating listicle inclusion, updating G2/Capterra/TrustRadius/
Gartner Peer Insights profiles, producing the YouTube/LinkedIn/comparison assets, and sustaining a monthly
cadence. Peec's own reviewers state it plainly: "It identifies the opportunity; your team still executes it."

**Status in v2:** managed delivery is a **service business**, not a moat. Cross-client intervention-effect data
is retained as **[HYPOTHESIS, low credibility]** — incumbents hold 2B+ prompts and 30M+ sources; we cannot
out-data them, and pooling client data raises consent and confidentiality issues we would have to solve first.
**No defensible moat was identified in Phase 1.** That is a finding, not a gap in the analysis.

**Files affected:** `09` (rewritten), `00`, `01`, `06` (H-list relabelled), `05` (robustness re-score).

---

## C-09 — Break-even stated without distinguishing cash from economic profit — **CORRECTED**

**Claim as written (v1, `10` §5):** "break-even at ~2 clients" on ₹600/month fixed costs.

**Correction:** that is **operating cash break-even with the founder paid nothing**. v2 states both, with
formulas:

- `N_cash = F_cash / (P − V_cash)` — covers third-party cash costs only.
- `N_econ = (F_cash + founder_market_comp) / (P − V_cash − H_founder × founder_market_rate)` — covers fixed
  cash costs **and** pays the founder a market salary.

At Tier C ($1,500/mo, V = $264, 6 founder hours/client/month): **N_cash = 0.49 → 1 client**,
**N_econ = 4.6 → 5 clients** (4.2 at a $25/h founder opportunity cost, 5.9 at $75/h).
At Tier A (₹40,000/mo, V = $147, 3 founder hours): **N_cash = 2.2 → 3 clients**, but
**N_econ = 23 → 94 clients** depending on the founder's opportunity cost (30 clients at $40/h). In other words, the ₹40,000
price point the brief told us not to assume is **cash-positive almost immediately and economically hopeless**:
it cannot pay a market-rate founder until ~29 clients, which needs ~6 delivery FTEs and ~₹11.6 L/month of
revenue. `12-economics-v2.md` §5 carries the full grid.

**Files affected:** `12-economics-v2.md` §5, `00`, `06`.

---

## C-10 — Labour rate assumption was not grounded — **CORRECTED**

**Claim as written (v1, `10` §3):** delivery labour at $8–$12/hour, asserted.

**Correction:** grounded in published Indian salary data [VERIFIED, T2 aggregator]: Indeed India reports an
average SEO specialist salary of **₹19,763/month** (145 salaries, updated 21 Aug 2026), junior **₹12,694**,
senior **₹38,666**; percentile tables put the median at ₹22,000–₹35,000 and the 75th at ₹45,000–₹85,000;
SaaS/product-company specialists run ₹70,000–₹2,00,000/month. Loaded (+25–30%) that is roughly
**$3–6/hour for a mid-level analyst and $6–12/hour for a senior specialist** at ₹95/$1. v2 uses a blended
**$7/hour [ESTIMATED]** with a $4–$12 sensitivity band, and a founder opportunity cost of **$40/hour**
(band $25–$75) — the rate that actually decides whether the business is worth doing.

**Files affected:** `12-economics-v2.md` §1, `02` (+§14).

---

## C-11 — v1 arithmetic errors found in self-check (fixed before this review, recorded for audit)

| Location | Error | Correction |
|---|---|---|
| `10` margin-by-price grid, ₹20,000 optimistic | −25% | **+24%** (V=$159, P=$211) |
| `10` margin-by-price grid, ₹75,000 conservative | formatting/rounding artefact | **+39%** (V=$483, P=$789) |
| `10` §5 break-even text | "≈8 clients" at the ₹40,000 monitoring tier | **1.8 → 2 clients** (2.9 at $980 fixed) — itself superseded by C-09 |
| `08`, `00` diagnostic totals | inconsistent totals | **$300–$620 (₹28,500–₹59,000)** initially; **$100–$300 (₹9,500–₹28,500)** templated — superseded by C-04 |
| `08` validation budget | stale total | **₹60,000–₹1,30,000 (~$630–$1,370)** |
| `08` observation count | 3,750 vs 7,500 for the same plan | **7,500** for 20 diagnostics; **1,875** for 5 |

All v2 arithmetic is recomputed and shown in `12-economics-v2.md`.

---

## C-12 — Evidence not separated from inference — **CORRECTED**

**Claim as written (v1):** findings, estimates and hypotheses were mixed in prose without labels.

**Correction:** v2 labels every material claim **[VERIFIED] / [ESTIMATED] / [HYPOTHESIS] / [NOT YET VERIFIED]**,
and `02-evidence-register.md` gains §13 (execution-layer capability, official sources) and §14 (Indian labour
rates). Vendor marketing is never treated as independent evidence: capability statements from Peec/Profound/
Scrunch documentation are marked **[VERIFIED as claimed by vendor]** — verified that the vendor documents the
capability, **not** verified that it works as described. Capability verification requires hands-on trials,
which is Stage 1 work.

---

## C-13 — The 1,500-observation design assumed both surfaces were cheap — **CORRECTED (16 Oct 2026, v2.1)**

**Claim as written (`validation/00-integrated-plan.md` v1.0 §1):** 15 prompts × 5 runs × 2 windows × **2
surfaces** = 300 observations per diagnostic, 1,500 total, fitted inside a 52-founder-hour budget.

**Correction:** the second surface was human capture on a consumer interface at 1.5–3 minutes per observation.
750 human captures = **19–38 hours**, i.e. more than the entire 20-hour scenario and 36–73% of the 52-hour
plan. The design was arithmetically infeasible in the same way v1's 20-diagnostic sprint was (C-05) — hours were
asserted rather than computed. Rebuilt as three explicitly separated layers in
`validation/03-operational-readiness-memo.md` §2.3: **L1** controlled API repetitions (1,500 observations,
agent-run, ≈$16), **L2** vendor daily monitoring (Peec free 7-day pitch projects, $0, one window only,
labelled `[VENDOR-REPORTED]`, internal cross-check only), **L3** manual consumer capture reduced to
**2 brands × 10 prompts × 3 runs = 60 observations** (1.5–3 h). Controlled total **1,560** plus the L2
cross-check. Repetition semantics (within-window runs vs daily vendor monitoring vs manual capture) are now
defined separately and may never be blended.

## C-14 — Positioning language still implied proprietary advantage — **CORRECTED (condition 7)**

**Claim as written:** "citation-gateway engine", "proprietary dataset", "first-to-market action engine",
"exclusive execution workflow" survived in `09` §5–§6 and `00` §E as *withdrawn but still referenced* language,
and the recommended positioning was phrased as a conclusion.

**Correction:** all such claims are removed. The positioning is now a single **[HYPOTHESIS]** sentence —
"Specialized, evidence-backed AI-search optimization delivered as a managed service for B2B companies that lack
sufficient execution capacity" — decomposed into five components, each with a named falsifier and a named test
(`09` §6.1). It carries the [HYPOTHESIS] label in every document until a buyer demonstrates willingness to pay.

## Repository note - loss of the v1 commit history (16 Oct 2026)

This workspace was re-cloned and its git history squashed on 16 October 2026. The commits that
carried Phase 1 v1 (c6cfc22), the v2 corrections (34d7e11) and the integrated plan (d0538a3) no
longer exist in the repository; all current content sits in a single commit (bae95ed).
**Consequence for auditability:** v1 text can no longer be diffed against v2 in git. The
mitigation is that this correction log quotes every v1 claim verbatim before correcting it, so
the audit trail survives in the documents rather than in the history. Claims of the form
"preserved in git history" elsewhere in the repo have been reworded. **Standing rule going
forward:** superseded content is archived as an explicitly labelled file rather than left to
git history.

## What survives v1 unchanged

- The **demand-side** evidence (Pew, G2 Answer Economy, Seer, Ahrefs, Conductor, GSC generative-AI report,
  employer-published GEO/AEO job postings) and the measurement-volatility evidence (AirOps, Otterly, Keygrip,
  EWR Digital, arXiv 2604.07585, GTECH). These were T1 and are unaffected by C-01.
- The **beachhead construction** (≈480 accounts: ≈350 India-origin global SaaS + ≈130 cybersecurity vendors) —
  a bottom-up count from Tracxn/Nasscom/DSCI, still [ESTIMATED] and still unvalidated by conversation.
- The **ICP ranking arithmetic** (S1 3.94 > S4 3.76 > S2 3.70 > S5 3.46 …) — unchanged, with a new
  post-correction robustness check in `05` §6.
- The conclusion **"do not build a monitoring SaaS"** — strengthened, not weakened, by C-01/C-08: the category
  is more crowded and more capable than v1 believed.

## What changed in the recommendation

v1 recommended a services-first wedge differentiated by a proprietary citation-gateway engine.
v2 recommends a **staged test of a niche managed-delivery service that licenses best-of-breed measurement**,
with the moat question left honestly open, and with an explicit experiment designed to answer the most
dangerous question first: **would the buyer rather pay Peec $245/month and do it themselves than pay us
$1,500/month to do it for them?**
