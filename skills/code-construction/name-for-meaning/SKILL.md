---
name: name-for-meaning
description: "Chooses names that communicate purpose and domain meaning without needing the surrounding code. Use when naming a new variable, function, or flag, when renaming a generic or inconsistent symbol, or when a review flags two equivalent concepts named differently across nearby APIs. Not when a good name cannot be found because the unit has no single coherent responsibility, where the real fix is design-cohesive-functions or design-cohesive-classes, and not for top-level folder and module naming (see let-architecture-scream-the-domain)."
license: MIT
---

# Name for Meaning

## Intent

Use names that communicate purpose, responsibility, domain meaning, and relevant behavior clearly enough that the reader does not need surrounding implementation to decode them.

## Procedure

1. Identify the concept represented by the symbol.
2. Name it according to its role, not its current implementation.
3. Make common operations use consistent naming conventions.
4. Include important distinctions such as units, direction, lifecycle state, or side effects when the repository's conventions permit it.
5. If a good name is difficult to find, reconsider whether the symbol has a clear responsibility.

## Decision rules

- Prefer precise names over short names.
- A routine name should communicate what the routine actually does.
- Do not use a weak name to hide an unclear responsibility.
- Use repository/language naming conventions consistently; convention is part of readability.
- Avoid encoding transient implementation details into stable domain concepts.

## Anti-patterns

- Generic names such as `data`, `result`, `process`, `handle`, or `manager` when they conceal meaningful distinctions.
- Different names for the same operation across nearby APIs.
- Reusing a variable name for unrelated purposes.
- Naming based on what a value happens to be today rather than what it means.

## Exceptions and trade-offs

- Extremely short-lived local variables, such as a loop index or a one-line lambda parameter, don't need the same descriptive weight as a long-lived public symbol.
- Established domain or mathematical vocabulary (`i`, `dx`, `x`/`y`) can be clearer than a verbose "improved" name when the audience already shares that convention.
- Renaming a widely-used public symbol has a real migration cost; weigh that against the clarity gain, and prefer a deprecation path over a silent rename on a shared API.

## Verification

- Can the symbol's purpose be inferred without reading its implementation?
- Does the name describe all important externally visible behavior of a routine?
- Are equivalent concepts named consistently across the codebase?
- Does the name expose a weak design or responsibility split?
