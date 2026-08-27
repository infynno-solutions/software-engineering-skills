---
name: encapsulate-implementation-details
description: "Exposes only what callers need at a class, module, or service boundary, hiding storage and mechanism. Use when a repository layer leaks ORM entities into business code, a public field exposes a mutable internal list, or a return type forces callers to know how a value is stored internally. Not when the class mixes unrelated responsibilities rather than over-exposing internals (see design-cohesive-classes), when a single function exposes too much of its algorithm (see write-code-at-the-level-of-intent), or for one object's own fields in OO terms (see encapsulate-representation)."
license: MIT
---

# Encapsulate Implementation Details

## Intent

Expose only what consumers need to use a component and hide representations and mechanisms that may change independently.

## Procedure

1. Identify what callers actually need to know.
2. Separate stable contract from implementation mechanism.
3. Hide representation and internal sequencing when callers should not depend on them.
4. Expose the narrowest useful interface.
5. Recheck whether the boundary prevents implementation changes from propagating unnecessarily.

## Decision rules

- Default to hiding information that callers do not need.
- A public API should contain information needed to use the component, not its internal implementation details.
- Do not hide information that callers genuinely need to make correct decisions.
- Do not create wrappers that provide no meaningful information-hiding benefit.

## Anti-patterns

- Public fields exposing internal representation.
- Leaking persistence models into unrelated layers without a justified reason.
- Interfaces that expose internal lifecycle or storage details.
- Abstractions that simply mirror an implementation without insulating change.

## Exceptions and trade-offs

- Encapsulating code with a single internal caller can add indirection without payoff — apply where a real boundary or multiple consumers exist.
- Performance-critical code sometimes needs to expose internal representation deliberately (a buffer, a shared array); document the trade-off rather than hiding it behind a costly defensive copy.
- Encapsulation is not a reason to build speculative abstraction layers for flexibility nobody has requested yet.

## Verification

- Can the implementation change without changing consumers?
- Does the interface describe the contract rather than the mechanism?
- Are representation details inaccessible to consumers?
- Does the boundary meaningfully reduce coupling?
