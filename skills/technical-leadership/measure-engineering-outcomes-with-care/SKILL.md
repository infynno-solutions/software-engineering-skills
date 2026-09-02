---
name: measure-engineering-outcomes-with-care
description: "Designs and stewards engineering measurement so metrics improve real outcomes rather than produce good-looking numbers over a degrading reality. Use when proposing a new team metric such as deploy frequency, lead time, coverage, or velocity; when building a dashboard that will feed resourcing or performance decisions; or when a metric is being gamed - coverage rising via trivial tests, tickets shrinking, incidents no longer being filed. Not for choosing what to build or prioritizing roadmap work, and not for instrumenting a running system for operators (see make-systems-operable)."
license: MIT
---

# Measure Engineering Outcomes With Care

## Intent
Use metrics to genuinely improve engineering outcomes, not to create numbers that look good while the underlying reality degrades.

## Procedure
1. Start from the outcome you actually care about (reliability, delivery speed, code health) and only then look for a metric that plausibly tracks it — never start from "what can we easily measure."
2. For each candidate metric, explicitly ask how someone could improve the number without improving the underlying outcome, and judge whether that gaming path is easy and likely.
3. Prefer metrics that are hard to game cheaply (deployment frequency, change failure rate, time-to-restore) over ones that individuals directly control the surface of (lines of code, ticket count, story points).
4. Pair an output metric with at least one guardrail metric that would catch the obvious gaming path — e.g., pair velocity with defect escape rate so shrinking tickets to inflate throughput shows up elsewhere.
5. Decide and state upfront how the metric will and will not be used — informing team retros is different from feeding individual performance review, and the latter changes gaming incentives substantially.
6. Roll out a new metric with the team's input on what it might distort, since the people whose work it measures will find the gaming paths you didn't think of.
7. Review the metric periodically against the original outcome it was meant to track, and retire or revise it once you observe the number moving while the outcome does not.

## Decision rules
- If you can't articulate the outcome a metric is meant to track, don't adopt the metric.
- Never tie an individual-level metric directly to performance review without accepting that it will be optimized specifically for that review, often at the expense of the outcome.
- Prefer trend and direction over absolute target numbers for team health metrics — a fixed target invites gaming to hit it exactly.
- Any metric used to compare teams needs enough shared context (team size, system maturity, domain difficulty) to be a fair comparison, or it shouldn't be used comparatively at all.

## Anti-patterns
- Adopting an industry-standard metric (DORA, coverage percentage) wholesale without checking whether it fits this team's actual bottleneck or outcome.
- Using a single metric as the sole input to a consequential decision (a PIP, a team's headcount) instead of one signal among several including qualitative judgment.
- Publishing a leaderboard-style dashboard that ranks individuals or teams by an easily gamed number, which reliably produces the gaming rather than the outcome.
- Keeping a metric around indefinitely after its number has visibly decoupled from the outcome, out of inertia or because a dashboard already exists for it.

## Exceptions and trade-offs
- A crude proxy metric can be a legitimate starting point when nothing better exists yet, provided it's explicitly labeled as provisional and revisited once better signal is available.
- For a small team with high trust and visibility into each other's work, formal metrics may add overhead without adding information a good manager doesn't already have through direct observation.
- Some outcomes (code quality, architectural health) resist quantification; a well-reasoned qualitative review can be more honest than forcing a number onto something a number doesn't capture well.

## Verification
- For each proposed metric, confirm you can state the outcome it tracks and at least one plausible way to game it without improving that outcome.
- Confirm the intended use (informational, retro input, performance input) is stated explicitly before rollout, not decided implicitly after the fact.
- Check that a guardrail or counter-metric exists for any output metric that individuals can directly influence.
- Periodically confirm the metric and the outcome are still moving together; if they've diverged, that's grounds to revise or retire it.
