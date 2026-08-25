---
name: revisit-process-rules-using-evidence
description: "Treat engineering rules as hypotheses that should be revisited when technologies, costs, and observed outcomes change. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Revisit Process Rules Using Evidence

## Intent
Treat engineering rules as hypotheses that should be revisited when technologies, costs, and observed outcomes change.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. State the concrete engineering problem and desired outcome.
2. Inspect the relevant code, architecture, tests, data flow, or team/process context.
3. Choose the smallest change or practice that addresses the observed problem.
4. Verify both the intended result and the important side effects or trade-offs.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Apply the guidance as a mechanical rule without examining context.
- Introduce complexity without demonstrating the problem it solves.

## Exceptions and trade-offs
- Use project constraints, language/runtime capabilities, risk, and lifecycle to adapt the practice.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`treat-tooling-as-an-engineering-product`](../treat-tooling-as-an-engineering-product/SKILL.md)
