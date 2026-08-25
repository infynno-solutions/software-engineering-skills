---
name: manage-essential-vs-accidental-complexity
description: Distinguish complexity inherent to the problem from complexity introduced by the chosen design, and actively reduce the latter. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Manage Essential vs Accidental Complexity

## Intent

Distinguish complexity inherent to the problem from complexity introduced by the chosen design, and actively reduce the latter.

## Apply when

Use this skill when evaluating:

- architecture proposals
- abstractions
- infrastructure choices
- difficult code
- framework usage
- performance work
- “enterprise” patterns or layers
- any design that appears harder to understand than the problem itself

## Procedure

1. Describe the underlying problem without the current implementation.
2. Identify which complexity comes from the real domain, scale, correctness requirements, or unavoidable constraints.
3. Identify complexity introduced by abstractions, dependencies, state, indirection, configuration, or accidental coupling.
4. Remove or simplify accidental complexity where possible.
5. Preserve only complexity that is justified by the problem or an explicit requirement.

## Decision rules

- Prefer understandable designs over clever designs.
- Minimize the amount of complexity a developer must hold in mind at one time.
- Do not mistake abstraction count for design quality.
- Consider maintenance, integration, testing, and debugging cost—not just initial implementation effort.

## Anti-patterns

- Adding layers without reducing coupling or complexity.
- Premature generalization.
- Optimizing for hypothetical scale while making the current system substantially harder to reason about.
- Treating sophisticated technology as inherently more robust.

## Verification

Ask:

- Can the solution be explained more simply without losing a requirement?
- Which parts of the design exist only because of the current implementation?
- Does each abstraction reduce cognitive load or isolate a meaningful concern?
- Can an engineer safely ignore most of the system while working on one part?


## Related skills

- ENG-08 Prefer the Simplest Adequate Solution
- CODE-05 Minimize Function and Class Complexity
- MOD-11 Control Coupling Across Boundaries
