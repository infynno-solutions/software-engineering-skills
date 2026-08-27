---
name: use-test-doubles-selectively
description: "Chooses among stub, fake, mock, or the real implementation according to the boundary and its cost, avoiding doubles that make tests brittle or unfaithful. Use when deciding whether a collaborator needs only a canned answer, has behavior worth preserving, or whether the call itself is part of the contract being verified; or when a test mocks the type under test's own logic. Not for whether the design admits a seam at all (see design-for-testability), keeping a fake in sync with the real thing over time (see treat-test-infrastructure-as-production-code), or when only the real dependency can catch the bug (see test-risky-boundaries-and-integrations)."
license: MIT
---

# Use Test Doubles Selectively

## Intent
Use fakes, mocks, stubs, or real implementations according to the boundary and cost; avoid doubles that make tests brittle or unfaithful.

## Procedure
1. For each collaborator the unit under test depends on, classify it: pure/deterministic (no double needed), slow/external/nondeterministic (double needed), or something whose exact interaction is itself the behavior being verified (interaction test needed).
2. For collaborators that need a double, pick the lightest kind that's still faithful: a stub for canned return values, a fake for a lightweight working implementation (e.g., an in-memory repository), a mock only when the interaction itself — a call happened, with these args — is the thing under test.
3. Prefer a fake over a mock when the real collaborator has meaningful internal behavior (a repository that must enforce uniqueness) — a mock can't catch violations of that behavior, a fake can.
4. Keep the number of doubles per test small; if a test needs many doubles just to run, treat that as a signal the unit's dependencies are too broad rather than adding more mocking machinery.
5. Validate doubles against reality periodically (contract tests, or running the same test suite against the real implementation in a separate slower suite) so they don't drift into asserting a fiction.

## Decision rules
- Use a stub when you only need a canned answer; use a mock only when the fact that a call happened, and with what arguments, is itself part of the contract being verified.
- Use a fake in preference to a mock whenever the collaborator has behavior worth preserving in the test (ordering, uniqueness, state transitions) — a mock can't enforce that behavior back on the caller.
- Never mock the type under test's own logic — only mock its external collaborators.
- Avoid over-specifying mocks (verifying incidental call order or exact argument matchers unrelated to the behavior).
- Reach for the real implementation first; introduce a double only once the real thing is too slow, too flaky, or too costly to use directly in this test's scope.

## Anti-patterns
- Mocking a value object or a pure function that has no side effects and would be just as fast to call for real.
- "Mockist" tests that stub every single collaborator so thoroughly that the test only proves the mocks were called, not that the feature works.
- Using a mock where a fake would catch more bugs, e.g. mocking a repository's `save`/`findById` so an actual persistence bug (double-saving, wrong key) never surfaces.
- Brittle mocks with exact argument matchers on incidental details (timestamps, generated IDs) that break on unrelated changes.
- Building an elaborate custom mocking DSL/framework in-house when the collaborator could simply be swapped for a small hand-written fake.

## Exceptions and trade-offs
- For adapters whose whole job is calling another system, a mock verifying the call shape (endpoint, method, payload) is appropriate — the interaction is the behavior, ideally paired with a contract test against the real service.
- Heavyweight real dependencies (a full payment gateway, a third-party ML service) may never be practical to use directly in unit tests — a well-maintained fake is the right long-term investment there, not a one-off mock per test.
- Legacy code without seams may force liberal mocking in the short term until it's refactored for testability; treat that as a temporary cost, not a target design.

## Verification
- For each double in a changed test, confirm it's the lightest kind (stub/fake/mock) that still lets the test catch the bug it's meant to catch.
- Check that mocked interactions being verified are actually part of the contract, not incidental implementation detail.
- Confirm a fake standing in for stateful behavior (uniqueness, ordering, transactions) actually enforces that behavior rather than just returning canned data.
- Count doubles per test; investigate any test needing more than a handful as a possible design smell.
