---
name: separate-responsibilities-by-reason-to-change
description: Separate responsibilities when they have materially different reasons for change. Identify the actors, policies, or concerns that can change independently and avoid forcing unrelated changes through the same module. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Separate Responsibilities by Reason to Change

## Intent
Separate responsibilities when they have materially different reasons for change. Identify the actors, policies, or concerns that can change independently and avoid forcing unrelated changes through the same module.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Identify plausible sources of change.
2. Check whether those changes occur independently.
3. Separate responsibilities only when the separation reduces change propagation or improves understanding.
4. Keep closely related behavior together when separation would add needless coupling.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Splitting every class until each has one method.
- Treating "one thing" as a mechanical rule without considering reasons for change.

## Exceptions and trade-offs
- A module may legitimately coordinate several operations when orchestration is its responsibility.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`keep-changes-localized`](../keep-changes-localized/SKILL.md)
