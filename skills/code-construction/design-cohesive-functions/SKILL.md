---
name: design-cohesive-functions
description: "Give each function a clear, coherent purpose so that its name, interface, control flow, and effects form a consistent abstraction. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Design Cohesive Functions

## Intent

Give each function a clear, coherent purpose so that its name, interface, control flow, and effects form a consistent abstraction.

## Apply when

Use this skill when:

- creating a new function
- reviewing a long or unclear function
- deciding whether to extract a function
- a function has unrelated branches or multiple responsibilities
- a function needs flags to select materially different behaviors

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

## Verification

- Does the function have one clear reason for existing?
- Does its name match its actual behavior?
- Are its parameters coherent and necessary?
- Are side effects visible and unsurprising?
- Would extraction make the surrounding code easier to understand?


## Related skills

- CODE-02 Name for Meaning
- CODE-05 Minimize Function and Class Complexity
- CODE-06 Make Dependencies Explicit
- CODE-08 Simplify Conditional Logic
