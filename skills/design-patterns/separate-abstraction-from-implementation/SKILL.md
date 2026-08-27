---
name: separate-abstraction-from-implementation
description: "Splits an abstraction from its implementation via composition (Bridge) when both vary along independent axes. Use when a hierarchy has one subclass per combination - CircleOpenGLRenderer, SquareDirectXRenderer - and adding one new shape or one new backend means adding N subclasses rather than one. Not when only one axis actually varies, where a plain hierarchy or Strategy on that axis suffices (see encapsulate-algorithmic-variation), and not when the two axes always change together in practice."
license: MIT
---

# Separate Abstraction from Implementation

## Intent
Allow an abstraction and its implementation to evolve independently when both dimensions vary, instead of encoding the variation in inheritance or conditional logic.

## Procedure
1. Identify two independent axes of variation — confirm both actually vary on their own; a bridge is wasted structure if one axis is fixed in practice.
2. Separate the abstraction (the concept clients work with) from the implementation contract (the concern that varies independently underneath).
3. Define the implementation interface: the narrow set of operations the abstraction needs from whichever implementation is plugged in.
4. Connect the abstraction to implementations through composition/delegation — the abstraction holds a reference to an implementation object rather than inheriting from an implementation-specific subclass.
5. Verify each axis can evolve independently: adding a new abstraction subtype shouldn't require touching implementations, and vice versa.
6. Keep the number of resulting combinations manageable — the whole point is that combinations no longer require new classes, so check that this is actually true in the resulting design.

## Decision rules
- Bridge is justified by genuinely independent dimensions of variation, both of which are expected to grow or change over time.
- Prefer composition/delegation over inheritance when inheritance would otherwise couple the two axes together into one combinatorial hierarchy.
- Use Bridge only when the second axis is real and likely to matter — not merely theoretically separable.
- Avoid introducing Bridge merely because an inheritance hierarchy already exists; existing inheritance alone isn't evidence of two independent axes.

## Anti-patterns
- A Cartesian explosion of subclasses (`TypeA_BackendX`, `TypeA_BackendY`, `TypeB_BackendX`, ...) that a Bridge would collapse but hasn't yet.
- Introducing Bridge with only one stable implementation and no credible second axis — the structure exists but nothing actually varies along it.
- Abstraction and implementation that still change together despite the supposed separation, meaning the two "axes" were never really independent.

## Exceptions and trade-offs
- Bridge adds an extra layer of indirection (the abstraction delegates to the implementation object) that costs a small amount of directness even when correctly applied — worth it only once the combinatorial alternative is worse.
- If one axis is expected to stabilize permanently after this change (e.g., only one rendering backend will ever be supported), the bridge's flexibility becomes unused ceremony; revisit whether a simpler hierarchy on the remaining axis suffices.
- Bridge and Strategy look structurally similar (both favor composition over inheritance); the distinguishing question is whether you're separating a whole abstraction hierarchy from an implementation hierarchy (Bridge) or swapping one algorithm within an otherwise stable class (Strategy, see `encapsulate-algorithmic-variation`).

## Verification
- Can either axis change — a new abstraction subtype, or a new implementation — without multiplying the number of classes needed?
- Are both the abstraction and the implementation genuinely meaningful concepts on their own, not just an arbitrary split?
- Did the bridge reduce real dependency coupling between the two axes, rather than just adding a layer of ceremony around the same coupling?
