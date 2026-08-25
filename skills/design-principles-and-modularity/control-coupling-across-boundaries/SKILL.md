---
name: control-coupling-across-boundaries
description: "Minimize the amount of knowledge and implementation detail crossing module/component boundaries. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Control Coupling Across Boundaries

## Intent
Minimize the amount of knowledge and implementation detail crossing module/component boundaries.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Inventory data, control, temporal, and semantic dependencies crossing the boundary.
2. Hide representations and volatile mechanisms.
3. Narrow the contract to what the consumer needs.
4. Verify that internal changes do not propagate unnecessarily.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Passing internal data structures across boundaries.
- Using facades that merely conceal a deep shared dependency graph.

## Exceptions and trade-offs
- Some coupling is necessary; the goal is purposeful, low-cost coupling.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`group-components-by-cohesion`](../group-components-by-cohesion/SKILL.md)
- [`manage-abstraction-debt`](../manage-abstraction-debt/SKILL.md)
