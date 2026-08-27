---
name: apply-defensive-programming
description: "Makes invalid inputs and unexpected states fail loudly and diagnosably at trust boundaries and state transitions, instead of propagating corruption. Use when validating an HTTP payload, guarding a null or unexpected value returned from a third-party library, rejecting a config file that fails schema checks, or hardening a state machine against a transition that should never occur. Skip for a call site already covered by a validated boundary. Not for compile-time type errors (see use-compiler-and-static-feedback), an implicit dependency rather than an untrusted input (see make-dependencies-explicit), or runtime failure handling such as retries and timeouts (see design-for-failure, make-retries-safe-and-bounded)."
license: MIT
---

# Apply Defensive Programming

## Intent

Make incorrect assumptions, invalid inputs, and unexpected states fail in controlled and diagnosable ways rather than silently propagating corruption.

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

## Exceptions and trade-offs

- Every defensive check has a runtime and readability cost; do not re-validate the same invariant at every call site once a boundary already enforces it.
- In hot paths, prefer a single upfront validation over a repeated per-iteration check.
- Assertions meant to catch programmer errors are often stripped in release builds per language convention; do not conflate them with user-facing error handling that must survive in production.
- When the type system can make the invalid state unrepresentable, prefer that over a runtime check.

## Verification

- What invalid states can enter here?
- Where are they first detected?
- Does the failure preserve useful diagnostic information?
- Is the chosen failure mechanism consistent with the surrounding system?
