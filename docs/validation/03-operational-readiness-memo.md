# Operational readiness memo — Stage 1 + Stage 2

**To:** founder · **Date:** 16 October 2026 · **Version:** 1.0
**Issued under:** CONDITIONAL APPROVAL of 16 Oct 2026 (conditions 1–9).
**Status: NO-GO on all external activity today. GO on internal desk research (already authorised and continuing).**

Labels: **[VERIFIED]** official source retrieved today · **[PARTIALLY VERIFIED]** credible secondary or incomplete
official · **[ESTIMATED]** · **[HYPOTHESIS]** · **[NOT YET VERIFIED]** · **[NOT FOUND]** · **[UNKNOWN]**.
FX ₹95 = $1 (RBI reference rate, 14 Oct 2026) [VERIFIED].

---

> **PARTLY SUPERSEDED (16 Oct 2026).** The founder selected the **30-hour scenario as a provisional planning
> baseline — not a confirmation of availability** — and required the measurement design to be reduced further and
> shown to fit. The authoritative version is **`05-stage1-30-hour-plan.md`**: 3 diagnostics (floor 2), 12 prompts,
> **36 manual captures (1.2 h) instead of 60**, a 25-response adjudication set, and the vendor-trial layer (L2)
> **excluded** while the NO-GO on trial registrations stands. §1 below remains the reference for the 20 h / 40 h /
> 52 h alternatives.

## 1. Three founder-time scenarios (condition 2)

**Protected in every scenario** (your instruction): all five buyer conversations, basic measurement integrity
(two windows, per-surface separation, raw evidence + metadata, intervals on every rate), and real commercial
testing (three-option card, price ladder, ≥1 priced pilot proposal).

| | **20 h** | **30 h** | **40 h** | **52 h (planned)** |
|---|---|---|---|---|
| Protocol + candidate approval | 2.0 | 2.0 | 2.0 | 3.5 |
| 5 diagnostics — fact-verify, QA, deliver | 5 × **1.5** = 7.5 | 5 × 2.0 = 10.0 | 5 × 2.5 = 12.5 | 5 × 3.0 = 15.0 |
| Adjudication set (extraction accuracy) | **25 responses ≈ 1.2** | **50 responses ≈ 2.5** | 75 ≈ 3.8 | 100 ≈ 5.0 |
| 5 buyer conversations (75 min + notes) | 7.5 | 7.5 | 7.5 | 7.5 |
| Outreach approval + sends | — (agent-drafted, batch-approved 0.5) | 1.5 | 1.5 | 3.0 |
| Agency interviews (H4 / O2 channel) | **postponed** | 2 × 1.0 = 2.0 | 2.0 | 2.0 |
| Paid-pilot proposal | 2.0 | 2.0 | 2.5 | 2.5 |
| Stage 2 review (matrix, differentiation) | **postponed to agent + async note** | 2.0 | 3.0 | 8.0 |
| Co-observation cards | — | — | 1.5 | 1.5 |
| Hour/cost log + reconciliation | 0.8 | 1.0 | 1.2 | 2.0 |
| Contingency | — | 0.5 | 2.0 | 2.0 |
| **Total** | **≈21** | **≈30.5** | **≈39.5** | **52** |

### What each scenario costs us in evidence

| Scenario | Delegated to agent | Postponed | Reduced | Claims that become **unsupported** |
|---|---|---|---|---|
| **20 h** | Collection, extraction, statistics, all drafting, outreach copy, longlist, matrix | Agency channel (H4/O2); Stage 2 founder review; co-observation cards | Adjudication to 25 responses; diagnostic QA to 1.5 h | **Inter-annotator κ (needs a second human).** Extraction precision/recall is founder-referenced only → automated extraction **may not** be used for paid client reporting (A3 consistent). No agency-channel evidence at all |
| **30 h** | as above | Co-observation cards optional | Adjudication at 50 | κ still NOT MEASURED unless S3 is approved. Otherwise Stage 1 is complete as designed |
| **40 h** | as above | — | — | Same as 30 h, plus prospect co-observation evidence |
| **52 h** | as above | — | — | None; full plan including deeper Stage 2 review |

**Recommendation: 30 h is the defensible floor.** At 20 h we still get a real commercial answer (five
conversations, three-option card, price ladder, one proposal) but we cannot validate extraction, and we learn
nothing about the agency channel — which is the fallback if the direct service fails. At 20 h the honest
position is "commercial signal only, measurement unvalidated." **Do not choose 20 h and then describe the
output as a validated diagnostic.**

Delegation principle applied throughout: the agent drafts, collects, computes and logs; **the founder verifies
business facts, talks to buyers, and decides.** Fact verification and approval decisions are irreducibly human
(integrity rules 9, 15, 16), so they are never delegated in any scenario.

---

## 2. Corrected measurement arithmetic (condition 5)

### 2.1 The 1,500-observation calculation, shown in full

```
1,500 observations = 5 brands × 15 prompts × 5 repetitions × 2 time windows × 2 surfaces
                     5 × 15 = 75 prompt-cases
                     75 × 5 = 375 observations per window per surface
                     375 × 2 windows = 750 per surface
                     750 × 2 surfaces = 1,500
```

- **Brands (5):** 3 × S1 India-origin global B2B SaaS, 1 × S2 cybersecurity product vendor, 1 × S4 US/EU
  mid-market SaaS.
- **Prompts (15 per brand):** pre-registered, SHA-256 hashed, frozen before the first run — category
  commercial-intent queries, competitor-comparison queries, and problem-statement queries. Reduced from 25 to
  fit the hour budget; **repetitions per prompt were not reduced**, so per-prompt interval width is unchanged.
- **Repetitions (5 per prompt per window):** identical prompt, fresh stateless call, no conversation context.
- **Windows (2, ≥7 days apart):** required for any stability claim.
- **Surfaces (2):** never blended.

Statistical consequence [ESTIMATED]: 5 repetitions give a Wilson 95% half-width of **±0.29 to ±0.33**; 15
prompts × 5 runs = 75 observations per brand-window give a brand-level rate half-width of about **±0.11** if
prompts are treated as independent — which they are **not** (prompts within a brand are correlated), so the
brand-level figure must be reported with an effective-sample-size adjustment, not as 75 independent draws.
Detecting a 0.30 → 0.60 lift still needs **≈42 runs per arm** — unchanged, and still out of reach in Stage 1.

### 2.2 Feasibility correction — the original two-surface design was not affordable in hours

The v1.0 plan assumed both surfaces were cheap. They are not:

| Surface | How observations are obtained | Cash | **Hours** |
|---|---|---|---|
| Official search-enabled API | Stateless repeated calls, same prompt hash, model id + timestamp + region + retrieval evidence logged per call | ~$0.012–0.02 each | **≈0 (agent-run)** |
| Vendor platform (Peec / Profound / Scrunch / Otterly) | Vendor's own collection on its tracking schedule (**daily** for Peec); we read exports/dashboards | $0 during trial | ≈0.5 h per brand to export and record |
| **Human-captured consumer interface** | A person opens the consumer product, logged out, fresh session, types the prompt, screenshots + transcribes | $0 | **1.5–3 min each** |

750 human captures × 1.5–3 min = **19–38 hours** — more than the entire 20 h scenario, and 36–73% of the 52 h
plan. **Logged as correction C-13.** The design is therefore rebuilt as three separated layers:

### 2.3 The three-layer measurement design (Stage 1)

| Layer | What it is | Volume | Cash | Hours | Role |
|---|---|---|---|---|---|
| **L1 — Controlled repetitions (API)** | Perplexity **Sonar** via the Agent API, and **Gemini 3 Flash with Grounding with Google Search** | 5 × 15 × 5 × 2 = **750 per provider**, 1,500 total across two providers | **$13–20** (§3) | agent | The quantitative backbone: intervals, κ across runs, window-to-window stability |
| **L2 — Vendor daily monitoring** | Peec **free 7-day pitch projects** (one per candidate brand), plus one other vendor trial as cross-check | vendor-controlled, daily, window 1 only | **$0** during trial | 2.5 h total | **Cross-check and capability verification (B1/CG-6)** — labelled `[VENDOR-REPORTED]`, method not fully disclosed, never blended with L1 |
| **L3 — Manual consumer-interface capture** | Human, logged out, fresh session, desktop, named 6-hour window | **2 brands × 10 prompts × 3 runs × 1 window = 60** | $0 | **1.5–3 h** | Anchors L1 to the consumer experience and supports prospect co-observation |

**Total controlled observations: 1,500 (L1) + 60 (L3) = 1,560**, plus L2 vendor data as a labelled cross-check.
L2 has **one window only** → no vendor trend claim is possible, and we will not make one.

### 2.4 Repetition semantics, kept separate (condition 5)

- **Controlled repetitions (L1):** *n* identical stateless calls inside one window. Measures within-window
  stochasticity. We control timing, region, session state and prompt text.
- **Daily monitoring (L2):** one observation per prompt per day, vendor-run. Measures day-to-day drift on the
  vendor's schedule and method. We control neither. Comparable to our **window-to-window** statistics, **not**
  to our within-window run statistics.
- **Manual consumer captures (L3):** few, expensive, highest ecological validity. Used to bound the difference
  between API and consumer surfaces (hypothesis H11), never as a sample large enough for rates.

Mixing these three into one number is the specific error this section exists to prevent.

### 2.5 Permissions, raw-data access, export rights, provider limitations (condition 5)

| Provider | Access / export | Permissions & limitations | Status |
|---|---|---|---|
| **Peec (agency pitch projects)** | Custom **CSV export** listed on agency plans; **MCP included free on every paid plan** (connects to Claude, Cursor, n8n, Make); API listed under Data access | Pitch projects are **free, 7 days, outside the client quota**, "data instantly available", convertible to a paid project in three clicks with 7 days of history kept as baseline. Prompt allowance per pitch project is plan-dependent | **[VERIFIED]** for existence and pricing page contents; **prompt limit per pitch project [NOT FOUND]** in the retrieved chunk; **trial ToS, export rights during trial, and whether API is included below Enterprise [NOT YET VERIFIED]** |
| **Perplexity (Sonar via Agent API)** | Raw JSON responses with citations; we store bodies ourselves | **Sonar Chat Completions support ended 27 Sep 2026**; Sonar now runs as presets of the Agent API. Search API returns raw results with no answer. Rate limits per plan | **[PARTIALLY VERIFIED]** — three consistent Oct-2026 secondary sources; official rate card not retrieved today |
| **Google Gemini (Grounding with Google Search)** | Response text + inline citation annotations + `google_search_call` / `google_search_result` steps with the queries executed | **Billed per query the model executes**, not per prompt — one prompt can trigger several billable queries. 5,000 free search requests/month shared across Gemini 3+ models, then $14/1,000. Grounding returns an AI answer, **not** a SERP — no ranking positions or ordered result URLs | **[VERIFIED]** — official docs at ai.google.dev, retrieved today |
| Consumer interfaces (ChatGPT/Gemini/Perplexity web) | Screenshot + transcript, stored by us | **No programmatic extraction** — OpenAI's terms prohibit extraction outside the API; we use human capture only | **[VERIFIED]** position, unchanged |
| Free API tiers generally | — | Free tiers may permit the provider to use inputs/outputs to improve their products. Our prompts contain candidate brand and competitor names | **[NOT YET VERIFIED]** — must be checked before any client-identifying prompt is sent on a free tier. Mitigation: prompts are public-intent queries, not confidential client data; disclose to candidates |

**Rule adopted:** vendor-trial data (L2) is used for **internal cross-check and capability verification only**
and is **not** placed in any candidate-facing deliverable until export and usage rights are verified in the
vendor's terms. This keeps us compliant and still delivers the B1/CG-6 value.

---

## 3. Lowest-cost compliant tool comparison (conditions 1 and 4)

All prices retrieved **16 October 2026**. Vendor-claimed capabilities are marked; undocumented items are
**NOT FOUND**, never "absent".

### 3.1 Free and trial routes that can cover five candidates

| Vendor | Free route | What you get free | Cost if continued | Evidence |
|---|---|---|---|---|
| **Peec — agency plans** | **Free 7-day pitch projects on every agency plan, outside the client quota** + 7-day trials of Essential/Growth/Scale | Per pitch project: prospect AI visibility profile, competitor benchmarking, the prompts where they are invisible, across **six channels**; instant data; convert to paid in 3 clicks keeping 7 days of history; **MCP free on every paid plan** | Essential **€205/mo (10,000 credits, ~111 prompts daily)** · Growth **€425/mo (25,000 credits, ~277 prompts)** · Scale **€675/mo (65,000 credits, ~722 prompts)** · Comprehensive custom/unlimited/annual | **[VERIFIED]** peec.ai/pricing-agencies and peec.ai/for-agencies retrieved today; trial availability **[PARTIALLY VERIFIED]** via Semrush's agency-tools roundup (31 Jul 2026) |
| **Profound — Agency Growth** | Free 7-day brand trial; **$99/mo Agency Growth includes 10 pitch workspaces/month** | Each pitch workspace: **25 prompts × 3 engines (ChatGPT, Perplexity, Google AI Overviews) × 7 days**, extendable | $99 base + **$399 per full client workspace** ($498 for one real client; 10 clients ≈ $4,089/mo); extra trial workspaces $199/mo per 5 | **[PARTIALLY VERIFIED]** — three consistent secondary sources (26 Aug, 30 Jul, 14 Oct 2026); official agency page not retrieved |
| **Scrunch** | **7-day free trial on Starter, no credit card**; free "AI visibility audit — results in 30 seconds, no credit card required" | Audit + trial tracking | Starter **$250/mo annual or $300 monthly**; Growth $417/$500; Enterprise custom; extra seats $25/mo | **[PARTIALLY VERIFIED]** — free audit and trial signup verified on scrunch.com today; prices via a secondary comparison citing scrunch.com/pricing on 15 Sep 2026 |
| **Otterly.AI** | Free trial, **no credit card** — **7 days with 50 prompts, 100 GEO audit URLs, 1,000 API calls, unlimited team members** (one source) or **14 days** (another) | Trial tracking + audits; white-label Looker Studio reports for agency partners | Lite **$29** (15 prompts, 4 engines, 1,000 URL audits/mo, 1 workspace, unlimited team members, 3 weekly recommendations) · Standard **$189** (100 prompts, 5,000 audits, unlimited workspaces, **API 2,000 req/mo, MCP, Agent Analytics**) · Premium **$489** (400 prompts, 10,000 audits, 5,000 API + 5,000 MCP) · Enterprise from $1,000; 15% annual discount; **Claude ($29–$439) and Gemini/Google AI Mode ($9–$149) are paid add-ons by tier** | **[PARTIALLY VERIFIED]** — two secondary sources citing otterly.ai/pricing (15 Sep, 2 Oct, 24 Jul 2026); **trial length conflict recorded (7 vs 14 days)** |
| Semrush / Ahrefs *(lighter pass)* | Semrush 7-day free trial | Semrush AI Visibility Toolkit **$99/domain** (bundled in Semrush One $199); Ahrefs Brand Radar **$398 vs $199 add-on — unresolved conflict**; Ahrefs free AI-crawler tier and free checker | — | **[PARTIALLY VERIFIED]** from register; conflict unresolved (gap CG-1) |

### 3.2 Recommended Stage 1 stack — **$0 tooling**

1. **Peec agency 7-day trial → five free pitch projects** (one per candidate). Covers L2 for all five brands at
   zero cash, and simultaneously performs the hands-on capability verification B1/CG-6 requires (do Actions
   name real, actionable earned-media targets? is gap analysis usable? what does the CSV export contain?).
2. **Perplexity Sonar (Agent API) + Gemini 3 Flash with Google Search grounding** for L1 controlled
   repetitions — 1,500 observations for **$13–20**.
3. **One secondary vendor trial (Otterly or Scrunch) as an independent cross-check** on 1–2 brands only, to test
   whether vendor numbers agree with ours (a live demonstration of the vendor-vs-protocol difference we sell).
4. **Human capture (L3)** for 60 observations on 2 brands.

**Why not Peec Starter at $95:** it includes **one project**, so it cannot cover five candidates; the agency
route covers all five **free**. S1 is therefore **withdrawn**, not merely deferred. If the trial requires a card
or the pitch-project prompt allowance proves too small, the fallback is **Otterly's free trial (50 prompts)**
plus APIs — still $0.

### 3.3 API rate card for the S2 cap (condition 4: providers, models, rates, observation counts)

| Provider / model | Rate | Stage 1 usage | Cost |
|---|---|---|---|
| **Perplexity Sonar** (Agent API preset) | $1/M input + $1/M output tokens **+ request fee $5 / $8 / $12 per 1,000** (low/medium/high context); a plain Sonar answer ≈ **$0.007** | 750 observations (5 × 15 × 5 × 2), low context | tokens ≈ $5.25 + fee ≈ $3.75 = **$9.00** |
| Perplexity Search API | flat **$5 per 1,000 requests**, up to 5 queries per request, no token charges, raw results **no answer** | Not used for answers; optional 100 calls for gateway URL discovery | **$0.50** |
| **Google Gemini 3 Flash + Grounding with Google Search** | **5,000 free search requests/month** shared, then **$14 per 1,000**, billed **per query executed** (one prompt may trigger several); tokens $0.75/M in, $3.75/M out until 31 Dec 2026 (doubling 1 Jan 2027) | 750 observations ≈ 1,125 billable queries (1.5 avg) → **inside the free allowance**; tokens ≈ $2.53 | **$2.53** |
| Development, retries, failed calls (~25%) | — | ~380 extra calls | **≈$4** |
| **Total proposed** | | **1,500 L1 observations** | **≈$16, cap $40** |

**Revised S2 request: cap $40 (₹3,800), not $110.** The earlier $110 assumed three surfaces and higher per-call
costs; the corrected design is cheaper and better documented. If Gemini's free allowance is exhausted by other
work in the same month, the worst case is 1,125 queries × $14/1,000 = $15.75 extra → still inside a $60 cap.

### 3.4 Agency and white-label comparators (full-depth targets 7–9)

| Target | Published offer | Evidence |
|---|---|---|
| **SourceRank AI** (Aarhus) | **$497 one-time AI Visibility Audit; ongoing from $997/mo (Foundation tier)** | **[PARTIALLY VERIFIED]** — stated on their own blog (12 Oct 2026); own pricing page not yet retrieved |
| **MADX Digital** | $2,500/mo per pillar; **$5,500/mo fully managed** (6-month term then monthly) | **[PARTIALLY VERIFIED]** — third-party roundup (30 Sep 2026) |
| **DemandLocal** (white-label digital PR for GEO) | $3,000–$10,000/mo mid-market; $25,000–$30,000+/mo enterprise; explicit **white-label** programme so agencies deliver under their own brand | **[PARTIALLY VERIFIED]** — their own playbook; rate card not retrieved |
| Category bands | Self-serve tools **$29–$489/mo**; mid-market agency **$2,000–$10,000/mo**; entry programmes $1,000–$2,500; enterprise $10,000–$25,000+; standalone GEO audit quoted from $497 to $8,000–$25,000 (**wide spread — both recorded**) | T3, multiple consistent sources Jun–Oct 2026 |

**The most dangerous published sentence found today** (a competitor's own content, Jun 2026): *"Most teams under
$3,000/month do better with one tool plus in-house fixes than with a thin retainer."* That is a direct, public
argument against Option C at $1,500/month. It is recorded in the evidence register and **built into the buyer
conversation as the objection we expect** — which is exactly what condition 6 asks us to test rather than assume.

---

## 4. Updated purchase approvals needed (condition 4)

| # | Item | v1.0 request | **Revised** | Why |
|---|---|---|---|---|
| **S1** | Peec Starter $95 | Approve | **WITHDRAWN → replace with S1a: approval to create free trial accounts** | Starter covers 1 project; five candidates need the agency route, which is **free** for 7 days. No purchase required |
| **S1a** *(new)* | Create free-trial accounts: Peec agency (5 pitch projects), plus one of Otterly / Scrunch as cross-check | — | **Approve account creation** | Zero cash, but it is an external commitment: it creates an account in your name, may require an email address and possibly a card, and is governed by trial terms we have **not yet read**. **I will read and summarise the trial ToS and data-export terms before any account is created, and will stop if a card is mandatory or if terms restrict our use** |
| **S2** | API credits | $110 cap | **$40 cap (₹3,800)** | Rate card in §3.3; expected spend ≈$16 |
| **S3** | Second annotator $56 | Approve later | **DEFER — κ reported as NOT MEASURED** | Your condition. Consequence stated plainly: without a second human annotator there is **no inter-annotator agreement figure at all**, and extraction precision/recall is founder-referenced only. Automated extraction therefore **cannot** be used for paid client-facing reporting in Stage 1 (A3-consistent) |
| **S4** | Domain/email/contract $60 | Approve | **DEFER — not essential** | Deliverable would have been a one-page site + contract template. **Not needed for any approved interaction**: diagnostics can be delivered as PDF from an existing address, and the pilot proposal can use a plain document with the clauses we draft. Revisit only if a prospect asks for a website or a countersigned contract — at which point it becomes essential and I will re-request it |
| **S5** | Peec Advanced $495 | Not recommended | **WITHDRAWN** | Free pitch projects remove the need |
| **Total proposed cash** | | $265 | **$40 (₹3,800)**, ceiling unchanged at ₹38,760 | 90% below the cap; no automatic expenditure |

---

## 5. Final prospect selection criteria (condition 3)

Full criteria, scoring sheet and cold-outreach fallback in **`04-prospect-selection-criteria.md`**. Summary:

**Hard requirements (all must hold, each checkable from public sources):**
1. India-headquartered (S1/S2) or US/EU mid-market (S4), B2B software product company.
2. Sells to US/UK/EU buyers — English site, USD or multi-currency pricing, named Western customers or case
   studies.
3. Research-led category where buyers compare options: dev tools, data/AI infrastructure, martech, sales tech,
   HR tech, fintech infrastructure, cybersecurity products.
4. Visible marketing function: ≥1 person with a marketing remit, and a blog/changelog updated within 90 days.
5. A **named, reachable decision-maker** (founder, CMO, Head of Growth/Marketing/Demand Gen) findable without
   purchasing contact data.
6. We can produce **one true, checkable AI-visibility finding** about them before contact (this is the outreach
   hook and the diagnostic's entry point).
7. Not an AI-search/GEO vendor itself; not a direct competitor of another candidate in the same cohort.

**Scoring:** 8 criteria × 1–5 (fit, reachability, severity signal, budget evidence, content base, category
competitiveness, confidentiality risk, finding strength); **threshold ≥28/40**; rank and take the top 20, then
select 5 with the segment mix 3 × S1, 1 × S2, 1 × S4.

**Cold-outreach fallback (no warm introductions required):** channel order — (1) LinkedIn direct to the named
buyer with one finding; (2) email from the company's own published address or team page; (3) public community
engagement (SaaSBoomi directory, DSCI/Nasscom events, Product Hunt, relevant subreddits) followed by a direct
message; (4) a specific, useful reply to their own public content. Message rules: one true finding, no price in
message one, no unsourced claim, no competitor disparagement, honour opt-out immediately, maximum two
follow-ups, every send logged. Expected conversion **[HYPOTHESIS — no data]:** 20 sends → 5–8 replies → 3–5
conversations.

**Confidentiality:** no candidate's data reused for another candidate; no brand named in any output without
written permission; candidate list and messages approved by you before anything is sent (gates O1/O2).

---

## 6. Final 14-day execution schedule

> Superseded by `05-stage1-30-hour-plan.md` §5, which re-sequences the same 14 days around 3 diagnostics,
> excludes the vendor-trial layer, and lists blocking dependencies per approval.

Assumes the **30 h scenario**; swap the diagnostic/QA hours per §1 for 20 h or 40/52 h. **Day numbers shift if
you choose a 21-day spread.**

| Days | Block | Founder | Agent | Gate needed |
|---|---|---|---|---|
| **1** | Approve protocol v1.1 (three-layer design, §2.3) and prompt registry; approve selection criteria | 1.0 | 4 | G-Plan |
| **1–2** | Build 20-account longlist with scored fit evidence; read + summarise Peec/Otterly/Scrunch **trial terms, data-export and usage rights** | 1.0 | 6 | — |
| **2** | You select 5 candidates + approve outreach list and message text | 1.0 | 2 | **O1, O2, S1a** |
| **3** | Create trial accounts; open 5 Peec pitch projects; start L1 collection window 1; send outreach batch 1 (10) | 0.5 | 6 | S1a, O2, S2 |
| **3–5** | Adjudication set (50 responses); extractor precision/recall; diagnostics #1–#2 drafted | 4.5 | 12 | G-Deliver |
| **5–6** | Verify facts, QA and deliver diagnostics #1–#2; buyer conversations #1–#2 | 5.5 | 3 | G-Deliver, O5 |
| **7** | **Checkpoint:** replies, collection health, extraction quality, hours vs plan | 1.0 | 3 | — |
| **8** | Outreach batch 2 (10); L1 window 2 begins (≥7 days after window 1) | 0.5 | 3 | O3 |
| **8–10** | Diagnostics #3–#4 drafted; agency interview #1; Stage 2 matrix tranche 2 | 4.0 | 14 | — |
| **10–11** | Deliver #3–#4; buyer conversations #3–#4; co-observation cards if hours allow | 5.5 | 3 | O6 |
| **11–12** | Diagnostic #5; agency interview #2; update economics with **actual** logged cost | 4.0 | 8 | — |
| **12–13** | Deliver #5; buyer conversation #5; three-option and price-ladder results consolidated | 3.5 | 4 | — |
| **13** | Paid-pilot proposal written, priced, clause-complete | 2.0 | 4 | **G-Proposal (D5)** |
| **14** | Integrated decision pack; GO / MODIFY / STOP; hours and cost reconciled | 2.5 | 6 | — |
| | **Founder total** | **30.5** | **≈92** | |

**Hard sequencing constraints:** window 2 must start ≥7 days after window 1 (so window 1 starts by day 3);
the 7-day vendor trial must open on day 3 to cover window 1; the proposal cannot be sent before D5 approval.

---

## 7. Positioning update (condition 7)

**Removed from all documents, effective now:** every claim of a unique citation dataset, a first-to-market
action engine, or an exclusive execution workflow. Verified reason: Peec ships source analytics with source
classification, gap analysis by domain/subdomain/URL/host, and recommended actions grouped **earned vs owned**,
with CSV/MCP/API export at $95–$495/month (agency from €205); Profound sells earned-media opportunities and
publisher-correction drafting; Scrunch/Sitecore publishes projected citation lift with in-CMS apply/decline
[VERIFIED today].

**Proposition now under test — a hypothesis, not a claim:**

> **"Specialized, evidence-backed AI-search optimization delivered as a managed service for B2B companies that
> lack sufficient execution capacity."**

Each word is a testable component, and each has a named falsifier:

| Component | What must be true | Falsifier | Evidence status |
|---|---|---|---|
| **lack sufficient execution capacity** | Buyers have identified work they cannot staff | ≥3 of 5 name no unfinished work, or have spare internal hours | [HYPOTHESIS] — Q5 of the buyer set measures it directly |
| **managed service** | They will pay someone else to do it rather than license a tool | ≥3 of 5 choose Option A or B | [HYPOTHESIS] — three-option card |
| **evidence-backed** | Disclosed intervals and error rates help rather than hurt the sale | Buyers treat uncertainty as incompetence | [HYPOTHESIS] — Q13 co-observation reaction |
| **specialized** | Segment or vertical focus is worth paying for versus a generalist | Buyers see no difference versus a $997/mo generalist | [HYPOTHESIS] — compare S1/S2/S4 responses |
| **B2B / price** | $1,000–$1,500/mo is inside an approvable budget line | First "no" at or below ₹40,000 for ≥3 of 5 | [HYPOTHESIS] — price ladder |

Until a buyer demonstrates willingness to pay, the proposition carries **[HYPOTHESIS]** in every document.

---

## 8. Downgrade-adjusted base case (condition 8)

**Now the planning base, not a downside:** Tier C clients step down after month 6 to a maintenance tier.

| Package | Price | Hours/client/mo | Contribution | Role |
|---|---|---|---|---|
| **Project-only** (one-time diagnostic/implementation) | $497 – ₹75,000 | 6–9 h once | $409–$722 | Entry wedge; **zero recurrence** — CAC never amortised |
| **Managed sprint** (90 days, Tier B/C) | ₹75,000 / $1,500 | 12–21 | $591 / $1,236 | Where the value is proved |
| **Ongoing managed** (Tier C, no step-down) | $1,500 | 21 | $1,236 | Upper bound only — **not the base case** |
| **Quarterly monitoring** (step-down) | $400–$500 | 2–3 | ≈$350 | Honest landing spot after optimisation |

LTV with step-down at month 6 [ESTIMATED]: **−36% at a 12-month life, −54% at 24 months, −60% at 36 months**
(24-month LTV $29,656 → **$13,719**). LTV:CAC on economic CAC ($4,328) = **2.2× at 12 months, 3.2× at 24**.
Founder-compensated break-even is **unchanged at 5 clients** for the sprint phase, but a book composed of
stepped-down clients needs roughly **13 clients at $400** to cover the same $4,600/month — which is a
capacity argument for keeping the pipeline full, not for resisting step-downs. `12-economics-v2.md` §7.2 is
patched to make this the base case.

---

## 9. Go / no-go for beginning external activity

| Activity | Decision | Condition |
|---|---|---|
| Stage 2 desk research (B1–B6, retrieval queue, matrix, differentiation analysis) | **GO** | Already authorised; continuing now |
| Revising existing Phase 1 documents | **GO** | Already authorised |
| Creating free-trial vendor accounts (S1a) | **NO-GO today** | Requires: (i) your approval, (ii) my written summary of each trial's terms, data-export and usage rights, (iii) confirmation that no card is mandatory. If a card is required → back to you |
| Provider API spend (S2, $40 cap) | **NO-GO today** | Requires your approval of the revised cap and the rate card in §3.3 |
| Building the prospect longlist | **GO** (internal, no contact) | Uses only public sources; nothing sent |
| Sending any outreach (O2/O3) | **NO-GO** | Requires O1 (list) + O2 (message text) approval |
| Booking or holding any buyer conversation (O5) | **NO-GO** | Requires O1/O2 first |
| Delivering any diagnostic to a candidate (D2) | **NO-GO** | Requires G-Deliver: template + disclosure language approved |
| Sending any pilot proposal or accepting any deposit (D5/D6) | **NO-GO** | Requires your approval of price, scope, term, liability, exit clauses |
| Publishing anything (G-Publish) | **NO-GO** | Not requested in Stage 1; blocked by the n ≥ 20 / two-window rule regardless |
| Any client-site change, any code, any platform build | **NO-GO** | Not authorised in Stage 1 |

### What I need from you to move from NO-GO to GO

1. **Q1 — your real founder hours** (20 / 30 / 40 / 52). Until this is answered the schedule is provisional.
2. **S1a** — approval in principle to create free trial accounts, subject to my ToS summary first.
3. **S2** — approval of the **revised $40 cap** (down from $110).
4. **O1/O2** — approval of the longlist and message text, when produced.
5. **Confirmation** that S3 and S4 stay deferred (κ NOT MEASURED; no website or contract spend).

**I am continuing Stage 2 desk research now and stopping before every item marked NO-GO.**
