---
name: test-risky-boundaries-and-integrations
description: "Exercises the interactions where assumptions actually break - serialization, databases, external services, configuration, concurrency, real infrastructure. Use when a bug could only be caught by talking to the real dependency (actual DB engine quirks, actual JSON encoding, actual HTTP client behavior), or when a format crosses a process or storage boundary and needs a round-trip or golden-payload test. Not for choosing scope in general (see choose-the-right-test-scope), invalid inputs and error paths (see verify-unhappy-paths-and-failure-modes), or keeping such tests fast and stable (see keep-tests-fast-and-deterministic)."
license: MIT
---

# Test Risky Boundaries and Integrations

## Intent
Exercise interactions where assumptions can break: serialization, databases, services, configuration, concurrency, and real infrastructure.

## Procedure
1. List every boundary the change touches: wire format/serialization, database queries or schema, third-party API/service calls, configuration parsing, concurrency/locking, filesystem or OS interaction.
2. For each boundary, identify the assumption that could silently be wrong — the ORM maps this column the way you think, the API returns this field as a string not a number, two writers can't interleave on this row.
3. Write a test that exercises the real boundary, or the most faithful available substitute (a real local DB instance, a consumer-driven contract test against the actual API schema), rather than only a mock of it.
4. For concurrency-sensitive boundaries, add a test that forces the risky interleaving (concurrent writers, a race on initialization) rather than relying on sequential-only tests.
5. Record the specific real-world assumption each boundary test encodes, in the test name or a comment, so a future schema/API change that breaks it fails loudly and explainably.

## Decision rules
- If a bug could only be caught by talking to the real dependency (actual DB engine quirks, actual JSON encoding, actual HTTP client behavior), a mock-based test is not sufficient — use the real thing or a high-fidelity substitute.
- Prefer consumer-driven/contract tests against external services over hand-rolled mocks whose behavior can drift from the real API.
- Test serialization round-trips (encode then decode, or against a fixed golden payload) whenever a format crosses a process or storage boundary.
- Concurrency boundaries need at least one test that deliberately induces contention, not just single-threaded happy-path coverage.
- Keep these tests identifiable and separately runnable (tagged "integration") since they're slower and environment-dependent.

## Anti-patterns
- Mocking the database driver so completely that a test would still pass even if the actual SQL query were syntactically invalid.
- Trusting a hand-written stub of a third-party API that hasn't been checked against the real API's current response shape.
- Only testing serialization by asserting a mock never gets called, instead of actually serializing and deserializing a real payload.
- Skipping concurrency tests because "it's hard to write a reliable one" and shipping locking/queueing logic with only sequential coverage.
- Treating a passing integration test in a dev environment as sufficient proof for production-like config (different pool sizes, timeouts, network topology).

## Exceptions and trade-offs
- Real third-party services that are costly, rate-limited, or unreliable to call in CI justify a recorded-interaction (VCR-style) or contract test instead of live calls on every run — but refresh the contract against reality periodically.
- Full concurrency/load testing under realistic traffic may only be feasible in a staging environment, not per-commit CI; a smaller deterministic race test can still catch the core defect class.
- Local development can fall back to lightweight substitutes (in-memory DB) for iteration speed as long as the CI/pre-merge suite runs the real boundary at least once.

## Verification
- Confirm at least one test in the suite talks to the real, or a schema-faithful, version of each new/changed boundary, not exclusively a mock.
- For serialization changes, confirm a round-trip or golden-file test catches a format regression.
- For concurrency-sensitive code, confirm a test fails without the fix (lock, atomic op, transaction) and passes with it.
- Check that these tests are tagged/separated so they don't silently slow down or destabilize the fast unit suite.
