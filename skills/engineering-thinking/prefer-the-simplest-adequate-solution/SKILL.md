---
name: prefer-the-simplest-adequate-solution
description: "Chooses the solution that satisfies the actual requirements with the least unnecessary indirection and speculative flexibility. Use when choosing between a plain function and a full strategy hierarchy for logic with exactly one implementation today, when a framework or library is proposed for what a few lines of existing-language code would handle, or when a reliability improvement is scoped larger than the failure mode it addresses. Not when several non-trivial alternatives need comparing on cost, risk, and speed (see evaluate-engineering-trade-offs), or when it is unclear whether the complexity is essential or accidental (see manage-essential-vs-accidental-complexity first)."
license: MIT
---

# Prefer the Simplest Adequate Solution

## Intent

Choose a solution that satisfies the actual requirements while introducing as little unnecessary complexity, indirection, and speculative flexibility as practical.

## Procedure

1. Establish the actual requirements and constraints.
2. Identify the simplest design that can satisfy them.
3. List additional machinery introduced by more elaborate alternatives.
4. Keep an elaborate option only when it buys a requirement, meaningful risk reduction, or a justified future-change benefit.

## Decision rules

- Simplicity means fewer unnecessary concepts, not merely fewer lines of code.
- Do not reject necessary complexity simply because it is complicated.
- Do not add flexibility without a credible change driver.
- A simple design that is wrong is not preferable to a more complex design that satisfies a real requirement.

## Anti-patterns

- Abstraction for abstraction's sake.
- Framework-driven architecture.
- Configurability without a known configuration need.
- Premature optimization.
- “Enterprise” layering that increases navigation without isolating meaningful concerns.

## Exceptions and trade-offs

- "Simplest" is judged against the actual requirements, not against an imagined minimal version that quietly drops a real one — cutting a requirement to look simpler is not a valid simplification.
- A known near-term requirement (already committed, not merely plausible) can justify a small amount of extra structure now rather than a rewrite in a month.
- When two designs are close in complexity, prefer the one with a smaller blast radius if it breaks, not just the one with fewer moving parts.

## Verification

Ask:

- What requirement justifies each major abstraction or mechanism?
- Can one or more layers be removed without violating a requirement?
- Does the extra machinery reduce total lifecycle cost?
