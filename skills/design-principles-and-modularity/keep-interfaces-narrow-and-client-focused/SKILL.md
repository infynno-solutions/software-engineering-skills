---
name: keep-interfaces-narrow-and-client-focused
description: "Splits or shapes an interface so each client depends only on the operations it actually calls. Use when implementers stub out or throw on half the methods, a read-only consumer depends on a type that also exposes writes and admin operations, or a test mock must implement a dozen methods it never uses. Not when the concern is which side owns the interface (see invert-dependencies-around-stable-policy), what crosses the boundary at all (see control-coupling-across-boundaries), or a consumer depending on a concrete class rather than a contract (see program-to-abstractions)."
license: MIT
---

# Keep Interfaces Narrow and Client-Focused

## Intent
Expose only the operations a client genuinely needs so clients do not inherit unnecessary coupling.

## Procedure
1. List each client and the operations it consumes.
2. Identify dependencies on unused members or transitive details.
3. Split or reshape interfaces around client needs.
4. Verify changes to unused operations no longer affect unrelated clients.

## Decision rules
- Group interface members by which client role actually needs them (reader vs. writer, admin vs. regular user), not by which class happens to implement them together.
- An empty or throwing method implementation signals the interface is too wide for that implementer, not that the implementer is incomplete.
- One concrete class implementing several narrow interfaces is fine; narrowness is about what each client sees, not how many interfaces exist.
- Group operations that are always called together into the same narrow interface, even if that's more than one method — don't split by method count alone.

## Anti-patterns
- Giant "god interfaces" used by many unrelated clients.
- Splitting every interface into trivial single-method fragments regardless of how clients actually call them.

## Exceptions and trade-offs
- A cohesive interface can remain broad when its operations form one stable client-facing contract that every client genuinely uses.

## Verification
- Check that no implementer of the (post-split) interface leaves a method unimplemented, stubbed, or throwing "not supported."
- Confirm each client's compiled or imported dependency now lists only the narrow interface it uses, not the original wide one.
- Confirm a change to an operation in one narrow interface leaves clients of the other narrow interfaces unaffected.
