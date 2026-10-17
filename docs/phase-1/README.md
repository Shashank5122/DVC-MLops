# Phase 1 — Market research & problem validation

**Status: v2 complete, awaiting founder decisions D-1 … D-6** (`00-decision-memo.md` §I).
Started and finished 2026-10-16; v2 issued the same day after the founder withheld approval of v1 and
required seven corrections. **No application code was written in this phase, per the brief, and none is
proposed by the recommendation.**

## Read in this order

| # | File | What it gives you |
|---|---|---|
| 0 | [`00-decision-memo.md`](00-decision-memo.md) | **Start here (v2).** A–I response format, the six decisions needing approval, and the closing four |
| — | [`11-correction-log.md`](11-correction-log.md) | **Read second.** C-01 … C-12: each v1 claim as written, the correction, the evidence (mostly official vendor documentation), and every file affected |
| 12 | [`12-economics-v2.md`](12-economics-v2.md) | **Authoritative economics.** Definitions and formulas, capacity model, COGS (buy vs build), margin grid, **operating cash vs founder-compensated break-even**, CAC/payback/LTV, 24-month scenarios, sensitivity, pricing verdict, 8 financial risks |
| 13 | [`13-measurement-reproducibility-protocol.md`](13-measurement-reproducibility-protocol.md) | **Authoritative protocol.** Extraction accuracy vs measurement reproducibility, 14 recorded factors, gold-set validation, the statistics (Wilson, κ, Jaccard, RBO, rule of three, power), prospect co-observation, decision bands, reporting and publishing rules |
| 8 | [`08-validation-plan-v2.md`](08-validation-plan-v2.md) | **Staged, gated plan.** Stage 1 = 14 days, 98 founder-hours, $408 cash, 5 diagnostics, 5 buyer conversations, 2 agency interviews, hour/cost logging, ≥1 priced pilot proposal, gates G0/G1/G2 |
| 9 | [`09-competitive-threats.md`](09-competitive-threats.md) | **v2 competitive picture.** Four populated layers, verified capability matrix with retrieval dates, published managed-service prices, R1–R10, differentiation theses v2, 10 gaps |
| 1 | [`01-executive-research-summary.md`](01-executive-research-summary.md) | Problem statement, demand evidence, WTP hypotheses, viability — with a v2 correction banner and corrected §5–§9 |
| 2 | [`02-evidence-register.md`](02-evidence-register.md) | ~90 sourced findings in 15 sections. **§13 execution-layer capability (official vendor sources), §14 managed-service market prices, §15 Indian labour rates**; contradictions recorded; 20 verification gaps |
| 3 | [`03-market-assessment.md`](03-market-assessment.md) | Answers the brief's ten Phase-1 market questions in order |
| 4 | [`04-pain-point-map.md`](04-pain-point-map.md) | Nine pains with customer voice, evidence, severity, who already solves them — P3 and P4 corrected in v2 |
| 5 | [`05-icp-scoring-and-ranking.md`](05-icp-scoring-and-ranking.md) | Eight segments, nine weighted criteria, arithmetic shown, two sensitivity scenarios, **plus §6.1 post-correction robustness re-score showing the top three collapse to a 0.08 spread** |
| 6 | [`06-assumptions-hypotheses-failures.md`](06-assumptions-hypotheses-failures.md) | A1–A16 assumptions, H1–H12 + H3b hypotheses with falsification signals, pivot branches, `[UNVERIFIED]` list, answers to the brief's 15 challenge questions |
| 7 | [`07-discovery-interview-guide.md`](07-discovery-interview-guide.md) | Discovery script with the **buy-vs-hire card (Q18a)**, the ascending price ladder, the **co-observation card (Q23)**, agency channel interview, scoring sheet and pre-set aggregation rules |
| 10 | [`10-tam-bottom-up.md`](10-tam-bottom-up.md) | **§1 only (account universe) is still valid.** §2–§6 are superseded by `12` and carry a warning banner |

## The one-paragraph version (v2)

Buyer behaviour has verifiably shifted — 51% of B2B software buyers now start research in an AI chatbot more
often than Google, up from 29% a year earlier, and chatbots are the #1 influence on shortlists — and money has
followed, from ~12% of enterprise digital budgets to employer-published roles at $127k–$318k. **But v1's
central strategic claim was wrong.** It said the mid-market execution layer was empty. Official vendor
documentation retrieved on 16 October 2026 shows the opposite: Peec ships ranked actions including *earned*
actions ("getting listed, pitching editorial, and growing reviews"), a content optimizer with
accept/edit/reject/revert, an agent with 30 skills and 20+ MCP connectors, and Google Analytics joins carrying
conversions and revenue — at €70–€360/month, with $15M ARR and 19% market adoption. Profound's AI Marketer
drafts the work and stages it for approval, traces false claims to the publishers repeating them, and writes
into WordPress, Sanity, Contentful and Framer. Scrunch/Sitecore surfaces AEO opportunities with a projected
citation lift that you apply or decline inside the CMS. And the human half of the loop is sold by agencies from
**$997/month** ("GEO and AEO done for you, measurement included"), with white-label digital-PR suppliers behind
them. **SignalGEO therefore has no identified moat — that is a finding of this phase, not a gap in it.** What
survives is a niche managed-delivery service for India-origin software companies selling to US/UK/EU, competing
on accountability, segment knowledge, disclosed measurement uncertainty and price — cash-positive at **one
client**, but needing **5 clients at $1,500/month (or ~30 at ₹40,000)** to pay the founder a market salary,
with a bootstrapped 24-month ARR band of **$61k–$375k** and $2M ARR requiring **12–21 delivery staff**. The
recommendation is therefore narrow and deliberately cheap: **run Stage 1 — 5 real diagnostics, 5 buyer
conversations built around a buy-vs-hire card, a written measurement protocol with a 200-response gold set,
line-by-line hour and cost logging, and at least one priced pilot proposal — in 14 days, for $408 of cash and
98 founder-hours, building nothing.** Expansion to 20 diagnostics is gated on technical credibility, measured
cost control and genuine commercial interest. v1's "let every prospect check our numbers with a single rerun"
test is withdrawn: one rerun is a draw from a distribution whose 95% interval at n = 5 is ±0.33, so we now
score co-observations against a stated interval and separate extraction accuracy from reproducibility
altogether.

## Claim labels used throughout v2

`[VERIFIED]` primary or official source retrieved · `[VERIFIED-VENDOR-CLAIM]` the vendor documents it; we have
not tested it · `[ESTIMATED]` computed by us from stated assumptions · `[HYPOTHESIS]` plausible, untested ·
`[NOT YET VERIFIED]` needs a source or an experiment we have not run.
