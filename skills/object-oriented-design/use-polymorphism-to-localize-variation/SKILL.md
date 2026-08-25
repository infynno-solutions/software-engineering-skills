---
name: use-polymorphism-to-localize-variation
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Keep variant-specific behavior close to the variant instead of spreading type checks across unrelated clients.

# When to apply

Consider this when:

- the same type switch or conditional appears repeatedly;
- every new variant requires edits in many callers;
- variants have different algorithms but a common conceptual contract;
- a stable interface can describe the operation cleanly.

# Procedure

1. Identify repeated branching on type, mode, status, or variant.
2. Determine whether the branches represent a stable family of behaviors.
3. Define the common behavioral contract.
4. Move variant-specific behavior behind the contract.
5. Let the caller invoke the abstraction without selecting every implementation detail.
6. Keep construction/selection separate from behavior execution where appropriate.
7. Re-evaluate whether the polymorphism actually reduces change propagation.

# Decision rules

- Use polymorphism when the alternatives are genuine implementations of one concept.
- Keep the shared contract small enough that each implementation can honor it naturally.
- Retain a simple conditional when the alternatives are few, stable, and clearer as data/control flow.
- Do not replace every `switch` with a class hierarchy.

# Anti-patterns

- Pattern-driven polymorphism for a one-off conditional.
- Interfaces that exist only to hide a trivial branch.
- Polymorphic hierarchies whose implementations do not share a meaningful contract.
- Moving a large conditional into an even larger strategy-selection layer.

# Verification

- Adding a new variant should primarily affect the new implementation and the composition/registration point.
- Existing clients should not need to know variant-specific logic.
- The common abstraction should remain meaningful across all implementations.

# Source basis

GoF identifies polymorphism and interface-based collaboration as central tools for reusable OO design. Head First uses Strategy, State, and Observer to show how composition can localize varying behavior. Code Complete explicitly connects repeated case statements with the possibility of replacing conditionals with polymorphism.
