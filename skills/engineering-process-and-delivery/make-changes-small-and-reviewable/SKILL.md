---
name: make-changes-small-and-reviewable
description: "Packages work into coherent changes that are easy to understand, test, revert, and integrate. Use when scoping a multi-file feature before writing code, when a PR has grown too large to review in one sitting, or when sequencing a large refactor or migration against a behavior change. Not for branch lifecycle and merge mechanics (see manage-version-control-for-continuous-flow), how a reviewer critiques content once the PR is open (see conduct-effective-code-reviews), or splitting refactoring from feature commits specifically (see separate-feature-work-from-refactoring)."
license: MIT
---

# Make Changes Small and Reviewable

## Intent
Package work into coherent, reviewable changes that are easy to understand, test, revert, and integrate.

## Procedure
1. Before writing code, decide the smallest end-to-end slice that delivers verifiable value or can land safely behind a flag.
2. Separate mechanical changes (renames, formatting, moving files) from behavioral changes into distinct commits or PRs.
3. When a change requires both a migration and new behavior, sequence them: land the behavior-preserving migration/refactor first, then the behavior change.
4. Keep each PR to a single reviewable concern; if the description needs "and" to explain it, consider splitting.
5. For unavoidably large changes (e.g., a cross-cutting rename), use tooling (codemods, scripted diffs) and call that out so reviewers skim mechanical parts and focus on the risky ones.
6. Use feature flags or incremental rollout to decouple "merged" from "fully active," letting large changes land in small, safe increments.

## Decision rules
- If reverting a PR would also revert unrelated functionality, it's too large — split it.
- A PR whose diff a reviewer can't reasonably reason about in one sitting should be split, even if each piece "isn't done" alone (use flags or stacking).
- Prefer several small sequential PRs over one large PR, even if intermediate states are temporarily inert code.
- Pure refactors and behavior changes should not share a commit or PR.

## Anti-patterns
- Bundling an unrelated drive-by fix into a feature PR because "I was already in the file."
- A PR description that says "various improvements" instead of describing one coherent purpose.
- Splitting a change into PRs that are individually broken with no flag or branch strategy to keep main green.
- Waiting to open a PR until an entire multi-week feature is complete, so review happens on a giant diff at the end.

## Exceptions and trade-offs
- Some changes (e.g., an atomic schema rename with no compatibility shim available) genuinely can't be split further; state that explicitly in the PR description rather than pretending it's small.
- Very small teams or projects may tolerate somewhat larger PRs than a large team where reviewer context-switching cost is higher.
- Splitting has a coordination cost (more PRs to track and sequence); weigh it against a genuinely small, low-risk change that's fine as one PR.

## Verification
- Each commit in the PR builds and passes tests on its own (bisectable).
- The PR can be described in one sentence without "and."
- Reverting the PR alone, without reverting siblings, would cleanly restore prior behavior.
