# S2 — Provider specification and cost sheet for 720 API observations

**Prepared for final sign-off, 16 October 2026.** Companion to `05-stage1-30-hour-plan.md` §3 (L1).
**Status: NO-GO. No API calls have been made. No account exists. No money has been spent.**
**Requested authorisation: S2, maximum $40 total, expected ≈$5.61, conservative worst case $21.28.**

Every figure below is labelled. Where sources conflict, **both** figures are shown and the cost model uses the
higher one — we would rather over-budget than silently overspend.

---

## 1. Correction applied: Perplexity adapter targets the Agent API, not the legacy Sonar interface

Your instruction was correct and it matters. **Sonar Chat Completions support ended 27 September 2026**; Sonar
now runs as **presets of the Agent API** [PARTIALLY VERIFIED — three consistent Oct-2026 secondary sources; the
official deprecation notice has not been retrieved]. An adapter written against `POST /v1/chat/completions` with
`model: "sonar"` may still respond today, but it is the deprecated path, its request-fee semantics are unclear
post-migration, and it could stop without notice mid-window — which would corrupt a measurement series.

### 1.1 Adapter specification (Perplexity — Surface A1)

| Field | Value | Source / status |
|---|---|---|
| Endpoint | **`POST https://api.perplexity.ai/v1/agent`** (canonical). `/v1/responses` is documented as an OpenAI-compatible alias | [PARTIALLY VERIFIED — official tools doc retrieved today + two secondary sources] |
| Auth | `Authorization: Bearer $PERPLEXITY_API_KEY` | [VERIFIED pattern in official doc example] |
| Model | **Sonar preset** — the exact preset identifier must be read from the console at setup and **pinned in config**; it is recorded per observation from the response, never assumed | Preset identifier **[NOT YET VERIFIED]** — do not hard-code from a secondary source |
| Request body | `model`, `input` (the prompt, verbatim from the frozen registry), `instructions` (fixed collection instruction, identical for every observation), `tools` | [VERIFIED shape in official tools doc example] |
| Tools | **`web_search` only.** `fetch_url`, `people_search`, `finance_search` and custom functions are **disabled** — they add cost and change what is being measured | [VERIFIED: tools exist and are separately billed] |
| `search_type` | `"web"` (standard). `"fast"` is cheaper but is a **different retrieval path**; using it would change the measurement, so it is not used | [VERIFIED both exist; equivalence not established] |
| `max_results` | Pinned (1–50 allowed). Same value for every observation | [VERIFIED range] |
| `max_tokens`, `max_tokens_per_page` | Pinned explicitly rather than left to defaults, so token cost and context are stable across runs | [VERIFIED both parameters exist] |
| `search_domain_filter` | **Not used** in Stage 1 (allow/deny-listing would bias which sources can be cited) | [VERIFIED parameter exists; up to 20 domains] |
| Statelessness | One request per observation. No conversation id, no session reuse, no memory | Protocol requirement |
| Recorded per observation | Full raw JSON body · HTTP status · latency · UTC timestamp (ms) · prompt SHA-256 · run index · window id · **model string sent** · **model string returned** · `search_invocations` count from `tool_calls_details.search_web` · citations/URLs as returned · token usage as returned · retry count · estimated cost | Protocol §3 |

**`grounding_used` flag (your requirement):** set to `true` when the response contains search-invocation evidence
(`tool_calls_details.search_web` > 0 or citations present), `false` when it does not, and **`unknown` when the
response is ambiguous**. The derivation rule is written into the protocol before the first run. **`false` and
`unknown` observations are reported separately and never pooled with `true`** — an ungrounded answer is a
different measurement, and pooling them would be the same category of error as blending surfaces.

### 1.2 Rate limits — these constrain the schedule, not the budget

| Tier | Lifetime spend | Agent API |
|---|---|---|
| **0** | **$0** | **1 query/sec · 50 requests/min** |
| 1 | $50+ | 3 QPS · 150 RPM |
| 2 | $250+ | 8 QPS · 500 RPM |

[PARTIALLY VERIFIED — two consistent secondary sources; official rate-limit page not retrieved]

**We will certainly be on Tier 0**, because Tier 1 requires $50+ lifetime spend and our cap is $40. Consequences:
throttle to **0.8 QPS** with exponential backoff and jitter on 429; **436 requests need ≥9 minutes** of wall-clock,
which is trivial. **The design must not require Tier 1** — reaching it would breach the cap.

### 1.3 Unresolved Perplexity questions (must be closed before the first run)

| # | Question | Why it matters | Status |
|---|---|---|---|
| P1 | Does a **Sonar preset on the Agent API still carry the $5/$8/$12 per-1,000 request fee**, or only tokens + per-invocation tool fees? | Doubles or halves the A1 cost line. The cost model below budgets **both** | **[UNKNOWN]** — sources describe the fee for the Sonar interface and the tool fees for the Agent API, not their combination |
| P2 | Exact Sonar preset identifier and whether **model fallback chains** can be disabled | Fallback would silently change the model mid-series — explicitly forbidden by your instruction | **[NOT YET VERIFIED]**; the Agent API documents fallback chains, so the adapter must detect and abort on any mismatch |
| P3 | Are failed / rate-limited requests billed? | Affects retry budget. The Search API documents that invalid, rate-limited and upstream-failed requests are **not** billed; the Agent API is not stated | **[NOT YET VERIFIED]** — assume billed until proven otherwise |
| P4 | Data-use terms: may Perplexity use inputs/outputs to improve its models? | Our prompts name candidate brands and competitors | **[NOT YET VERIFIED]** — must be read before the first run |

---

## 2. Gemini grounding — verification

| Item | Verified position | Source / status |
|---|---|---|
| **Model** | Grounding with Google Search per-query billing applies to **Gemini 3 and newer**; Gemini 2.5 and older are billed **per prompt**. Free-tier reporting names **Gemini 3 Flash** as the current free-tier default | Billing split **[VERIFIED — official ai.google.dev, retrieved 16 Oct 2026]**; free-tier model naming **[PARTIALLY VERIFIED — T3, Sep 2026]**. **Exact model id string is pinned from the console at setup and recorded per observation from the response** — never assumed |
| **Retrieval behaviour** | "The model analyzes the user prompt and determines if a Google Search can improve the answer… automatically generates **one or multiple** search queries and executes them… processes the search results, synthesizes the information" | **[VERIFIED official]**. **Critical for measurement:** retrieval is **model-discretionary, not forced** — some prompts may trigger **zero** searches. That is exactly why `grounding_used` must be recorded per response |
| **Source metadata returned** | "a final, user-friendly response… grounded in the search results. This response includes the model's text answer with **inline annotations containing the citations**, as well as **`google_search_call` and `google_search_result` steps with the search queries and search suggestions**" | **[VERIFIED official]** — so we get the executed queries and citation annotations. Field names beyond these (e.g. a `groundingMetadata` wrapper) are **[NOT YET VERIFIED]**; the adapter therefore **stores the entire raw response body** and parses defensively rather than depending on unverified field paths |
| **Billing** | **Per query executed**, not per prompt: "your project is billed for **each** search query that the model decides to execute… if the model executes multiple search queries to answer a single prompt, this counts as **two billable uses**". Empty web-search queries are ignored for billing | **[VERIFIED official]** |
| **Free allowance** | **5,000 free search requests per month, shared across all Gemini 3 and newer models**, then **$14 per 1,000** | **[VERIFIED official]** |
| **Token rates** | Gemini 3.8/3.7/3.6 Flash: **$0.75/M input, $3.75/M output through 31 Dec 2026**, rising to **$1.50/$7.50 on 1 Jan 2027** | **[PARTIALLY VERIFIED — T3 citing Google's rate card as of 4 Oct 2026; official pricing page not retrieved]. Stage 1 runs in October 2026, so the lower rates apply** |
| **What it is NOT** | "Grounding with Google Search returns an AI answer backed by search, **not** the results page itself. You get no ranking positions, no per-result URLs in order, and no SERP features" | **[PARTIALLY VERIFIED — T3, consistent with the official description]** |
| **Request limits (free tier)** | **Conflicting:** 10 RPM / 250,000 TPM / **1,500 RPD** (Sep 2026) vs 15 RPM / 1M TPM / 1,500 RPD (Apr 2026) vs OAuth 1,000/day at 30 RPM and API-key 250/day at 15 RPM (Apr 2026) | **[UNKNOWN — three conflicting T3 sources].** Mitigation: throttle to **8 RPM** (safe under every reported value) and cap daily volume at **250 requests**, which is safe under all reported RPD figures. 446 total requests over two windows = ~223/day, inside that cap |
| **Free-tier data use** | One source states "**Data usage for training: Yes (free tier)** — Google may use free tier data"; free tier has no SLA | **[NOT YET VERIFIED — single T3 source; official terms not retrieved].** This is a real decision for you — see §5 |

---

## 3. Cost model for the 720 planned observations

### 3.1 Volume

```
Planned observations:  3 brands × 12 prompts × 5 runs × 2 windows × 2 API surfaces = 720
Per surface:           360 requests
Pre-flight (dev, logged separately, NOT observations):
                       3 brands × 12 prompts × 1 run = 36, plus a 10-request smoke test = 46
Retry allowance:       +10%
Billable requests:     A1 = (360 + 46) × 1.10 ≈ 446   A2 = same ≈ 446
```

Pre-flight runs **before** the registry is frozen, on throwaway prompts, so no observation is contaminated. They
are logged as `dev`, excluded from all statistics, and costed.

### 3.2 Surface A1 — Perplexity Agent API (Sonar preset, `web_search`)

| Component | Rate | Assumption | Expected | Conservative |
|---|---|---|---|---|
| Tokens | $1/M input, $1/M output | 80 in / 600 out (expected); 200 in / 1,000 out (conservative) | 446 × $0.00068 = **$0.30** | 446 × $0.0012 = **$0.53** |
| Request fee *(P1 unresolved — budgeted in both cases)* | $5 / $8 / $12 per 1,000 by context size | low context (expected); medium (conservative) | 446 × $0.005 = **$2.23** | 446 × $0.008 = **$3.57** |
| `web_search` invocations | **official $2.50 per 1,000** ($1.00 fast) · secondary sources report **$5.00 per 1,000** — conflict recorded | 1 invocation/request (expected); 2 invocations/request at the higher rate (conservative) | 446 × $0.0025 = **$1.12** | 892 × $0.005 = **$4.46** |
| `fetch_url` and other tools | $0.0005 / $0.005 per invocation | **disabled** | **$0** | **$0** |
| Failed requests (P3) | unknown | assumed billed | included above | included above |
| **A1 subtotal** | | | **$3.65** | **$8.56** |

### 3.3 Surface A2 — Gemini 3 Flash class + Grounding with Google Search

| Component | Rate | Assumption | Expected | Conservative |
|---|---|---|---|---|
| Grounding search queries | **5,000 free/month**, then $14 per 1,000 | 1.5 queries/request avg → **669 queries**, inside the free allowance | **$0** | allowance unavailable/exhausted → 669 × $0.014 = **$9.37** |
| Tokens (grounding injects retrieved context, so input is large) | $0.75/M in, $3.75/M out | 3,000 in / 600 out (expected); 6,000 in / 900 out (conservative) | 446 × $0.0045 = **$2.01** | 446 × $0.0079 = **$3.51** |
| **A2 subtotal** | | | **$2.01** | **$12.88** |

### 3.4 Total against the $40 cap

| Case | A1 | A2 | **Total** | % of $40 cap |
|---|---|---|---|---|
| **Expected** | $3.65 | $2.01 | **$5.66** | **14%** |
| **Conservative worst** | $8.56 | $12.88 | **$21.44** | 54% |
| **Absolute worst** (conservative + Gemini on the paid grounding rate + 20% extra retries) | $10.3 | $15.1 | **$25.4** | 64% |
| **Authorised cap** | | | **$40.00** | 100% |
| **Hard abort trigger** | | | **$35.00** cumulative estimated spend | 88% |

Headroom is real: even the absolute worst case leaves 36% of the cap unused. **If Gemini's paid grounding rate
applies and you would rather not pay it, dropping A2 to a second Perplexity preset is not permitted without your
approval** — that would be a silent surface substitution (§4).

---

## 4. Controls that make the cap and the integrity rules enforceable

| # | Control | Behaviour |
|---|---|---|
| K1 | **Spend counter** | Every request logs an estimated cost from the returned token usage and invocation counts; cumulative total is compared against $35 → **abort and report**; against $40 → **hard stop, no further calls** |
| K2 | **No silent model substitution** | Config pins the exact model string. The adapter compares the **returned** model identifier to the pinned string; any mismatch → **abort the run, log, report to founder** |
| K3 | **No silent fallback** | Perplexity's Agent API documents model fallback chains; they are **not configured**, and any evidence of a fallback in a response aborts the run |
| K4 | **No silent surface substitution** | If a provider is unavailable, deprecates an endpoint, changes pricing, or exceeds the retry budget → **stop and report**. We do not switch provider, model, region or surface. A missing surface is reported as missing |
| K5 | **Frozen registry** | The SHA-256 hash of the prompt list is recorded before the first observation. Any mismatch at run time → abort. No post-hoc prompt edits (integrity rule 20) |
| K6 | **Raw evidence, append-only** | Complete raw response bodies plus all metadata; nothing is overwritten, smoothed or re-derived. Prompts are stored by hash and by verbatim text |
| K7 | **Per-surface reporting** | A1 and A2 are never pooled into one rate. Every reported figure names its surface, model string, n, window and interval |
| K8 | **`grounding_used` per observation** | `true` / `false` / `unknown`, with the derivation rule fixed in advance. `false` and `unknown` are reported separately |
| K9 | **Rate limiting** | A1 at 0.8 QPS (Tier 0 = 1 QPS); A2 at 8 RPM and ≤250 requests/day. Backoff with jitter on 429; bounded retries (max 3 per observation), each retry logged |
| K10 | **Dev/observation separation** | Pre-flight calls are tagged `dev` and excluded from every statistic and every deliverable |
| K11 | **Two windows** | W1 days 3–7, W2 days 8–12, ≥7 days apart, identical config. Window id recorded per observation |

---

## 5. Two decisions this sheet surfaces for you

**D-a — Gemini free tier and data use.** One secondary source states Google may use free-tier data to improve its
products **[NOT YET VERIFIED]**. Our prompts will contain candidate brand names and their competitors. Options:

| Option | Cost | Trade-off |
|---|---|---|
| (i) Use the free allowance, disclose to candidates that prompts are public-intent queries | **$0** grounding | Cheapest; relies on the prompts containing no confidential client data — true by design, since we only query public buyer-intent questions |
| (ii) Use the paid tier for grounding | **+$9.37** (669 queries × $14/1,000) | Removes the free-tier data-use question; still inside the cap (total ≈$15) |
| (iii) Drop A2 and use a second Perplexity preset | $0 | **Not recommended** — loses the per-surface separation that the whole protocol rests on |

**Recommendation: (i), and I will read Google's API terms before the first run and stop if they are more
permissive than the secondary source suggests.** If you prefer certainty, (ii) costs $9.37 and stays well inside
the cap.

**D-b — Perplexity P1 (does the Sonar preset still carry a per-1,000 request fee?).** Unresolved. The cost model
budgets it in both cases, so the cap holds either way. **Recommendation: confirm in the console at account setup
(a $0 action) before the first run, and report the answer to you.** If it turns out the fee applies at the higher
context tier, expected A1 rises to ~$5.9 and the total to ~$7.9 — still 20% of the cap.

---

## 6. What remains unverified, and the order in which it will be closed

| # | Item | Blocks | How it will be closed |
|---|---|---|---|
| 1 | Official Perplexity deprecation notice, Agent API rate-limit page and pricing page | Cost certainty (not feasibility) | Retrieve `docs.perplexity.ai` pricing/rate-limit pages — **no account needed** |
| 2 | Sonar preset identifier and fallback-chain configuration | K2/K3 | Console at account setup (**requires S1a-style account approval**) |
| 3 | Google's official Gemini API terms on free-tier data use | D-a | Retrieve `ai.google.dev` terms — **no account needed** |
| 4 | Exact Gemini model id string for the grounded Flash-class model | K2 | Console / official model list |
| 5 | Whether failed Agent API requests are billed (P3) | Retry budget | Official pricing/billing docs |

Items 1, 3 and 5 need no approval and are already in the Stage 2 retrieval queue. Items 2 and 4 need an account,
which is **NO-GO** — so the collection code cannot be finally pinned until that gate clears. **I will not create
an account, and I will not make an API call, without explicit authorisation.**

---

## 7. Sign-off block

| Item | Requested | Value |
|---|---|---|
| **S2 total cap** | Authorise | **$40.00 (₹3,800)** — hard stop, abort trigger at $35 |
| Expected spend | Informational | **$5.66 (₹538)** |
| Conservative worst case | Informational | **$21.44 (₹2,037)** |
| Surfaces | Fixed | A1 Perplexity Agent API (Sonar preset) · A2 Gemini 3 Flash class + Grounding with Google Search |
| Observations | Fixed | 720 (3 brands × 12 prompts × 5 runs × 2 windows × 2 surfaces) + 46 dev |
| Substitution policy | Fixed | **None without your written approval** (K2–K4) |
| D-a (Gemini free tier) | **Decision needed** | Recommended (i) free allowance with disclosure; alternative (ii) +$9.37 |
| Trial accounts (S1a) | **Not requested** | L2 vendor layer remains excluded from the baseline |

**Nothing in this document authorises itself. Execution begins only on your explicit approval of S2.**
