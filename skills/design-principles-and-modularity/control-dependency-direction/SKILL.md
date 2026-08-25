---
name: control-dependency-direction
description: "Treat dependency arrows as an architectural design tool and ensure they reinforce stability, ownership, and desired change flow. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Control Dependency Direction

## Intent
Treat dependency arrows as an architectural design tool and ensure they reinforce stability, ownership, and desired change flow.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Build a dependency graph.
2. Mark volatile and stable components.
3. Find dependencies pointing toward volatile policy.
4. Invert or relocate dependencies where doing so reduces change propagation.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Optimizing diagrams instead of actual change behavior.
- Creating interface-only dependencies that still leak implementation details.

## Exceptions and trade-offs
- A dependency direction is useful only insofar as it supports real lifecycle and change goals.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`invert-dependencies-around-stable-policy`](../invert-dependencies-around-stable-policy/SKILL.md)
- [`prevent-dependency-cycles`](../prevent-dependency-cycles/SKILL.md)
