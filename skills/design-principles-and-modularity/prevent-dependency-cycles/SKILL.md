---
name: prevent-dependency-cycles
description: "Keep component/module dependencies acyclic so components remain buildable, testable, releasable, and understandable. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Prevent Dependency Cycles

## Intent
Keep component/module dependencies acyclic so components remain buildable, testable, releasable, and understandable.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify cycles in the dependency graph.
2. Find the conceptual reason for the cycle.
3. Break it through dependency inversion, extraction of shared policy, or relocation.
4. Re-run dependency checks after the change.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Suppressing cycle detection without fixing the structure.
- Creating a dumping-ground shared module just to break a cycle.

## Exceptions and trade-offs
- Some language-level cyclic references may be harmless; the skill targets architectural cycles that impede isolation and change.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`control-dependency-direction`](../control-dependency-direction/SKILL.md)
- [`align-stability-and-abstraction`](../align-stability-and-abstraction/SKILL.md)
