---
name: choose-the-right-test-scope
description: "Matches each test to the cheapest scope - unit, integration, or end-to-end - that would actually catch the failure it guards against. Use when deciding what kind of test to write for a change, when a suite is top-heavy with slow end-to-end tests, or when two real components must agree on a contract such as an ORM mapping or serialization format. Not for whether the code is shaped to be testable at all (see design-for-testability), which doubles to use inside a test (see use-test-doubles-selectively), or where in the workflow tests run (see use-continuous-testing-and-feedback)."
license: MIT
---

# Choose the Right Test Scope

## Intent
Match each test to the cheapest scope (unit, integration, or end-to-end) that would actually catch the failure it's guarding against.

## Procedure
1. Identify the specific behavior or contract under test and the collaborators it depends on.
2. Determine what could actually break: business logic in a single class/function, wiring between two components, or the correctness of an external integration.
3. Map that failure mode to the cheapest scope that would catch it: a unit test for pure logic, a narrow integration test for a boundary, a system/e2e test only for cross-cutting flows no smaller test can prove.
4. Check whether an existing broader test already exercises this behavior indirectly; if so, prefer adding a smaller, targeted test instead of layering another broad one.
5. Count how many slow/broad tests already cover this area; if the suite is inverted (more e2e than unit), push new coverage down a level unless the risk specifically lives at the boundary.

## Decision rules
- Default to a unit test when the logic is deterministic and has no I/O; escalate scope only when the risk lives in the interaction, not the logic.
- Use an integration test when two or more real components must agree on a contract (ORM mapping, serialization format, API client against a real schema).
- Reserve full end-to-end/system tests for user-visible flows that cross multiple services or processes, where wiring failures wouldn't show up any other way.
- One end-to-end test per critical journey is usually enough; enumerate variations at the unit or integration level instead.
- When a bug escapes to production, add the smallest-scope test that would have caught it, not automatically an e2e test.

## Anti-patterns
- Writing a full browser/e2e test to check input validation or a formatting rule with zero external dependencies.
- Testing only through the UI/API surface ("ice cream cone") so a single logic bug requires debugging through several layers of indirection.
- Duplicating the same business-rule assertions at every scope "just to be safe," inflating runtime without added risk coverage.
- Calling any test that hits a real database "integration" when a contract test against a fake would catch the same class of bug faster.

## Exceptions and trade-offs
- Legacy code with no seams may force integration-level tests until it's refactored for testability; treat that as a deliberate stopgap, not the target state.
- High-risk regulatory or financial workflows can justify redundant coverage across scopes even though it costs runtime.
- Greenfield exploratory code sometimes ships with only a thin top-level test until the design stabilizes enough to unit test economically.

## Verification
- For each new test, name the specific failure it would catch and confirm no smaller-scope test could catch the same failure equally well.
- Check the suite's scope distribution (unit vs integration vs e2e counts/runtime) isn't trending toward the ice-cream-cone shape.
- Confirm broad tests assert on user-observable outcomes, not on internals that a narrower test should own.
