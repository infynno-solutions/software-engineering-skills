---
name: invert-dependencies-around-stable-policy
description: "Places the interface on the stable policy side of a relationship and injects the concrete detail from outside. Use when a use-case or service class directly constructs a specific SDK client, ORM, or file-system API, or a test cannot exercise policy logic because there is no seam to substitute a fake. Not when there is no stable/volatile asymmetry between the two sides (see group-components-by-cohesion), when the interface exists but is too broad for its clients (see keep-interfaces-narrow-and-client-focused), or when only deciding which way the arrow points (see control-dependency-direction)."
license: MIT
---

# Invert Dependencies Around Stable Policy

## Intent
Make high-level policy independent of volatile implementation details by placing abstractions at the dependency boundary.

## Procedure
1. Identify which side is policy and which is volatile detail.
2. Determine which side should remain stable.
3. Define the minimal abstraction at the stable boundary, shaped by what policy needs.
4. Make details depend on the abstraction and inject or assemble the concrete implementation at the edge.

## Decision rules
- Shape the abstraction from the policy side's needs, not by mirroring the concrete implementation's method names.
- Own the interface in the same module as the policy that uses it, not in the module that implements it.
- Assemble concrete implementations at a single composition point (entry point, DI container, main) rather than scattering construction of concrete details through policy code.
- Only invert when the detail is genuinely volatile or swappable — multiple real or planned implementations, or a real need for a test double — not for every collaborator.

## Anti-patterns
- Inverting dependencies without a real volatility or ownership reason.
- Putting abstractions in the most volatile package by default.

## Exceptions and trade-offs
- Direct dependencies are acceptable inside a cohesive stable component.
- A policy module calling a small, stable standard-library or language-runtime facility usually doesn't need an inversion seam — the volatility that justifies inversion isn't there.

## Verification
- Confirm the policy module's source imports no concrete infrastructure package, only the abstraction it defines or owns.
- Confirm the policy can be exercised in a test using an in-memory or fake implementation of the abstraction, with no real I/O.
- Confirm swapping the concrete implementation (e.g., a new database driver) requires touching only the composition point, not the policy code.
