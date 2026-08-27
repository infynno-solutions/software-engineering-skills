---
name: minimize-state-and-side-effects
description: "Reduces hidden mutation and side effects that make behavior hard to reason about. Use when a function named calculateTotal also writes to a cache, when a supposedly pure function writes elsewhere, or when a test suite cannot isolate a case because an earlier test left shared state behind. Not when a dependency is merely invisible in the signature but the state itself is well-scoped (see make-dependencies-explicit), or when the concern is who may see the state rather than how much of it exists (see encapsulate-implementation-details)."
license: MIT
---

# Minimize State and Side Effects

## Intent

Reduce hidden state changes and side effects that make behavior difficult to reason about, test, compose, or modify.

## Procedure

1. Identify all state read and modified by the operation.
2. Distinguish required state changes from incidental ones.
3. Prefer local state and explicit outputs where practical.
4. Separate computation from side effects when doing so improves reasoning or testing.
5. Make unavoidable side effects visible through names, interfaces, or boundaries.

## Decision rules

- Minimize hidden mutation rather than banning mutation categorically.
- Keep side effects close to the boundary where they are required.
- A function whose name suggests a calculation should not silently perform unrelated external actions.
- Do not introduce abstraction solely to eliminate harmless local state if doing so increases complexity.

## Anti-patterns

- Hidden writes to shared state.
- Functions that appear pure but update external state.
- Implicit initialization and cleanup requirements.
- Order-dependent behavior that callers cannot see.

## Exceptions and trade-offs

- Some side effects are the entire point of the operation (writing to a database, sending a request); the goal is making them visible and scoped, not eliminating them.
- Local mutable state confined to a function body, such as a loop accumulator, is usually harmless and not worth restructuring into a pure fold purely on principle.
- Caching and memoization are legitimate uses of hidden state when the staleness-versus-performance trade-off is deliberate and documented.

## Verification

- Can you enumerate the operation's state transitions?
- Are side effects visible to callers?
- Can the operation be tested without reproducing unrelated global state?
- Would moving or reordering code accidentally change shared state?
