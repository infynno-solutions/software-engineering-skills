---
name: preserve-behavioral-substitutability
description: Require replacements behind an abstraction to honor the behavioral expectations clients rely on, not merely the method signatures. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Preserve Behavioral Substitutability

## Intent
Require replacements behind an abstraction to honor the behavioral expectations clients rely on, not merely the method signatures.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify the contract clients actually depend on.
2. Check preconditions, postconditions, invariants, error behavior, and side effects.
3. Verify each implementation can substitute without surprising clients.
4. Move abstraction boundaries when the contract is unstable or contradictory.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Using inheritance solely because names or shapes look related.
- Treating type compatibility as proof of substitutability.

## Exceptions and trade-offs
- Some languages/platforms enforce parts of the contract; behavioral verification is still needed.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`design-for-extension-without-fragile-modification`](../design-for-extension-without-fragile-modification/SKILL.md)
- [`keep-interfaces-narrow-and-client-focused`](../keep-interfaces-narrow-and-client-focused/SKILL.md)
