---
name: test-behavior-not-implementation
description: "Asserts externally meaningful behavior and contracts rather than incidental internal structure. Use when refactoring internals without changing observable behavior breaks a test, when assertions check which private methods were called and in what order, or when a mock-verify assertion could be a state assertion instead. Not for whether a mock, fake, or real object is the right collaborator (see use-test-doubles-selectively), test naming and readability (see write-clear-maintainable-tests), or using a suite as cover for a refactor (see use-tests-to-enable-refactoring)."
license: MIT
---

# Test Behavior, Not Implementation

## Intent
Assert externally meaningful behavior and contracts rather than locking tests to incidental internal structure.

## Procedure
1. Identify the public contract of the unit under test: its inputs, outputs, observable side effects, and error conditions — the things a caller actually depends on.
2. Write assertions against that contract (return values, state changes visible through the public API, messages sent to real collaborators) rather than against private fields, method call sequences, or internal helper functions.
3. When a test needs to reach into private state or call a private method to make an assertion, treat that as a signal to either expose the behavior through the public API or drop the assertion.
4. For interaction-heavy code, verify only the interactions that are actually part of the contract (e.g., "an email gets sent") — not incidental implementation details of how it gets sent internally.
5. Before finalizing a test, mentally swap in a second implementation that satisfies the same behavior differently (or perform a small internal refactor) and confirm the test would still pass.

## Decision rules
- If refactoring the internals of a unit without changing its observable behavior breaks a test, that test is coupled to implementation and should be rewritten.
- Assert on outputs and observable state, not on which private methods were called or in what internal order, unless that order is itself part of the documented contract.
- Prefer state-based assertions over interaction-based (mock-verify) assertions whenever the state is directly observable.
- Use interaction verification (`verify(mock).method()`) only for effects with no observable return value or state — not as a default testing style.

## Anti-patterns
- Testing a private/helper method directly, via reflection or by making it public just for tests, instead of testing it through the public behavior that uses it.
- Mocking every collaborator and asserting the exact sequence of calls, so any internal reordering that preserves behavior still breaks the test.
- Snapshot-testing an internal data structure or object graph instead of the meaningful output a consumer would see.
- Naming and structuring tests after implementation details (`testCallsRepositoryTwice`) rather than after behavior (`returnsCachedResultOnSecondCall`).

## Exceptions and trade-offs
- Some algorithms (a specific sort or caching strategy) are themselves the contract — asserting on the specific approach used there is legitimate, not implementation-coupling.
- For adapters whose entire job is to call another system correctly, interaction tests against that call (arguments, endpoint, payload shape) are the behavior being tested, not an implementation detail.
- Characterization tests on legacy code may deliberately pin current implementation behavior, quirks included, as a safety net before refactoring — a temporary, intentional exception.

## Verification
- Confirm each assertion could still pass under a plausible alternative implementation that preserves the same externally observable behavior.
- Grep the test file for calls into private/internal members, direct field access, or mock-verify calls on methods with no external effect; justify or remove each one.
- Perform, or mentally simulate, a non-behavior-changing refactor and confirm the test suite doesn't need to change.
