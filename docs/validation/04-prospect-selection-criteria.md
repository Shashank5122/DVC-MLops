# Prospect selection criteria + cold-outreach fallback

**Condition 3 of the founder's decision of 16 Oct 2026:** retain the segment mix, do **not** require warm-network
introductions, prepare evidence-based selection criteria and a cold-outreach fallback. Final list and all
external outreach are approved separately (gates O1/O2).

Internal document. Uses only public sources. Nothing here authorises contact.

---

## 1. Cohort design

Five candidates, deliberately mixed so the experiment can discriminate between segments — `05` §6.1 shows the
post-correction ICP ranking collapses to a 0.08 spread (S1 3.70 = S2 3.70 > S4 3.62), so buyer responses must
decide the beachhead, not the spreadsheet.

| Slot | Segment | Count | Purpose |
|---|---|---|---|
| 1–3 | **S1** — India-headquartered B2B SaaS selling to US/UK/EU (Series A–C, roughly $1M–$50M ARR) | 3 | Primary hypothesis; three data points allow within-segment comparison of the three options |
| 4 | **S2** — Indian cybersecurity product vendor selling globally | 1 | Higher severity, regulated-adjacent buyer; tests whether "evidence-backed" sells better where a false claim is expensive |
| 5 | **S4** — US/EU mid-market B2B SaaS (sold remotely from India) | 1 | Tests the USD-billing ARPU hypothesis (`12` §5: ~3.4× faster founder break-even on identical COGS) |

**Exclusions that apply across the cohort:** no two candidates may be direct competitors of each other
(confidentiality and trust); no AI-search/GEO/SEO vendor (conflict of interest and distorted responses); no
company in active public crisis or litigation that would make association risky; no company whose category is
dominated by regulated medical or financial-advice claims we are not yet equipped to verify.

---

## 2. Hard requirements (all must hold; each checkable from public sources)

| # | Requirement | How it is checked publicly | Why it matters |
|---|---|---|---|
| R1 | B2B software **product** company (not services-only, not an agency) | Site, pricing page, product docs, G2/category listing | Service firms buy differently and churn differently |
| R2 | India-headquartered (S1/S2) **or** US/EU mid-market (S4) | HQ on site/LinkedIn/Crunchbase; Tracxn or DSCI listing for Indian firms | Segment definition |
| R3 | **Sells to US/UK/EU buyers** | English site, USD or multi-currency pricing, named Western customers/case studies, Western time-zone coverage in careers or support pages | The pain is being invisible to *Western* AI answers; a purely domestic seller has a different problem |
| R4 | **Research-led category** where buyers compare options | dev tools, data/AI infrastructure, martech, sales tech, HR tech, fintech infrastructure, cybersecurity products | G2's population: 51% of B2B software buyers start in AI chat; comparison categories are where citations decide shortlists |
| R5 | Visible marketing function | ≥1 person with a marketing/growth remit on the team page or LinkedIn; blog or changelog updated within 90 days | No marketer ⇒ no budget line ⇒ no buyer for our service |
| R6 | **Named, reachable decision-maker** | Founder, CMO, VP/Head of Marketing, Head of Growth or Demand Gen, findable via the company's own site, team page, LinkedIn or public conference speaker lists — **without purchasing contact data** | Gate O1 requires a name for every candidate |
| R7 | Substantive owned content base | ≥20 indexable pages, or a documented product/comparison/alternative page set | On-site optimisation needs something to optimise; also predicts gateway exposure |
| R8 | **One true, checkable AI-visibility finding exists** | We run a small pre-contact probe (public prompts only, no client data) and confirm a specific, verifiable observation — e.g. a named competitor recommended for a category query while the candidate is absent, or a factual claim about them that is wrong | This is the outreach hook *and* the diagnostic's entry point. Without it we have nothing honest to say |
| R9 | No incumbent exclusivity barrier we would breach | Public information only; if they visibly retain an agency we still include them (that tests switching), but we never ask them to share confidential agency materials | Ethics and integrity rule 24 |
| R10 | Data-handling acceptable | They can consent to us storing raw observations about their public brand; no confidential data required to run the diagnostic | Multi-tenant isolation and consent start at prospecting |

---

## 3. Scoring sheet (8 criteria × 1–5; threshold ≥ 28/40)

| Criterion | 1 | 3 | 5 |
|---|---|---|---|
| **C1 Segment fit** | Outside S1/S2/S4 | Adjacent | Exactly S1/S2/S4 as defined |
| **C2 Reachability of the named buyer** | No plausible route | LinkedIn only, cold | Public email or highly active public profile |
| **C3 Severity signal** | No sign AI search matters to them | Generic "AI" mentions | Public post/job/talk showing they are actively worried about AI-search visibility |
| **C4 Budget evidence** | No marketing spend visible | Small team, some content | Visible paid acquisition, recent funding, or published marketing roles |
| **C5 Content base** | Brochure site | Some blog | Deep comparison/alternative/docs content that AI would plausibly cite |
| **C6 Category competitiveness** | Category AI rarely answers | Moderately covered | Category with active listicles, G2 pages, Reddit/YouTube coverage — i.e. gateways exist to win |
| **C7 Confidentiality risk** | Competitor of another candidate, or sensitive claims | Manageable | Clean |
| **C8 Finding strength** | No true finding available | Weak/generic finding | Specific, checkable, commercially uncomfortable finding |

**Selection procedure:** agent builds a longlist of 20 with scores and evidence links → founder reviews and
selects 5 respecting the slot mix → any candidate scoring < 28 is dropped even if the mix suffers (record the
substitution). **Approval gate O1 covers the final five names; nothing is sent before O2 approves the text.**

---

## 4. Cold-outreach fallback (no warm introductions)

Channel order — use the first that yields a named, reachable buyer; log which channel produced each reply.

| # | Channel | Method | Notes |
|---|---|---|---|
| 1 | **LinkedIn direct** | Message to the named buyer containing **one true finding** about their brand, no pitch, no price | Highest signal; keep under 90 words; link nothing that requires a login |
| 2 | **Published email** | Address from the company's own site, team page, press page or public speaker bio | **No purchased lists, no scraped private data, no enrichment vendors** |
| 3 | **Public community** | SaaSBoomi directory and events, DSCI/Nasscom events and member lists, Product Hunt launch pages, relevant subreddits and forums → engage substantively first, then a direct message | Two-touch minimum before any ask; never post a candidate's finding publicly |
| 4 | **Reply to their own content** | A specific, useful reply to a blog post, changelog entry or LinkedIn post they published | Slowest, highest trust |

### Message rules (binding)

1. **One true, checkable finding** per message, stated with its method ("5 runs on Perplexity on 14 Oct, logged
   out, US region") and its limit ("n = 5, so treat this as directional").
2. **No price in message one.** Price appears only in a conversation or an approved proposal (gate D4/D5).
3. **No claim we cannot source.** No invented statistics, no market-size numbers, no competitor disparagement,
   no implication that a competitor's product is deficient unless we hold a dated official source.
4. **No guarantee** of placement, ranking or citation. Integrity rule 7.
5. **Honour opt-out immediately** and permanently; maximum **two** follow-ups, then stop.
6. **Every send logged**: date, channel, recipient name and role, company, segment slot, message version hash,
   reply, and outcome. The log is the denominator for all conversion claims.
7. **Never state or imply that we already work with a comparable client.** We do not.
8. **No attachment or link that requires the recipient to create an account.**

### Expected conversion **[HYPOTHESIS — we have zero observations]**

| Step | Assumption | Basis |
|---|---|---|
| 20 sends → replies | 25–40% (5–8) | Category norms for hyper-personalised B2B outreach; **no data of our own** |
| Replies → conversations | 60–75% (3–5) | The finding is about *their* brand, which raises reply-to-meeting conversion |
| Conversations → priced-proposal requests | unknown | This is what Stage 1 measures |
| Conversations → signed/deposited pilot | unknown | The decisive number (evidence tier T1) |

If batch 1 (10 sends, day 3) produces **fewer than 2 replies by day 7**, the finding quality or the channel is
wrong — rewrite and re-target a fresh 10 rather than concluding anything about demand for the service. That is
gate G1's purpose, and it is a *messaging* conclusion, not a *market* conclusion.

---

## 5. Pre-contact probe (R8) — how the finding is produced without spending or contacting

- Public prompts only, phrased as a buyer would phrase them; **no candidate-confidential information** is used
  or needed.
- 3–5 prompts × 3 runs on one free/low-cost surface (within the S2 API cap) or from an already-approved vendor
  trial, **after** gates S1a/S2 clear.
- Record: prompt hash, surface, model id, timestamp, region, retrieval evidence, raw response.
- The finding must be **true, specific and checkable by the recipient in under two minutes**, and must be stated
  with its n and its uncertainty. If the probe yields nothing honest, the candidate is dropped — we do not
  manufacture a hook.

**Order of operations:** criteria → longlist (20, scored, with evidence links) → **O1 approval** → probe on the
selected 5 → message drafts → **O2 approval** → send batch 1.
