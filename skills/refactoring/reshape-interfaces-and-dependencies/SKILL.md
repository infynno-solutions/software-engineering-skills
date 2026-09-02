---
name: reshape-interfaces-and-dependencies
description: "Reshapes signatures, parameter ownership, and dependency direction in existing code for cleaner testing and reuse. Use for an overgrown parameter list, a reached-through dependency that should be passed in, or introducing an inversion seam so a component can be tested without its real collaborator. Not for splitting what a class does rather than what it depends on (see extract-and-recompose-responsibilities, usually first), nor for deciding the target direction as a design question (see control-dependency-direction, invert-dependencies-around-stable-policy)."
license: MIT
---

# Reshape Interfaces and Dependencies

## Intent
Change signatures, ownership, and dependency structure to create cleaner seams without hiding a broader design problem.

## Procedure
1. Identify the specific interface pain: too many parameters, a parameter object that should be passed whole instead of destructured, a dependency reached for internally that should be injected, or a dependency pointing the wrong direction.
2. Determine the correct owner of each piece of data or behavior in the signature — who naturally has it, who naturally needs it — before changing the shape.
3. Apply the targeted move: Introduce Parameter Object, Preserve Whole Object, Change Function Declaration, Move Function, or Introduce/Extract Interface, choosing the smallest move that fixes the specific pain.
4. When changing a widely-called signature, use expand/contract: add the new signature, migrate callers incrementally, then remove the old signature.
5. When inverting a dependency, introduce the abstraction at the point that actually needs to vary or be tested in isolation, not at every dependency in the module.
6. Re-check after the change whether the reshaped interface is actually simpler to call correctly — if callers now need to know more to construct the right arguments, complexity may have moved rather than been removed.

## Decision rules
- Prefer passing an existing whole object over destructuring it into several parameters when the callee will need more of that object later or already has access to it.
- Introduce an abstraction or interface only at a seam that actually needs to vary, meaning multiple implementations, or needs isolation for testing — not on every dependency by default.
- A long parameter list of unrelated data is a sign the function is doing too much, not just a signature problem — check whether extraction is the real fix before just grouping parameters.
- Keep dependency direction pointing from concrete detail toward abstraction or policy, not the reverse, when introducing a new seam.

## Anti-patterns
- Adding an interface with exactly one implementation "for testability" when a simple constructor-injected fake would do, adding indirection without a real seam benefit.
- Grouping unrelated parameters into a generic "Options" or "Config" object just to shorten the signature, hiding what's actually required versus optional.
- Reshaping a signature to hide that the function is doing too many unrelated things, instead of fixing the underlying responsibility problem.
- Changing a public API's signature in place with no migration path, breaking all callers in one step on a widely-used interface.

## Exceptions and trade-offs
- In small, single-team codebases with no external consumers, breaking a signature in place, without expand/contract, can be acceptable since every caller can be updated atomically.
- Dependency inversion has a real readability cost, more indirection to trace — for code with a single implementation and no foreseeable second one or test-isolation need, a direct dependency is often clearer than an interface.

## Verification
- Confirm every caller of a changed signature was updated, or migrated via expand/contract, and the old form fully removed once migration completes.
- Confirm a newly introduced interface or abstraction has, or will imminently have, more than one real implementation, or a concrete testing need it serves.
- Confirm the new dependency direction doesn't introduce a cycle between modules.
