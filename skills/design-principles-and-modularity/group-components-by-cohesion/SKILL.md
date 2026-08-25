---
name: group-components-by-cohesion
description: Group classes into components according to shared change/reuse/release characteristics while respecting the tension between cohesion goals. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Group Components by Cohesion

## Intent
Group classes into components according to shared change/reuse/release characteristics while respecting the tension between cohesion goals.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify classes that change together.
2. Identify classes reused and released together.
3. Identify dependencies on individual classes that cause unnecessary release propagation.
4. Choose a component boundary balancing closure, reuse, and release cost.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Maximizing any single cohesion principle blindly.
- Making components large solely to avoid duplication.

## Exceptions and trade-offs
- The optimal balance changes as a system and organization mature.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`align-stability-and-abstraction`](../align-stability-and-abstraction/SKILL.md)
- [`control-coupling-across-boundaries`](../control-coupling-across-boundaries/SKILL.md)
