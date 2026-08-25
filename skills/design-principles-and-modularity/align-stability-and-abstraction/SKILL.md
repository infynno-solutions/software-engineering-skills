---
name: align-stability-and-abstraction
description: "Use abstraction where stable components need flexibility, while avoiding stable concrete components that become difficult to change and unstable abstract components that add little value. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Align Stability and Abstraction

## Intent
Use abstraction where stable components need flexibility, while avoiding stable concrete components that become difficult to change and unstable abstract components that add little value.

## When to apply
Apply this skill when the current task, code review, design change, incident, test strategy, or engineering-process decision materially involves this concern. First establish the concrete problem; do not invoke the skill only because its terminology appears in the task.

## Procedure
1. Estimate component stability from incoming/outgoing dependencies.
2. Estimate where abstraction is actually needed.
3. Compare the component to its intended role in the dependency graph.
4. Adjust coupling or abstraction when the combination creates a problematic component.

## Decision rules
- Prefer the smallest intervention that addresses the observed problem.
- Make assumptions and trade-offs explicit when they materially affect the decision.
- Preserve existing behavior unless the task explicitly requires a behavior change.
- Prefer evidence from the codebase, tests, measurements, and system constraints over personal preference.

## Anti-patterns
- Applying abstractness metrics as a target rather than a diagnostic.
- Making every stable component fully abstract.

## Exceptions and trade-offs
- Metrics are heuristics; architectural intent and change patterns matter more.

## Verification
- Verify the affected behavior with the narrowest reliable automated checks available.
- Inspect the resulting structure for unnecessary complexity or new coupling.
- For system-level changes, verify operational and integration consequences, not only local correctness.


## Related skills
- [`prevent-dependency-cycles`](../prevent-dependency-cycles/SKILL.md)
- [`group-components-by-cohesion`](../group-components-by-cohesion/SKILL.md)
