---
name: identify-the-shape-of-change
description: "Identify what is likely to change independently and arrange the design so those changes do not unnecessarily propagate through unrelated parts of the system. This is a foundational reasoning skill for abstraction, modularity, architecture, and refactoring. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Identify the Shape of Change

## Intent

Identify what is likely to change independently and arrange the design so those changes do not unnecessarily propagate through unrelated parts of the system.

This is a foundational reasoning skill for abstraction, modularity, architecture, and refactoring.

## Apply when

Use this skill before:

- introducing an abstraction
- splitting a module
- selecting a design pattern
- designing an API boundary
- restructuring a subsystem
- deciding whether two responsibilities belong together

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

## Verification

For every proposed boundary, the agent should be able to state:

- What change does this boundary isolate?
- Why would that change happen independently?
- What dependencies cross the boundary?
- What complexity does the boundary introduce?
- Would removing the boundary materially increase future change cost?


## Related skills

- ENG-07 Defer Decisions When Uncertainty Is High
- OO-04 Encapsulate What Varies
- MOD-01 Separate Responsibilities by Reason to Change
- MOD-02 Keep Changes Localized
