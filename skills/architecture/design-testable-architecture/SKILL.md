---
name: design-testable-architecture
description: "Shapes core business logic so it runs in fast in-process tests with no database, server, or UI. Use when a rule can only be tested through an HTTP request or a live database, or it lives inside a controller or handler. Not for the general policy/detail split (see separate-policy-from-details), database- or framework-specific coupling (see keep-databases-as-details, keep-frameworks-as-details), or writing the tests themselves (see design-for-testability, write-clear-maintainable-tests)."
license: MIT
---

# Design Testable Architecture

## Intent
Make the core business/decision logic callable and verifiable in isolation — in memory, without a database, network, UI, or framework runtime — so most tests are fast, deterministic, and don't require standing up the full system.

## Procedure
1. Locate the actual decision or business rule inside the code under test — the part that takes inputs and produces a decision/output, as distinct from the parts that fetch input from a database, render output to a UI, or handle an HTTP request.
2. Extract that decision logic into a plain function, method, or class with no dependency on a framework base class, database client, HTTP context, or UI toolkit — its inputs and outputs should be plain data or domain objects.
3. For any external dependency the logic genuinely needs (current time, a random value, an external lookup), pass it in as an explicit parameter or interface rather than reading it from a global, static call, or ambient context — so a test can supply a controlled value.
4. Where the logic must interact with I/O (persistence, network calls) as part of its job, depend on a narrow interface expressed in the logic's own vocabulary, and provide a fast in-memory fake implementing that interface for tests.
5. Push the remaining framework/UI/I/O-specific code to a thin adapter layer (sometimes called a "humble object") that does as little as possible besides calling the extracted logic and translating input/output — thin enough that it barely needs testing itself, or is covered by a small number of end-to-end tests instead of many unit tests.
6. Write the test against the extracted logic directly: construct inputs as plain data, call the function/method, assert on the output — no server start, no database, no browser.
7. Confirm test run time and flakiness improve: an in-process unit test for business logic should run in milliseconds and never fail due to network/timing issues.

## Decision rules
- If testing a business rule requires standing up infrastructure the rule doesn't conceptually need (a database, a server, a browser), the rule is in the wrong place — extract it.
- Logic that decides something (validate, calculate, authorize, transform) should be reachable by a test without going through the delivery mechanism (HTTP, CLI, UI) that happens to invoke it in production.
- Prefer passing dependencies explicitly (constructor/parameter injection) over reaching for them via static/global access, singletons, or ambient framework context — explicit dependencies are what make substitution in tests possible.
- The adapter/humble-object layer should be thin enough that its own defect surface is small; if it's accumulating real logic, that logic should be extracted further into the testable core.
- Favor a small number of true end-to-end tests to cover wiring and infrastructure integration, and many fast unit tests to cover business-rule variations — not the reverse.

## Anti-patterns
- Business validation or calculation logic written directly inside an HTTP controller/handler method, framework lifecycle callback, or UI event handler, so the only way to test it is through that entry point.
- A "unit test" that spins up a real database, a real HTTP client, or a headless browser to test a decision that doesn't actually need any of those to compute its answer.
- Reading the current time, a feature flag, or a random seed directly from a static/global source inside business logic, making the outcome untestable without monkeypatching or clock manipulation.
- A test suite where most tests need extensive fixture/container setup because core logic is entangled with infrastructure, so every test pays an I/O cost even for logic that's conceptually pure.
- Mocking so many collaborators that the test no longer verifies real behavior, just that specific methods were called — a sign the extracted logic still has too many entangled responsibilities rather than one clear decision to test.

## Exceptions and trade-offs
- Some logic genuinely is "call this external system and use the answer" with no independent decision to isolate; for that, an integration test against a real (or realistic sandboxed) dependency is more honest than an artificial unit test around a fake.
- Extracting every trivial pass-through function into its own testable unit for its own sake adds indirection without adding real test value — apply this skill where there's actual decision logic worth isolating, not to every line of code.
- Early-stage prototypes where the "business logic" is still being discovered may reasonably stay entangled with the delivery mechanism until the logic stabilizes enough to be worth extracting — don't over-invest in testability structure before the logic settles.

## Verification
- The core decision logic under review can be unit-tested with plain in-memory inputs and outputs, with zero database, network, or UI dependency required to run the test.
- Time, randomness, and other ambient inputs the logic depends on are passed in explicitly, not read from global/static state.
- The adapter/controller/handler layer contains little to no untested business logic of its own — it's thin enough to trust by inspection or a handful of integration tests.
- Test run time for the business-logic suite is fast (typically sub-second per test) and doesn't depend on external service availability.
