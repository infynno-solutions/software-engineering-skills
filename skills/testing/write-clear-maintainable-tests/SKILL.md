---
name: write-clear-maintainable-tests
description: "Makes tests concise, understandable, behavior-focused, and diagnostically useful when they fail. Use when a failed-test list gives no hint what broke without opening the file, when one test bundles unrelated scenarios, or when test data is foo and test1 rather than expired_coupon or user_with_no_email. Not for whether the assertions target behavior or internals (see test-behavior-not-implementation), the quality of shared helpers and fixtures (see treat-test-infrastructure-as-production-code), or production code readability (see write-for-the-maintainer)."
license: MIT
---

# Write Clear Maintainable Tests

## Intent
Make tests concise, understandable, behavior-focused, and diagnostically useful when they fail.

## Procedure
1. Name each test after the behavior and condition it verifies (e.g., `returns_404_when_resource_missing`) so a failure list is readable without opening the file.
2. Structure each test around a single clear scenario — arrange the specific preconditions, act once, assert the outcome (Arrange-Act-Assert or Given-When-Then) — rather than covering multiple unrelated scenarios in one test body.
3. Keep setup minimal and relevant: include only the state that matters for this scenario, and make what varies between similar tests obvious (a clearly named builder or parametrization) rather than duplicating large opaque fixtures.
4. Write assertions that fail with a message pointing directly at what's wrong (expected vs actual value, a meaningful diff) rather than a bare boolean check that requires a debugger to diagnose.
5. Remove or refactor tests whose intent isn't clear from reading them alone — a test that requires reading the production code to understand what it's checking needs a better name or clearer structure.

## Decision rules
- A test name should let someone reading a failed-test list understand what broke without opening the file.
- One logical assertion-concept per test; multiple asserts checking facets of the same outcome are fine, but unrelated scenarios belong in separate tests.
- Prefer descriptive, purpose-built test data ("expired_coupon", "user_with_no_email") over generic placeholders ("foo", "test1", "x") that give no hint about why that value was chosen.
- Assertion failure output must be self-explanatory, showing expected vs. actual; avoid `assertTrue(result.isValid())`-style asserts when a comparison assertion would show the actual mismatch.
- Prefer a small number of well-named helper/builder functions over duplicating large setup blocks across many tests, but keep the helper transparent enough that a reader can still tell what's being set up.

## Anti-patterns
- Test names like `test1`, `testFoo`, or `testBugFix1234` that give no indication of the behavior under test.
- A single test method that exercises five different scenarios with a wall of asserts, so a failure requires reading the whole body to figure out which scenario broke.
- Copy-pasted, near-identical test bodies differing in one line, where a parametrized test or shared builder would make the actual variation obvious.
- Asserting with a generic `assertTrue(...)`/`assert(...)` on a complex boolean expression instead of a comparison assertion that shows expected vs. actual.
- Comments explaining what the test does in place of a clear name and clear structure.

## Exceptions and trade-offs
- Some domains genuinely need large parametrized tables (exhaustive input-validation matrices); a single parametrized test with many rows is fine as long as each row is independently identifiable in failure output.
- Extremely thin, obvious tests (a one-line getter) may not need elaborate AAA structure — brevity itself is the clarity there.
- Shared setup via `beforeEach`/fixtures is reasonable for truly common preconditions, but only when it doesn't hide state that's actually relevant to a specific test's outcome.

## Verification
- Read the list of test names alone, no bodies, and confirm each communicates the scenario and expected outcome.
- Intentionally break the production code and check that the resulting failure message tells you what's wrong without attaching a debugger.
- Check for tests with more than one clearly distinct scenario bundled into a single test body and split them.
- Scan for generic/non-descriptive test data and rename it to reflect why that value matters to the scenario.
