---
name: apply-defensive-programming
description: "Make incorrect assumptions, invalid inputs, and unexpected states fail in controlled and diagnosable ways rather than silently propagating corruption. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Apply Defensive Programming

## Intent

Make incorrect assumptions, invalid inputs, and unexpected states fail in controlled and diagnosable ways rather than silently propagating corruption.

## Apply when

Use this skill at:

- public APIs
- trust boundaries
- file/network/database boundaries
- configuration parsing
- state transitions
- code handling external or partially trusted data

## Procedure

1. Identify assumptions the code makes about its inputs and environment.
2. Determine which assumptions should be enforced by types, validation, assertions, or explicit error handling.
3. Reject impossible or invalid states close to their source.
4. Choose error-handling behavior that matches the contract and operational context.
5. Preserve enough information to diagnose the failure.

## Decision rules

- Defend boundaries where invalid data can enter the system.
- Prefer strong types and explicit contracts when the language supports them.
- Use assertions for programmer invariants and explicit error handling for expected operational failures, according to repository conventions.
- Do not add validation that duplicates guarantees already enforced by a reliable boundary without a reason.

## Anti-patterns

- Silently accepting invalid input.
- Catching errors and continuing with an invalid or ambiguous state.
- Using exceptions as arbitrary control flow when simpler mechanisms are clearer.
- Validating everywhere because validation was missing at the real boundary.

## Verification

- What invalid states can enter here?
- Where are they first detected?
- Does the failure preserve useful diagnostic information?
- Is the chosen failure mechanism consistent with the surrounding system?


## Related skills

- CODE-06 Make Dependencies Explicit
- CODE-09 Minimize State and Side Effects
- CODE-14 Use Compiler and Static Feedback
- REL-01 Design for Failure
