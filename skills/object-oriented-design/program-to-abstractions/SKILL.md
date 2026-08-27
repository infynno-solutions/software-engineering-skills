---
name: program-to-abstractions
description: "The general habit of making a consumer depend on a small contract shaped by its own needs rather than a concrete class. Use when several implementations can satisfy one client need, an algorithm or policy varies independently of its consumer, or a test needs a stable seam. Not for judging whether one specific dependency is volatile enough to deserve a swap boundary (see design-for-replaceability), hiding an object's own internals (see encapsulate-representation), relocating construction instead of adding an interface (see separate-collaboration-from-implementation), or trimming an existing interface per client (see keep-interfaces-narrow-and-client-focused)."
license: MIT
---

# Program to Abstractions

## Intent

Reduce implementation dependencies by expressing collaboration through an abstraction that captures what the consumer actually needs.

## Procedure

1. Identify the client's actual required behavior.
2. Define the smallest meaningful contract for that behavior.
3. Make the consumer depend on the contract.
4. Make concrete implementations satisfy that contract.
5. Put construction/wiring at the appropriate composition boundary.
6. Verify that the abstraction corresponds to a real variation or dependency boundary.

## Decision rules

- Abstract the client-facing behavior, not every concrete class.
- Let the consumer's needs shape the interface.
- Use an abstraction when it reduces meaningful implementation coupling or isolates a genuine point of variation.
- Keep concrete instantiation at a boundary rather than spreading it throughout business logic.

## Anti-patterns

- Interfaces for every class by default.
- "IUserService", "IThingManager", etc. that simply mirror one implementation.
- Abstractions whose names describe implementation technology instead of client behavior.
- Abstracting before there is a meaningful reason for substitution or dependency inversion.

## Exceptions and trade-offs

- An interface with exactly one implementation and no plausible second one is often ceremony wrapping a single class; every abstraction is a small ongoing maintenance and readability tax paid whether or not a second implementation ever materializes, so weigh that cost even when the anti-pattern isn't blatant.
- In ecosystems with structural typing (duck typing, structural interfaces), an explicit interface declaration can be unnecessary — the contract is implicit as long as consumers only call the methods they need.
- Abstracting a dependency purely for unit-test isolation is defensible, but if the only implementation ever exercised in tests is a hand-rolled fake that drifts from the real one, the abstraction can hide integration bugs; pair it with at least one contract or integration test run against the real implementation.

## Verification

A good abstraction should let the consumer:

- remain unaware of concrete implementation details;
- express its intent without construction knowledge;
- accept another implementation without changing its own behavior;
- keep the contract smaller than the implementation.
