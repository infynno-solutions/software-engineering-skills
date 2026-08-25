---
name: make-evidence-based-engineering-decisions
description: "Base engineering decisions on the best available evidence rather than authority, taste, habit, or untested assumptions. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Make Evidence-Based Engineering Decisions

## Intent

Base engineering decisions on the best available evidence rather than authority, taste, habit, or untested assumptions.

## Apply when

Use this skill for:

- architecture choices
- performance claims
- technology selection
- process changes
- refactoring priorities
- reliability decisions
- productivity improvements

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

## Verification

A decision record should distinguish:

- observed facts
- measurements/estimates
- assumptions
- interpretation
- decision


## Related skills

- ENG-05 Evaluate Engineering Trade-offs
- ENG-09 Iterate Design Before Committing
- ENG-10 Revisit Decisions as Context Changes
