---
name: encapsulate-representation
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Expose what clients need to use an object and hide what they do not need to know.

# When to apply

Use when:

- designing public APIs for classes;
- exposing fields or internal collections;
- deciding whether callers should mutate state directly;
- wrapping third-party or infrastructure details;
- preparing a component for likely implementation changes.

# Procedure

1. Identify the behavior clients actually require.
2. Identify internal state, data structures, algorithms, and invariants required to implement that behavior.
3. Keep internal representation private whenever clients do not need it.
4. Expose operations that preserve invariants and communicate intent.
5. Prevent callers from depending on representation-specific details.
6. Check whether getters/setters or direct collection exposure have unintentionally expanded the contract.

# Decision rules

- Prefer behavior-oriented interfaces over representation-oriented access.
- Expose an internal collection only when its mutability and representation are genuinely part of the contract.
- Hide details that can change independently of client needs.
- Do not manufacture elaborate abstractions solely to hide trivial implementation details; the boundary should earn its complexity.

# Anti-patterns

- Public mutable fields for state that has invariants.
- Returning internal mutable collections directly.
- APIs that expose database records, framework objects, or storage details as domain contracts.
- Clients branching on internal implementation types.
- Abstracting everything simply because encapsulation exists as a principle.

# Verification

Ask:

- Could the implementation change without forcing callers to change?
- Can invariants be protected inside the object?
- Do consumers depend on behavior or on representation?
- Is the public interface smaller than the implementation knowledge behind it?

# Source basis

GoF defines encapsulation as hiding representation and implementation behind operations. Code Complete recommends exposing information on a need-to-know basis and hiding implementation details. Clean Architecture extends the same principle to architectural boundaries.
