---
name: use-continuous-testing-and-feedback
description: "Places the right tests at the right workflow stages so evidence about a change arrives before the author context-switches. Use when deciding what runs pre-commit, in PR checks, or post-merge; when a blocking gate is slow or unreliable enough that people route around it; or when flaky tests need quarantining out of a blocking stage. Not for making the tests themselves fast and deterministic (see keep-tests-fast-and-deterministic), what scope each test should be (see choose-the-right-test-scope), or CI infrastructure and release gates generally (see use-continuous-integration, automate-quality-gates-and-delivery)."
license: MIT
---

# Use Continuous Testing and Feedback

## Intent
Run the right tests at the right workflow stages to provide timely evidence about whether a change is safe to progress.

## Procedure
1. Inventory the test suite by cost (runtime) and signal (what class of bug each layer catches): fast unit tests, slower integration tests, full e2e/system tests, nightly/scheduled suites.
2. Assign each layer to the earliest workflow stage where it's cheap enough to run without discouraging the behavior that stage is for — sub-second checks on save/pre-commit, minutes-scale checks on PR, longer suites pre-merge or nightly.
3. Ensure a developer gets a signal on the specific change they made before it's buried under unrelated work: fast tests local or on push, not only after a batch of commits lands.
4. Make failing feedback actionable: a CI failure should point at what broke and why, not require reproducing the whole pipeline locally to understand.
5. When a stage becomes a bottleneck (CI queue backs up, PR checks take too long), move slow-but-low-signal tests to a later or scheduled stage rather than skipping them or leaving everyone blocked.

## Decision rules
- Feedback that arrives after a developer has moved on to something else is much less valuable than the same feedback arriving before they context-switch — optimize placement, not just existence, of each check.
- Anything that blocks a merge should run reliably and fast enough that people don't route around it, e.g. by merging with failing checks or disabling the gate.
- Non-deterministic or environment-flaky tests must not sit in a blocking stage — quarantine them to a monitored, non-blocking stage until fixed.
- Nightly/scheduled runs are for coverage that's valuable but too slow or too flaky for per-PR gating, not a dumping ground for tests nobody wants to fix.
- The earlier and cheaper a check is, the more often it should run; the more expensive, the less frequently.

## Anti-patterns
- A single monolithic CI stage that runs every test (unit through e2e) serially, so a one-line fix waits 40 minutes for feedback that could have come in 30 seconds.
- Disabling or skipping a flaky blocking test instead of fixing it or moving it to a quarantined, non-blocking stage.
- Running expensive e2e suites on every commit to every branch when they only need to run pre-merge or nightly.
- Merging with CI red because "it's always flaky anyway," which erodes the entire point of the gate.
- No feedback loop before merge at all, relying solely on a nightly build to discover breakage a day after it happened.

## Exceptions and trade-offs
- Small teams or early-stage projects may reasonably run everything in one stage until suite size actually causes pain; don't over-engineer pipeline staging preemptively.
- Some checks (security scans, license audits, load tests) are inherently slow and belong in a scheduled or pre-release stage even though earlier feedback would in principle be nicer.
- Splitting stages adds pipeline complexity and maintenance cost; only split once a specific stage is demonstrably the bottleneck.

## Verification
- Confirm the fastest, most frequently-run stage (pre-commit/on-push) actually catches the most common class of regression for this codebase.
- Check CI dashboards/logs for chronically flaky tests sitting in a blocking stage and confirm they're tracked for fix or quarantine.
- Time each pipeline stage and confirm none of them silently grew past the point where people start ignoring or bypassing it.
- Confirm a broken blocking check actually blocks the merge (branch protection / required status checks are correctly configured).
