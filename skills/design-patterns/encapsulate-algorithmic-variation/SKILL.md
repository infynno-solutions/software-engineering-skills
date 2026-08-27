---
name: encapsulate-algorithmic-variation
description: "Separates a varying algorithm from the stable context using it (Strategy), or factors an invariant skeleton with variable steps (Template Method). Use when logic branches on a mode flag between interchangeable ways of computing the same result - pricing rules, sort comparators, compression algorithms - or when several algorithms share a sequence but differ in a few steps. Not for layering optional behavior onto an object (see compose-and-augment-object-behavior), not when only one stable algorithm exists, and not for deciding whether the variation is real (see encapsulate-what-varies)."
license: MIT
---

# Encapsulate Algorithmic Variation

## Intent
Separate an algorithm or policy that varies from the context that uses it, so strategies can be selected, replaced, or extended without rewriting the stable context.

## Procedure
1. Identify the algorithmic decision point — the branch, flag, or duplicated-with-small-differences function that signals variation.
2. Determine whether the alternative algorithms share a meaningful contract (same inputs/outputs, same role in the larger flow) or whether they only superficially resemble each other.
3. Define the smallest strategy interface that captures just the varying behavior, not incidental details specific to one implementation.
4. Implement each algorithm independently against that interface.
5. Inject or compose the selected strategy into the context, rather than having the context construct or branch on it internally.
6. Keep selection policy (which strategy to use, and why) separate from the algorithm implementations themselves.

## Decision rules
- Use Strategy when algorithm variation is meaningful and ongoing, and the context can stay stable while the algorithm changes.
- Template Method is useful when the invariant algorithm skeleton should remain in one base abstraction, with only specific steps varying by subclass or hook.
- Prefer composition (Strategy) over inheritance (Template Method) when runtime replacement of the algorithm or low coupling between context and algorithm matters more than sharing a fixed skeleton.
- Do not create a strategy hierarchy for a single stable algorithm with no realistic second implementation.

## Anti-patterns
- Boolean flags selecting between unrelated algorithms bolted onto one function, rather than distinct implementations of a shared interface.
- Strategy interfaces bloated with methods unrelated to the actually-varying behavior, forcing every implementation to stub out irrelevant methods.
- A strategy abstraction that has exactly one implementation and merely renames a single existing function call with no near-term second variant planned.
- Putting selection logic (deciding which strategy to use) inside every strategy implementation instead of in the context or a dedicated selector.

## Exceptions and trade-offs
- If the branching logic is small (two clear cases, unlikely to grow) and unlikely to change, a simple conditional is more readable than a strategy interface, a factory, and two classes.
- Template Method couples subclasses to a base class's control flow via inheritance, which is harder to change later than Strategy's composition-based coupling — prefer Strategy when you expect the shared structure itself to shift.
- Introducing a strategy interface ahead of a second real implementation (speculative generality) adds abstraction cost before it's earned; wait for a second concrete case unless the interface is very cheap and obviously correct.

## Verification
- Can the context operate correctly without knowing which concrete algorithm/strategy it is using?
- Can a strategy be replaced or a new one added without modifying the context or existing strategies?
- Is the strategy interface no larger than the variation it actually represents?
