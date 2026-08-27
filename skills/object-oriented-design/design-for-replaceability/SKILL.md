---
name: design-for-replaceability
description: "Shapes a contract around one specific dependency judged genuinely likely to be swapped, so replacing it later touches only the boundary. Use when an infrastructure vendor may change, an algorithm has several valid implementations, or a test needs a seam because the real implementation is slow, external, or non-deterministic. Not when there is no plausible swap and the goal is just a cleaner collaboration contract (see program-to-abstractions, separate-collaboration-from-implementation), for business or algorithmic variation (see encapsulate-what-varies), or for whether the seam warrants an architectural boundary (see identify-and-place-architectural-boundaries)."
license: MIT
---

# Design for Replaceability

## Intent

Use stable contracts and controlled collaboration boundaries so legitimate implementation changes remain localized.

## Procedure

1. Identify the replacement scenario that matters.
2. Determine what must remain stable for consumers.
3. Define the smallest contract that captures that stable behavior.
4. Move implementation-specific construction behind a boundary.
5. Ensure consumers interact only through the stable contract.
6. Verify replacement is actually possible without leaking type-specific assumptions.
7. Remove unnecessary flexibility if the expected replacement is too speculative to justify the abstraction.

## Decision rules

- Design for replaceability when the cost of future change is significant or the implementation is already volatile.
- A replaceable design still needs a clear default implementation and simple wiring.
- Replaceability should not become an excuse for abstracting every dependency.
- The stable contract must be based on client needs, not on exposing every implementation capability.

## Anti-patterns

- Over-generalized interfaces created only "for testing."
- Multiple abstraction layers around a single stable implementation with no change pressure.
- Contracts that leak concrete framework types.
- Designing for imagined provider changes while known business requirements remain unresolved.

## Exceptions and trade-offs

- Every seam is a layer that must be maintained and understood; a boundary that is never exercised by a real swap is pure cost with no benefit.
- It's fine, even preferable, for a replaceable contract to have exactly one production implementation as long as construction stays isolated at a single wiring point — replaceability is about where the seam is, not about how many implementations currently exist.
- When the organization is contractually or strategically locked into one vendor for the foreseeable future, the replaceability boundary can be deferred until the day the contract actually changes.
- A test-only seam (to avoid a slow or flaky real dependency) is a legitimate reason to introduce a contract even absent any production replacement — but be explicit that the contract exists for test isolation, not architectural flexibility, so it doesn't get over-designed.

## Verification

Test the design mentally with a realistic replacement:

- Can the implementation be swapped at the composition boundary?
- Do consumers remain unchanged?
- Does the contract still represent the same conceptual capability?
- Is the replacement simpler than rewriting every consumer?
