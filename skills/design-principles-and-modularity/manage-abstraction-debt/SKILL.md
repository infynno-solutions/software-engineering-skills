---
name: manage-abstraction-debt
description: "Treats each interface, plugin point, config flag, or generic layer as a standing cost and collapses it back to direct code once it stops paying for itself. Use when a strategy interface still has a single production implementation years later, a plugin or config system's options have never varied in practice, or someone proposes a factory for a type with one concrete form. Not for judging whether a new, not-yet-built variation point is worth adding (see design-for-extension-without-fragile-modification), whether a subclass breaks its parent's contract (see preserve-behavioral-substitutability), or whether a seam deserves an architectural boundary (see identify-and-place-architectural-boundaries)."
license: MIT
---

# Manage Abstraction Debt

## Intent
Treat abstractions as design investments: introduce them when they pay for real variation or dependency control, and remove abstractions that add more complexity than value.

## Procedure
1. Identify the change or problem the abstraction is supposed to solve.
2. Measure or reason about actual reuse, variation, and coupling it provides today.
3. Compare the abstraction's ongoing cost with the cost of direct code.
4. Refactor — collapse or simplify — when the original abstraction no longer earns its keep.

## Decision rules
- An interface or seam with exactly one implementation and no concrete plan for a second is a debt candidate, not a design win by default.
- Weigh removal cost (call sites, test doubles, indirection) against the ongoing cost of keeping unused flexibility (extra files, harder tracing, onboarding cost).
- Treat a config flag that has only ever had one value in production the same as dead code, unless a second value is imminently planned.
- When collapsing an abstraction, inline the single implementation in one clear change rather than leaving the seam "just in case" indefinitely.

## Anti-patterns
- Speculative generalization built for variation that never materializes.
- Keeping abstractions forever because removing them feels like regression.

## Exceptions and trade-offs
- Premature abstraction and insufficient abstraction are both failure modes; neither is automatically the safer default.
- An abstraction kept solely to make unit testing possible (substituting a fake for a slow or external dependency) can still earn its keep with only one production implementation — testability is real value, not speculative generalization.

## Verification
- For each abstraction reviewed, confirm it has ≥2 real implementations, a concretely scheduled second one, or a distinct test-double use — otherwise flag it.
- After collapsing an abstraction, confirm all call sites still compile/pass against the concrete type and no test relied on swapping implementations.
- Re-check call sites for leftover indirection (factories, registries) that now serve only one branch.
