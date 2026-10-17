# 13 — Measurement & reproducibility protocol (v1)

**Status: authoritative.** Replaces the ground-truth test in `07-discovery-interview-guide.md` (D1-Q23, D3),
experiment V4 in `08`, and kill condition N-3 in `06`. Created in response to correction **C-07**.

Prepared 16 October 2026. This document is a **pre-registration**: prompts, run counts, factors and decision
bands are written down before any Stage 1 collection, and any later deviation is logged in §11 rather than
quietly absorbed.

---

## 1. Why this exists

v1 assumed a prospect could validate our measurement by re-running one prompt in ChatGPT and comparing. That is
wrong twice over:

1. **A single rerun is one draw from a distribution, not ground truth.** Published evidence in our own register
   says the distribution is wide: source overlap 34–42% day-to-day with brand Jaccard 0.45–0.59 (arXiv
   2604.07585); ~30% brand persistence run-to-run, 1-in-5 across five runs (AirOps); exact-repeat citation rate
   of 0.06% for ChatGPT over 12,778 answers (EWR Digital); 82% of Perplexity answers containing no brand
   mention at all (Otterly, 252,407 answers). Against that background, one matching or non-matching rerun
   carries almost no information.
2. **It conflated two different measurement questions** — whether we *read* an answer correctly, and whether the
   answer *is stable*. They fail for different reasons and need different tests.

Consequence for the business, stated up front: **we cannot promise proof; we can promise disclosed
uncertainty.** Every deliverable must carry the interval, the n, the surface and the window, or it must not be
sent.

---

## 2. Two separate questions

| | **E — Extraction accuracy** | **R — Measurement reproducibility** |
|---|---|---|
| Question | Given a stored response, did we label it correctly? | Given the same prompt, do repeated observations agree? |
| Ground truth | **Exists**: a human-labelled gold set | **Does not exist**: there is no oracle for what ChatGPT "would have said" |
| Failure mode | missed alias, wrong entity, hallucinated citation, position error | model/version drift, retrieval on/off, geo, session state, genuine stochasticity |
| Test | Precision / recall / F1 per label, inter-annotator κ | Agreement statistics across controlled repeats, with confidence intervals |
| Fix | better extractor, better prompt registry, re-validate on model change | more runs, tighter controls, honest reporting, narrower claims |
| Can be "solved"? | Yes, to a measurable error rate | No — only bounded and disclosed |

**Rule:** never report an R statistic computed with an unvalidated extractor, and never claim an E error rate
without stating the gold-set size and κ. If E is bad, R is meaningless; if R is bad, E is irrelevant to any
trend claim.

---

## 3. Factors that move an observation (taxonomy)

Recorded for **every** observation. Fields marked ★ are held constant in Stage 1; ◇ are varied deliberately to
measure their effect.

| # | Factor | Levels | Stage 1 |
|---|---|---|---|
| F1 | Surface | consumer web UI · consumer mobile app · official search-enabled API | ★ one API + one consumer UI, never blended |
| F2 | Model id / version string | as reported by the surface at response time (e.g. Peec's changelog records "OpenAI Search API" renamed **OpenAI Luna**, and models Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, GPT-6.1 Sol) | ★ recorded verbatim per observation |
| F3 | Retrieval actually performed | evidence: citations/links present · "searching" indicator · API search-tool call logged · none | ★ recorded; observations without retrieval are **excluded** from citation statistics and reported separately |
| F4 | Geography / exit region | US-East · US-West · UK · IN | ◇ IN vs US-East, 1 prompt subset |
| F5 | Language / market | en-US · en-GB · en-IN | ★ en-US only |
| F6 | Session context | logged out, fresh session, memory off, no custom instructions, no prior turns | ★ mandatory |
| F7 | Account / plan tier | free · plus · team · enterprise · API key tier | ★ logged-out/free where available; recorded otherwise |
| F8 | Device / client | desktop browser · mobile browser · official app | ★ desktop browser |
| F9 | Time of day | recorded in UTC with local offset | ◇ two windows per day |
| F10 | Date / measurement window | calendar date; windows separated ≥7 days for any trend claim | ★ 2 windows for the 5 Stage 1 diagnostics |
| F11 | Prompt text | exact string, hashed (SHA-256), versioned in the prompt registry | ★ no edits after pre-registration |
| F12 | Run index within window | 1…n | ★ n = 5 (see §6 for why this is weak and what we say about it) |
| F13 | Answer shape | length in tokens · list vs prose · presence of a comparison table | recorded, used to explain disagreement |
| F14 | Capture method | API response body · human screenshot + transcript · vendor platform export | ★ recorded; vendor exports are marked as vendor-collected |

**Vendor-collection caveat [NOT YET VERIFIED]:** at least one category review reports (attributing it to Peec
support in 2025) that Peec collects data by **scraping LLM user interfaces** for its six core engines and uses
APIs only for enterprise-tier models. If true, vendor numbers are drawn from consumer surfaces we cannot
legally replicate at scale (OpenAI's terms prohibit programmatic extraction outside the API). We must (a) not
accuse without evidence, (b) disclose our own collection method in every report, and (c) treat vendor-vs-our
differences as a *method* difference, not an error by either side. This is also a genuine trust differentiator
with security-conscious buyers: our protocol is API-plus-human-capture only, ToS-compliant, auditable.

---

## 4. Protocol E — extraction accuracy (gold set)

**Objective:** a measured, published error rate for every label we sell.

1. **Corpus:** 200 stored responses spanning the 3 surfaces × 2 windows × the Stage 1 prompt set, sampled
   stratified so that each surface contributes ≥50 and at least 40 responses contain zero brand mentions
   (the hard negative case).
2. **Label schema (per response):**
   - `brand_mentioned` ∈ {yes, no} — target brand named or unambiguously referred to
   - `brand_recommended` ∈ {yes, no} — named as a suggested/positive option
   - `brand_position` ∈ 1…k or null — order of first recommendation
   - `brand_cited` ∈ {yes, no} + `cited_urls[]` — a link/URL attributable to the brand's own domain
   - `third_party_cited_urls[]` — every non-brand URL cited, normalised to registrable domain
   - `sentiment` ∈ {positive, neutral, negative, mixed} for the brand passage
   - `entity_id` — resolved against a per-client alias table (brand names, product names, misspellings,
     transliterations). **Aliases are pre-declared per client and never inferred at extraction time.**
3. **Annotation:** two independent annotators, blind to each other and to the extractor output, using a written
   codebook with 10 worked examples per label. Disagreements adjudicated by a third; adjudication reasons
   recorded.
4. **Metrics:** inter-annotator **Cohen's κ per label** before any automation is used; extractor
   **precision / recall / F1 per label** against the adjudicated gold set; **URL-level precision/recall** for
   citation extraction (exact-match and registrable-domain-match reported separately).
5. **Acceptance:** κ ≥ **0.80** on `brand_mentioned` and `brand_cited` before the gold set may be used at all;
   extractor F1 ≥ **0.90** on mentions and ≥ **0.85** on citations before results are shown to a client.
   Below acceptance → fix and re-run; **do not ship with a disclosed-but-bad extractor**.
6. **Re-validation triggers:** any model-version change on a tracked surface; any extractor/prompt change; any
   new surface; monthly otherwise. Gold set grows by 50 responses per trigger.
7. **Reporting:** every client deliverable states gold-set size, date, κ and per-label F1 for the extractor
   version used.

---

## 5. Protocol R — reproducibility study

**Design.** For each of the 5 Stage 1 diagnostics: 25 pre-registered prompts × 5 runs × 2 windows (≥7 days
apart) × 2 surfaces (one official search-enabled API, one consumer UI captured by a human) = **500
observations per client**, **2,500 across Stage 1**. (v1's plan of 20 diagnostics × 25 × 5 × 3 = 7,500 is what
made the sprint impossible; see C-05.)

**Metrics, per surface, never blended:**

| Metric | Definition | Use |
|---|---|---|
| Raw agreement | proportion of run pairs with identical `brand_mentioned` | intuitive, but inflates with base rates |
| **Fleiss' κ** (multi-run) / Cohen's κ (pairwise) | agreement corrected for chance | the headline reproducibility statistic |
| **Wilson 95% interval** on mention rate | interval estimate from n runs | what we publish instead of a point estimate |
| **Jaccard** on cited-URL sets | \|A∩B\| / \|A∪B\| per run pair | citation-set stability |
| **RBO** (rank-biased overlap) | ordering similarity of recommended brands | list-order stability |
| **ICC** across windows | intraclass correlation of per-prompt mention rates between window 1 and 2 | is there a stable per-prompt signal at all? |
| Effective sample size | n adjusted for within-window correlation | prevents overstating precision |
| Rule-of-three upper bound | 95% UB ≈ 3/n when 0 of n observed | how to talk about absence honestly |

---

## 6. What n actually buys (the uncomfortable arithmetic)

Wilson 95% intervals on an observed mention rate [ESTIMATED, computed]:

| n runs | p̂ = 0.2 | p̂ = 0.4 | p̂ = 0.6 | p̂ = 0.8 | half-width |
|---|---|---|---|---|---|
| 3 | [0.06, 0.79] | — | [0.21, 0.94] | — | ±0.37 |
| **5** | [0.04, 0.62] | [0.12, 0.77] | [0.23, 0.88] | [0.38, 0.96] | **±0.29 to ±0.33** |
| 10 | [0.06, 0.51] | [0.17, 0.69] | [0.31, 0.83] | [0.49, 0.94] | ±0.23 to ±0.26 |
| 20 | [0.08, 0.42] | [0.22, 0.61] | [0.39, 0.78] | [0.58, 0.92] | ±0.17 to ±0.20 |
| 30 | [0.10, 0.37] | [0.25, 0.58] | [0.42, 0.75] | [0.63, 0.90] | ±0.14 to ±0.17 |
| 50 | [0.11, 0.33] | [0.28, 0.54] | [0.46, 0.72] | [0.67, 0.89] | ±0.11 to ±0.13 |
| 100 | [0.13, 0.29] | [0.31, 0.50] | [0.50, 0.69] | [0.71, 0.87] | ±0.08 to ±0.09 |

Runs required for a target half-width at the worst case p = 0.5 (`n = z²·0.25 / w²`): ±0.30 → **11**,
±0.20 → **24**, ±0.15 → **43**, ±0.10 → **96**, ±0.05 → **384**.

Runs required per arm to detect a before/after difference at α = 0.05, power 0.80:
0.30 → 0.60 = **42**, 0.20 → 0.40 = **81**, 0.30 → 0.50 = **93**, 0.40 → 0.60 = **97**.

**Three consequences we must design around, not explain away:**

1. **n = 5 supports no comparison claim.** Five runs put a 40% observation at [0.12, 0.77]. Stage 1 therefore
   reports *distributions and stability*, and never "brand X is more visible than brand Y" from 5 runs.
2. **"We improved your visibility by Z points" requires ~40–100 runs per prompt per window per surface.** That
   is affordable on APIs (25 prompts × 42 runs × 2 windows ≈ 2,100 observations ≈ $20–$45 per surface at
   Perplexity Sonar's published $5–$14 per 1,000 requests) and **impossible on consumer UIs by human capture**
   (42 × 25 × 2 = 2,100 manual runs). Any ROI claim must therefore be scoped to API-measurable surfaces or
   expressed as directional with wide intervals. **This is a product-shaping constraint, and it is the reason
   we must not sell "proven lift".**
3. **The surfaces we can measure rigorously are not the surfaces buyers care about.** Our own register records
   ChatGPT/Gemini/Copilot top-10 citation overlap of ~12%, Ahrefs' ChatGPT-vs-Google overlap falling 76.1% →
   37.9%, and 28.3% of ChatGPT's most-cited pages having zero Google visibility. Rigorous API measurement
   therefore describes *a* related distribution, not the consumer experience. We must say so in writing, every
   time — and this is exactly the disclosure a competitor selling confidence is unlikely to make.

---

## 7. Protocol C — prospect co-observation (replaces the "rerun it yourself" test)

**Purpose unchanged, method replaced.** We still want a buyer to see our numbers with their own eyes; we no
longer pretend their single rerun is ground truth.

1. Give the prospect a **co-observation card**: exact prompt string, surface and version, region/exit node,
   "logged out, fresh session, memory off, no custom instructions", desktop browser, a 6-hour window on a named
   date, and **3 runs** (not 1).
2. Ask them to record, per run: was our brand mentioned; was it recommended; what was recommended first; which
   URLs were cited (screenshot acceptable); did the surface appear to search.
3. We compare their 3 observations to our **predictive interval** for that prompt/surface/window, computed from
   our own runs in the same window and region. Success criterion: **their observations fall inside our stated
   interval** — not "they match our point estimate".
4. Report the result as: "3 of 3 co-observations inside the predicted interval" or "1 of 3 outside, on the
   consumer UI, which has the widest interval — here is why".
5. Log their free-text reaction verbatim. **A buyer who says "these numbers move around, so I won't pay for
   them" is the single most valuable negative signal Stage 1 can produce**, and it must be recorded as such
   rather than argued with on the call.
6. Never run this test as a sales trick on a prompt we chose because we knew the answer. Prompts are
   pre-registered (§5) before the card is sent.

Internal dry run **before any prospect sees it**: two team members independently capture the same 10 prompts
under identical controls; compute inter-observer agreement. If two people in the same office cannot reproduce
each other, no prospect test is worth running.

---

## 8. Decision bands (replaces automatic kill thresholds)

Thresholds are **decision bands that trigger a review**, never automatic company-wide kills. The founder
decides, in writing, with the evidence in front of them; the reasoning is filed in §11.

| Band | Extraction (E): gold-set F1 on mentions | Reproducibility (R): Fleiss' κ within surface/window | Interpretation | Action |
|---|---|---|---|---|
| **Green** | ≥ 0.90 | ≥ 0.60 | measurement premise supported | proceed; publish intervals as usual |
| **Amber** | 0.80–0.90 | 0.40–0.60 | usable with disclosure | proceed; cap claims at directional; increase runs to 10; disclose κ in every deliverable |
| **Red** | 0.70–0.80 | 0.20–0.40 | premise at risk | **methodology review** — narrow prompt set, drop the weakest surface, re-run; do not sell trend or comparison claims; no automatic kill |
| **Black** | < 0.70 | < 0.20 | premise falsified *for that surface* | stop selling measurements from that surface; keep only surfaces in Green/Amber; if **all** surfaces are Black, escalate to a strategy decision about whether the service can exist at all — decided by the founder, recorded, not automatic |

Additional non-threshold triggers for review (each is evidence, not a verdict): a surface changes model naming
or search behaviour mid-window; retrieval-on rate differs by >20 points between surfaces; one client's alias
table produces κ < 0.6; a vendor platform's export disagrees with our own capture on >30% of shared prompts.

---

## 9. Reporting rules (client-facing)

1. Report **per surface, per window, with n and the Wilson interval**. No blended "AI visibility score" unless
   the blend weights and the interval of the blend are shown.
2. Report absence as an **upper bound**: "not observed in n = 5 runs; 95% upper bound on the true mention rate
   is 60% (rule of three)" — never as "you are invisible".
3. Label every number **[MEASURED]**, **[MODELLED]** or **[VENDOR-REPORTED]**.
4. Never use the words *guarantee*, *ensure*, *will rank*, *placement secured*. Never imply we control model
   behaviour.
5. State the collection method (official API / human capture on consumer UI / vendor export) and the
   ToS-compliance position in the methodology footer of every deliverable.
6. Cite the extraction quality (gold-set size, κ, F1, extractor version) in the same document as the findings.
7. Every optimisation recommendation must name the **verified business fact** it rests on and the person who
   verified it. No recommendation without a fact source. (Product-integrity rule 9.)
8. Changes to a client's site require **explicit written authorisation**, are staged, diffed, approved
   item-by-item, and reversible — the same discipline Peec/Profound/Scrunch now ship natively, so ours must be
   *at least* as good, and ours is human-verified.

---

## 10. Publishing rules (public content) — closes C-06

1. Titles carry the actual n, the prompt count, the surfaces and the window: e.g. *"We measured 20 brands
   across 500 prompts and 5,000 observations over 6 weeks"* — never a number we did not measure.
2. **No findings article before n ≥ 20 brands and two measurement windows.** At n = 5 we publish methodology
   only.
3. No named-brand deficits without written permission; otherwise aggregate and anonymise ("one India-origin
   cybersecurity vendor, n = 25 prompts").
4. Pre-register the prompt list and analysis plan before collection; publish deviations with the article.
5. Publish the intervals, not just the point estimates. A public article whose numbers cannot be re-derived
   from a stated protocol is marketing, and we do not do marketing that way.

---

## 11. Deviation log

*(empty at pre-registration — 16 Oct 2026. Any change to prompts, n, factors, bands or acceptance criteria is
recorded here with date, what changed, why, and who approved.)*

---

## 12. Stage 1 execution checklist

| # | Artifact | Owner | Acceptance |
|---|---|---|---|
| 1 | Prompt registry (25 prompts/diagnostic × 5) with SHA-256 hashes, pre-registered | founder | frozen before first run |
| 2 | Codebook + alias tables per client | founder | 10 worked examples per label |
| 3 | Gold set: 200 responses, 2 annotators, adjudicated | founder + 1 contract annotator | κ ≥ 0.80 |
| 4 | Extractor + per-label precision/recall/F1 report | founder | mentions F1 ≥ 0.90, citations ≥ 0.85 |
| 5 | Raw observation store (immutable, append-only; response body, all §3 fields, cost) | founder | every observation has all 14 factor fields |
| 6 | Reproducibility report per surface/window (κ, Wilson, Jaccard, RBO, ICC) | founder | produced for all 5 diagnostics |
| 7 | Internal inter-observer dry run (10 prompts, 2 people) | founder + 1 | agreement computed before any prospect test |
| 8 | Co-observation cards + results | founder | 3 runs, same window, interval-based scoring |
| 9 | Hour and cost log per diagnostic (actual vs §3.1 budgets in `12-economics-v2.md`) | founder | variance explained, not smoothed |
| 10 | Decision-band assessment + founder's written interpretation | founder | filed even when Green |
