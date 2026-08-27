---
name: make-dependencies-explicit
description: "Makes data, ordering, and resource dependencies visible in signatures instead of hidden coupling. Use when tests only pass under a specific execution order, or a service assumes an init() or setup step was called first without that requirement appearing anywhere in its signature. Not when the hidden dependency is really a class exposing internal representation (see encapsulate-implementation-details), when the concern is the state footprint rather than its visibility (see minimize-state-and-side-effects), or when the fix is object-level injection design (see program-to-abstractions, invert-dependencies-around-stable-policy)."
license: MIT
---

# Make Dependencies Explicit

## Intent

Make data, control, ordering, and resource dependencies visible so that readers and maintainers can reason about the code without discovering hidden coupling through failures.

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

## Exceptions and trade-offs

- Widening a signature to make every dependency explicit can produce unwieldy parameter lists; prefer grouping into a cohesive context object over enumerating a dozen arguments.
- Framework-managed dependency injection sometimes hides wiring by design (ambient request context, DI container magic); accept it where the framework convention is well understood repo-wide.
- Not all coupling is worth eliminating — document a truly unavoidable ordering requirement rather than forcing an awkward API just to make it syntactically visible.

## Verification

- Can a caller understand what must be true before invoking the operation?
- Can the dependency be seen in the signature or boundary?
- Would changing an implementation detail unexpectedly break consumers?
- Are ordering requirements explicit and testable?
