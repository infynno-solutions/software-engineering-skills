---
name: keep-tests-fast-and-deterministic
description: "Controls external dependencies, time, randomness, and concurrency so test feedback is repeatable and fast enough for normal development. Use when a test fails differently on two consecutive runs with no code change, when tests sleep on real time for timeouts or debouncing, when unseeded randomness makes failures irreproducible, or when the suite is too slow to run routinely. Not for where in the pipeline tests run or which gate blocks a merge (see use-continuous-testing-and-feedback), or for the fidelity of a fake against the real dependency (see use-test-doubles-selectively, treat-test-infrastructure-as-production-code)."
license: MIT
---

# Keep Tests Fast and Deterministic

## Intent
Control external dependencies, time, randomness, and concurrency so test feedback is repeatable and fast enough for normal development.

## Procedure
1. Identify every source of non-determinism in the test: wall-clock time, random values, thread/goroutine scheduling, network calls, filesystem ordering, unseeded UUIDs.
2. Replace real time with an injectable/fake clock; replace real randomness with a seeded or fixed generator so assertions don't depend on "now" or "chance."
3. Replace real sleeps/polling waits with explicit synchronization (await a specific event or condition) instead of `sleep(n)` guesses.
4. Isolate the test from shared external state — no test should depend on another test's leftover data, execution order, or a shared mutable fixture.
5. Route real I/O (network, disk, DB) through a boundary that can be swapped for an in-memory or local substitute for the tests that don't specifically need the real thing.
6. Measure: if a test or suite is slow enough to discourage running it locally, profile what's actually taking the time (setup, real I/O, unnecessary sleeps) before adding parallelism as a band-aid.

## Decision rules
- A test that can fail differently on two consecutive runs with no code change is a bug in the test, not acceptable noise — fix or delete it, don't just retry it.
- Prefer fake/virtual time over real `sleep()` for anything involving timeouts, debouncing, or scheduling.
- Seed all randomness used in tests, including via test-data generators/fuzzers, so failures are reproducible from the seed.
- Keep the default local/CI test run free of real network calls; anything hitting a live external service belongs in a separate, explicitly-marked slow/integration suite.
- Tests must be safe to run in parallel and in any order — no reliance on shared global state or execution sequence.

## Anti-patterns
- `Thread.sleep(2000)` or equivalent used to "wait long enough" for an async operation instead of waiting on the actual signal.
- Tests that pass locally but flake in CI due to timing assumptions tied to machine speed.
- Using `new Date()` / `DateTime.Now()` directly inside code under test with no way to control it from the test.
- Retrying a flaky test automatically until it passes instead of diagnosing the non-determinism.
- Sharing one database or fixture across tests without resetting state, so test order changes the outcome.

## Exceptions and trade-offs
- A small, clearly-labeled slow/integration suite that hits real infrastructure is fine and often necessary — the goal is isolating it from the fast feedback loop, not eliminating it.
- Some concurrency bugs only reproduce under real scheduling pressure; a dedicated stress/soak test, run separately rather than on every commit, is an accepted exception to strict determinism.
- Fixed random seeds can mask edge cases a truly random input would find; periodically running with rotating seeds, and recording the seed on failure, balances reproducibility with coverage.

## Verification
- Run the suite (or the changed tests) multiple times in a row, and in isolation vs. full-suite, to confirm identical results.
- Check for any direct use of system clock, unseeded RNG, or bare `sleep` in the changed test or the code path it exercises.
- Confirm the fast/local suite's total runtime hasn't regressed past the team's feedback-loop budget; slow tests should be tagged and separately invocable.
