---
name: minimize-function-and-class-complexity
description: "Reduces the branches, nesting, and state a reader must track at once. Use when reviewing a function or class whose branch count or nesting depth has grown past what a reader can hold in mind in one pass. Not when the complexity is specifically in conditional predicates (see simplify-conditional-logic), specifically in state and side effects rather than sheer size (see minimize-state-and-side-effects), or when the unit needs splitting along responsibility lines under tests (see extract-and-recompose-responsibilities)."
license: MIT
---

# Minimize Function and Class Complexity

## Intent

Reduce the amount of code and state a developer must mentally track at once while preserving required behavior.

## Procedure

1. Identify the sources of cognitive complexity.
2. Separate essential domain complexity from accidental implementation complexity.
3. Reduce nesting and branching where possible.
4. Extract cohesive operations or state transitions.
5. Remove unnecessary indirection, duplication, and shared state.
6. Reassess the resulting code from the reader's perspective.

## Decision rules

- Prefer straightforward designs over clever ones.
- Optimize for comprehension before micro-optimization.
- Do not assume that fewer lines means lower complexity.
- Do not introduce abstractions that make the control flow harder to follow merely to reduce local code size.

## Anti-patterns

- Dense clever code.
- Deeply nested conditionals.
- Large methods with multiple unrelated decision domains.
- Clever abstractions whose cognitive cost exceeds their benefit.

## Exceptions and trade-offs

- Essential domain complexity (a tax calculation with genuinely many legal cases) should not be papered over by an artificial split that hides the domain's real shape.
- A complexity metric like line count or branch count is a proxy, not the goal — a short function using unfamiliar tricks can be harder to follow than a longer, plain one.
- Extracting helpers purely to satisfy a linter threshold, without a real conceptual boundary behind the split, trades one form of complexity for scattered indirection.

## Verification

- Can a developer understand one local piece without understanding the entire surrounding system?
- Is the nominal path obvious?
- Can independent pieces be reasoned about separately?
- Has accidental state or indirection been removed?
