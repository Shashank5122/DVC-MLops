# SignalGEO integrity rules (operative checklist)

These are constraints on our own work, not marketing copy. Anything we ship — research, product,
sales material, code — must pass these checks.

## Research integrity

1. Every material market, competitor, pricing, platform or technical claim carries a source URL
   and an access date.
2. Facts are separated from estimates and assumptions, explicitly, in the same document.
3. We never invent customer numbers, market sizes, growth rates, pricing, API capabilities or
   traction. If we cannot verify, we write `[UNVERIFIED]` and say what verification would cost.
4. Vendor marketing is never treated as independent evidence. Vendor-published studies are
   tagged T2 and their incentive is named.
5. Contradictory sources are surfaced side by side rather than resolved silently in favour of
   the story we want.
6. When browsing/verification is unavailable for a claim, we state which claims require
   verification before a decision is made on them.

## Product integrity

7. We never promise guaranteed placement in ChatGPT, Gemini, Perplexity or Google AI answers.
8. We never claim that search-enabled LLM APIs reproduce the consumer-facing search experience
   unless we hold evidence for that specific claim. Default position: they do not, and we say so
   in the product UI and in every report.
9. No fabricated reviews, fake citations, astroturfed community content, manipulative link
   schemes, spam, unauthorized scraping, or violations of platform terms — including on behalf
   of a client who asks for it.
10. Every optimization proposal is grounded in verified business facts about the client and
    delivers legitimate user value. If a proposed change would make a page more citable but less
    true or less useful, we do not propose it.
11. Measurement reports disclose confidence intervals, run counts, time windows, and the fact
    that AI answers are non-deterministic.

## Engineering integrity

12. Design for real production constraints (cost, latency, rate limits, multi-tenancy).
13. Typed schemas and deterministic workflows by default; agents only where they demonstrably
    beat a simpler alternative.
14. Research, recommendation, approval, publishing and evaluation are separate concerns with
    separate permissions.
15. Explicit, logged, revocable client authorization before anything touches a client website.
16. Multi-tenant isolation, credential security, auditability, cost controls, retries and
    rollback are designed in, not bolted on.
17. We do not invent API methods, endpoints or integration capabilities. If we have not read the
    doc page, we mark the integration as unconfirmed.
18. Tests exist for critical logic and for security boundaries. We never claim tests passed
    unless they actually ran.

## Business integrity

19. We optimize for willingness to pay, not user interest.
20. Revenue is not profit: inference, infrastructure, labour, acquisition and support costs are
    modelled before a price is quoted.
21. Churn is modelled, including the optimize-then-downgrade-to-maintenance path.
22. No unrealistic TAM and no unsupported ROI claims in any sales asset.
23. We state plainly what a client can verify independently, and we build the product so that
    the client can verify it without us.
24. We do not manufacture work to justify a subscription. If a client's visibility is stable and
    nothing needs changing, the report says so and the plan steps down.
