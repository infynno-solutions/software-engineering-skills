---
name: compose-patterns-without-pattern-accumulation
description: "Evaluates a design that already combines several patterns, keeping only those still addressing a distinct live force and flattening the rest. Use when a Factory produces Strategies that are wrapped in Decorators and each layer's value is unclear, or when a review finds pattern density beyond what current requirements justify. Not for naming a force before any pattern is chosen (see recognize-recurring-design-forces), choosing among candidates for a single force (see select-patterns-by-forces-and-consequences), or retiring an unused abstraction generally (see manage-abstraction-debt)."
license: MIT
---

# Compose Patterns Without Pattern Accumulation

## Intent
Use multiple patterns together as cooperating structures when they each address a distinct force, while avoiding accumulation of patterns until the design becomes more abstract and harder to follow than the original problem required.

## Procedure
1. Evaluate each pattern present in the design independently against a real, currently-present force — not the force that justified it historically.
2. Identify interactions between patterns and any abstractions they share, such as a common interface used by both a Factory's products and a Strategy's implementations.
3. Check whether the combination creates cycles, unnecessary indirection, or duplicated concepts (e.g., a Decorator and a Proxy both intercepting the same call for no distinct reason).
4. Remove or flatten patterns whose forces are no longer present — a Strategy with only one implementation left, a Factory with one product, a Mediator coordinating two objects.
5. Prefer a dense, coherent design over a catalog of unrelated pattern instances stitched together because each one seemed locally reasonable.

## Decision rules
- Patterns can compose and reinforce one another when each addresses a distinct, real force in the same area of the design.
- A combination is justified only when each participating pattern, examined on its own, still addresses a force that is actually present.
- Reassess the combined design after requirements change — a combination justified a year ago may no longer be.
- The resulting system should be easier to understand and change than the pre-pattern design; if it isn't, the combination has failed its purpose regardless of how "correctly" each pattern was applied.

## Anti-patterns
- Pattern soup: multiple patterns layered in the same area with no one able to explain what force each layer removes.
- Naming every class after a pattern (`XxxFactory`, `XxxStrategy`, `XxxAdapter`) as a stylistic habit rather than because the structure is warranted.
- Combining patterns because a reference catalog lists them as commonly interacting, without checking whether that interaction applies here.
- Preserving obsolete pattern layers because they were once justified, even after the variation or force that justified them has disappeared.

## Exceptions and trade-offs
- A codebase with genuinely orthogonal forces (creation varies, algorithm varies, and access needs control) may legitimately need three cooperating patterns at once — density is not automatically a smell if each layer maps to a distinct, real force.
- Removing an "unused" pattern layer has a cost too: if the variation it supported is likely to return soon (a second Strategy implementation is already planned), collapsing it prematurely just means re-adding it shortly after.
- When in doubt during a review, prefer flagging the combination for discussion over silently ripping out layers — some accumulated structure may be intentional scaffolding for near-term work.

## Verification
- Can each pattern's purpose in the combination be stated independently, in one sentence, without referencing the others?
- Does the combination measurably reduce coupling or change amplification compared to not having it, or does it just add ceremony?
- Is the final design simpler to reason about than the plausible alternatives, including the alternative of removing one or more of the patterns?
