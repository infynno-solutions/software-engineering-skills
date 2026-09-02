---
name: make-evidence-based-engineering-decisions
description: "Bases decisions on the best available evidence rather than authority, taste, habit, or untested assumption. Use when someone claims a rewrite will be faster or a new queue will scale better with no benchmark or production data, when a teammate's preference is treated as sufficient justification between two libraries, or when a refactor is prioritized by gut feeling rather than profiling, error-rate, or churn data. Not when alternatives have not been enumerated yet (see evaluate-engineering-trade-offs first), or when the evidence concerns whether a past decision still holds (see revisit-decisions-as-context-changes)."
license: MIT
---

# Make Evidence-Based Engineering Decisions

## Intent

Base engineering decisions on the best available evidence rather than authority, taste, habit, or untested assumptions.

## Procedure

1. State the decision and hypothesis.
2. Identify what can be measured or estimated.
3. Gather existing evidence from the codebase, production, tests, benchmarks, logs, documentation, or prior decisions.
4. Identify what cannot be measured reliably.
5. Use a focused experiment when uncertainty materially affects the decision.
6. Record the evidence and uncertainty.
7. Decide based on the current evidence and define what would cause the decision to be revisited.

## Decision rules

- Prefer evidence over preference when evidence is available.
- Do not fabricate precision where measurements are weak.
- Treat qualitative evidence, precedent, and engineering judgment as legitimate inputs when quantitative evidence is unavailable—but label them accordingly.
- Measure expensive or uncertain assumptions before building large abstractions around them when practical.

## Anti-patterns

- “We know this will be faster” without a measurement or benchmark.
- Using benchmark results from a materially different workload.
- Hiding uncertainty behind exact-looking numbers.
- Treating seniority or authority as evidence.

## Exceptions and trade-offs

- Not every decision merits an experiment — spending a week benchmarking a choice that costs a day to reverse is itself poor evidence-based judgment.
- When no measurement is feasible in the available time, documented engineering judgment is an acceptable substitute, but it must be labeled as judgment, not presented as data.
- Evidence from a different workload, scale, or environment than the one in question should be discounted, not treated as equivalent to a direct measurement.

## Verification

A decision record should distinguish:

- observed facts
- measurements/estimates
- assumptions
- interpretation
- decision
