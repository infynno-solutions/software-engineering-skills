---
name: encapsulate-what-varies
description: "Identifies a source of variation that changes for its own reasons and walls it off behind a narrow boundary. Use when a conditional keeps gaining branches for new implementations, requirements name alternative strategies, or a class keeps changing for unrelated algorithmic reasons. Not for the specific mechanism of replacing a type switch with dispatch (see use-polymorphism-to-localize-variation), infrastructure or vendor swaps (see design-for-replaceability), the module-level open/closed seam (see design-for-extension-without-fragile-modification), or naming the concrete pattern (see encapsulate-algorithmic-variation)."
license: MIT
---

# Encapsulate What Varies

## Intent

Design around change by separating independently varying behavior from the parts of the system that should remain stable.

## Procedure

1. Identify the behavior that varies.
2. Confirm that it varies for a reason different from the surrounding behavior.
3. Identify the stable contract around that variation.
4. Extract the variable behavior behind that contract.
5. Compose or inject the selected implementation.
6. Keep the stable caller independent of the concrete variants.
7. Re-check that the abstraction does not introduce more concepts than the variation justifies.

## Decision rules

- Encapsulate variation that is real, recurring, or explicitly required.
- Do not infer variation solely from imagination.
- Prefer a small stable boundary over a conditional spread through many clients.
- Reuse the same variation boundary when multiple consumers need the same independent behavior.

## Anti-patterns

- "Future-proofing" every branch with speculative interfaces.
- A giant interface containing unrelated variants.
- One class with many flags that select unrelated algorithms.
- Encapsulating something that has no credible independent change pressure.

## Exceptions and trade-offs

- If a "variation" has exactly one known implementation and no second is credible even in the near future, extracting a boundary is speculative generality — wait until a second real case appears, or is contractually certain.
- Two behaviors that look similar today but vary for unrelated business reasons should not share one encapsulation boundary just because their signatures happen to match; conflating them creates a contract that leaks whichever variant was designed first.
- Runtime-injected variation (a strategy object, a plugin) costs an extra indirection hop even in a single-implementation case; a plain `if` can stay clearer when the two branches really are permanently exactly two.

## Verification

- Can one variant be introduced or replaced without editing every consumer?
- Is the stable contract understandable without knowing the variants?
- Does each variant implement one coherent behavior?
- Did the abstraction reduce change propagation rather than merely move conditionals?
