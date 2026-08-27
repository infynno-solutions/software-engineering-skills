---
name: manage-essential-vs-accidental-complexity
description: "Distinguishes complexity inherent to the problem from complexity introduced by the chosen design, and actively reduces the latter. Use when a PR adds a factory, a strategy interface, and a config layer for a single if/else worth of variation; when a review flags this is hard to follow and it is unclear whether the domain or the implementation is the cause; or when enterprise patterns appear on a small system with no scale problem to justify them. Not when picking between several already-simple designs (see evaluate-engineering-trade-offs), or when the question is whether a variation point deserves a boundary given expected change (see identify-the-shape-of-change first)."
license: MIT
---

# Manage Essential vs Accidental Complexity

## Intent

Distinguish complexity inherent to the problem from complexity introduced by the chosen design, and actively reduce the latter.

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

## Exceptions and trade-offs

- Some accidental complexity is the price of working within a platform, framework, or legacy integration — the goal is minimizing it, not eliminating what the environment genuinely requires.
- Complexity introduced to make a system testable, observable, or debuggable is often essential in practice even though it is not required by the domain itself — weigh it against those operational needs, not just the literal problem statement.
- Removing an abstraction that several teams already depend on may cost more in migration risk than leaving it in place, even if it was accidental in origin.

## Verification

Ask:

- Can the solution be explained more simply without losing a requirement?
- Which parts of the design exist only because of the current implementation?
- Does each abstraction reduce cognitive load or isolate a meaningful concern?
- Can an engineer safely ignore most of the system while working on one part?
