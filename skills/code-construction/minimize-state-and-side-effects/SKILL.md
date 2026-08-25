---
name: minimize-state-and-side-effects
description: Reduce hidden state changes and side effects that make behavior difficult to reason about, test, compose, or modify. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Minimize State and Side Effects

## Intent

Reduce hidden state changes and side effects that make behavior difficult to reason about, test, compose, or modify.

## Apply when

Use this skill when code involves:

- mutable shared state
- global variables
- hidden writes
- functions with surprising side effects
- shared caches or singletons
- complicated ordering dependencies
- difficult-to-isolate tests

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

## Verification

- Can you enumerate the operation's state transitions?
- Are side effects visible to callers?
- Can the operation be tested without reproducing unrelated global state?
- Would moving or reordering code accidentally change shared state?


## Related skills

- CODE-06 Make Dependencies Explicit
- CODE-10 Encapsulate Implementation Details
- TEST-01 Design for Testability
