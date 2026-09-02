---
name: separate-feature-work-from-refactoring
description: "Keeps commits and PRs for structural refactoring distinct from behavior changes, so each can be reviewed and reverted independently. Use when a feature needs surrounding code restructured to land cleanly, or a diff is growing to mix a rename or extraction with new behavior. Not for defining what counts as an observable-behavior change in the first place (see preserve-observable-behavior-during-refactoring), nor for general PR-size discipline (see make-changes-small-and-reviewable)."
license: MIT
---

# Separate Feature Work From Refactoring

## Intent
Keep feature behavior changes conceptually separate from pure structural refactoring so reviews, tests, and debugging remain tractable.

## Procedure
1. When a feature requires restructuring existing code to fit cleanly, do the restructuring first, as its own commit or PR with no behavior change, before writing the new feature logic.
2. Get the refactoring-only change merged, or at least reviewed and approved, on its own, so reviewers evaluate structure and behavior-preservation independently of new logic.
3. Layer the feature or behavior change on top of the now-restructured code in a separate commit or PR.
4. If a refactor is discovered to be needed during feature work already in flight, stop and extract the refactor into its own commit retroactively rather than leaving it interleaved.
5. In the PR description, label each commit or PR explicitly as "refactor: no behavior change" or "feature: behavior change" so reviewers know which review lens to apply.

## Decision rules
- If a diff both restructures code and changes what it does, split it before requesting review — reviewers cannot verify "no behavior change" claims on a mixed diff.
- Sequence refactor-then-feature by default; only interleave when the refactor is too small to be worth a separate review cycle, such as a single obvious rename.
- A refactor commit should be revertible independently of the feature commit that follows it — if reverting the refactor alone would break the feature commit, they weren't actually separable.
- When time pressure tempts combining them, weigh the review and debugging cost of a mixed diff against the modest overhead of two smaller reviews.

## Anti-patterns
- A PR titled "Add discount feature" that also renames several classes and changes an internal data structure, forcing reviewers to untangle which lines are risk-bearing.
- Claiming a large mixed diff is "mostly just refactoring" as a way to rush it through review with less scrutiny of the behavior change buried inside.
- Splitting commits by refactor and feature after the fact but leaving them in one PR or review request, so reviewers still can't approve them independently.
- Doing the refactor only in service of the feature and abandoning it if the feature is later cut, when the refactor had independent value.

## Exceptions and trade-offs
- For a trivial, obviously-safe refactor, such as renaming a local variable or extracting a two-line block used once, the overhead of a separate PR may exceed its benefit — use judgment on the size threshold.
- Under a hard deadline, combining a small refactor with a feature to avoid a second review round-trip may be pragmatic, but the trade-off in harder revert and harder review should be a conscious choice, not a default.

## Verification
- Confirm the refactor-only commit or PR has passing tests with zero behavior change and no new functionality mixed in.
- Confirm the feature commit or PR, viewed alone against the post-refactor baseline, contains only the intended new behavior.
- Confirm each commit could be reverted independently without breaking the other's stated purpose.
