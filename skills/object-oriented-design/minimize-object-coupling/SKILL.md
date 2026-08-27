---
name: minimize-object-coupling
description: "The broad diagnostic for when an object's coupling - concrete-type dependence, shared mutable state, or leaked internals - has become the problem, and which kind it is. Use when a constructor or method signature keeps growing dependencies, changes propagate through long call chains, tests must build large object graphs for a small unit, or objects communicate through shared mutable state. Not for the specific fixes of naming a contract (see program-to-abstractions) or relocating construction (see separate-collaboration-from-implementation), and not for coupling across an API, package, or service boundary (see control-coupling-across-boundaries)."
license: MIT
---

# Minimize Object Coupling

## Intent

Keep object collaborations small, explicit, and stable so each object can be understood and changed with limited knowledge of the rest of the system.

## Procedure

1. Inventory important collaborators and dependencies.
2. Determine what knowledge each dependency requires.
3. Remove dependencies that are incidental rather than necessary for the responsibility.
4. Replace concrete or representation-level dependencies with narrow contracts when justified.
5. Reduce shared mutable state and hidden ordering assumptions.
6. Keep each collaboration focused on a coherent request.
7. Check the result for over-indirection and excessive plumbing.

## Decision rules

- Prefer small, explicit collaborations over broad object knowledge.
- Reduce coupling when it creates change propagation, cognitive load, or testing difficulty.
- Do not confuse fewer references with lower conceptual coupling; a single dependency can still expose many assumptions.
- Do not eliminate necessary domain relationships merely to achieve a low dependency count.

## Anti-patterns

- Objects reaching through several collaborators to manipulate internal state.
- Shared mutable globals used as an implicit coordination protocol.
- Concrete implementation dependencies spread across consumers.
- A "facade" that merely hides a huge dependency graph without simplifying the underlying contract.

## Exceptions and trade-offs

- Some domain relationships are inherently wide — an aggregate root that must coordinate several child entities, for example. Forcing that down to an arbitrarily "small" dependency count can hide real complexity rather than remove it.
- Introducing a facade or mediator to reduce visible coupling adds its own object and indirection — worthwhile only when it actually narrows the contract, not when it just relocates the same broad dependency behind one more name.
- Passing a single rich object rather than several primitive parameters can look like "one dependency" while still coupling the caller to many of that object's fields; count conceptual coupling, not reference count.

## Verification

- Can an object use its collaborator without knowing its internals?
- Are dependencies visible in the contract or constructor?
- Does a local implementation change avoid forcing broad changes?
- Can the object be tested without recreating unrelated system state?
