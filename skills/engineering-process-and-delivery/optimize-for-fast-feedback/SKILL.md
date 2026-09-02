---
name: optimize-for-fast-feedback
description: "Moves inexpensive, high-signal checks earlier and reduces feedback latency without sacrificing important coverage. Use when a CI pipeline or local dev loop takes long enough to break flow, when deciding what runs pre-commit versus pre-push versus in CI, or when a flaky slow test is undermining trust in a fast-path check. Not for turning a check into an enforced blocking gate (see automate-quality-gates-and-delivery), choosing which analysis rules to enable (see use-static-analysis-in-the-core-workflow), or the placement of tests specifically (see use-continuous-testing-and-feedback)."
license: MIT
---

# Optimize for Fast Feedback

## Intent
Move inexpensive, high-signal checks earlier and reduce feedback latency without sacrificing important coverage.

## Procedure
1. Measure the current feedback loop: time from making a change to knowing whether it's correct, at each stage — local, pre-commit, CI, deploy.
2. Classify checks by cost and signal: fast, high-signal checks (unit tests, type checks) run first/locally; slow, lower-marginal-signal checks (full E2E suites) run later or in parallel.
3. Move fast checks as early as possible — editor-integrated, pre-commit hook, or watch mode — so failures are caught before a commit or push.
4. Parallelize independent slow checks in CI rather than running them serially.
5. Cache build and dependency-install steps between runs so re-verification doesn't re-pay fixed cost every time.
6. Identify and quarantine or fix flaky slow tests, since flakiness silently pushes people toward ignoring feedback.
7. Re-measure periodically; feedback loops silently regress as suites grow.

## Decision rules
- A check that takes long enough for a developer to context-switch away before it finishes has failed its purpose; move it later or speed it up.
- Put a check earlier in the loop only if it's both fast enough not to disrupt flow and reliable enough not to cry wolf.
- When a check can't be both fast and comprehensive, split it: a fast subset runs early, the comprehensive version runs later without blocking the immediate loop.
- Prefer fixing or removing a flaky check over leaving it in a fast-feedback stage where flakiness erodes trust.

## Anti-patterns
- Running the full test suite, including slow integration/E2E tests, on every pre-commit hook, training developers to disable it.
- A CI pipeline where slow, low-signal jobs run before fast, high-signal ones, so a trivial typo isn't caught until far into the run.
- Serial CI stages that could run in parallel with no shared dependency.
- Leaving known-flaky tests in the blocking fast path instead of quarantining them.

## Exceptions and trade-offs
- Some high-signal checks (e.g., full security scans) are inherently slow; accept that they belong later in the pipeline rather than forcing them into the fast loop.
- Extremely small projects may not need pipeline parallelization investment; the payoff scales with team and suite size.
- Over-investing in shaving seconds off an already-fast loop has diminishing returns compared to fixing a genuinely slow stage.

## Verification
- Time-to-first-signal for a typical change is measured and tracked, not assumed.
- The fastest, most frequently-run checks have a low false-positive/flake rate.
- Slow checks run in parallel with, not serially blocking, other independent slow checks.
- No known-flaky test sits in a blocking fast-feedback stage.
