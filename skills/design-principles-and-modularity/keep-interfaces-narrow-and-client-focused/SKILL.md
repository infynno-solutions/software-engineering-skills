---
name: keep-interfaces-narrow-and-client-focused
description: Expose only the operations a client genuinely needs so clients do not inherit unnecessary coupling. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Keep Interfaces Narrow and Client-Focused

## Intent
Expose only the operations a client genuinely needs so clients do not inherit unnecessary coupling.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. List each client and the operations it consumes.
2. Identify dependencies on unused members or transitive details.
3. Split or reshape interfaces around client needs.
4. Verify changes to unused operations no longer affect unrelated clients.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Giant "god interfaces" used by many unrelated clients.
- Splitting every interface into trivial fragments.

## Exceptions and trade-offs
- A cohesive interface can remain broad when its operations form one stable client-facing contract.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`preserve-behavioral-substitutability`](../preserve-behavioral-substitutability/SKILL.md)
- [`invert-dependencies-around-stable-policy`](../invert-dependencies-around-stable-policy/SKILL.md)
