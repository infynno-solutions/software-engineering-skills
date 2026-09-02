---
name: control-coupling-across-boundaries
description: "Limits what one module must know about another's internal representation, timing, and control flow across an API, package, or service boundary. Use when designing a new public API, when an internal refactor on one side broke callers on the other, or when callers pass control flags such as mode=delete instead of calling a distinct operation. Not for which package owns the interface (see control-dependency-direction), trimming an interface to one client (see keep-interfaces-narrow-and-client-focused), or one object's collaborator count (see minimize-object-coupling)."
license: MIT
---

# Control Coupling Across Boundaries

## Intent
Minimize the amount of knowledge and implementation detail crossing module/component boundaries.

## Procedure
1. Inventory data, control, temporal, and semantic dependencies crossing the boundary.
2. Hide representations and volatile mechanisms behind the contract.
3. Narrow the contract to what the consumer actually needs.
4. Verify that internal changes on either side do not propagate across the boundary unnecessarily.

## Decision rules
- Pass the smallest data shape the boundary needs, not the caller's internal struct or ORM entity.
- Replace boolean/flag parameters that alter the callee's control flow with distinct operations or explicit types.
- If both sides must agree on call order (temporal coupling), make that order part of the contract — a builder, an explicit state machine — rather than an implicit convention.
- Treat shared mutable or global state crossing the boundary as coupling to eliminate, not to document.

## Anti-patterns
- Passing internal data structures or entities across boundaries.
- Using a facade that merely conceals a deep shared dependency graph underneath.
- Leaking ordering requirements ("call init() before use()") without enforcing them in the type or API.

## Exceptions and trade-offs
- Some coupling is necessary; the goal is purposeful, low-cost coupling, not zero coupling.
- High-throughput internal boundaries within a single deployable may tolerate tighter coupling than public or cross-service boundaries, where the cost of a breaking change is much higher.

## Verification
- Confirm a caller can be exercised with a fake or stub built only from the published contract, without reaching into the callee's internals.
- Confirm renaming or reordering an internal field or method on either side doesn't require touching the other side's code.
- For control-flow flags that were removed, confirm each call site now expresses intent directly instead of through a mode parameter.
