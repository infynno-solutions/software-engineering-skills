---
name: design-for-independent-module-development
description: "Structure components and interfaces so teams can understand, modify, test, and integrate work with minimal unnecessary coordination. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Design for Independent Development

## Intent
Structure components and interfaces so teams can understand, modify, test, and integrate work with minimal unnecessary coordination.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Map ownership and change boundaries.
2. Find areas requiring synchronized edits.
3. Stabilize interfaces where independent work is valuable.
4. Use dependency direction and small contracts to reduce coordination cost.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Architecture that mirrors the org chart without regard to technical cohesion.
- Assuming every team needs an independently deployable service.

## Exceptions and trade-offs
- The right granularity depends on team size, system lifecycle, and deployment constraints.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`manage-abstraction-debt`](../manage-abstraction-debt/SKILL.md)
