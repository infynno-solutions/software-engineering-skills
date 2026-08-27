---
name: keep-control-flow-understandable
description: "Keeps the normal execution path visible and unobscured by nested error handling. Use when several levels of nested try/catch bury an operation's main sequence of steps, or when deciding where the happy path should exit versus where an exceptional case should short-circuit it. Not for restructuring the predicates themselves (see simplify-conditional-logic), complexity spanning a whole function or class (see minimize-function-and-class-complexity), or restructuring existing nested conditionals under tests (see simplify-conditionals-and-control-flow)."
license: MIT
---

# Keep Control Flow Understandable

## Intent

Structure conditionals, loops, and exceptional paths so that the normal execution path is clear and unusual cases do not obscure the main behavior.

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

## Exceptions and trade-offs

- A domain with genuinely many distinct cases may need a wide `switch`/dispatch; flattening it artificially can make an omitted case harder to spot, not easier.
- Early-return-heavy style is not universally correct — in resource-cleanup-heavy code, a single-exit structure can be safer depending on whether the language offers `defer`/`finally`-style guarantees.
- Separating error handling from the operation it guards structurally can obscure that a specific line can fail; keep the association visible even when the code is split.

## Verification

- Can a reviewer follow the nominal path top-to-bottom?
- Are exceptional paths distinguishable?
- Is each decision understandable without parsing several nested conditions?
- Does each loop have one clear iterative purpose?
