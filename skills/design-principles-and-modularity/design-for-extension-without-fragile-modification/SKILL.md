---
name: design-for-extension-without-fragile-modification
description: Use stable seams to accommodate foreseeable variation when modifying existing behavior repeatedly would spread risk. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Design for Extension Without Fragile Modification

## Intent
Use stable seams to accommodate foreseeable variation when modifying existing behavior repeatedly would spread risk.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify a genuine variation point.
2. Estimate how often and how independently it is likely to change.
3. Choose an extension mechanism that keeps stable policy intact.
4. Reject the abstraction if the variation is speculative or the seam costs more than it saves.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Adding factories/interfaces for every possible future feature.
- Using OCP as a mandate for inheritance-heavy frameworks.

## Exceptions and trade-offs
- Small, stable systems may be better served by direct code until variation becomes real.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`keep-changes-localized`](../keep-changes-localized/SKILL.md)
- [`preserve-behavioral-substitutability`](../preserve-behavioral-substitutability/SKILL.md)
