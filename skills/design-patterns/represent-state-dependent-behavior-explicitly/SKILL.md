---
name: represent-state-dependent-behavior-explicitly
description: "Makes state-dependent behavior explicit via the State pattern. Use when a status, mode, or phase field is switched on inside several methods of the same class, all needing updates whenever a state is added, or when illegal transitions such as Cancelled back to Pending are possible only because nothing prevents them. Not for two or three states with simple, stable differences, and not for a type switch that varies algorithm rather than lifecycle state (see use-polymorphism-to-localize-variation, encapsulate-algorithmic-variation)."
license: MIT
---

# Represent State-Dependent Behavior Explicitly

## Intent
Make behavior that changes with object state explicit when state transitions cause conditionals and duplicated logic to become difficult to understand or extend.

## Procedure
1. Identify the meaningful states and the transitions that are actually valid between them — draw or list this before writing any code.
2. Separate state-dependent behavior (what changes per state) from invariant behavior (what stays the same regardless of state).
3. Define the state contract: the set of operations whose behavior varies by state.
4. Move state-specific behavior into explicit state objects when the complexity (number of states, number of varying operations) warrants the extra structure.
5. Centralize or formalize transitions — ideally in one place (the state objects themselves, or a transition table) rather than scattered across every method that happens to change status.
6. Preserve invariants across transitions: fields or constraints that must hold true regardless of which state the object is in.

## Decision rules
- Prefer explicit state modeling when state-dependent behavior is substantial (several methods, several states) or clearly growing over time.
- Keep state transitions visible and testable — a reviewer or a test suite should be able to enumerate valid transitions without running the whole system.
- Avoid introducing state objects when two or three simple branches remain clearer than a set of classes plus a transition mechanism.
- Ensure invalid transitions are handled deliberately — either made structurally impossible or explicitly rejected with a clear error, never silently ignored.

## Anti-patterns
- Giant conditional blocks covering every state, duplicated across multiple methods in the same class.
- State classes introduced with no meaningful behavior of their own — just a differently-named `if` branch wrapped in a class.
- Hidden transitions scattered across unrelated methods, so no single place shows the full set of legal state changes.
- The State pattern applied where a simple enum and a small `switch` statement would be clearer, because the number of states and varying behaviors is genuinely small.

## Exceptions and trade-offs
- Explicit state objects add files and indirection; for a status field checked in exactly one place, that overhead isn't justified — inline branching is fine.
- A formal state machine (with a transition table) trades some flexibility for safety: it becomes harder to make ad hoc exceptions later, which is usually the point, but confirm the domain doesn't have a legitimate need for such exceptions before locking it down.
- If state and behavior are tightly entangled with persistence (e.g., a database-backed workflow status), the state representation may need to stay serializable and simple, constraining how far into full state objects you can go.

## Verification
- Are the states and their transitions understandable from a single place in the code, without hunting across the whole class?
- Does adding a new state require editing one focused location, rather than every method that happens to branch on status?
- Are illegal transitions prevented or explicitly, visibly handled — never silently allowed through?
