---
name: minimize-function-and-class-complexity
description: "Reduce the amount of code and state a developer must mentally track at once while preserving required behavior. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Minimize Function and Class Complexity

## Intent

Reduce the amount of code and state a developer must mentally track at once while preserving required behavior.

## Apply when

Use this skill when code contains:

- deep nesting
- many branches
- large functions or classes
- complex boolean expressions
- too much shared state
- multiple interacting concerns
- difficult-to-follow control flow

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

## Verification

- Can a developer understand one local piece without understanding the entire surrounding system?
- Is the nominal path obvious?
- Can independent pieces be reasoned about separately?
- Has accidental state or indirection been removed?


## Related skills

- ENG-04 Manage Essential vs Accidental Complexity
- CODE-03 Design Cohesive Functions
- CODE-07 Keep Control Flow Understandable
- CODE-08 Simplify Conditional Logic
