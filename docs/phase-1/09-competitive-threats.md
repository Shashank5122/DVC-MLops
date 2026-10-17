# 09 — Competitive threats v2 (corrected against official documentation)

**Status: authoritative.** Replaces v1 of this file (the workspace was re-cloned and its history squashed on 16 Oct 2026, so v1 text is **no longer retrievable from git**; every v1 claim that matters is quoted verbatim in `11-correction-log.md`). Created in
response to corrections **C-01** and **C-08** (`11-correction-log.md`).

Every capability claim below is sourced from **vendor documentation, vendor changelogs or vendor pricing pages
retrieved 16 October 2026**, or from published agency pricing. Labels:
**[VERIFIED]** we retrieved the primary/official page · **[VERIFIED-VENDOR-CLAIM]** the vendor documents it; we
have not tested whether it works · **[ESTIMATED]** · **[HYPOTHESIS]** · **[NOT YET VERIFIED]**.

**The single most important methodological lesson:** three independent reviews published between 26 August and
26 September 2026 said Peec has "no built-in content generations" and "does little to fix it." Peec's changelog
of **13 October 2026** ships a content optimizer, an approval-bound action system including earned media, and an
agent with 20+ MCP connectors. The reviews were wrong within weeks of publication. **Any competitive claim older
than ~30 days in this category is unusable.**

---

## 1. The corrected picture: four layers, not two

v1 described a barbell — measurement SaaS on one side, expensive agencies on the other, an empty middle. That is
false. There are four populated layers, and the middle is where the most activity happened in the last 90 days.

| Layer | Who | What they actually do | Price evidence |
|---|---|---|---|
| **L1 Measurement** | Otterly, Semrush AI Visibility, Ahrefs Brand Radar, HubSpot AEO, Athena HQ, SE Visible, IndexGraph (₹799–₹5,999) | Sample prompts, report mentions/citations/sentiment, recommend | $29–$489/mo; $99/domain; ~$337/mo category average |
| **L2 Measurement + software-assisted execution** | **Peec, Profound, Scrunch/Sitecore** | All of L1 **plus** ranked actions, content drafting/optimisation, approval-bound publishing into a CMS, agents, fact-checking with outreach drafting, earned-media opportunity identification, first-party analytics joins | Peec €70–€360/mo; Profound custom (agency $399/mo per workspace); Scrunch $300/$500+ enterprise |
| **L3 Managed human delivery** | GEO/AEO agencies, PR-native GEO firms, white-label digital-PR partners, "tool + contractor" operators | All of L2's *outputs*, executed by people: pitching editors, listicle and review-platform placements, community contributions, original research, asset production, monthly cadence | **$997/mo (SourceRank, audit $497)** · $2,000–$5,000/mo ("tool plus contractor") · $2,500/mo per pillar or $5,500/mo fully managed (MADX) · $3,000–$10,000/mo digital-PR-for-GEO mid-market · $5,000–$20,000/mo typical GEO retainer · $12,000–$25,000/mo PR-native (Crackle) · $25,000–$30,000+/mo enterprise |
| **L4 In-housing** | Enterprise marketing teams | Hire AEO/GEO managers and specialists | AWS AEO Manager $152,300–$216,090; Victoria's Secret Director AI & Organic Search $224,000–$318,000; Home Depot Sr Manager SEO/GEO $127,200–$165,000 [VERIFIED, employer-published] |

**Where SignalGEO's v1 proposal sat:** L3 with L2-grade measurement, priced at $1,000–$1,500/mo with India-based
delivery. **That position is occupied** — by SourceRank at $997/mo ("GEO and AEO done for them, measurement
included"), by the published "$2,000–$5,000/mo tool plus contractor" tier, by MADX at $2,500/mo per pillar, and
by white-label digital-PR suppliers who let any agency resell the earned-media workstream under its own brand.
What is *not* obviously occupied is that position **specialised on India-origin software companies selling to
US/UK/EU**, at INR or USD pricing, with a **published measurement protocol** — which is a go-to-market wedge and
a credibility angle, not a product moat.

---

## 2. Verified capability matrix

Retrieved 16 October 2026. "— " = not found in official sources we checked; absence is **not** proof of absence.

| Capability | Peec | Profound | Scrunch / Sitecore | GEO agencies (L3) | SignalGEO v1 claim |
|---|---|---|---|---|---|
| Cross-engine prompt sampling, mentions/citations/sentiment | Yes [V-V] | Yes [V-V] | Yes [V-V] | Yes, via tools | Yes |
| **Ranked, evidence-backed action list** | **Yes — Actions, all plans, opportunity score 1–3** [V-V, changelog 13 Oct 2026] | **Yes — Opportunities + Aim** [V-V] | **Yes — AEO opportunities with "projected lift" (est. pp improvement in citation rate) + recommendation per opportunity** [V-V, official Sitecore docs] | Analyst judgement | Claimed open → **FALSE** |
| **Earned-media / third-party actions recommended** | **Yes — "earned actions such as getting listed, pitching editorial, and growing reviews"; fact-checking actions name contradicting source pages; Sources surfaces "third-party channels worth working with"** [V-V] | **Yes — "opportunities to secure earned media placements at highly cited sources"; FactCheck traces claims to publishers, drafts a personalised correction per publisher, tracks which updated** [V-V] | Partly — Insights "actionable tips"; citation monitoring [V-V] | **Yes — this is the core of the retainer** [V, published pricing + workstream tables] | Claimed open → **FALSE** |
| **Content optimisation / drafting in-product** | **Yes — content optimizer: in-app editor, accept/edit/reject/revert per suggestion, passage-level rework; feature pages, articles, listicles** [V-V] | **Yes — Agents/Sheets draft, refresh, translate, generate FAQs; templates marketplace** [V-V] | **Yes — Content Enrichment and Content Transformation recommendations, applied in Page Builder** [V-V] | Yes, by humans | Claimed open → **FALSE** |
| **Approval-bound publishing into the client's CMS** | Yes — "Nothing changes without your approval"; atomic edit API (up to 50 passages, all-or-nothing) [V-V, docs.peec.ai API changelog] | **Yes — Agents read/write WordPress, Sanity, Contentful, Framer; "Stage everything, do not publish" → "All staged as drafts, nothing live"** [V-V] | **Yes — apply or decline each AEO optimisation in Page Builder; AXP serves agent-optimised content at the edge** [V-V] | Yes — with client sign-off | Claimed open → **FALSE** |
| **Agent layer with context/memory/skills** | Yes — Peec Agent: user/project/company context, file uploads, 20+ MCP connectors (Notion, Linear, DataForSEO), 30 skills incl. **prompt auditor that flags self-favouring prompts**, intelligence tiers [V-V] | Yes — AI Marketer (Aim) + Agents on schedules/triggers, Context Manager, Knowledge Bases (Notion, Google Drive), reasoning shown per run [V-V, blog 16 Oct 2026] | Partly — enterprise governance, RBAC, audit logs [V-V] | No | Claimed partly open → **FALSE** |
| **First-party analytics join (GA4 / GSC / logs / revenue)** | **Yes — AI referrals connects Google Analytics: sessions, engaged sessions, conversions and revenue by assistant/landing page/country/device; "My website" with Google Search Console (early access); Vercel, Cloudflare, AWS CloudFront, WordPress log integrations; Power BI + Looker Studio** [V-V, changelog 11 Sep & 13 Oct 2026 + press release] | Yes — Agent Analytics (server-side AI traffic) [V-V] | Yes — Agent Traffic [V-V] | Only where the client shares data | Claimed open → **FALSE** |
| Site/technical readiness checks (sitemaps, `llms.txt`, schema, crawlability) | Yes [V-V] | Yes [V-V] | Yes — Site Optimization / site diagnostics [V-V] | Yes | Not claimed |
| Paid AI-search placement | — | **Yes — "captures the AI search demand you cannot earn organically": finds prompts where you never appear, writes sponsored-answer creative, stages the campaign for approval** [V-V] | — | Some | Not claimed |
| Machine-readable page delivery to agents | — | — | **Yes — AXP at CDN/edge, "200× token efficiency", vendor-claimed +364% brand presence for Akamai** [V-VENDOR-CLAIM; the case number is unverified] | No | Not claimed |
| **Published statistical methodology** | **PARTLY YES — this is a correction to v2.** Peec published "The key to prompt tracking" (29 Sep 2026): the **Wald confidence interval**, the **rule of three** ("how far off you can be = 3 ÷ number of runs"), ±10 pp requires ~100 runs and ±5 pp ~400, four times the runs for twice the precision, change detection depends on runs not prompts, and worked examples (50 runs/day → daily changes below 12.4 pp may be chance; 350 weekly → 4.7 pp; 1,500 monthly → 2.3 pp), computed from **~120 million chats, Feb–Aug 2026** [VERIFIED, vendor blog]. Third-party audits however find the **product output** carries no intervals or sample sizes: "Neither publishes confidence intervals or sample sizes" (Popsight, Apr 2026); "**Zero of the 14 disclose run-to-run variance**" (pepper.inc, Sep 2026); "Peec, Profound and Conductor document **one run per prompt per model per day**" (Ranketta, Sep 2026) | **No** found; blog "acknowledges variability but no sample sizes or CIs published" | **No** found; publishes "projected lift" with no stated uncertainty method | **No** — and one agency explicitly warns against guaranteed mentions | **Claimed open → NARROWED FURTHER.** What survives is not "we publish the math" (Peec does) but "we **report** n, intervals, per-surface separation and **extraction accuracy (F1, κ)** in every deliverable, and take ≥5 controlled runs per prompt per window instead of one run per day" |
| **Human-executed off-site work as a managed monthly service** | No — "It identifies the opportunity; your team still executes it" (third-party review of Peec, Aug 2026) | No — agents draft and stage; a human must still pitch and publish externally | No | **Yes — the entire L3 layer** | Claimed open → **FALSE for L3, TRUE only against L2** |
| Vertical specialisation on India-origin global software | No | No | No | A few Indian agencies serve Indian clients; none found specialising in India-origin companies selling to US/UK/EU with USD billing | Claimed open → **SURVIVES as a wedge, not a moat** |
| Collection method, and whether it is disclosed | **UI scraping of chat interfaces for the core engines, "documented openly"; API for the extra Enterprise models (Claude, GPT-5 Search, DeepSeek, Qwen, Mistral)** [PARTIALLY VERIFIED — two independent secondary sources citing Peec's own tracking-method documentation; primary page not retrieved]. One run per prompt per model per day | **"Captures answers directly from consumer front ends rather than APIs"** plus **consumer panels** for prompt volume [PARTIALLY VERIFIED — two independent sources citing Profound's collection-methodology page] | Not stated in sources checked | "Not documented"; described as "neutral, non-personalized querying" with **undocumented transport** (Otterly) | Tools-dependent | **This is a trade-off, not a clean advantage.** Their consumer-interface collection has higher ecological validity at scale; ours (official APIs + human capture) is ToS-compliant and auditable but narrower, and it cannot reach the run counts they achieve. Our honest claim is **compliance, auditability and measured variance** — not superior fidelity |

**Traction context [VERIFIED, press release 13 Oct 2026, citing Ramp Rate data]:** Peec ARR **$15M**, market
adoption **quadrupled to 19%**, second-highest enterprise adoption at **21%**, New York office opened. Scrunch:
"trusted by over 500 companies" [V-VENDOR-CLAIM], acquired by Sitecore 3 Jun 2026 (~$225M reported by Bloomberg,
unconfirmed). Profound: $180M Series D at $1.8B valuation (15 Sep 2026), ~$335M raised total; customers include
Walmart, Comcast, Estée Lauder, MongoDB.

---

## 3. What is actually open (and what is not)

**Closed as of October 2026 — do not build here, do not pitch here:**
1. Prompt-level visibility measurement and scoring.
2. Ranked, evidence-backed opportunity lists, including **earned-media** opportunities.
3. Third-party citation-source mapping ("which pages gate this query cluster"). Peec's Sources and Actions,
   Profound's citation categories and earned-media opportunities, Scrunch's Insights and Ahrefs/Semrush citation
   reports all do versions of this.
4. In-product content optimisation with per-suggestion accept/reject/revert.
5. Approval-bound publishing into a client CMS, staged diffs, atomic edits.
6. First-party analytics joins, including conversions and revenue from AI referrals.
7. Fact-checking that identifies contradicting third-party pages and drafts corrections.
8. Agent layers with brand context, memory, skills and MCP-style connectors.

**Open, narrowly, and each with a caveat:**
| Opening | Evidence it is open | Caveat that limits its value |
|---|---|---|
| **Human execution of the off-site workstream for mid-market India-origin vendors, at INR/USD mid-market prices** | L2 vendors explicitly leave execution to the customer's team; L3 agencies price at $997–$30,000/mo and mostly target US/EU clients or Indian domestic clients | It is a **service** business: capacity-capped, 5 clients/FTE at full scope (`12` §3), no software leverage, and any agency (or a white-label PR partner) can copy the offer in a quarter |
| **Published measurement honesty** — protocol, n, Wilson intervals, κ, per-surface separation, rule-of-three upper bounds, disclosed extraction error rates | No vendor protocol found; one agency publicly refuses to guarantee mentions; Otterly publishes stability research that argues against naive scoring | It is a **credibility** asset, not a feature: it wins trust in regulated/cautious verticals, but it also *limits* what we can claim — honest intervals at n = 5 are ±0.33 (`13` §6), which many buyers will read as "you don't know either" |
| **Vertical/network wedge** — India-origin B2B software selling to US/UK/EU, ~480 accounts (`10` §1) | No L2 vendor targets this segment; Indian L3 agencies mostly serve domestic clients | Replicable by anyone with a list and a dialler; a wedge, not a moat |
| **ToS-compliant, disclosed collection** | At least one leading vendor reportedly collects by scraping consumer UIs [NOT YET VERIFIED] | Matters to security-conscious and enterprise buyers; invisible to most SMB buyers; and it may *disadvantage* us on data richness versus competitors who sample consumer surfaces at scale |

**Not open, and we should stop pretending otherwise:** any dataset-based moat. Incumbents hold 2B+ prompts,
30M+ cited sources and 19% market adoption. We cannot out-data them, and pooling client data across accounts
would raise consent and confidentiality problems we have not solved.

---

## 4. The market's published price for exactly what we proposed

This is the most useful competitive finding in v2, because it is simultaneously a threat and a gift.

| Offer in market | Price | Source (retrieved 16 Oct 2026) |
|---|---|---|
| "GEO and AEO done for them, measurement included" | **$497 one-time audit + $997/mo** | SourceRank AI (Aarhus) via a B2B agency roundup, 12 Oct 2026 |
| "Tool plus contractor": monitoring tool + a contractor executing 2–6 pieces/month, measurement included | **$2,000–$5,000/mo** | Klarivo, "Done-for-You GEO Agency: What a Retainer Buys", 17 Aug 2026 |
| Per-pillar GEO or fully managed | **$2,500/mo per pillar · $5,500/mo fully managed** (6-month term) | MADX Digital via Scalerrs roundup, 30 Sep 2026 |
| Multi-surface citation building (Reddit, YouTube, Wikipedia, listicles) + SEO/content/links | month-to-month, custom | Scalerrs (self-described), same roundup |
| Digital PR for GEO (research production + distribution + citation tracking) | **$3,000–$10,000/mo mid-market; $25,000–$30,000+/mo enterprise** | DemandLocal agency playbook |
| PR-native GEO (earned media + schema + citation tracking) | **from $12,000/mo** | Crackle PR |
| Done-for-you brand placements, self-serve checkout | per-placement, monthly report | Respona |
| Typical GEO agency retainer | **$5,000–$20,000/mo** | multiple 2026 roundups |

Two conclusions:

1. **Willingness to pay well above ₹40,000/month is documented in the market.** Published done-for-you-with-
   measurement offers cluster at **$997–$5,500/month**. Our Tier B/C prices ($1,000–$1,500) sit at the bottom
   of that band — which is where an India-cost-structure operator belongs, and which makes the ₹40,000 (~$421)
   assumption look like under-pricing rather than realism. (Still **[NOT YET VERIFIED]** for *our* specific
   buyers; Stage 1's price ladder tests it.)
2. **Our offer is not novel, so it must be better on a dimension buyers can verify**: segment expertise,
   measurement honesty, price, or responsiveness. "We close the loop" is not one of them — three funded vendors
   close the loop in software today.

Two constraints the agency evidence adds to our own delivery model:
- **95% of AI-cited links come from non-paid sources** (Muck Rack analysis of 1M+ AI citations, cited by
  DemandLocal). Paid placement does not buy citations. Our earned-media work must be genuine editorial and
  community value — which is exactly what integrity rules 9–10 already require, now with market evidence behind
  it.
- A **Stacker + Scrunch study (Mar 2026)** reports a median **239% lift in brand citations** from distributing
  the same article across third-party news sites [VENDOR/AGENCY-CLAIMED, not independently verified]. This is
  the tactic an aggressive competitor will sell. At scale it is syndication spam. **We will not sell it without
  an explicit written ethics ruling, and we will disclose our position when prospects raise it.**

---

## 5. Commoditization and threat register (updated)

| # | Risk | Status | Severity | Mitigation |
|---|---|---|---|---|
| R1 | Measurement becomes free (GSC generative-AI report already free worldwide; HubSpot free Grader; Ahrefs free checker) | **Demonstrated** | 4 | Never sell the number; sell executed work + disclosed uncertainty |
| R2 | Prompt sampling is trivially reproducible ($5–$14 per 1,000 Perplexity requests) | **Certain** | 5 | Measurement is a cost of delivery, not a product |
| R3 | **Platforms add execution** | **Demonstrated — Peec Actions/content optimizer/agent 13 Oct 2026; Profound CMS write + sponsored answers; Scrunch/Sitecore in-CMS apply/decline** | **5** | Compete only where software cannot go: human pitching, relationships, judgement, accountability, vertical knowledge |
| R4 | Provider restriction / API churn (OpenAI ToS bar programmatic extraction outside the API; "OpenAI Search API" renamed **OpenAI Luna**; Sonar deprecation notices; new models monthly) | **Demonstrated** | 4 | Multi-surface protocol; licensed tooling absorbs vendor churn; disclose limits |
| R5 | "GEO" becomes a dirty word through over-promising vendors | Practitioner scepticism loud in our register | 3 | Publish the protocol and our own failures; refuse guarantees |
| R6 | Labour is the bottleneck (5 clients/FTE at Tier C) | **Now quantified** (`12` §3) | 4 | Bound scope contractually; step clients down to Tier A when stable |
| R7 | Agencies copy us / already do this | **Demonstrated — L3 published prices and workstream tables match our v1 proposal** | 5 | Segment focus + measurement credibility + speed; consider selling *to* agencies as a white-label measurement/QA layer |
| R8 | **White-label digital-PR suppliers remove the scarcity of the earned-media workstream** — any agency can resell it tomorrow | **Demonstrated** (DemandLocal playbook) | 4 | Our value must be judgement, verification and accountability, not access to pitching capacity |
| R9 | Legal/ethical incident (fake reviews, astroturfed communities, an agent publishing a false claim about a client's security posture) | Low probability, existential impact | 5 | Integrity rules 7–11, 24; verified-fact sourcing per recommendation; staged diffs; written refusal policy |
| R10 | **Our own competitive intelligence goes stale in weeks** (v1's central error) | **Demonstrated** | 4 | Monthly changelog watch on Peec, Profound, Scrunch/Sitecore, Semrush, Ahrefs, HubSpot, Google Search Central; every competitive claim carries a retrieval date and is re-checked before external use |

---

## 6. Differentiation theses v2

**Thesis 1 — "Evidence-grade GEO for India-origin global software companies."** *(positioning, retained, weakened)*
What it is: a published measurement protocol (n, runs, Wilson intervals, κ, per-surface separation, disclosed
extraction error rates, rule-of-three upper bounds), executed on-site and off-site work with human approval, and
a client-verifiable three-tier evidence report — at $1,000–$1,500/mo with India-based delivery.
*Strength:* attacks the pains that survive (no capacity, no verification, no accountability); credible to
cybersecurity and regulated buyers; hard to fake because the protocol is public and the numbers are
reproducible by the client under `13` §7.
*Weakness:* "evidence-grade" is a claim until we publish the protocol **and** the intervals, and honest
intervals at feasible n are wide — which can read as incompetence to a buyer who has been sold certainty.
Geography is not a moat. Agencies can copy the pitch in a quarter.
*Invalidated if:* ≥4 of 5 Stage 1 buyers prefer the buy-it-yourself option (`08` §7.1), or treat intervals as a
reason not to pay, or an L2 vendor begins **reporting** intervals, sample sizes and extraction accuracy in the
product output. **Partial invalidation has already occurred:** Peec published Wald-confidence-interval and
rule-of-three methodology with run-count guidance on 29 Sep 2026 (register X17-1). What survives is narrower
than v2 claimed — not "we publish the math" but "we report n, intervals, per-surface separation and measured
extraction accuracy (F1, κ) in every deliverable, and take ≥5 controlled runs per prompt per window instead of
one run per prompt per day" (X17-1/X17-2/X17-3). A third-party audit of 14 platforms found **zero disclose
run-to-run variance** in their output, which is the part of the claim that still holds.

**Thesis 2 — "The third-party citation-gateway engine."** *(v1's recommended core — **WITHDRAWN as a moat**)*
The underlying market fact is intact: ~85% of commercial brand discovery happens on third-party pages, brands
are ~6.5× more likely to be cited via third parties than their own domain, ~90% of those mentions come from
listicles/comparison/review roundups (AirOps), and 95% of AI-cited links are non-paid (Muck Rack). That is why
the work exists. It is **not** why the work would be defensible: Peec, Profound, Scrunch, Ahrefs and Semrush all
already map cited third-party sources and recommend earned-media actions, and L3 agencies execute them for
$997–$30,000/mo. Retained only as a **delivery capability we must have**, not as a differentiator.
*Invalidated:* already — by official vendor documentation (see §2).

**Thesis 3 — "AI-search revenue attribution layer."** *(retained as a reporting layer only)*
Peec already joins Google Analytics conversions and revenue to AI referrals, and GSC's generative-AI report is
free. A CFO-facing joined report is therefore **not** a product. What survives is the discipline: non-causal
language, three evidence tiers, and refusing to claim incremental revenue we cannot attribute. Use it inside
Thesis 1; never as the promise.

**Thesis 4 (new) — "The accountable operator for a segment the platforms do not serve."** *(recommended core)*
What it is: we are not a tool and not a generic agency. We are a small, named, accountable team that (a) knows
India-origin software companies' actual product facts, buyer geography and category dynamics, (b) runs the
earned-media and on-site work end-to-end with human verification of every claim, (c) publishes its measurement
protocol and its uncertainty, (d) bills in INR or USD at $1,000–$1,500/mo — the bottom of the published L3 band
— and (e) licenses best-of-breed measurement instead of building it.
*Strength:* it is the only position that survives §2 and §3; it needs no capital, no moat and no platform; it can
be cash-positive with one client (`12` §5); and its credibility comes from disclosure rather than from a
proprietary dataset we do not have.
*Weakness:* **it is an agency.** Ceiling ~$60k–$375k ARR bootstrapped in 24 months, $2M ARR only with 12–21
delivery FTEs (`12` §8). No software leverage, no compounding data asset, valuation as a services business.
*Invalidated if:* buyers choose tools over us (Stage 1 §7.1), or if the L3 price floor collapses because
white-label PR suppliers commoditise delivery below our cost.

**Recommended combination for v2: Thesis 4 as the business, Thesis 1 as the positioning and credibility
mechanism, Thesis 3 as the reporting discipline, Thesis 2 downgraded to a required delivery capability.** The
moat question stays **open and honestly unanswered** — that is a finding of Phase 1, and the founder should
decide whether a moat-less but cash-generating niche service is the company they want before we spend another
phase on it.

---

## 6.1 Positioning statement under test (added 16 Oct 2026, condition 7 of the founder's decision)

**Removed from every SignalGEO document, effective immediately:** any claim of a unique or proprietary citation
dataset, a first-to-market action engine, or an exclusive execution workflow. The verified reason is in §2:
Peec ships source analytics with source classification, gap analysis enumerated "by source, domain, subdomain,
URL, and host", and recommended actions "grouped by earned and owned", with CSV/MCP/API export from
$95–$495/month (agency plans from €205/month); Profound sells earned-media opportunities and publisher-correction
drafting; Scrunch/Sitecore publishes projected citation lift with in-CMS apply-or-decline.

**The proposition now under test — a [HYPOTHESIS] until a buyer demonstrates willingness to pay:**

> **"Specialized, evidence-backed AI-search optimization delivered as a managed service for B2B companies that
> lack sufficient execution capacity."**

| Component | Must be true | Falsifier | Test |
|---|---|---|---|
| lack sufficient execution capacity | Buyers have identified work they cannot staff | ≥3 of 5 name no unfinished work, or have spare internal hours | Buyer question 5 |
| managed service | They will pay us rather than license a tool | ≥3 of 5 choose Option A (software) or B (agency) | Three-option card |
| evidence-backed | Disclosed intervals and error rates help the sale | Buyers read uncertainty as incompetence | Co-observation reaction |
| specialized | Segment/vertical focus is worth paying for | No perceived difference vs a $997/month generalist | S1 vs S2 vs S4 responses |
| price | $1,000–$1,500/month is inside an approvable line | First "no" at or below ₹40,000 for ≥3 of 5 | Price ladder |

**The strongest published counter-argument found on 16 Oct 2026**, from a competitor's own content:
*"Most teams under $3,000/month do better with one tool plus in-house fixes than with a thin retainer."*
It is recorded in the evidence register (§16) and built into the buyer conversation as the objection we expect
rather than the objection we hope to avoid.

## 7. Answers to the brief's competitive questions, revised

- **"Why wouldn't traditional SEO agencies simply offer the same service?"** They already do, at published
  prices from $997/mo to $30,000/mo, with digital PR as the core workstream, and they can white-label the
  earned-media execution from specialist suppliers. Their constraint is not capability. It is **measurement
  discipline and disclosure** — an agency billing $5,000/mo has little incentive to publish confidence intervals
  that reveal its numbers are noisy, or to tell a client that its own site is the smallest lever. That is a real
  but narrow opening, and it closes the moment a platform publishes a protocol.
- **"How will we compete with established GEO monitoring tools?"** We will not compete with them — **we will
  buy them.** v2's cost model (`12` §4.1) shows building our own measurement is more expensive per client than
  licensing until N ≈ 25–30. Our competition is with the *service* layer, and our leverage against tools is that
  tools leave execution to the customer's team.
- **"What is our real proprietary advantage?"** **None identified.** Candidates, ranked by how badly they fail:
  (1) longitudinal gateway data — incumbents hold 2B+ prompts, we cannot compete; (2) joined first-party client
  data — Peec already joins GA4 revenue; (3) delivery IP (templated audits, validated extractors, fact-
  verification workflow) — real but replicable in a quarter; (4) India cost structure applied to USD-priced work
  — real, durable for a while, and already used by Indian agencies and by white-label suppliers; (5) segment
  network and trust — real, non-transferable, and the only one that compounds with reputation rather than data.
  **Items 4 and 5 are the business. They support a good small company, not a venture-scale one.**
- **"What stops a client from doing this themselves?"** Time and accountability, not information — Peec will tell
  them exactly what to do for €180/month. Our answer must be "we do it, we verify every claim against your
  product facts, and we show our uncertainty," not "we can see something you cannot."

---

## 8. Verification gaps carried to Phase 2

| # | Gap | Why it matters |
|---|---|---|
| CG-1 | Live Peec pricing (one Oct-2026 comparison says pricing is "not shown publicly"; earlier sources give $95/$245/$495 and €70/€180/€360) | Determines our tooling COGS (`12` A-9) |
| CG-2 | Live Profound brand pricing after the mid-Sep 2026 removal of $99/$399 self-serve tiers | Same |
| CG-3 | Scrunch/Sitecore current packaging post-acquisition and whether AXP requires Sitecore CMS | Determines whether L2 execution is reachable for non-Sitecore mid-market clients |
| CG-4 | Whether Peec's collection method is consumer-UI scraping (attributed to Peec support in 2025, third-party) | Our ToS-compliance positioning depends on not misstating a competitor's method |
| CG-5 | Do Peec/Profound/Scrunch publish any measurement-uncertainty methodology? | The last remaining pillar of Thesis 1 |
| CG-6 | Hands-on trial of Peec Actions and Profound Agents: do the earned-media recommendations name real, actionable targets? | Vendor documentation proves intent, not quality; this is the "software-assisted vs managed delivery" question in practice |
| CG-7 | Actual delivery hours and quality of a $997/mo or $2,500/mo L3 competitor | Tells us whether the low end is under-served or under-delivered |
| CG-8 | Do white-label digital-PR suppliers serve India-origin clients at INR prices? | If yes, our cost advantage narrows further |
| CG-9 | Independent verification of the Stacker+Scrunch "239% citation lift" syndication claim | Determines whether we must compete with a tactic we consider spam |
| CG-10 | Is "AthenaHQ now operating as Otterly" true (asserted by one agency's self-published list)? | Conflicts with our register; affects L1 pricing evidence |
