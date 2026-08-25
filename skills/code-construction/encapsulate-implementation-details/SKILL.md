---
name: encapsulate-implementation-details
description: Expose only what consumers need to use a component and hide representations and mechanisms that may change independently. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Encapsulate Implementation Details

## Intent

Expose only what consumers need to use a component and hide representations and mechanisms that may change independently.

## Apply when

Use this skill at:

- class and module interfaces
- library APIs
- database/repository boundaries
- framework integrations
- configuration boundaries
- reusable components

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

## Verification

- Can the implementation change without changing consumers?
- Does the interface describe the contract rather than the mechanism?
- Are representation details inaccessible to consumers?
- Does the boundary meaningfully reduce coupling?


## Related skills

- OO-02 Encapsulate Representation
- OO-03 Program to Abstractions
- MOD-06 Invert Dependencies Around Stable Policy
- MOD-11 Control Coupling Across Boundaries
