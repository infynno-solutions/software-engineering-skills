---
name: verify-unhappy-paths-and-failure-modes
description: "Deliberately tests invalid inputs, failures, retries, timeouts, boundary conditions, and unexpected side effects. Use when a catch, validation check, or error return has no test that actually triggers it; when only typical mid-range inputs are covered and not empty, zero, negative, or maximum values; or when retry and timeout logic is untested for termination. Not for the runtime design of those failure behaviors (see design-for-failure, make-retries-safe-and-bounded, use-timeouts-and-deadlines), or for integration-boundary risk generally (see test-risky-boundaries-and-integrations)."
license: MIT
---

# Verify Unhappy Paths and Failure Modes

## Intent
Deliberately verify invalid inputs, failures, retries, timeouts, boundary conditions, and unexpected side effects.

## Procedure
1. For each public operation being tested, enumerate its failure surface: invalid/malformed input, missing/null values, boundary values (empty, zero, max, off-by-one), and the failure modes of every collaborator it depends on (timeout, exception, partial failure).
2. For each identified failure mode, write a test asserting the specific expected behavior — the right exception/error type, the right fallback value, the right retry/backoff, or the right cleanup — not just "it doesn't crash."
3. For retry/timeout logic specifically, test both that it retries/times out under the failure condition and that it stops (doesn't retry forever, respects the timeout) under sustained failure.
4. Check side effects on the failure path: partial writes, resource leaks, whether a failed operation left the system in a consistent state (a transaction rolled back, a lock released, a connection closed).
5. Cross-reference recent incidents/bugs in this area — each one implies a failure mode that wasn't covered; add a regression test for it specifically.

## Decision rules
- Every code path with a `catch`/`except`/`rescue`, a validation check, or a conditional error return needs at least one test that actually triggers it — untested error-handling code is a common home for silent bugs.
- Boundary values (empty collection, zero, negative, max-int, empty string, single-element) get explicit tests, not just "typical" mid-range inputs.
- Retry and timeout logic must be tested for termination (it does eventually stop) as rigorously as for triggering (it does retry/timeout when expected).
- When an operation can partially fail (multi-step write, batch operation), test that partial failure leaves state consistent, not just that the whole-success and whole-failure cases work.
- Failure-path tests should assert on the specific error/outcome the caller needs to act on, not merely that "an exception was thrown."

## Anti-patterns
- A PR that adds a `try/catch` or validation branch with zero tests exercising the catch/invalid branch.
- Testing only that an exception "is thrown" without asserting its type, message, or the resulting state, so a caller catching the wrong exception type would still pass.
- Retry logic tested only for "it retries once" with no test proving it eventually gives up, risking infinite retry loops in production.
- Treating "the happy path passed" as sufficient sign-off for a change whose entire purpose was to add error handling.
- Swallowing exceptions in test setup/helpers so a failure in the code under test gets masked instead of surfaced by the test.

## Exceptions and trade-offs
- Exhaustively testing every combination of invalid input is rarely worth it; prioritize failure modes by real-world likelihood and blast radius (malformed user input over a truly impossible internal state).
- Some failure modes (hardware failure, OS-level resource exhaustion) are impractical to trigger in a normal test and are better handled by fault-injection/chaos testing as a separate, occasional exercise.
- For prototype/spike code explicitly not headed to production, skipping failure-path coverage is a reasonable, time-boxed trade-off — but it must be backfilled before the code ships.

## Verification
- Confirm every new/changed error-handling branch (catch block, validation guard, early return on failure) is reached by at least one test.
- Confirm retry/timeout logic has a test proving eventual termination, not only a test proving it triggers.
- Check that boundary and empty/null/zero cases for new inputs have explicit tests, not just typical-value cases.
- For multi-step operations, confirm a partial-failure test verifies the system is left in a consistent, documented state.
