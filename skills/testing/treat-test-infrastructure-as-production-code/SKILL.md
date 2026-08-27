---
name: treat-test-infrastructure-as-production-code
description: "Maintains test helpers, fakes, harnesses, and fixtures with the discipline needed to keep tests trustworthy. Use when a fake has drifted from the real dependency it stands in for, when a helper with branching logic has no coverage of its own, or when shared fixtures force every test to specify a wall of unrelated fields. Not for choosing whether to use a double at all (see use-test-doubles-selectively), the readability of individual tests (see write-clear-maintainable-tests), or CI and developer tooling generally (see treat-tooling-as-an-engineering-product)."
license: MIT
---

# Treat Test Infrastructure as Production Code

## Intent
Maintain test helpers, fakes, harnesses, and infrastructure with the same discipline required to keep tests trustworthy.

## Procedure
1. When adding a test helper, fake, or fixture that more than one test file will use, design its API deliberately — clear name, documented behavior, single responsibility — instead of copy-pasting setup inline everywhere.
2. Give shared fakes and test doubles the same review scrutiny as production classes: does the fake's behavior actually match the real dependency's contract, including its error cases?
3. Hold test infrastructure to the same quality bars as production code — no dead code, no untested helper logic that itself has bugs, no god-object "TestUtils" file that accumulates unrelated grab-bag functions.
4. When a fake's real counterpart changes behavior (new field, new error case, changed default), update the fake in the same change; don't let it silently drift out of sync.
5. Periodically audit shared test infrastructure for helpers nobody uses anymore, or ones whose complexity now exceeds what they save.

## Decision rules
- A fake standing in for a real dependency is only trustworthy if it's kept behaviorally in sync with that dependency; assign it an owner or a contract test against the real thing.
- Test helper functions with any nontrivial logic (branching, computed values) need their own coverage, or a bug in the helper silently invalidates every test that uses it.
- Shared fixtures/builders should have sensible, minimal defaults and let each test override only what's relevant to it — not force every test to specify a wall of unrelated fields.
- Delete unused test helpers and fixtures during the same change that removes their last caller; don't let them accumulate as untended debt.

## Anti-patterns
- A hand-maintained in-memory fake of a service that hasn't been updated in a year while the real service's API moved on, so tests pass against a fiction.
- A sprawling `TestHelpers`/`Utils` file with dozens of unrelated functions, no ownership, and no tests of its own.
- Copy-pasted setup boilerplate duplicated across dozens of test files instead of extracted into one reviewed, named builder.
- Test infrastructure changes pushed without review, "it's just test code," that quietly change what every consuming test actually verifies.
- A fixture that mutates shared/global state and leaks between tests because nobody treats its lifecycle as a real concern.

## Exceptions and trade-offs
- For a one-off test with no reuse potential, inline setup is simpler and clearer than prematurely extracting a shared helper; extract only once duplication actually appears.
- A quick throwaway fake for an experimental spike doesn't need production-grade polish, but should be clearly marked and not promoted to shared infrastructure without hardening.
- Very thin wrappers, like a one-line test-data factory, don't need dedicated tests of their own if their logic is trivial and misuse would be immediately obvious from failing consumer tests.

## Verification
- Check that any fake standing in for a real dependency has been validated against that dependency's actual current contract, via a contract test or a recent manual comparison.
- Confirm shared test helpers with nontrivial logic have their own test coverage or are simple enough that failure would be obvious.
- Look for duplicated setup across test files that should be consolidated, and for helpers with zero remaining callers that should be deleted.
- Confirm test infrastructure changes went through the same review/PR process as production code changes.
