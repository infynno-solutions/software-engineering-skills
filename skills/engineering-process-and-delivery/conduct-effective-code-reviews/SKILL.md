---
name: conduct-effective-code-reviews
description: "Uses review to improve correctness, readability, maintainability, and knowledge sharing rather than as a gate for personal style preferences. Use when writing or responding to review comments on a specific PR, deciding whether a comment should block merge, or resolving a disagreement between author and reviewer. Not for sizing or structuring the PR before review begins (see make-changes-small-and-reviewable), whether review is enforced as a required gate at all (see automate-quality-gates-and-delivery), or the team's feedback norms and tone (see create-healthy-review-and-feedback-culture)."
license: MIT
---

# Conduct Effective Code Reviews

## Intent
Use review to improve correctness, readability, maintainability, and knowledge sharing rather than as a gate for personal style preferences.

## Procedure
1. Read the PR description and linked issue first so you review against intent, not just the diff in isolation.
2. Do a first pass for correctness and behavior: does this do what it claims, are edge cases and error paths handled.
3. Do a second pass for structure: naming, duplication, and whether tests actually cover the change.
4. Label each comment's severity explicitly — blocking, non-blocking, nit, or question — so the author knows what must change before merge.
5. For blocking comments, state the concrete risk or defect, not just a preference; route style-only comments to a linter instead of a review comment.
6. Respond to author pushback by re-examining the evidence, not by defaulting to reviewer authority.
7. Approve as soon as blocking comments are resolved; don't hold a PR hostage to non-blocking nits.

## Decision rules
- A comment blocks merge only if it points to a correctness, security, data-loss, or maintainability risk that outweighs the cost of delay.
- If the same comment would recur on every PR (formatting, import order), it belongs in a linter, not in review.
- Prefer asking a question over asserting a fix when the reviewer is unsure of the author's intent.
- Disagreement on a non-blocking comment defaults to the author's judgment unless a third opinion is sought.

## Anti-patterns
- Rewriting the PR in comments instead of describing the problem and letting the author choose the fix.
- Blocking merge on a personal style preference not backed by a team convention or linter rule.
- Rubber-stamp approvals with no evidence the diff was actually read.
- Comments that state something is wrong without saying what would make it right.
- Letting a PR sit unreviewed past the team's expected review-latency norm.

## Exceptions and trade-offs
- Security-, compliance-, or data-migration-sensitive changes warrant slower, more thorough review than typical feature work.
- A trusted, well-tested internal-tool change from an experienced author may reasonably get a lighter review than user-facing or shared-library code.
- Under incident/hotfix pressure, review can be compressed to correctness-only, with a follow-up cleanup review after.

## Verification
- Every blocking comment has a corresponding fix or an explicit resolution before merge.
- The PR's tests actually exercise the changed behavior, not just pre-existing paths.
- The diff is re-read after requested changes land, rather than approving on trust alone.
