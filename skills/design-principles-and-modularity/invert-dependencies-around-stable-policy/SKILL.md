---
name: invert-dependencies-around-stable-policy
description: "Make high-level policy independent of volatile implementation details by placing abstractions at the dependency boundary. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Invert Dependencies Around Stable Policy

## Intent
Make high-level policy independent of volatile implementation details by placing abstractions at the dependency boundary.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify policy and detail.
2. Determine which side should remain stable.
3. Define the minimal abstraction at the stable boundary.
4. Make details depend on the abstraction and inject/assemble the concrete implementation at the edge.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Inverting dependencies without a real volatility or ownership reason.
- Putting abstractions in the most volatile package by default.

## Exceptions and trade-offs
- Direct dependencies are acceptable inside a cohesive stable component.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`keep-interfaces-narrow-and-client-focused`](../keep-interfaces-narrow-and-client-focused/SKILL.md)
- [`control-dependency-direction`](../control-dependency-direction/SKILL.md)
