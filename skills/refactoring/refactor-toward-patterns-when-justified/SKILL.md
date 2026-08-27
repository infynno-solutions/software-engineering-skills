---
name: refactor-toward-patterns-when-justified
description: "Introduces a named pattern such as Strategy or Factory into existing code only once repeated variation justifies the indirection, reached through incremental refactoring. Use once two or three concrete instances of the same variation exist today, or a class is accumulating constructor parameters and flags to switch behavior. Not for simplifying a single messy conditional without a named pattern (see simplify-conditionals-and-control-flow, usually the precondition), nor for choosing between candidate patterns in a fresh design (see select-patterns-by-forces-and-consequences)."
license: MIT
---

# Refactor Toward Patterns When Justified

## Intent
Introduce a pattern only when repeated variation and forces justify it, and evolve toward the pattern incrementally through refactoring.

## Procedure
1. Confirm the trigger: at least two, ideally three, concrete instances of the same variation exist in the code today, not hypothetical future ones.
2. Name the axis of variation precisely, such as "how a discount is computed per customer tier" — the pattern must map to a real axis, not a generic desire for flexibility.
3. Identify which pattern's forces match: Strategy for interchangeable algorithms, Factory for varied construction, Decorator for stackable behavior, Observer for one-to-many notification. Reject the pattern if the forces don't actually match.
4. Refactor toward the pattern incrementally: extract the varying behavior into its own unit first, then introduce the abstraction once at least two concrete implementations exist side by side.
5. Replace the original conditional or switch with dispatch through the new abstraction, verifying each replaced call site individually.
6. Name the abstraction after the domain concept it represents, not after the pattern itself — "TieredDiscountStrategy," not "Strategy1."

## Decision rules
- Require at least two real, existing call sites or variants before introducing the pattern; "we'll probably need this" is not sufficient justification.
- Prefer the simplest structure that removes the duplication — a small Strategy interface over a full plugin or factory framework unless the variation count and churn justify the framework.
- If the variation is closed and rarely changes, such as three fixed cases unchanged for years, a straightforward conditional may remain simpler than a pattern.
- Choose the pattern whose forces match the actual extension axis, not the pattern whose name matches the code's superficial shape.

## Anti-patterns
- Introducing a Strategy, Factory, or Visitor for a single concrete case "in case we need more later."
- Applying a pattern by matching a tutorial example rather than checking that this codebase's actual forces — what varies, how often, who extends it — match.
- Replacing a short if/else with a much larger pattern implementation because the pattern is the "textbook correct" answer, not because it reduces real complexity here.
- Leaving the old conditional path in place alongside the new pattern instead of fully migrating call sites, so both must be maintained.

## Exceptions and trade-offs
- Frameworks or plugin systems intended for external, not just internal, extension may justify a pattern ahead of a second internal use case, since the "second user" is external and unobservable in the repo.
- In performance-critical code, some patterns add indirection, such as virtual dispatch or decorator chains, that may cost more than the conditional it replaces — profile before committing.

## Verification
- Confirm at least two concrete, real implementations exist behind the new abstraction, not one implementation plus a hypothetical.
- Confirm all former call sites of the old conditional or switch now go through the pattern, with no leftover parallel path.
- Confirm the resulting code is measurably simpler to extend — adding a third variant should now touch one new file or class, not the original conditional.
