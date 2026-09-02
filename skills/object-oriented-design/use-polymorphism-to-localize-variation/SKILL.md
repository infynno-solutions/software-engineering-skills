---
name: use-polymorphism-to-localize-variation
description: "Replaces a repeated type, mode, or status conditional with dispatch through a shared contract, so each variant's logic lives with the variant instead of in every caller. Use when the same switch appears in several places, adding a variant means editing many callers, or variants differ in algorithm but share a conceptual contract. Not for deciding whether the variation is real and independent in the first place (see encapsulate-what-varies), for a status field with illegal transitions (see represent-state-dependent-behavior-explicitly), or for simplifying a one-off nested conditional (see simplify-conditional-logic)."
license: MIT
---

# Use Polymorphism to Localize Variation

## Intent

Keep variant-specific behavior close to the variant instead of spreading type checks across unrelated clients.

## Procedure

1. Identify repeated branching on type, mode, status, or variant.
2. Determine whether the branches represent a stable family of behaviors.
3. Define the common behavioral contract.
4. Move variant-specific behavior behind the contract.
5. Let the caller invoke the abstraction without selecting every implementation detail.
6. Keep construction/selection separate from behavior execution where appropriate.
7. Re-evaluate whether the polymorphism actually reduces change propagation.

## Decision rules

- Use polymorphism when the alternatives are genuine implementations of one concept.
- Keep the shared contract small enough that each implementation can honor it naturally.
- Retain a simple conditional when the alternatives are few, stable, and clearer as data/control flow.
- Do not replace every `switch` with a class hierarchy.

## Anti-patterns

- Pattern-driven polymorphism for a one-off conditional.
- Interfaces that exist only to hide a trivial branch.
- Polymorphic hierarchies whose implementations do not share a meaningful contract.
- Moving a large conditional into an even larger strategy-selection layer.

## Exceptions and trade-offs

- A conditional with exactly two stable branches that will realistically never grow a third is often clearer as a plain `if`/`else` than as a two-implementation interface hierarchy — polymorphism tends to pay off starting around three variants, or with a set that is actively growing.
- When branches differ mainly in data rather than behavior (different constant thresholds per type, say), a lookup table or map is usually simpler than a class hierarchy.
- Centralizing variant selection behind a registry or factory adds indirection that can make "where does this actually happen" harder to find via plain code search — worth it once the switch has spread across call sites, not before it has.

## Verification

- Adding a new variant should primarily affect the new implementation and the composition/registration point.
- Existing clients should not need to know variant-specific logic.
- The common abstraction should remain meaningful across all implementations.
