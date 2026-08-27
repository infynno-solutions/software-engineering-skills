---
name: iterate-design-before-committing
description: "Treats design as iterative: explore alternatives, test risky assumptions, and refine before an expensive commitment. Use when a design doc goes straight from problem statement to a single architecture with no alternative written down, when a risky assumption such as a third-party API's behavior or a query's performance at scale underlies the whole design and has never been tested, or when a spike's findings never became an explicit decision. Not when alternatives already exist and are being compared (see evaluate-engineering-trade-offs), or when the problem itself is not yet understood (see frame-the-problem)."
license: MIT
---

# Iterate Design Before Committing

## Intent

Treat design as an iterative engineering activity: explore alternatives, compare them, test important assumptions, and refine the solution before making an expensive commitment.

## Procedure

1. Produce at least two plausible approaches for material design decisions.
2. Compare them against explicit criteria.
3. Identify assumptions that can be tested cheaply.
4. Prototype, benchmark, spike, or inspect the codebase as appropriate.
5. Choose the smallest design that survives the evaluation.

## Decision rules

- Do not treat the first workable design as automatically good.
- The amount of design exploration should be proportional to the cost of being wrong.
- Prefer cheap experiments over prolonged speculation when practical.
- Iteration does not justify endlessly postponing implementation.

## Anti-patterns

- Coding the first idea immediately for a large architectural change.
- Generating many designs with no decision criteria.
- Prototyping without converting findings into a decision.
- Designing everything up front when small feedback cycles would reveal more information.

## Exceptions and trade-offs

- Scale the exploration to the stakes: a two-line bug fix does not need two competing designs, and demanding them wastes time without reducing risk.
- A cheap prototype that answers the risky question is worth more than a long comparison table of untested designs — spend the budget on testing assumptions, not on generating options.
- Iteration has a stopping point: once the dominant uncertainty is resolved, commit rather than continuing to explore for its own sake.

## Verification

For a non-trivial design, retain a brief record of:

- alternatives considered
- important assumptions
- evaluation performed
- selected approach
- rejected alternatives and why
