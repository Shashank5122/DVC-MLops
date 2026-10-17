# Phase 1 — Customer discovery interview guide

Two instruments: **D1 discovery call (75 min, prospect)** and **D2 channel interview (30 min,
agency owner)**. Plus **D3 internal scoring sheet** so every call produces comparable data rather
than impressions.

> **v2 revision, 16 Oct 2026** (corrections C-05, C-06, C-07 — see `11-correction-log.md`):
> - Volume re-scoped to **Stage 1**: **5 buyer conversations and 2 agency interviews**, not 15 and 5
>   (`08-validation-plan-v2.md`). At n = 5 every percentage is directional; the sheet records counts,
>   not rates, wherever possible.
> - **Q23 "check it yourself right now" is replaced by the co-observation card** in
>   `13-measurement-reproducibility-protocol.md` §7. A single rerun is one draw from a wide
>   distribution (Wilson half-width ±0.29–±0.33 at n = 5), not ground truth.
> - **New Q18a — the buy-vs-hire card.** This is now the most important question in the guide, because
>   Peec, Profound and Scrunch/Sitecore all ship approval-bound execution at €70–€360/month, and agencies
>   sell the same workstream from $997/month (`09` §2, §4). If buyers prefer the tool, our offer is wrong.
> - **Price ladder extended to four steps** and asked in ascending order, recording the first "no".
> - Segment mix for the 5 diagnostics/conversations: **3 × S1, 1 × S2, 1 × S4** (`05` §6.1).

Rules for both instruments:
- Ask about the past, not the future. "What did you do last quarter?" beats "would you buy X?"
- Never pitch in the first 20 minutes. The pitch is a *reaction* to what we hear.
- Ask the price question before revealing our price.
- Log every answer in the scoring sheet within 1 hour; memory is not data.
- If they say "that's interesting," that is a **no**. Only three things count as a yes: a calendar
  commitment, an introduction to the economic buyer, or money.

---

## D1 — Discovery call with a prospect (founder / Head of Growth / CMO / VP Marketing)

**Target (v2, Stage 1): 5 calls** — 3 × S1 (India-origin global B2B software), 1 × S2 (Indian cybersecurity
product vendor), 1 × S4 (US/EU mid-market SaaS, sold remotely from India). The mix is deliberate: `05` §6.1
shows the post-correction segment ranking collapses to a 0.08 spread (S1 3.70 = S2 3.70 > S4 3.62), so the
conversations must discriminate between segments rather than confirm one. Stage 2 adds 10 more (including S5
agency-channel and S6 controls) **only** if gate G2 passes. Each call pairs with one delivered diagnostic.

### Block 1 — Context and current motion (5 min)
1. Walk me through how a buyer actually finds and evaluates you today, from first touch to signed
   contract. What does that look like in your last three deals?
2. Where does your pipeline come from right now, by source? What share is organic search?
3. Who owns that number, and what are they measured on?
4. What's your marketing headcount and roughly what does your search/content budget look like per
   month? *(Anchor for WTP. Accept a range.)*

### Block 2 — The AI-search experience, asked as behaviour not opinion (8 min)
5. Have you or anyone on your team ever typed your own category into ChatGPT, Perplexity or Gemini
   to see what comes back? What happened when you did? *(If never: that is the single most
   important data point of the call. Note it.)*
6. When you did — was the answer accurate about your product? What was wrong or missing?
7. Have you ever lost a deal, or had a prospect arrive misinformed, where you suspect AI answered
   something about you or a competitor first? Tell me about that specific deal.
8. Have you seen AI-referral traffic in your analytics? What do you do with it today?
9. In your last 10 won/lost deals, did anyone mention that they'd asked an AI assistant about you
   or your category? How would you know either way?

### Block 3 — Current spend and what's been tried (5 min)
10. What SEO or content agencies/tools do you pay for today, and what does each cost per month?
11. Have you tried anything specifically for AI search — a tool, an agency, an in-house experiment?
    What was it, what did you pay, and why did it stop (or continue)?
12. Have you looked at Peec, Otterly, Semrush's AI toolkit, Profound, HubSpot's grader, or an
    Indian GEO agency? What did you conclude? *(Tests whether the monitoring layer already feels
    "solved" to them — our H-falsification.)*
13. Does your Search Console show the new generative-AI report? Have you looked at it? What was
    useful and what was missing? *(Tests awareness of the free first-party option.)*

### Block 4 — Pain severity, scored (4 min)
14. On a scale of 1–5, how serious a problem is "buyers form an opinion about you inside an AI
    answer before they ever reach your site"? What makes it a [their number] and not one lower?
15. What would have to be true for that number to be a 5?
16. If nothing changed in the next 12 months, what would that cost you? In pipeline, in deals, in
    credibility — whatever is real for you.
17. Whose problem is this — yours, your CMO's, your CEO's? Who else would need to approve spending
    on it?

### Block 5 — Willingness to pay (10 min)
18. Forget our offer. For a service that (a) measured your visibility across ChatGPT, Perplexity,
    Gemini and Google AI Overviews with proper statistics — run counts and confidence intervals, not
    a single blended score, (b) told you exactly what to change and why, with the evidence,
    (c) made those changes with your approval, (d) did the off-site work — pitching the listicles and
    editors, updating G2/Capterra/TrustRadius, producing the comparison and video assets that get
    cited — and (e) reported the traffic and pipeline effect monthly, what would you expect that to
    cost per month?
**18a. THE BUY-VS-HIRE CARD *(ask every prospect; do not recommend either option; read verbatim).***
> **Option 1 — Do it yourself with a tool.** A measurement platform (Peec Pro ≈ $210/month, Otterly
> ≈ $189/month, Semrush AI Visibility $99/domain) shows where you appear, ranks the opportunities,
> drafts the content changes, and names the third-party pages worth pitching. Your team executes.
> Estimated internal effort: 6–10 hours/month.
>
> **Option 2 — We do it.** The same measurement discipline, plus execution: on-site optimisation
> staged for your approval, and the off-site work — pitching editors and listicles, updating review
> and analyst profiles, producing the assets that get cited. **$1,500/month (₹1,00,000)** for managed
> + earned media, or **₹75,000/month** for on-site only. Estimated internal effort: 1–2 hours/month.

Record verbatim: which option, why; what they believe an hour of their team's time costs; which tool
they already use or have evaluated; what would make Option 2 worth it; what would make them cancel
Option 2 in month 4. **If ≥4 of 5 choose Option 1, hypothesis H3b fails and the service is dead at our
price** — that is a result to report, not to argue with.
19. **Ascending price ladder** — ask in this order and record the **first "no"**: ₹40,000/mo (measurement
    + report + prioritised backlog, your team executes) → ₹75,000/mo (we execute on-site) →
    ₹1,00,000 / $1,500/mo (on-site + earned media) → $3,000/mo (dedicated, weekly cadence). Then:
    at what price would you say "that's so cheap something must be wrong"? *(A "yes" without a named
    budget line, approver and start date is logged as **interest**, not willingness to pay.)*
20. Your current SEO spend is [their number from Q10]. Would this replace part of it, sit on top
    of it, or come out of a different budget?
21. Would you pay in USD against a US/UK entity, or in INR against the Indian entity? Does that
    change the number? *(Tests A9 — `12` §5 shows a USD buyer breaks even ~3.4× faster on identical
    COGS, so this is the single biggest ARPU lever.)*

### Block 6 — The two things we most need to learn (3 min)
22. To prove any of this works, we'd need to connect your GA4 and Search Console and add a "what
    led you to evaluate us?" field to your demo form. Is that something you'd authorize? Who would
    say no? *(Tests A10/H6.)*
23. **Co-observation card** *(replaces v1's "check it yourself right now" — C-07)*. Here is what we
    found: [one true, specific finding, with **n, surface, runs, window and the interval** — e.g. "for
    '<category> best tools for <use case>' on Perplexity, 5 runs on 14 Oct from a US-East logged-out
    session named X, Y, Z and did not mention you; 95% upper bound on your true mention rate is 60%"].
    Then hand them the card from `13` §7: exact prompt string, surface and version, region, "logged
    out, fresh session, memory off, no custom instructions", desktop browser, a named 6-hour window,
    **3 runs**. Scored as: *were their observations inside our stated interval?* — never "did they match
    our point estimate". Record their reaction to the intervals verbatim, including "these numbers move
    around so I wouldn't pay for them", which is the most valuable negative signal available.
    **Never** run this on a prompt chosen because we knew the answer: prompts are pre-registered and
    hashed before the card is sent.
24. What's the most useful thing we could send you in the next 48 hours?

### Close (only after all of the above)
25. We're running a 90-day pilot with a small number of companies: [scope], [price], [pre-registered
    success metrics], [what we will not promise — no guaranteed placement, no proven revenue lift,
    intervals on every number]. Would you want one of those slots? If not now, what would need to
    change? *(The proposal goes out with the free diagnostic attached and time-boxed, so the free work
    cannot be mistaken for the product — `08` VR-6.)*
26. Who else should I talk to — inside your company or outside it?

**Never say:** "guaranteed," "we'll get you into ChatGPT," "rank #1 in AI." Integrity rule 7.

---

## D2 — Channel interview with an SEO/digital agency owner (**2 in Stage 1**, 5 in Stage 2)

Purpose: test H9 (would agencies white-label/resell?) and learn the real delivery economics from
people who already do this work.

1. What do you charge for SEO today, and how has that changed in the last 12 months? Did AI-search
   work change your pricing? *(Cross-check against P2: 56.2% of agencies raised prices citing AI
   search work.)*
2. Do you sell anything specifically branded as GEO or AEO? What is it, what does it cost, and how
   many clients bought it?
3. What tool do you use to measure AI visibility? What do you pay? What do you hate about it?
4. When a client asks "did it work?", what do you show them? What do you show the CFO?
5. Where does your delivery actually go — on-page changes, content, structured data, or off-site
   work like review sites, listicles, Reddit, YouTube, digital PR? Roughly what share of effort is
   off-site? *(Tests A4/M8 against practitioner reality — the 85% third-party finding.)*
6. If a client asked you to get them cited in the third-party pages that AI actually quotes, what
   would you do on Monday? What stops you from doing more of it?
7. What would you white-label, and at what margin? What would you never outsource?
8. If we sold you a measurement + execution layer that you could put your brand on, at what price
   per client workspace would it work for you? *(Compare to Profound agency at $399/mo per client
   workspace, F2 — and to white-label digital-PR-for-GEO suppliers, who already let agencies resell the
   earned-media workstream at $3,000–$10,000/mo retainers, register §14. What do you need that they do
   not supply?)*
8a. Would you resell **measurement credibility** rather than capacity — i.e. a protocol-validated,
   interval-reported audit your team puts its name on? At what price per client, and what would it have
   to include for your clients to believe it? *(This is the O2 option in `00` §D.)*
9. What's the thing vendors in this category get wrong that makes you not trust them?
10. Who are the two best agencies doing AI-search work right now, and what do they do that others
    don't?

---

## D3 — Internal scoring sheet (fill within 1 hour of every call)

| Field | Values |
|---|---|
| Company / segment (S1–S8) / domicile of buying entity (IN / US / UK / other) | text |
| Interviewee role; is this the economic buyer? (Y/N/who) | text |
| Revenue band; marketing headcount; monthly search/content budget | numbers |
| Ever self-checked their brand in an AI answer? (Y/N) | **Y/N** |
| Could describe a specific deal affected by AI answers? (Y/N + note) | **Y/N** |
| Currently paying for AI-visibility tooling or GEO service? (name + price) | text |
| Severity score 1–5 (Q14) and the reason they gave | number |
| Expected monthly price (Q18) / "expensive but I'd buy" (Q19a) / "too cheap" (Q19b) | 3 numbers |
| Replace existing budget / additive / other budget | choice |
| USD-billing possible? (Y/N/unknown) | **Y/N** |
| Would authorize GA4 + GSC + self-attribution field? (Y/N/who blocks) | **Y/N** |
| **Buy-vs-hire card (Q18a): Option 1 tool / Option 2 us / neither / "tool + us"**, and their stated reason | **critical — H3b** |
| Price ladder (Q19): **first "no" rung** (₹40k / ₹75k / ₹100k–$1,500 / $3,000) + "too cheap" rung | **critical — H3** |
| Co-observation (Q23): runs completed / inside our interval (count of 3) / reaction to intervals, verbatim | **critical — H5** |
| Tool they already use or evaluated (name + price paid) | text |
| Asked for a pilot slot? (Y/N/later) | **Y/N** |
| Next commitment obtained (call / intro / money / nothing) | text |
| One thing they said that surprised us | text |
| One reason this deal will NOT happen | text |

### Aggregation rules (decided in advance so we cannot rationalize afterwards)
All rules are pre-registered here, before Stage 1 day 1, and quoted verbatim in the Stage 1 memo.
At n = 5 a "rate" is a count out of five; report counts.
- **H2 pass** if ≥2 of 5 calls score severity 4–5 (40%).
- **H3 pass** if the median first-"no" rung is ≥ ₹75,000/mo (INR entities) or ≥ $1,000/mo (USD entities).
- **H3b pass** *(new, and the decisive one)* if **≤1 of 5** buyers chooses Option 1 (tool) over Option 2
  (us). **≥4 of 5 choosing the tool fails H3b outright** and routes to O2/O3, not to Stage 2.
- **H5 pass** if co-observations fall **inside our stated interval** for ≥2 of 3 runs, for ≥3 of 5
  prospects. Scoring is interval-based; "matched our point estimate" is not the criterion.
- **H6 pass** if ≥2 of 5 authorize instrumentation.
- **H4 pass** if ≥1 paid pilot is signed or verbally committed **with a named budget line, approver and
  start date**; ≥3 priced-proposal requests count as a conditional pass (gate G2/T3).
- Any prospect whose co-observations fall outside our interval **systematically** (≥2 of 3 runs, on more
  than one prospect) is written up the same day and treated as a **measurement defect**, not a sales
  objection — and triggers the band review in `13` §8, never an automatic company kill.
