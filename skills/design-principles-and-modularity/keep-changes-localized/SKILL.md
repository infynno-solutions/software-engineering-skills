---
name: keep-changes-localized
description: "Structure code so common changes touch a small, coherent region rather than rippling through unrelated modules. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Keep Changes Localized

## Intent
Structure code so common changes touch a small, coherent region rather than rippling through unrelated modules.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Trace a representative change through the dependency graph.
2. Find unrelated modules affected by the same change.
3. Group or decouple responsibilities to localize the change.
4. Verify the resulting change path with tests and dependency analysis.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Creating abstractions that merely move a change through many layers.
- Splitting code without reducing change propagation.

## Exceptions and trade-offs
- Some duplication can be cheaper than coupling when it preserves independence.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`separate-responsibilities-by-reason-to-change`](../separate-responsibilities-by-reason-to-change/SKILL.md)
- [`design-for-extension-without-fragile-modification`](../design-for-extension-without-fragile-modification/SKILL.md)
