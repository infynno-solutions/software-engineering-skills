---
name: preserve-observable-behavior-during-refactoring
description: "Defines what counts as the same behavior that a structural change must not disturb - same inputs, outputs, errors, and side effects. Use whenever a change is framed as just structural: a rename or move, replacing a data structure, restructuring a class hierarchy, or reimplementing an algorithm to the same contract. Not for packaging commits and PRs once structural and behavioral changes are already distinguished (see separate-feature-work-from-refactoring), nor for getting tests in place to detect drift (see use-tests-to-enable-refactoring)."
license: MIT
---

# Preserve Observable Behavior During Refactoring

## Intent
Keep externally observable behavior unchanged while improving internal structure, and treat any behavior change as a separate, explicit step.

## Procedure
1. Enumerate what counts as "observable" for this unit before touching code: return values, thrown exceptions or error codes, logged output, emitted events, persisted state, timing or ordering guarantees, and public API shape.
2. Capture or confirm characterization tests, or rely on existing tests, covering those observable points, including edge cases and error paths, before restructuring.
3. Make the structural change.
4. Diff observable behavior against the pre-change baseline: run the full test suite, and where tests are thin, manually compare outputs for representative and edge-case inputs.
5. If the refactor incidentally fixes a bug or changes behavior, stop and split it into its own separate commit or PR rather than folding it into the "pure" refactor.

## Decision rules
- Treat any change to error types or messages, log lines other systems parse, ordering of side effects, or public signatures as a behavior change requiring its own review path, not "just refactoring."
- When a refactor reveals dead code or an unreachable branch, removing it is a behavior change, however small, and should be called out explicitly rather than folded in silently.
- Performance characteristics count as observable behavior when the system has performance-sensitive callers; note explicitly whether they were and were not verified.
- If no test could catch a given behavior change, treat that as a gap to fill, not as license to skip verification.

## Anti-patterns
- Labeling a commit "refactor" while also fixing a bug, changing a default, or altering an API contract inside it.
- Relying on "the code obviously still does the same thing" for complex branching or concurrency without executing tests that exercise those paths.
- Refactoring error handling and treating a changed exception type as equivalent to the old one because "it's still an error."
- Skipping verification of side effects that don't show up in a return value — logging, metrics, events, writes — because they're inconvenient to test.

## Exceptions and trade-offs
- Genuinely private, unreachable, or dead code has no external observers — removing it during a refactor is legitimate and doesn't need separate review, but confirm it's truly unreachable first.
- Some behavior, such as timing or memory allocation patterns, may be acceptable to change within a refactor if no consumer depends on it and the task explicitly documents the exception.

## Verification
- Confirm the full relevant test suite passes unchanged, with no tests edited to accommodate new behavior, after the refactor.
- Confirm public signatures, thrown exception types, and logged or emitted output formats are identical unless explicitly documented as an intended change.
- For refactors touching concurrency or ordering, confirm ordering guarantees still hold under the same conditions as before.
