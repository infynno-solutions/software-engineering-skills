---
name: design-cohesive-functions
description: "Gives a function one coherent purpose so its name, inputs, and effects match. Use when a function has quietly picked up an unrelated side effect under a name suggesting a narrower operation, or when extracting logic from a function that has grown to do several unrelated things. Not when the multi-responsibility problem is at class level (see design-cohesive-classes), when the purpose is clear but the branching is hard to follow (see simplify-conditional-logic), or when splitting existing code mechanically under tests (see extract-and-recompose-responsibilities)."
license: MIT
---

# Design Cohesive Functions

## Intent

Give each function a clear, coherent purpose so that its name, interface, control flow, and effects form a consistent abstraction.

## Procedure

1. State the function's single primary responsibility.
2. Check whether every major statement contributes directly to that responsibility.
3. Make the function's inputs, outputs, and side effects explicit.
4. Extract independently understandable operations when doing so improves comprehension or reuse.
5. Re-evaluate the function name after restructuring.

## Decision rules

- Functional cohesion is more important than an arbitrary maximum line count.
- The primary reason to create a routine is intellectual manageability, not merely saving lines.
- A function should not quietly perform unrelated side effects under a name that suggests a narrower operation.
- A flag that selects unrelated operations is a signal to examine whether separate functions or another design are clearer.

## Anti-patterns

- Giant functions containing unrelated operations.
- `processEverything(flag)` functions whose flag selects different responsibilities.
- Extracting trivial one-line wrappers that add no readability or semantic boundary.
- Splitting code solely to satisfy a numeric line-count rule.

## Exceptions and trade-offs

- Splitting a small, already-clear function purely to reduce line count can add indirection without improving comprehension.
- A tight algorithmic routine (a numeric kernel, a parser's inner loop) may look "non-cohesive" by naive statement-counting while actually being a single coherent computation — judge by concept, not line count.
- Extraction that requires threading many parameters through a new function boundary can trade one form of complexity for another; weigh the resulting signature against the readability gained.

## Verification

- Does the function have one clear reason for existing?
- Does its name match its actual behavior?
- Are its parameters coherent and necessary?
- Are side effects visible and unsurprising?
- Would extraction make the surrounding code easier to understand?
