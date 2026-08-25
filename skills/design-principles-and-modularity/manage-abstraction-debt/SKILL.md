---
name: manage-abstraction-debt
description: Treat abstractions as design investments: introduce them when they pay for real variation or dependency control, and remove abstractions that add more complexity than value. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Manage Abstraction Debt

## Intent
Treat abstractions as design investments: introduce them when they pay for real variation or dependency control, and remove abstractions that add more complexity than value.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify the change/problem the abstraction is supposed to solve.
2. Measure or reason about actual reuse, variation, and coupling.
3. Compare abstraction cost with the cost of direct code.
4. Refactor when the original abstraction no longer earns its keep.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Speculative generalization.
- Keeping abstractions forever because removing them feels like regression.

## Exceptions and trade-offs
- Premature abstraction and insufficient abstraction are both failure modes.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`control-coupling-across-boundaries`](../control-coupling-across-boundaries/SKILL.md)
- [`design-for-independent-module-development`](../design-for-independent-module-development/SKILL.md)
