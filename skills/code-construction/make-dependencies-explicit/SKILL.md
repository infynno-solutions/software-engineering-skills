---
name: make-dependencies-explicit
description: Make data, control, ordering, and resource dependencies visible so that readers and maintainers can reason about the code without discovering hidden coupling through failures. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Make Dependencies Explicit

## Intent

Make data, control, ordering, and resource dependencies visible so that readers and maintainers can reason about the code without discovering hidden coupling through failures.

## Apply when

Use this skill when:

- functions depend on call ordering
- global or shared state is involved
- parameters encode hidden assumptions
- one module relies on another's internal behavior
- tests fail because setup or ordering is implicit
- a change has surprising downstream effects

## Procedure

1. Identify what the operation needs from its environment.
2. Determine whether those dependencies are represented in parameters, interfaces, state, or control flow.
3. Expose important dependencies explicitly where practical.
4. Reduce semantic coupling that the compiler cannot enforce.
5. Document unavoidable ordering or environmental assumptions.

## Decision rules

- Prefer visible dependencies over hidden assumptions.
- Do not rely on global mutable state when an explicit dependency is practical.
- Make call-order requirements part of a clear interface when they cannot be eliminated.
- Treat semantic coupling as a design concern even when the type system cannot detect it.

## Anti-patterns

- Hidden initialization requirements.
- Global state with undocumented ownership.
- APIs whose correct use requires knowledge of internal call sequences.
- Passing broad objects when only a narrow contract is actually required.

## Verification

- Can a caller understand what must be true before invoking the operation?
- Can the dependency be seen in the signature or boundary?
- Would changing an implementation detail unexpectedly break consumers?
- Are ordering requirements explicit and testable?


## Related skills

- CODE-09 Minimize State and Side Effects
- CODE-10 Encapsulate Implementation Details
- MOD-07 Control Dependency Direction
- MOD-11 Control Coupling Across Boundaries
