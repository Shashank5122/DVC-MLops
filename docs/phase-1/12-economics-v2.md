# 12 — Economics v2 (corrected model)

**Status: authoritative.** Supersedes `10-tam-bottom-up.md` §2–§6 (hour definitions, COGS, margins,
break-even, revenue ceilings, venture conditions). `10` §1 (bottom-up account universe) is unchanged and still
applies.

Prepared 16 October 2026 in response to corrections **C-02, C-03, C-04, C-09, C-10** (`11-correction-log.md`).

Labels: **[VERIFIED]** sourced externally · **[ESTIMATED]** computed by us from stated assumptions ·
**[HYPOTHESIS]** untested · **[NOT YET VERIFIED]** needs data we do not have.

---

## 0. The one-paragraph summary

At honest hour counts and honest tooling costs, a managed GEO/AEO service is a **high-gross-margin,
capacity-capped, low-ceiling business**. A single founder can serve **~9 clients at monitoring scope, ~5 at
full managed scope**, and reaches **operating cash break-even with 1–3 clients** but needs **5 clients at
USD pricing (Tier C)** — and **~30 clients at ₹40,000/month (Tier A)** — to pay themselves a market salary.
Over 24 months, bootstrapped and founder-led, the plausible ARR band is **$60k (conservative) → $162k (base) →
$375k (optimistic)**; the ₹40,000-only variant caps at **~$70k ARR and never becomes economically profitable
inside 24 months**. Reaching **$2M ARR requires 12–21 delivery FTEs** — it is an agency, not a product.
Nothing in this model is a reason not to run Stage 1; it is a reason not to promise ourselves a software
company's economics from a services company's cost structure.

**FX assumption: ₹95 = $1.** [VERIFIED] RBI reference rate USD/INR 95.032 on 14 Oct 2026. All INR figures are
converted at this rate; a 5% rupee move changes USD-equivalent prices by 5% and is inside our rounding noise.

---

## 1. Assumption register

| # | Assumption | Value | Label | Basis |
|---|---|---|---|---|
| A-1 | FX | ₹95 = $1 | [VERIFIED] | RBI reference rate, 14 Oct 2026 |
| A-2 | Mid-level analyst loaded hourly rate (India) | $4–$6 | [ESTIMATED] | Indeed India avg SEO specialist ₹19,763/mo, junior ₹12,694, senior ₹38,666 (145 salaries, upd. 21 Aug 2026); +25–30% employer load; ÷160 h |
| A-3 | Senior specialist loaded hourly rate | $6–$12 | [ESTIMATED] | 75th pct ₹45,000–₹85,000/mo; SaaS/product specialists ₹70,000–₹2,00,000/mo |
| A-4 | **Blended delivery rate used in the model** | **$7/h** (band $4–$12) | [ESTIMATED] | Midpoint of A-2/A-3 for a senior-ish, English-fluent, US-buyer-facing analyst |
| A-5 | Founder opportunity cost | $40/h (band $25–$75) | [ESTIMATED] | Market rate for an ML/MLOps/LLM engineer in India; used only in economic-profit calculations |
| A-6 | Founder market monthly comp | $4,000/mo (₹3.8 L) | [ESTIMATED] | Band $3,000–$6,000; the comp the business must eventually cover |
| A-7 | Gross hours per FTE per month | 160 | [ESTIMATED] | 40 h × 4 weeks |
| A-8 | **Effective delivery hours per FTE per month** `H_eff` | **90 / 110 / 130** | [ESTIMATED] | 160 less sales, marketing, internal tooling, learning, admin, prospect support, leave. Founder-only `H_eff` = **70** (heavier selling load) |
| A-9 | Measurement tooling, per client per month (buy path) | $30 / **$100** / $400 | [VERIFIED as priced] | Otterly $29–$489; Peec €70/€180/€360/mo billed annually for 1/2/5 projects (≈$82/$210/$420) + extra engine €25/€55/€115; Profound agency self-serve $399/mo per client workspace |
| A-10 | API + infrastructure if we build our own sampling | $22–$83/client/mo | [ESTIMATED] | From `10` §3; Perplexity Sonar $5–$14 per 1,000 requests, plus LLM inference and storage |
| A-11 | Engineering time to run a build-path pipeline | ~40 h/month | [HYPOTHESIS] | Maintenance of collectors, extractors, prompt registry, reports, provider-version drift |
| A-12 | Fixed operating cash cost | $600/mo (band $300–$1,200) | [ESTIMATED] | Tooling seats, infra, domain/email, accounting, legal templates, misc. Excludes all labour |
| A-13 | Churn (monthly, managed tiers) | 2% / **3%** / 5% | [HYPOTHESIS] | **No data.** Single largest financial unknown; see §7 |
| A-14 | Pipeline additions per month (founder-led, no ads) | 0.6 / 0.9 / 1.2 net new clients | [HYPOTHESIS] | **No data.** Stage 1 measures conversion, not additions |
| A-15 | Delivery hire loaded monthly cost | $500 / $700 / $900 | [ESTIMATED] | A-2/A-3 scaled to full-time |

**Every figure in §8 that depends on A-13 or A-14 is a scenario, not a forecast.** They are included because
the brief demands 24-month revenue scenarios, and they are labelled so nobody mistakes them for evidence.

---

## 2. Definitions and formulas

The v1 defect was two different hour definitions. There is now one.

```
H_tier  = ALL client-facing hours per client per month
          (collection + QA + analysis + proposal drafting + third-party corroboration
           + reporting + client calls + fact verification + ticket handling)
H_eff   = effective delivery hours per FTE per month            (A-8)
r       = blended delivery rate $/hour                          (A-4)
T       = per-client tooling + API + infra $/month              (A-9 or A-10 + A-11/N)
s       = support/allocation overhead = 0.05 × (H_tier × r)
V       = variable cost per client per month = T + H_tier×r + s + infra
P       = monthly price per client
GM%     = (P − V) / P
C_cash  = P − V                            # cash contribution margin
C_econ  = P − V − H_f × r_f                # economic contribution; H_f = founder hours/client/mo, r_f = A-5
N_max   = (H_eff_founder + H_eff × FTE) / H_tier      # capacity cap on clients
N_cash  = F_cash / C_cash                  # operating cash break-even (founder paid ₹0)
N_econ  = (F_cash + founder_comp) / C_econ # founder-compensated break-even
ARR     = N × P × 12
LTV     = C_cash × min(1/churn, life_cap)
Payback = CAC / C_cash   (months)
```

**Operating cash break-even ≠ economic profitability.** `N_cash` answers "does the bank balance stop falling?"
`N_econ` answers "is this worth the founder's time versus a job?" A business can sit comfortably above `N_cash`
for years while destroying founder value. Both are reported below for every price point.

---

## 3. Capacity model (corrects C-02)

### 3.1 Service tiers and hour budgets

| Tier | Scope | Hours itemised | `H_tier` |
|---|---|---|---|
| **A — Measure & advise** | Sample surfaces, extract, analyse, monthly report, prioritised backlog, one call. **Client executes.** | collection/QA 1.0 · analysis 1.5 · report 1.5 · call+comms 1.0 | **5** |
| **B — Managed on-site** | A, plus drafting optimisations, diffs, publish coordination, fact verification of every claim | A 5 · proposals/diffs 3.0 · publish coordination + QA 2.5 · fact verification 1.5 | **12** |
| **C — Managed + earned** | B, plus third-party corroboration: gateway research, pitching editors/listicles, profile & review-site updates, asset production coordination | B 12 · gateway research 2.0 · outreach/pitching 4.0 · profile/review updates 2.0 · asset coordination 1.0 | **21** |

Itemisations are **[ESTIMATED]** — Stage 1 replaces them with logged actuals (see `08-validation-plan-v2.md` §6).

### 3.2 Clients per FTE

`N_max = H_eff / H_tier` [ESTIMATED]

| Tier | `H_eff` = 90 (cons.) | 110 (base) | 130 (opt.) | Founder-only (`H_eff` = 70) |
|---|---|---|---|---|
| A (5 h) | 18.0 | 22.0 | 26.0 | 14.0 |
| B (12 h) | 7.5 | 9.2 | 10.8 | 5.8 |
| C (21 h) | 4.3 | 5.2 | 6.2 | 3.3 |

**v1's "10 clients per FTE" was only correct for Tier A.** At the managed scope v1 actually proposed
(Tier C), capacity was overstated by roughly **2×**. Everything downstream in v1 inherited that error.

**Team capacity, base case:** founder (70 h) + 1 delivery FTE (110 h) = 180 h → Tier C **8.6 clients**,
Tier B **15.0**, Tier A **36.0**. Founder + 2 FTEs (290 h) → Tier C **13.8**, Tier B **24.2**, Tier A **58.0**.

---

## 4. Cost per client per month, and gross margin (corrects C-03)

### 4.1 Buy vs build

| Path | Per-client cash cost | Plus | Verdict |
|---|---|---|---|
| **Buy** (license Peec / Otterly / Profound) | $30–$400/mo (A-9) | zero build time; capability drift handled by vendor; our data lives in someone else's platform | **Use for Stage 1–2** |
| **Build** (own collectors + extraction) | $22–$83/mo (A-10) | ~40 h/mo engineering (A-11) = $160/client at N=10, $80 at N=20, $53 at N=30, $40 at N=40, $27 at N=60 | Only cheaper than buying at **N ≈ 25–30** |

Total variable cost by path [ESTIMATED]:

| N clients | Build path, Tier A | Build, Tier B | Build, Tier C | Buy path ($100), Tier A | Buy, Tier B | Buy, Tier C |
|---|---|---|---|---|---|---|
| 10 | $219 | $270 | $336 | $147 | $198 | $264 |
| 20 | $139 | $190 | $256 | $147 | $198 | $264 |
| 30 | $112 | $164 | $230 | $147 | $198 | $264 |
| 40 | $99 | $150 | $216 | $147 | $198 | $264 |
| 60 | $85 | $137 | $203 | $147 | $198 | $264 |

**Decision:** buy now. Revisit building only when (i) N ≥ 25, (ii) the licensed tool cannot produce the
evidence we sell (per-surface confidence intervals, reproducibility bands, gold-set-validated extraction), and
(iii) we have measured that the missing capability is the reason clients pay us. Condition (ii) is a
**[HYPOTHESIS]** worth testing in Stage 1 by running the protocol manually on top of a licensed tool.

### 4.2 Gross margin grid (buy path, r = $7/h)

`V = T + H×7 + 0.05×H×7 + $10 infra`; GM% = (P − V)/P. [ESTIMATED]

| Tier | Price | P ($) | T = $30 | T = $100 (base) | T = $400 |
|---|---|---|---|---|---|
| **A** | ₹40,000 | 421 | $77 → **+82%** | $147 → **+65%** | $447 → **−6%** |
| **A** | $500 | 500 | $77 → **+85%** | $147 → **+71%** | $447 → **+11%** |
| **B** | ₹75,000 | 789 | $128 → **+84%** | $198 → **+75%** | $498 → **+37%** |
| **B** | $1,000 | 1,000 | $128 → **+87%** | $198 → **+80%** | $498 → **+50%** |
| **C** | ₹1,00,000 | 1,053 | $194 → **+82%** | $264 → **+75%** | $564 → **+46%** |
| **C** | $1,500 | 1,500 | $194 → **+87%** | $264 → **+82%** | $564 → **+62%** |

Read this table's **first column of prices** carefully: at ₹40,000/month with a $400 tool seat we are
**gross-margin negative**. The tooling choice is not an implementation detail at low price points — it is the
difference between a business and a hobby. Note also that v1's "+80% monitoring-tier margin" survives only if
tooling stays ≤$30/client/month.

**Labour share of V:** 35 h × ... at Tier C, labour = $154 of $264 = **58%**; tooling = 38%; infra/support 4%.
Labour still dominates — so margin improvement comes from hours per client (templates, reuse, tooling
automation), not from negotiating API prices.

---

## 5. Break-even: cash vs economic (corrects C-09)

Fixed cash `F_cash` = $600/mo (A-12). Founder hours per client `H_f` = 3 (Tier A) / 4 (Tier B) / 6 (Tier C).
Founder opportunity cost `r_f` = $40/h (A-5). Founder target comp = $4,000/mo (A-6).

| Tier / price | V | `C_cash` | **`N_cash`** | `C_econ` | **`N_econ`** | `N_econ` @ r_f=$25 | `N_econ` @ r_f=$75 |
|---|---|---|---|---|---|---|---|
| A · ₹40,000 ($421) | $147 | $274 | **2.2 → 3** | $154 | **30** | 23 | 94 |
| A · $500 | $147 | $353 | **1.7 → 2** | $233 | **20** | 16 | 45 |
| B · ₹75,000 ($789) | $198 | $591 | **1.0 → 1** | $431 | **11** | 9 | 21 |
| B · $1,000 | $198 | $802 | **0.7 → 1** | $642 | **7** | 6 | 13 |
| C · ₹1,00,000 ($1,053) | $264 | $789 | **0.8 → 1** | $549 | **8** | 7 | 16 |
| C · $1,500 | $264 | $1,236 | **0.5 → 1** | $996 | **5** | 4 | 6 |

### The two numbers that matter

1. **Operating cash break-even is trivially easy: 1–3 clients.** Anybody who says "we need funding to start
   this" is wrong. Fixed cash is $600/month.
2. **Founder-compensated break-even is the real test, and it is price-dominated, not cost-dominated.** At
   $1,500/month it is **5 clients**. At ₹40,000/month it is **30 clients** — which needs ~6 delivery FTEs
   (Tier A, 5 h each → 30 × 5 / 110 = 1.4 FTEs, but at Tier A we cannot sell managed execution) and
   ~₹12 L/month of revenue. **The ₹40,000 price point cannot fund a market-rate founder inside 24 months.**

### Sensitivity of `N_econ` (Tier C, $1,500)

| | `F_cash` $300 | $600 | $1,200 | + $4,000 founder comp |
|---|---|---|---|---|
| `C_econ` $996 | 0.3 → 1 | 0.6 → 1 | 1.2 → 2 | **4.6 → 5** |
| `C_econ` $786 (r=$12/h) | 0.4 → 1 | 0.8 → 1 | 1.5 → 2 | **5.9 → 6** |
| `C_econ` $1,116 (r=$4/h) | 0.3 → 1 | 0.5 → 1 | 1.1 → 2 | **4.1 → 5** |

`N_econ` is insensitive to delivery rate (±1 client across a 3× rate range) and highly sensitive to **price**
and **founder opportunity cost**. Implication: do not optimise labour cost; optimise price and domicile of the
buying entity. A USD-billed client is worth ~3.4× an identically-served INR-billed client.

---

## 6. Validation unit economics (corrects C-04)

Per-diagnostic labour, itemised [ESTIMATED]:

| Step | First diagnostic | 5th diagnostic (templated) |
|---|---|---|
| Client-specific research (product, ICP, competitors, category facts) | 1.5 h | 0.8 h |
| Prompt design + pre-registration | 1.0 h | 0.4 h |
| Collection setup, run monitoring, raw capture | 0.5 h | 0.3 h |
| Extraction QA against gold sample (~10% of observations) | 1.0 h | 0.5 h |
| Reproducibility analysis, confidence intervals | 1.0 h | 0.6 h |
| Gateway identification + owner/actionability classification | 1.5 h | 0.8 h |
| Report writing + internal QA | 2.0 h | 1.2 h |
| Delivery call | 0.5 h | 0.4 h |
| **Total** | **9.0 h** | **5.0 h** |

Cost per diagnostic: **$68 initially / $40 templated at hired rates (r = $7)**, or **$365 / $205 at founder
opportunity cost ($40/h)**, plus $3–$7 of API spend. v1's "$15–$31 falling to $5–$15" is withdrawn: it counted
collection only. The "templated = 5 h" figure is itself a **[HYPOTHESIS]** that Stage 1 must measure —
we log actual hours on all five diagnostics and only then decide whether Stage 2 is affordable.

**Stage 1 budget** (5 diagnostics + protocol + 5 buyer conversations + logging; full detail in
`08-validation-plan-v2.md` §5). Two versions, because the biggest line is labour and the founder can either do
it or buy it:

| Line | Low | Base | High | Who |
|---|---|---|---|---|
| API/inference (2,500 observations, 2 surfaces, 2 windows) | $60 | $110 | $200 | cash |
| Measurement tool seat, 1 month (Otterly or Peec Starter) | $30 | $100 | $210 | cash |
| Gold-set annotation, 200 responses × 2 annotators (~27 h @ $4/h) | $50 | $108 | $220 | cash |
| Domain, email, landing page, contract template | $50 | $90 | $150 | cash |
| **Out-of-pocket cash** | **$190** | **$408** | **$780** | |
| **₹ equivalent** | **₹18,050** | **₹38,760** | **₹74,100** | |
| **Founder hours** (98 h scheduled) | | **98 h → $3,920** at $40/h | | founder |
| **Economic total** | **$3,230** | **$4,328** | **$5,480** | |
| *Alternative: hire the diagnostic labour instead (5 × 9 h @ $7)* | *+$315* | *+$315* | *+$315* | *cuts founder hours by ~45* |

The cash number is trivially affordable. The economic number is the honest one, and it is what Stage 1 must
justify: **~$4,300 of founder time to learn whether anyone will pay.** Stated differently: Stage 1 costs about
**one third of a single Tier C client-year**, so a single signed pilot repays the entire validation.

---

## 7. CAC, payback, LTV

### 7.1 CAC (founder-led, Stage 1) [ESTIMATED]

Stage 1 **is** the acquisition experiment, so CAC is read directly off its log rather than modelled separately.
Scheduled effort (see `08-validation-plan-v2.md` §4):

| Activity | Hours |
|---|---|
| Protocol freeze, tooling setup, raw store, logging | 8 |
| Target list (40 accounts with fit evidence) + outreach copy + 2 send batches | 15 |
| 5 free diagnostics @ 9 h | 45 |
| Gold-set adjudication + extractor QA + reproducibility analysis | 14 |
| 5 buyer conversations + 2 agency interviews (calls, prep, notes) | 11 |
| Paid-pilot proposals (≥1) | 5 |
| **Founder hours total** | **98** |
| Out-of-pocket cash (API, tool seat, annotators, setup) | **$408** |

- **CAC (cash)** = $408 / pilots won → **$408** for one pilot, **$204** for two, **undefined for zero** — and
  zero is the kill signal, not a number to average away.
- **CAC (economic)** = ($408 + 98 h × $40) / pilots won = **$4,328 for one pilot**, $2,164 for two.
- **Payback** on cash contribution: Tier C ($1,500, `C_cash` $1,236) → **0.33 months** cash / **3.5 months**
  economic. Tier A (₹40,000, `C_cash` $274) → **1.5 months** cash / **15.8 months** economic.

At scale (Stage 3, founder no longer doing delivery), the comparable inputs are a hire's loaded cost and a
conversion rate we have not measured. **Do not put a scaled CAC in any document until we have logged 20 real
outreaches-to-signature conversions.**

### 7.2 LTV [HYPOTHESIS — no churn data exists]

`LTV = C_cash × min(1/churn, life_cap)`, Tier C at $1,500, `C_cash` = $1,236:

| Monthly churn | Implied life | LTV (uncapped) | LTV (capped 24 mo) | LTV:CAC @ cash $408 | @ economic $4,328 |
|---|---|---|---|---|---|
| 1% | 100 mo | $123,565 | $29,656 | 49× | 15× |
| 2% | 50 mo | $61,783 | $29,656 | 49× | 15× |
| 3% | 33 mo | $41,188 | $29,656 | 49× | 15× |
| 4% | 25 mo | $30,891 | $29,656 | 49× | 15× |
| 6% | 17 mo | $20,594 | $20,594 | 34× | 10× |
| 8% | 12.5 mo | $15,446 | $15,446 | 26× | 8× |

Read the **right-hand column**. Cash-CAC ratios look extraordinary only because the denominator hides 98 hours
of founder time; the economic column is the one to quote to anyone: **LTV:CAC ≈ 6.9× at 3% monthly churn, 3.6×
at 8%** — plausible for a services business, and only plausible because the CAC is founder-led. A hired sales
motion at $1,500–$2,500 cash CAC would land at 6–20× on cash contribution and roughly 3–10× on economic. Services businesses also carry expansion revenue and
reference value we have not modelled, and concentration/relationship risk we have not discounted.

**Do not use LTV:CAC to justify spending on acquisition yet.** We have zero observations of churn. Stage 1
produces the first; the pilot contract length and the reason given for any "no" are the data.

---

### 7.3 Downgrade-adjusted retention is the **base planning case** (added 16 Oct 2026, condition 8)

Founder decision of 16 Oct 2026: plan on the assumption that clients **step down** after optimisation, not that
every client stays on the highest retainer. Resisting step-down is how agencies manufacture work (integrity
rule 21), so the honest curve is modelled as the base case and the flat-retainer curve as the upper bound.

**Package ladder:**

| Package | Price | Hours/client/mo | V | Contribution | Role |
|---|---|---|---|---|---|
| **Project-only** diagnostic/implementation | $497 – ₹75,000 one-time | 6–9 h once | $60–$88 | **$409–$722** | Entry wedge; **zero recurrence**, CAC never amortised |
| **Managed sprint** (90 days, Tier B/C) | ₹75,000 / $1,500 | 12 / 21 | $198 / $264 | $591 / **$1,236** | Where value is proved |
| **Ongoing managed** (no step-down) | $1,500 | 21 | $264 | $1,236 | **Upper bound only — not the base case** |
| **Quarterly monitoring** (step-down landing spot) | $400–$500 | 2–3 | ≈$50–$57 | **≈$350** | Honest destination after optimisation |

**LTV with step-down at month 6** (`C_full` = $1,236 for 6 months, then `C_maint` = $350) [ESTIMATED]:

| Client life | Flat retainer LTV | **Step-down LTV (base case)** | Change |
|---|---|---|---|
| 12 months | $14,828 | **$9,516** | **−36%** |
| 24 months | $29,656 | **$13,719** | **−54%** |
| 36 months | $44,483 | **$17,923** | **−60%** |

LTV:CAC on economic CAC ($4,328): **2.2× at 12 months, 3.2× at 24 months** — viable, and these replace the
flat-retainer ratios in §7.2 as the planning numbers. On cash CAC ($408) the ratios are 23× and 34×, which is
an artefact of uncharged founder time and must not be quoted externally.

**Capacity consequence:** a book of stepped-down clients at $400/month needs **~13 clients** to cover the same
$4,600/month (fixed cash + founder market comp) that **5** Tier C clients cover. Step-down therefore converts a
margin question into a **pipeline question** — the answer is to keep filling the top of the ladder, not to resist
the descent. Published downgrade criteria are in `13` §9 and `validation/03-operational-readiness-memo.md` §8.

## 8. 24-month revenue scenarios (corrects C-02, recomputes v1 §6)

Bootstrapped, founder-led, no paid acquisition, capacity-capped (`N_max`), hiring only when cash covers three
months of the hire. Churn and additions per A-13/A-14 — **scenarios, not forecasts**.

| | **Conservative** | **Base** | **Optimistic** | **INR Tier-A only (stress)** |
|---|---|---|---|---|
| Avg price | $579 (₹55,000) | $900 | $1,400 | $421 (₹40,000) |
| Scope / `H_tier` | A–B blend, 8 h | B, 12 h | B–C blend, 15 h | A, 5 h |
| V | $169 | $198 | $220 | $147 |
| Net new clients/mo | 0.6 | 0.9 | 1.2 | 1.0 |
| Monthly churn | 4% | 3% | 2% | 5% |
| Delivery hires by m24 | 0 | 1 | 3 | 0 |
| Clients at m24 | 8.8 | 15.0 | 22.3 | 13.9 |
| **ARR at m24** | **$60,800** | **$162,000** | **$374,600** | **$70,000** |
| **Cumulative 24-mo revenue** | **$72,500** | **$181,200** | **$402,300** | **$82,900** |
| Ending cash (from −$1,500) | +$35,500 | +$114,200 | +$291,600 | +$38,100 |
| First cash-positive month | 4 | 2 | 2 | 4 |
| First economic-profit month (founder @ $40/h + $4,000/mo) | **never within 24 mo** | **13** | **5** | **never within 24 mo** |

Monthly path, base case [ESTIMATED]:

| Month | Clients | FTE | Revenue | Variable | Fixed | Net | Cumulative cash | Economic profit |
|---|---|---|---|---|---|---|---|---|
| 3 | 1.8 | 0 | $1,596 | $351 | $600 | $644 | −$1,424 | −$3,568 |
| 6 | 4.2 | 0 | $3,814 | $840 | $600 | $2,374 | +$4,004 | −$2,134 |
| 9 | 6.5 | 1 | $5,839 | $1,286 | $1,300 | $3,253 | +$13,616 | −$1,525 |
| 12 | 8.5 | 1 | $7,687 | $1,693 | $1,300 | $4,694 | +$26,287 | −$331 |
| 15 | 10.4 | 1 | $9,373 | $2,064 | $1,300 | $6,009 | +$43,026 | +$759 |
| 18 | 12.1 | 1 | $10,913 | $2,403 | $1,300 | $7,209 | +$63,478 | +$1,754 |
| 21 | 13.7 | 1 | $12,318 | $2,713 | $1,300 | $8,305 | +$87,320 | +$2,663 |
| 24 | 15.0 | 1 | $13,500 | $2,973 | $1,300 | $9,227 | +$114,177 | +$3,427 |

**What the scenarios actually say:**
- Cash survival is never the problem. All four variants are cash-positive by month 4 with no external capital.
- **Founder compensation is the problem.** Both INR-dominated variants never reach economic profit in 24
  months. The base case reaches it at month 13 and the optimistic case at month 5 — the difference is entirely
  **price and billing domicile**, not cost control.
- The conservative and stress cases are **founder-capacity-bound** (8.8 and 13.9 clients vs caps of 8.8 and
  14.0) — growth stops because one person runs out of hours, not because demand stops.

### 8.1 Ceiling analysis (recomputes v1 §6 "revenue ceilings")

`FTEs required = ARR / (12 × P) × H_tier / H_eff`, `H_eff` = 110 [ESTIMATED]:

| Target ARR | P = $500 (Tier A) | P = $1,000 (Tier B) | P = $1,500 (Tier C) |
|---|---|---|---|
| $0.5M | 83 clients · **9 A-FTEs** / 16 C-FTEs | 42 · 4.5 B / 8.0 C | 28 · 3.0 B / 5.3 C |
| $1M | 167 · 7.6 A / 31.8 C | 83 · 9.1 B / 15.9 C | 56 · 6.1 B / 10.6 C |
| **$2M** | 333 · **15.2 A / 63.6 C** | 167 · **18.2 B / 31.8 C** | 111 · **12.1 B / 21.2 C** |
| $4M | 667 · 30.3 A / 127.3 C | 333 · 36.4 B / 63.6 C | 222 · 24.2 B / 42.4 C |

**v1's "$2–4M ARR with agency channel at 60–80% margin" implied a 12–40 person delivery organisation.** That
is an achievable agency, and it is worth stating plainly: **this is not a small team's outcome at managed
scope.** The only routes to a small-team, high-ARR outcome are (i) Tier A scope at scale (monitoring — the
crowded, commoditising end of the market we already decided not to enter), or (ii) software, which Phase 1
found to be a closed window (C-01, C-08).

---

## 9. Sensitivity: what actually moves the answer

Ranked by effect on founder-compensated break-even `N_econ` (Tier C, $1,500 base = 5 clients):

| Lever | Change | `N_econ` | Verdict |
|---|---|---|---|
| **Price / billing domicile** | $1,500 → ₹40,000 ($421) at Tier A | 5 → **30** | **Dominant.** 6× |
| **Founder opportunity cost** | $25 → $75/h | 4 → 6 | Material, ±20% |
| **Scope creep** | `H_tier` 21 → 28 h (uncontrolled corroboration work) | 5 → 7 | Material; must be contractually bounded |
| **Tooling choice** | $30 → $400/client/mo | 5 → 6 (Tier C) / **margin −6%** at Tier A | Material at low prices only |
| **Delivery labour rate** | $4 → $12/h | 5 → 6 | **Immaterial.** Do not optimise here |
| **Fixed cash cost** | $300 → $1,200 | 4.3 → 5.2 | Immaterial |
| **Churn** | 2% → 8%/mo | no effect on break-even; LTV −75% | Affects valuation and acquisition spend, not survival |

**Conclusion: pricing power and scope discipline are the whole game.** Cost engineering is nearly irrelevant at
this scale. That inverts the instinct to optimise API spend.

---

## 10. Pricing verdict (updates v1's answer on ₹40,000/month)

1. **₹40,000/month (~$421) is a real, published Indian market price** [VERIFIED: Adexorb ₹19,999; Digimark
   ₹39,999 + ₹40,000 audit; Raasis ₹24,000–₹2,80,000; DigiStreet ₹50,000–₹2,00,000] — but it buys **Tier A
   only**, with tooling ≤$30/client/month, and it cannot pay a market-rate founder inside 24 months.
2. **Managed execution requires ≥₹75,000/month (Tier B) or ≥₹1,00,000/month (Tier C)** in INR terms, or
   **$1,000–$1,500/month** from a USD-domiciled buyer. On identical COGS, the USD buyer is worth ~3.4× the
   INR buyer at break-even.
3. **Willingness to pay is still unvalidated [NOT YET VERIFIED].** Every number in this file assumes a price we
   have not yet seen anyone accept. Stage 1's paid-pilot proposal is the experiment; the two prices to test are
   **₹75,000/month (Tier B, INR entity)** and **$1,500/month (Tier C, USD entity)**, with ₹40,000 offered only
   as an explicitly-scoped Tier A fallback so we can measure the demand curve rather than guess it.
4. **Do not discount to win the first client below Tier A economics.** A ₹20,000 pilot at base tooling is
   gross-margin negative and teaches us nothing about willingness to pay at a viable price.

---

## 11. Unresolved financial risks

| # | Risk | Label | How Stage 1 addresses it |
|---|---|---|---|
| FR-1 | Churn is unknown; every LTV figure is invented | [HYPOTHESIS] | First pilot contract gives retention terms + a reason-code for every "no" |
| FR-2 | Hour budgets (`H_tier`) are guesses | [ESTIMATED] | Logged actuals on all 5 diagnostics; templated-time hypothesis tested |
| FR-3 | Tooling prices and packaging change frequently (Peec pricing not shown publicly per one Oct-2026 comparison; Profound removed self-serve brand tiers mid-Sep 2026) | [NOT YET VERIFIED] | Buy one month of a real seat in Stage 1 and record the invoice |
| FR-4 | Pipeline addition rate (0.6–1.2/mo) is unsupported | [HYPOTHESIS] | 40 outreaches → measured reply/call/proposal conversion |
| FR-5 | Client concentration: 5 clients = ~60% of revenue in one account | structural | Contract minimum 3 clients before any hire |
| FR-6 | If a platform vendor (Peec/Profound/Scrunch) starts selling managed delivery, our only surviving differentiator disappears | [HYPOTHESIS] | Watch vendor changelogs monthly; Peec already ships an agent with 20+ MCP connectors and Profound republishes content — this is the live threat, not a distant one |
| FR-7 | INR revenue with USD tooling costs creates FX exposure on the largest cost line | structural | Price INR clients with a 10% FX buffer, or bill USD where possible |
| FR-8 | Building our own measurement later may cost far more than 40 h/month once provider APIs change (v1 already recorded "OpenAI Search API" renamed **OpenAI Luna**, Sonar deprecation notices, model churn) | [VERIFIED churn, ESTIMATED cost] | Another reason to buy now |
