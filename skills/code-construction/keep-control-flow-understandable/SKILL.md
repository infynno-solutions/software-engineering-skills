---
name: keep-control-flow-understandable
description: Structure conditionals, loops, and exceptional paths so that the normal execution path is clear and unusual cases do not obscure the main behavior. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Keep Control Flow Understandable

## Intent

Structure conditionals, loops, and exceptional paths so that the normal execution path is clear and unusual cases do not obscure the main behavior.

## Apply when

Use this skill when writing or reviewing:

- conditionals
- loops
- state transitions
- early returns
- error paths
- nested control structures
- dispatch logic

## Procedure

1. Identify the nominal path through the operation.
2. Make that path visually and structurally obvious.
3. Separate unusual/error paths from the normal path where that improves clarity.
4. Keep each control structure focused on one coherent decision.
5. Simplify nesting and complex expressions before adding further abstractions.

## Decision rules

- Order branches for readability and according to repository conventions.
- Prefer early handling of exceptional cases when it makes the normal path clearer.
- Use the control construct that best expresses the logic.
- Do not contort code to avoid a legitimate branch when the domain actually has multiple cases.

## Anti-patterns

- Deep nesting that hides the main path.
- Complex conditions duplicated across branches.
- Error handling interleaved so heavily with normal logic that the core behavior is obscured.
- Artificial use of `switch`/`case` or equivalent constructs.

## Verification

- Can a reviewer follow the nominal path top-to-bottom?
- Are exceptional paths distinguishable?
- Is each decision understandable without parsing several nested conditions?
- Does each loop have one clear iterative purpose?


## Related skills

- CODE-05 Minimize Function and Class Complexity
- CODE-08 Simplify Conditional Logic
- CODE-13 Apply Defensive Programming
