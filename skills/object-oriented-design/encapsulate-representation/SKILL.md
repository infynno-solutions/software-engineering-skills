---
name: encapsulate-representation
description: "Hides one object's own fields and storage format, exposing behavior-oriented operations so callers cannot depend on the representation. Use when designing a class's public API, exposing internal collections, deciding whether callers may mutate state directly, or wrapping third-party data. Not for depending on someone else's behavior through a contract (see program-to-abstractions), the breadth of an object's collaborators (see minimize-object-coupling), or a module- or service-level boundary leaking mechanism (see encapsulate-implementation-details)."
license: MIT
---

# Encapsulate Representation

## Intent

Expose what clients need to use an object and hide what they do not need to know.

## Procedure

1. Identify the behavior clients actually require.
2. Identify internal state, data structures, algorithms, and invariants required to implement that behavior.
3. Keep internal representation private whenever clients do not need it.
4. Expose operations that preserve invariants and communicate intent.
5. Prevent callers from depending on representation-specific details.
6. Check whether getters/setters or direct collection exposure have unintentionally expanded the contract.

## Decision rules

- Prefer behavior-oriented interfaces over representation-oriented access.
- Expose an internal collection only when its mutability and representation are genuinely part of the contract.
- Hide details that can change independently of client needs.
- Do not manufacture elaborate abstractions solely to hide trivial implementation details; the boundary should earn its complexity.

## Anti-patterns

- Public mutable fields for state that has invariants.
- Returning internal mutable collections directly.
- APIs that expose database records, framework objects, or storage details as domain contracts.
- Clients branching on internal implementation types.
- Abstracting everything simply because encapsulation exists as a principle.

## Exceptions and trade-offs

- Simple data-carrier types (DTOs, value objects, immutable records) can expose fields directly when there are no invariants to protect — encapsulation has no protective work to do there, and getters would be pure ceremony.
- Returning a defensive copy of an internal collection costs an extra allocation; on a hot path, an unmodifiable/read-only view can be an acceptable middle ground even though it still reveals the collection's element type.
- Wrapping every primitive field in its own tiny accessor method for no protective reason adds ceremony without guarding any real invariant — this principle is not "no public fields, ever."
- ORMs and serialization frameworks sometimes require public fields or setters for mechanical reasons; confine that exposure to the mapping layer rather than letting it define the domain-facing API.

## Verification

Ask:

- Could the implementation change without forcing callers to change?
- Can invariants be protected inside the object?
- Do consumers depend on behavior or on representation?
- Is the public interface smaller than the implementation knowledge behind it?
