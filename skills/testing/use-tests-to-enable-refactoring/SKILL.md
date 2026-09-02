---
name: use-tests-to-enable-refactoring
description: "Establishes and relies on a meaningful behavioral test suite as protection while internals are restructured, writing characterization tests first where coverage is missing. Use when about to refactor a module with thin or no coverage, when a legacy function's behavior is unclear and needs pinning before restructuring, when asking whether the current suite would actually catch a regression, or when a refactor requires editing many tests just to keep them passing (a sign they are coupled to implementation). Not for defining exactly what behavior must stay the same (see preserve-observable-behavior-during-refactoring), sizing and sequencing the refactor's steps (see refactor-in-small-safe-steps), choosing the scope of a test in general (see choose-the-right-test-scope), or decoupling an individual test from internals (see test-behavior-not-implementation)."
license: MIT
---

# Use Tests to Enable Refactoring

## Intent
Use a meaningful behavioral test suite as protection while restructuring internals.

## Procedure
1. Before restructuring, identify the observable behavior the code currently exhibits (inputs to outputs/effects) that must be preserved through the refactor.
2. Check whether existing tests exercise the actual code paths about to be restructured, including error and edge cases, or only the happy path; if not, add characterization tests against current behavior first, even for legacy/undocumented code, capturing surprising or undocumented quirks as the baseline rather than the behavior you assume it should have.
3. Run the new or existing tests against the pre-refactor code to confirm they pass; a red test before anything has changed means the test itself is wrong.
4. Run the full relevant test suite green before starting, so any new red after a refactoring step is attributable to that step.
5. Refactor in small, reversible steps, re-running the safety-net tests after each step rather than batching many structural changes before checking.
6. Once the new structure is in place, resist changing test internals to match — behavior-focused tests should still pass unmodified; only update tests whose assertions were coupled to the old implementation.

## Decision rules
- Never refactor code with materially untested behavior "and add tests after" for anything beyond trivial, low-risk changes — write the characterization tests first.
- If a refactor requires editing many tests just to keep them passing, suspect the tests were coupled to implementation, not behavior, and fix that coupling as a prerequisite, not a side effect.
- Keep refactoring commits separate from behavior-changing commits so the safety net's job — behavior preserved — stays verifiable in isolation.
- A test suite that's slow or flaky can't function as a refactoring safety net; stabilize it before relying on it for a big restructuring.
- For legacy code with no seams, use the smallest viable technique (e.g., a wrapping characterization test around the whole class) to get a safety net before introducing seams, rather than refactoring blind.
- Write characterization tests against the current actual output, even if it looks wrong; the goal at this stage is a safety net, not correctness — fix bugs separately once the net is in place, as an intentional behavior change after the refactor.
- Test at the boundary that survives the refactor, such as a public method, API endpoint, or CLI output, rather than internal calls the refactor will itself change or remove.
- If writing a good test for a code path is impractical due to hidden dependencies such as global state or hard-coded I/O, treat that as a signal the code needs a seam introduced first, purely to make it testable, before the main refactor.
- A failing test during refactoring means stop and diagnose, not "update the test to make it pass," unless the deliberate decision is that this is now a behavior-changing step, not a refactor.

## Anti-patterns
- "Big bang" refactors that touch structure and behavior simultaneously, so a red test can't tell you which change caused the failure.
- Refactoring by deleting or loosening failing tests to make the build green again instead of investigating whether behavior actually changed.
- Skipping characterization tests on legacy code because "it would take too long," then discovering the refactor silently changed behavior in production.
- Treating 100% line coverage as proof of a safety net when the tests don't actually assert meaningful outcomes (assertion-free or trivially-true tests).
- Rewriting tests to match the new implementation's internals as part of "cleaning up" the refactor, erasing the very check that validated the refactor.
- Treating "the suite is green" as sufficient when the suite doesn't actually exercise the code paths being restructured, producing false confidence from unrelated passing tests.

## Exceptions and trade-offs
- For a genuinely trivial, mechanical refactor (rename, extract with no behavior touched, IDE-automated) with strong tooling guarantees, a full new characterization pass may be overkill — existing coverage plus the tool's guarantees can suffice.
- Time-boxed spikes/prototypes intentionally skip this discipline since the code is expected to be thrown away, not hardened — but promoting that code to production requires backfilling the safety net first.
- When no test suite exists and building one fully first is impractical, a partial safety net around the highest-risk paths, expanded incrementally, is an acceptable staged approach.
- Writing exhaustive characterization tests for code about to be deleted or replaced entirely, rather than refactored, is wasted effort — confirm the code is being restructured, not replaced, before investing in this net.

## Verification
- Confirm the full safety-net suite is green immediately before starting the refactor and after every incremental step.
- Diff the test files before/after the refactor: assertions on observable behavior should be largely unchanged; only setup/mocking tied to removed internals should differ.
- Spot-check that characterization tests added for legacy code actually exercise the risky paths being restructured, not just the easy happy path.
- Confirm new characterization tests fail if the refactor's intended change is temporarily reverted, meaning they actually test something, not tautologies.
- Confirm coverage includes error paths and edge cases the refactor touches, not only the primary happy path.
- After the refactor, confirm no tests were deleted, skipped, or loosened to make the suite pass.
