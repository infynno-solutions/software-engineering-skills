---
name: identify-the-shape-of-change
description: "Works out what is likely to change independently, so the design keeps those changes from propagating through unrelated parts of the system. Use when deciding whether billing and notification logic belong in the same service by asking what would force each to change, when a review comment says let's make this generic and a second real variation may not exist, or when two pieces of logic keep being edited together though they look unrelated. Not when the change points are already agreed and concrete designs need comparing (see evaluate-engineering-trade-offs), or when the question is whether to build the abstraction now at all (see defer-decisions-when-uncertainty-is-high)."
license: MIT
---

# Identify the Shape of Change

## Intent

Identify what is likely to change independently and arrange the design so those changes do not unnecessarily propagate through unrelated parts of the system.

This is a foundational reasoning skill for abstraction, modularity, architecture, and refactoring.

## Procedure

1. List the important changes the system is expected to absorb.
2. For each change, identify its reason, source, and likely frequency.
3. Group changes that are coupled by the same reason to change.
4. Separate changes that should evolve independently.
5. Choose the smallest boundary that prevents unnecessary propagation.

## Decision rules

- Separate things that change for different reasons when the cost of coupling is meaningful.
- Keep things together when they genuinely change together and separation would add needless complexity.
- Do not introduce an abstraction merely because two implementations are technically different.
- Prefer boundaries justified by actual change characteristics, not by pattern familiarity.

## Anti-patterns

- Abstracting every variation point “just in case.”
- Keeping unrelated concerns together because they currently live in one file.
- Splitting components based only on aesthetics.
- Assuming future change without identifying a plausible source or reason for it.

## Exceptions and trade-offs

- A boundary that isolates a real change source still costs indirection — for a component that changes rarely, that cost may outweigh the benefit even if the reasoning is technically sound.
- Two things that change for different reasons can still be kept together temporarily if the system is small enough that the coupling cost is negligible; revisit once the codebase grows.
- Predicting change sources is judgment, not certainty — when evidence is thin, prefer the boundary that is cheapest to introduce later over one that is expensive to introduce now.

## Verification

For every proposed boundary, the agent should be able to state:

- What change does this boundary isolate?
- Why would that change happen independently?
- What dependencies cross the boundary?
- What complexity does the boundary introduce?
- Would removing the boundary materially increase future change cost?
