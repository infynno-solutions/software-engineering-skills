---
name: use-static-analysis-in-the-core-workflow
description: "Integrates linters, type checkers, and SAST scanners into editing, review, and submission workflows, emphasizing actionable signal quality. Use when adding or configuring an analyzer, when its output is being routinely ignored, or when deciding which rules should be blocking versus warning. Not for choosing which dependencies to track for vulnerabilities (see manage-dependencies-explicitly), where in the pipeline a check runs for latency reasons (see optimize-for-fast-feedback), or one engineer acting on local compiler and lint output (see use-compiler-and-static-feedback)."
license: MIT
---

# Use Static Analysis in the Core Workflow

## Intent
Integrate useful automated analyses into editing, review, and submission workflows, emphasizing actionable signal quality.

## Procedure
1. Run static analysis — linter, type checker, security/SAST scanner as relevant — in the editor and pre-commit/pre-push, not only as a separate manual step.
2. Curate the ruleset: enable rules that catch real defects or genuine maintainability problems; disable or downgrade rules that mostly produce noise for this codebase.
3. Fix or explicitly suppress, with a stated reason inline, existing violations before making a new rule blocking, so the signal starts clean.
4. Make violations blocking in CI once the local/pre-commit signal is reliable, so static analysis is enforced consistently, not just advisory.
5. Track false-positive reports and prune or tune rules that generate them repeatedly, rather than letting people learn to ignore the tool's output.
6. Periodically add new checks as the codebase or team encounters a bug class a rule would have caught, closing the loop from incident to prevention.

## Decision rules
- A rule stays enabled only if it catches real problems often enough to be worth its noise; track and prune otherwise.
- Prefer catching an issue class with a rule over relying on reviewers to notice it manually in every PR.
- New rules that would generate a large backlog of existing violations should land non-blocking or auto-fixed first, then flip to blocking after cleanup.
- Suppressions need a stated reason at the suppression site, not a bare disable comment.

## Anti-patterns
- Static analysis output that's generated but nobody reads because it's not wired into the workflow people actually use.
- A ruleset so noisy with false positives that people reflexively ignore all its output, including real findings.
- Blanket-disabling a rule at the project level because of a handful of false positives, instead of fixing or scoping the exceptions.
- Adding a large, aggressive ruleset all at once as blocking, dumping hundreds of pre-existing violations on the team overnight.

## Exceptions and trade-offs
- Some analyzers (deep security/SAST scans) are too slow for the pre-commit path; run those in CI or on a schedule instead, accepting slower feedback for that class of check.
- Generated code or vendored/third-party code is often reasonably excluded from lint/type-check scope rather than forced to pass project rules.
- A legacy codebase adopting static analysis for the first time may need a long non-blocking ramp period rather than immediate enforcement.

## Verification
- Static analysis runs automatically — editor, pre-commit, or CI — not only when someone remembers to invoke it manually.
- Current violation count for blocking rules is zero, or explicitly suppressed with reasons, not just "mostly clean."
- A sample of recent real bugs is checked against whether an achievable rule addition would have caught it.
