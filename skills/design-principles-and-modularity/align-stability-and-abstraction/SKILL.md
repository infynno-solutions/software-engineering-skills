---
name: align-stability-and-abstraction
description: "Balances a component's instability (fan-in/fan-out) against its abstractness, so widely-depended-on components stay abstract and volatile ones stay concrete. Use when a shared core package exposes concrete classes many modules instantiate directly, or a supposedly stable module keeps breaking consumers whenever it changes internally. Not for cycles (see prevent-dependency-cycles), which way an arrow points (see control-dependency-direction), or removing an abstraction that stopped earning its cost (see manage-abstraction-debt)."
license: MIT
---

# Align Stability and Abstraction

## Intent
Use abstraction where stable components need flexibility, while avoiding stable concrete components that become difficult to change and unstable abstract components that add little value.

## Procedure
1. Estimate instability I = fan-out / (fan-in + fan-out) for the component in question.
2. Estimate abstractness A = (abstract classes + interfaces) / total types in the component.
3. Compare the component to its position on the main sequence (A + I ≈ 1); note how far it sits from that line.
4. If it's stable but concrete (low I, low A — Zone of Pain), extract the seam consumers depend on into an interface or abstract type.
5. If it's unstable but abstract (high I, high A — Zone of Uselessness), either give it real dependents or make it concrete.

## Decision rules
- A component many others depend on (low I) should expose behavior through interfaces or abstract types, not concrete classes clients instantiate directly.
- A component with few or no dependents should stay concrete; adding abstraction there pays for variation nobody uses yet.
- Don't force every stable component toward A=1: a stable, fixed-shape value type or DTO is fine concrete.
- Put the abstraction at the boundary with the most fan-in, not at the package that happens to change most often.

## Anti-patterns
- Applying abstractness/instability metrics as a target rather than a diagnostic.
- Making every stable component fully abstract regardless of whether variation exists.

## Exceptions and trade-offs
- Metrics are heuristics; architectural intent and observed change patterns matter more than the numbers.
- Value objects and DTOs with a fixed shape can remain stable and concrete — they aren't policy that needs an abstraction seam.

## Verification
- Recompute I and A after the change and confirm the component moved closer to the main sequence, not further from it.
- Check that downstream consumers now import the abstraction, not the concrete type.
- Confirm the abstraction has at least one real alternate implementation or a concrete test double, not just a single implementer wrapped in an interface.
