---
name: use-continuous-integration
description: "Continuously assembles and tests the real evolving system, including important external and cross-service dependencies. Use when setting up or modifying a CI pipeline's integration scope, when a change touches a shared or cross-service contract, when deciding what real dependencies CI should exercise, or when the mainline build goes red. Not for turning a passing pipeline into an enforced merge or release gate (see automate-quality-gates-and-delivery), or reordering checks purely for speed (see optimize-for-fast-feedback)."
license: MIT
---

# Use Continuous Integration

## Intent
Continuously assemble and test the evolving ecosystem, including important external and cross-service dependencies.

## Procedure
1. Trigger a build-and-test run on every push/PR against the actual integration target — the current mainline branch state, not just the feature branch in isolation.
2. Include the real or a faithful representation of important external dependencies (databases, other services, message brokers) in CI, not just mocks, for paths where integration behavior matters.
3. Keep the mainline build green as the top-priority signal: a red mainline blocks further merges, or triggers an immediate fix or revert, rather than being tolerated.
4. Run the full suite frequently enough that integration problems are caught within hours, not discovered days later at release time.
5. Make CI results visible and attributable — which commit broke it — so failures get fixed quickly by whoever is best positioned to fix them.
6. When CI catches a cross-service or cross-team integration failure, treat it as a signal to tighten the tested contract, not just to patch and move on.

## Decision rules
- Every merge to mainline must pass CI against the current state of mainline, not a stale branch snapshot from when the PR was opened.
- If a class of bug only shows up when components are integrated, CI should exercise that integration, not just each component alone.
- A broken mainline build is a stop-the-line event: fix forward quickly or revert, don't let it sit red while others build on top of it.
- Include real dependency versions in CI, not just what a developer happens to have locally, to catch environment drift.

## Anti-patterns
- Feature branches integrated only at the end of a long development cycle ("big bang" merge) rather than continuously.
- CI that only runs unit tests against mocks, never exercising the real interaction with a critical dependency.
- Tolerating a red mainline build for an extended period because "everyone knows it's broken right now."
- CI configured to test only the feature branch's own commit, never re-verified against the latest mainline before merge.

## Exceptions and trade-offs
- Running every integration against fully real external dependencies (e.g., a live third-party API) may be impractical; use a faithful sandbox or contract test instead and say so explicitly.
- Early-stage projects with a single contributor get less benefit from full CI infrastructure investment than a multi-contributor project integrating frequently.
- Balance CI runtime and cost against integration coverage — not every dependency combination needs testing on every commit; some can run on a slower cadence.

## Verification
- Mainline has been green, or fixed within the team's agreed window, as of the most recent commits.
- CI actually rebuilds against latest mainline before merging a PR, not a stale base.
- A recent integration-only bug (one unit tests wouldn't catch) has a corresponding CI check added afterward.
