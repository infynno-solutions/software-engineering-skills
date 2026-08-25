---
name: name-for-meaning
description: "Use names that communicate purpose, responsibility, domain meaning, and relevant behavior clearly enough that the reader does not need surrounding implementation to decode them. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Name for Meaning

## Intent

Use names that communicate purpose, responsibility, domain meaning, and relevant behavior clearly enough that the reader does not need surrounding implementation to decode them.

## Apply when

Use this skill for:

- variables and constants
- functions and methods
- classes and modules
- public APIs
- tests
- flags, states, and identifiers

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

## Verification

- Can the symbol's purpose be inferred without reading its implementation?
- Does the name describe all important externally visible behavior of a routine?
- Are equivalent concepts named consistently across the codebase?
- Does the name expose a weak design or responsibility split?


## Related skills

- CODE-01 Write Code at the Level of Intent
- CODE-03 Design Cohesive Functions
- CODE-04 Design Cohesive Classes
- CODE-11 Write for the Maintainer
