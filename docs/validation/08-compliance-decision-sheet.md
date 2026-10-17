# Compliance decision sheet — provider-use rights, alternatives, and remaining permissions

**Date:** 16 October 2026 · **Purpose:** resolve the blockers you raised before any paid measurement.
**Status: NO-GO maintained.** No API calls, no accounts, no spend, no outreach, no publishing, no implementation.
**Scope:** this sheet answers your eight items only. It does not rebuild the research report.

Labels: **[VERIFIED]** = official primary source retrieved today · **[PARTIALLY VERIFIED]** · **[NOT YET VERIFIED]** ·
**[NOT FOUND]** · **[UNKNOWN]**. FX ₹95 = $1.

---

## 1. Gemini Grounding with Google Search — restrictions and implications

**Source: Gemini API Additional Terms of Service, effective 23 March 2026, retrieved today from
`ai.google.dev/gemini-api/terms`** [VERIFIED, official, quoted exactly]:

> "You will only use Grounding with Google Search **in an application that is owned and operated by you** and will
> only display the Grounded Results with the associated Search Suggestion(s) **to the end user who submitted the
> prompt**."
>
> "You will not, and will not allow your end user or any third party to, **cache, frame, syndicate, resell,
> analyze, train on, or otherwise learn from** Grounded Results or Search Suggestions. For clarity, Grounded
> Results, Search Suggestions, and Links are intended to be used in combination to respond to a given end user
> prompt and **it is a violation of these terms to use Grounding with Google Search to extract or collect one or
> more of these components for another purpose** (for example, using programmatic or automated means to collect
> Links, **using Links to build an index**, or using Links to identify destination pages for crawling or
> scraping)."
>
> "You will not… **copy, store, or implement any click tracking, Link-tracking or other monitoring** of Grounded
> Results or Search Suggestions, except that: You may copy and store, for up to two (2) years, the **text** of the
> Grounded Result(s): (1) that were displayed by you **only to evaluate and optimize the display of the Grounded
> Results in your application**; (2) in chat history of an end user…; and (3) temporarily for the purpose of
> resubmitting…"
>
> "You may allow end user(s) to copy and store individual Grounded Results that were displayed to them through
> your application **as long as you do not allow Grounded Results to be accessed or collected by automated or
> programmatic means or to be used to create a database**."

### Verdict: the planned Surface A2 is prohibited on five independent grounds

| # | Planned activity | Clause breached |
|---|---|---|
| 1 | Automated extraction of brand mentions and citations from responses | "**analyze**… Grounded Results" |
| 2 | Building a 720-observation measurement dataset | "**extract or collect** one or more of these components **for another purpose**"; "**used to create a database**" |
| 3 | Tracking visibility over time across two windows | "**other monitoring** of Grounded Results" |
| 4 | Storing raw response bodies plus citation links in an append-only evidence store | "**copy, store**… except" — no exception applies (see below) |
| 5 | Showing results to a client who did not submit the prompt (a diagnostic deliverable) | "display… **only to the end user who submitted the prompt**" |

**The 2-year storage exception does not rescue any of this.** It permits storing Grounded Result *text* **only to
evaluate and optimize the display of Grounded Results in your own application** — a display-engineering purpose,
not measurement, benchmarking or client reporting. It also excludes Links, which are precisely the citation data
we wanted.

**Two further constraints found in the same document** [VERIFIED]:
- "**You may use only Paid Services when making API Clients available to users in the European Economic Area,
  Switzerland, or the United Kingdom.**" Any future client-facing tool touching EU/UK users must be on paid
  quota — consistent with your D-a preference, and a constraint on the product, not just Stage 1.
- "You may not use the Services to develop models that compete with the Services… may not attempt to reverse
  engineer, **extract or replicate** any component of the Services."

### Precedent check — no official clarification exists

A developer posted essentially our exact workflow to Google's own developer forum on **5 October 2026**
("Grounding terms clarification for internal brand visibility measurement"): a fixed panel of 56 public
product/service questions weekly, ≤280 responses/month, automatically recording own-brand mentions and cited
domains, private internal dashboard, no training, no resale — asking (1) is it permitted or does it need written
permission, (2) would retaining only derived counts help, (3) what retention/display rules apply, (4) which
channel gives authoritative clarification. **Retrieved today: 1 post, 0 replies, 30 views — no Google answer
after 11 days** [VERIFIED]. A related thread on offline Gemini benchmarking has one reply, content not retrieved.

**Implication:** the question is genuinely unresolved in public, the forum does not answer it, and the terms as
written prohibit our design. **Do not initiate grounded collection.** Your instruction is adopted as written:
no grounded collection, no storing grounded outputs as a monitoring dataset, no commercial visibility scores
from this endpoint, unless and until suitable rights are confirmed in writing.

**One practitioner's documented workaround is informative but is a different measurement:** a GEO operator states
they call Gemini's **plain `generateContent` endpoint with no search tool attached**, so it "returns the model's
own output rather than Grounded Results, and the clause above does not reach it" [PARTIALLY VERIFIED — T3
practitioner's legal reading, not Google's]. That yields an **ungrounded / parametric** answer: what the model
says from memory with no retrieval. It is legitimate to measure and commercially meaningful (brand knowledge in
model weights), but it is **not AI-search citation measurement** and must never be presented as such. See §4,
Option B.

---

## 2. Perplexity — commercial-use assessment

**Critical distinction: Perplexity has two different agreements.** The consumer Terms of Service
(`perplexity.ai/hub/legal/terms-of-service`, 23 Jan 2026) state "We hereby permit you to use the Services for your
**personal, non-commercial use only**" and prohibit exploiting the Services for any commercial purpose and using
automation software. **That agreement governs the consumer product, not the API** — using it would be the wrong
instrument. The **Perplexity API Terms of Service** (`perplexity.ai/hub/legal/perplexity-api-terms-of-service`,
23 Jan 2026) govern us [VERIFIED, retrieved today]:

| Clause | Text | Assessment for our use |
|---|---|---|
| **2.1 Right to Use** | Non-exclusive, non-sublicensable, non-transferable right to (i) internally use API Documentation to enable/maintain the integration between **Customer Applications** and the Services, (ii) use the Services and API Keys to submit Input and receive Output *(clause text truncated in retrieval — full clause **NOT YET VERIFIED**)* | Commercial use is contemplated. The truncation matters: the permitted purposes continue past what we retrieved and **must be read in full before the first call** |
| **2.3.1 Ownership** | "Customer (i) retains all ownership rights in Input and (ii) **owns all Output**. Perplexity asserts no ownership rights in any Output and, to the extent it obtains any such rights… **hereby assigns such rights to Customer**" | **Strong.** Explicit output ownership — better than the consumer terms and better than Gemini's grounding position |
| **2.3.3 Model Training** | "Perplexity **shall not** use (or authorize third parties to use) Customer Content to **train, retrain, fine-tune or otherwise improve** any generative artificial intelligence models" | **Resolves the data-use concern** that D-a raised for Gemini. Our prompts naming candidate brands are not training fodder |
| 2.3.4 License to Perplexity | Limited to what is necessary to perform its obligations and comply with law | Narrow, acceptable |
| **2.4 AUP** | No right to use the Services, Outputs or API Platform in a manner violating the **Acceptable Use Policy** at `perplexity.ai/hub/legal/aup`, incorporated by reference; "directly or indirectly use the Services" includes use via Customer Applications | **The AUP has NOT been read — this is the single most important open item.** It could restrict benchmarking, aggregation, scraping-like volumes, or competitive intelligence uses |
| **2.5 Suspension (the "competitive-application provision")** | Perplexity may terminate the license and deactivate API keys if it determines a Customer Application is "unlawful, unethical, inconsistent with the technical or security requirements…, inconsistent with the AUP, interfering with the operation or integrity of the Services, **competitive with Perplexity**, or likely to damage Perplexity's reputation or otherwise bring Perplexity into dispute" | **Unilateral and discretionary.** Our assessment: an AI-visibility measurement and managed-optimisation service is **not** a search or answer engine, so "competitive" should not apply — but Perplexity decides, and the same clause reaches "likely to… bring Perplexity into dispute", which a published benchmark naming their answer quality could plausibly trigger. **This is a strategic dependency risk, not just a Stage 1 issue**: if our measurement layer rests on one provider who can switch us off unilaterally, the business has a single point of failure. Mitigations in §4 |
| 9.1 Indemnity | Customer indemnifies Perplexity against third-party claims arising from our use, Customer Content, or any Customer Application | Publishing findings about third-party brands carries that risk → reinforces existing rule: no named-brand deficits without permission (`13` §10) |
| **Search Addendum** (`…-terms-of-service-search`, Schedule 1: `/search`) | For the **Search API** endpoint: "**Customer does not own**, and Perplexity shall not grant it ownership of, the Search API's Output"; IP indemnification does not apply to it | **Material.** The `/search` endpoint's output is *not* ours, unlike Agent-API Output. **Open question: does the `web_search` tool invoked inside the Agent API count as a "Search Service" under Schedule 1?** If yes, our citation data may not be owned by us even though the answer text is. **[UNKNOWN — needs written clarification]** |

**Bottom line:** Perplexity's API terms are **materially more favourable** than Google's grounding terms —
explicit Output ownership and an explicit no-training commitment. But three things are unresolved and each is
capable of blocking the design: the **full 2.1 clause**, the **AUP**, and whether **`web_search` output falls
under the Search Addendum**. None can be closed by reading alone with confidence; §3 requests them in writing.

---

## 3. Written permissions and clarifications required

| # | To | Ask exactly this | Why | Route | Expected |
|---|---|---|---|---|---|
| **W1** | **Google** (Gemini API / Google Cloud) | Whether a paid-Gemini-API workflow that (a) submits a fixed panel of public buyer-intent prompts, (b) records derived brand-mention and cited-domain counts, (c) retains raw response text and links in a private evidence store, and (d) reports aggregated results to the brand's own marketing owner under a paid consulting engagement, is permitted under the Grounding with Google Search Use Restrictions — or whether it requires separate written permission or a different licence. Ask specifically whether **retaining only derived counts** (no text, no links) changes the answer | The terms appear to prohibit (b)–(d); the forum has not answered in 11 days | The forum thread's own question 4 asks which channel is authoritative — so **first identify the correct channel** (Google Cloud sales / API terms contact), then submit in writing. **Do not email from a personal address implying a client relationship** | Weeks. **Not compatible with a 14-day Stage 1** → pursue in parallel only if Gemini-grounded data is strategically essential; do not build the plan on it |
| **W2** | **Perplexity** (API support / sales) | Confirm in writing that the following are permitted under the API ToS and AUP for a paying API customer: repeated brand-visibility benchmarking across a fixed prompt panel; automated analysis of returned answers; citation and source extraction; storage of raw responses and derived observations; aggregated performance reporting; and use in client diagnostics and **paid consulting deliverables**. Also ask (i) whether `web_search` tool invocations inside the Agent API are "Search Services" under the Search Addendum Schedule 1 (and therefore whether Customer owns that Output), (ii) whether a measurement/optimisation service is considered "competitive with Perplexity" under §2.5, and (iii) the exact Sonar preset identifier and whether model fallback can be disabled | §2.1 truncated, AUP unread, Addendum scope unknown, §2.5 is discretionary | API support ticket / sales contact, from the account that would hold the key. **Log the response with its date and exact scope**, per your instruction — and record that support answers are not necessarily binding on the company | Days to weeks |
| **W3** | *(none)* | — | **No other provider permission is sought.** We will not request rights we do not need, and we will not contact any vendor as a "customer" while NO-GO stands | — | — |

**Rule adopted:** a permission request is *outbound contact with a vendor*, which is not outreach to a prospect
but is still an external act. **W1 and W2 require your approval before they are sent** (new gates **W1**/**W2**).

---

## 4. Compliant measurement alternatives

None is adopted. Each is presented for your decision, with what it actually measures — because **the compliance
constraint changes the measurement, and pretending otherwise would be the same error as blending surfaces.**

| Option | What it is | Compliance basis | What it measures | Cash | Founder hours | Limitations |
|---|---|---|---|---|---|---|
| **A — Perplexity Agent API only** *(recommended, conditional on W2)* | Single API surface: Sonar preset + `web_search`, 360 observations | API ToS 2.3.1 (we own Output) + 2.3.3 (no training). **Conditional:** AUP unread, §2.1 truncated, Addendum scope unknown | AI-search answers **with citations** — mention rate, citation rate, cited domains, run-to-run variance, window-to-window stability | **$3.65 expected / $8.56 conservative** | 0.5 | **Single-provider dependence** — if terms change or §2.5 is invoked, measurement stops with no fallback. No cross-provider agreement evidence |
| **B — Gemini *ungrounded*** (`generateContent`, **no search tool**) | Plain model call, no retrieval | The grounding clause "does not reach it" per a practitioner's reading **[PARTIALLY VERIFIED — not Google's position]**; general Gemini terms still apply (paid quota for EEA/CH/UK users; no competing-model development) | The model's **parametric brand knowledge** — what Gemini says about a brand from memory. **Not** citation measurement | **≈$1.17** (no grounding fees; ~446 requests) | 0.2 | Must be labelled a **distinct surface** ("ungrounded / parametric") and never pooled with A or presented as AI-search visibility. Requires your explicit approval — adopting it silently would be a surface substitution |
| **C — Expand human consumer capture** | Human, logged out, fresh session, transcript + screenshot | No API terms engaged. Consumer-product terms bar **programmatic** extraction, not a person reading and recording | The **actual consumer experience** — highest ecological validity of anything available to us | **$0** | **+0.8 to +1.2 h** (see §5) | Small n, labour-bound, one region/device, and publishing derived data about third-party brands still needs care (existing rule: no named-brand deficits without permission) |
| **D — Vendor platform with contractual export rights** | Peec / Otterly / Scrunch seat, data taken via CSV export | The vendor holds its own upstream arrangements; **our right to analyse and resell derived metrics depends on their terms, which are unread** | Whatever the vendor collects (Peec documents UI scraping; Profound documents consumer front ends + panels) | $29–$495/mo; **$0 during a free trial** | +2.5 | **Blocked twice over:** trial registration is NO-GO, and export/usage rights during a trial are **[NOT YET VERIFIED]**. Would also make our numbers vendor-dependent — the exact thing we criticise |
| **E — Licensed retrieval API built for programmatic use** (e.g. Parallel Web Systems' Search API, marketed explicitly against grounding's "strings attached") | A retrieval/index API designed to be called by agents and stored | Terms not yet read; the product is sold for this use | **Which URLs are retrievable for a query** — input to the citation-gateway workstream (B4), **not** what an AI assistant says | Unknown; needs a quote | 0.5 | Different construct. Useful for gateway analysis; cannot substitute for answer-surface measurement. **[NOT YET VERIFIED]** |
| **F — Do nothing until W1/W2 answer** | Pause L1 entirely | Fully compliant | Nothing | $0 | 0 | Stage 1 becomes the **$0 conversations-only variant** (`05` §7): 5 buyer conversations, three-option card, price ladder, one priced proposal, Stage 2 desk research — **20.5 founder-hours, no measurement**. Diagnostics become labelled desk-research briefs, not measurements |

**Recommendation:** **A + C now, B only if you approve it as a separately labelled surface, D and E deferred,
F held as the fallback.** A+C preserves a real measurement (360 API observations + expanded human capture),
keeps per-surface separation, stays far inside the $40 cap, and — importantly — **A is conditional on W2**, so
nothing is spent until Perplexity confirms in writing. If W2 does not come back before Day 3, the plan drops to
F for the measurement layer and commercial validation proceeds untouched, because **your stated priority is the
first customer's buying commitment, not the observation count.**

**Concentration risk to record now regardless:** a business whose measurement layer depends on one API provider
that can unilaterally classify it as "competitive" has a structural vulnerability. That belongs in the Phase-1
risk register and in any future investor or client conversation. It is also an argument for **C (human capture)
and for owning our raw-evidence store** — assets no provider can revoke.

---

## 5. Updated cost and observation estimates

### 5.1 Recommended design (A + C), pending W2

| Layer | Arithmetic | Observations | Cash expected | Cash conservative | Founder hours |
|---|---|---|---|---|---|
| **L1 — Perplexity Agent API (Sonar preset + `web_search`)** | 3 brands × 12 prompts × 5 runs × 2 windows = **360**; + 36 pre-flight + 10 smoke = 46 dev; +10% retries ⇒ **446 billable** | **360** | **$3.65** | **$8.56** | 0.5 |
| ~~L1b — Gemini grounding~~ | **REMOVED — prohibited (§1)** | 0 | $0 | $0 | 0 |
| **L2 — vendor platform** | Excluded (NO-GO on trial registration) | 0 | $0 | $0 | 0 |
| **L3 — human consumer capture** | Variant **C-1** (as planned): anchor brand 10 × 3 = 30 + co-observation 2 × 3 = 6 ⇒ **36 captures** · Variant **C-2** (recommended): 2 brands × 10 × 3 = 60 + 6 ⇒ **66 captures** | **36 or 66** | $0 | $0 | **1.2 (C-1) or 2.2 (C-2)** |
| **Total** | | **396 (C-1) or 426 (C-2)** | **$3.65** | **$8.56** | |

Against the **$40 cap and $35 abort trigger**: expected spend is **9% of cap**, conservative worst **21%**. The
cap is unchanged and comfortably sufficient; **the binding constraint is now compliance, not money.**

### 5.2 Optional additions, each requiring separate approval

| Add | Observations | Cash | Hours | Condition |
|---|---|---|---|---|
| **B — Gemini ungrounded** (3 brands × 12 × 5 × 2 = 360) | +360 | **+$1.17** (conservative +$1.80) | +0.2 | Your explicit approval; labelled a distinct surface; paid quota if any EEA/CH/UK-facing use |
| **Second Perplexity preset** for cross-preset agreement | +360 | ≈+$3.65 | +0.1 | **Not recommended** — two presets of one provider is not two surfaces, and it doubles the §2.5 dependency |

### 5.3 Founder-hour fit (your standing requirement that the workload provably fits)

| | C-1 (36 captures) | **C-2 (66 captures, recommended)** |
|---|---|---|
| Block C (measurement) | 3.0 h | **3.7 h** (+0.7: captures 1.0 → 2.0, co-observation 0.5 → 0.2, protocol 1.0, oversight 0.5) |
| Plan total | 30.0 h | **30.7 h** |
| Offset | — | Trim **A6 Stage 2 review 1.5 → 0.8 h** (Stage 2 is agent-led; your review can be async notes) ⇒ **back to 30.0 h** |

No manual capture volume approaches the 750-capture error (C-13): **66 captures = 2.2 h, shown on the page.**

### 5.4 What we lose, stated plainly

- **No Google/Gemini answer surface at all** unless W1 succeeds — so we cannot report what Gemini or Google AI
  surfaces cite, which are among the highest-reach surfaces. Every deliverable must say so.
- **No cross-provider agreement evidence** within the API layer (single provider).
- Reported intervals widen slightly at the brand level (360 vs 720 observations): per-prompt precision is
  **unchanged** (5 runs per prompt per window), brand-level n per surface falls from 120 to 120 for A1 — actually
  unchanged for A1; what disappears is the second independent surface, not sample size.
- Consumer-surface coverage improves under C-2 (2 brands instead of 1) but remains small-n and single-window.

---

## 6. Verified US/EU prospect alternatives (O1-a)

All facts below are **T3 secondary sources retrieved today** and carry a Day-1 primary-source verification task.
**Nothing is repeated to a prospect until verified from a primary source.** Note the standing rule: **agency
case-study results are not evidence** — they are used here only to identify who already believes in AEO and who
owns the budget.

| # | Candidate | Segment / category | Public facts on record | Why it qualifies | Verify on Day 1–2 |
|---|---|---|---|---|---|
| 1 | **Qwilr** | S4 — proposal / sales-content SaaS, mid-market, US/AU | A **named Head of Growth (Brendon Connaughton)** is publicly quoted: "I can confidently say about **30% of our pipeline comes from AEO/SEO and AI search**. In the last month we got over **$300K in pipeline** just from AEO/SEO for really no additional work" (agency blog, 30 Sep 2026) | **Strongest S4 candidate**: a named economic buyer, a named role, and a public statement that AI search already drives pipeline — i.e. budget exists and the pain is felt. Also a **switch test**: they already work with an agency | HQ and entity, whether the quoted person still holds the role, current agency relationship, whether the figures are theirs or the agency's. **Never quote the numbers back to them as fact** |
| 2 | **Qrvey** | S4 — embedded analytics SaaS, US | Agency-reported: pipeline **$740K → $1.5M in one year** via SEO/AEO; "organic and AI search became their #1 and #2 discovery channels"; "**rank #3 in AI search brand visibility** across embedded analytics… ~2,836 LLM mentions" | Already invests in AEO with measurable internal reporting ⇒ realistic buyer for a **second opinion / measurement QA** offer, which is our honest differentiator | All figures are **agency claims** — treat as unverified. Confirm category, HQ, marketing owner, and whether they would entertain an independent measurement |
| 3 | **Render** | S4 — cloud hosting / developer platform, San Francisco | Founded 2018; team **100+**; last funding **Series B**; estimated $1B+ (roundup, 27 Jul 2026) | Mid-size devtools with a research-led buyer category (R4), plausible founder/marketing reachability, no size barrier like the unicorns in the same list | Funding stage and valuation, marketing leadership, content base, Western customer mix. **Valuation figure is a roundup estimate — do not use** |
| — | ~~Calendly, Webflow, Retool~~ | — | Unicorns / category leaders in the same roundup | **Excluded** — size and procurement process make a founder-led pilot unlikely (same rule that excluded Freshworks, Zoho, Postman) | — |

**Recommendation: Qwilr as the S4 conversation target** (named buyer + stated budget importance + switch test),
**Render as the diagnostic alternative** if a US/EU diagnostic is wanted, **Qrvey held in reserve**. If Qwilr's
quoted executive cannot be verified as current, fall back to Render and record S4 as verified-but-cold.

---

## 7. Finalized outreach templates (O2-a) — placeholders only, no invented facts

Unchanged in structure from `07-o1-o2-prospect-shortlist.md` §5, with two compliance amendments:

**Amendment 1 — measurement-source restriction.** No message may cite data obtained from Gemini grounding
(prohibited) or from any source whose terms we have not verified. Every `[FINDING]` must state its **surface,
model string, n, window, region and session state**, and must come from a **permitted** layer (L1 Perplexity
after W2, or L3 human capture).

**Amendment 2 — no pre-filled numbers, ever.** The placeholders below are the only form in which these templates
may be approved at O2-a. Filling them requires valid evidence, and O2-b remains gated on measurement approval
plus your review of each finished message. **Brand mentions, citations, percentages, intervals and observations
are not invented, estimated or illustrative in any outbound message.**

### 7.1 LinkedIn (≤90 words)

> Hi `[FIRST_NAME]` — I ran `[N_RUNS]` queries about `[CATEGORY]` on `[SURFACE_AND_MODEL]` on `[DATE]`, logged
> out, from `[REGION]`. In `[n_of_N]` of them, `[NAMED_ALTERNATIVE]` was recommended and `[COMPANY]` did not
> appear. Method and raw responses are available if useful: `[LINK]`. With n = `[N_RUNS]` this is directional,
> not a verdict — the 95% interval is roughly `[LO]`–`[HI]`. I'm doing a small study of AI-search visibility for
> `[SEGMENT_DESCRIPTOR]` and would rather show you the data than pitch you. Worth 20 minutes?

### 7.2 Email (published address only)

> **Subject:** `[COMPANY]` in `[N_RUNS]` AI-search runs — data inside
>
> Hi `[FIRST_NAME]`,
>
> One observation, with its limits stated up front. On `[DATE]` I ran the prompt "`[EXACT_PROMPT_TEXT]`"
> `[N_RUNS]` times on `[SURFACE_AND_MODEL]`, logged out, from `[REGION]`. `[COMPANY]` appeared in `[n_of_N]`;
> `[NAMED_ALTERNATIVE]` appeared in `[m_of_N]`. At n = `[N_RUNS]` the 95% interval on your appearance rate is
> roughly `[LO]`–`[HI]`, so treat this as directional.
>
> I'm not selling a tool. I'm running a small study of AI-search visibility for `[SEGMENT_DESCRIPTOR]`, and I'd
> rather show you the full method and raw responses — including the parts where our measurement is weak
> (`[STATED_LIMITATION]`).
>
> Would a 20-minute call in the next two weeks be useful? If not, one closing note and I won't follow up again.
>
> `[NAME]` · `[CONTACT]`

### 7.3 Sequence and binding rules (unchanged)

Follow-up 1 at day +4 (a new true finding, or a correction to the first if we find one) · follow-up 2 at day +9
(final note, explicit close) · permanent stop after that, and permanent on any opt-out. One true checkable
finding per message · no price in message one · no unsourced claim · no competitor disparagement · no guarantee of
placement, ranking or citation · no attachment or link requiring an account · never imply an existing comparable
client · every send logged (date, channel, recipient name and role, company, segment slot, message-version hash,
reply, outcome) · **no purchased lists, no scraped private data, no enrichment vendors**.

---

## 8. Exact remaining permissions required before execution

| # | Gate | What it authorises | Blocked until | Status |
|---|---|---|---|---|
| **W2** | New | Sending a written clarification request to **Perplexity** API support/sales (§3) — and logging the reply with date and exact scope | Your approval | **Required before S2** |
| **W1** | New | Sending a written permission request to **Google** (§3), if you want Gemini grounding pursued at all | Your approval | Optional; weeks-scale |
| **P1** | New | Reading, in full and at no cost: the **complete Perplexity API ToS §2.1**, the **Acceptable Use Policy**, the **Search Addendum Schedule 1**, and Google's **Unpaid/Paid Services data-use sections** | Nothing — desk research, already authorised | **In progress; will report as VERIFIED / NOT YET VERIFIED** |
| **D-b** | Existing | No-cost verification of the Sonar request fee via official docs, pricing pages and permitted console inspection | Nothing | Approved; **result: NOT YET VERIFIED** — official pricing page and console not yet retrieved; secondary sources conflict ($5/$8/$12 per 1,000 for the Sonar interface vs per-invocation tool fees on the Agent API). The cost model budgets both |
| **S2** | Existing | **Spending** up to $40 (abort at $35) on Perplexity Agent API calls | **W2 answered satisfactorily + P1 complete + D-a/Option-B decision + your explicit spend approval** | **NOT GRANTED** — limits retained, authority withheld |
| **D-a** | Revised | Gemini: **paid over unpaid** adopted as policy; grounded collection **prohibited** pending W1 | — | **Closed by §1** — Option B (ungrounded) needs separate approval |
| **O1** | Existing | Internal preparation of the longlist; Rocketlane, CometChat, CloudSEK provisional | — | **Approved** — primary-source verification and economic-buyer/marketing-owner identification are Day-1 tasks; **no outreach** |
| **O1-a** | Existing | Desk research on US/EU candidates | — | **Delivered (§6)** — Qwilr recommended; no contact |
| **O2-a** | Existing | Templates with placeholders | — | **Delivered (§7)** — approvable now |
| **O2-b** | Existing | Each **filled** message | Measurement approval + your review | **Gated** |
| **S1a / S3 / S4** | Existing | Trial accounts / second annotator / domain | — | **Deferred, unchanged** |
| **O5, D1, D5** | Existing | Conversations, diagnostic delivery, pilot proposal | O1 + O2 | **NO-GO** |

**Nothing is called, purchased, registered, sent or published until the matching gate is explicitly granted.**

---

## 9. What I did and did not do

**Did:** retrieved and quoted the official Gemini API Additional Terms; retrieved the Perplexity **API** ToS and
Search Addendum (distinguishing them from the consumer ToS); checked Google's developer forum for precedent
(no answer in 11 days); rebuilt the cost model without the prohibited surface; identified three S4 candidates
with sources; amended the templates for compliance.

**Did not:** make any API call, create any account, spend any money, contact any person or company, send any
permission request, substitute any model or surface, or fill any placeholder with a number.
