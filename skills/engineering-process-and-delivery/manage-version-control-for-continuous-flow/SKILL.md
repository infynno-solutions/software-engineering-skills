---
name: manage-version-control-for-continuous-flow
description: "Keeps work integrated, understandable, and reversible while minimizing long-lived divergence. Use when choosing a branching strategy, when a branch has been open longer than expected, when setting merge-versus-rebase policy, or when structuring commit history. Not for how large or coherent a single change's content should be (see make-changes-small-and-reviewable); this skill covers branch and commit lifecycle and integration cadence rather than diff sizing."
license: MIT
---

# Manage Version Control for Continuous Flow

## Intent
Use version-control practices that keep work integrated, understandable, and reversible while minimizing long-lived divergence.

## Procedure
1. Branch from the latest mainline and scope the branch to a single piece of work with a bounded expected lifetime.
2. Merge or rebase from mainline into the branch frequently — at least daily for active branches — to keep divergence small.
3. Prefer merging completed work back to mainline quickly, using feature flags for anything not yet user-visible, over keeping the branch alive until "fully done."
4. Keep commit history meaningful: each commit should be a coherent, buildable step, with a message explaining why, not just what.
5. Choose merge vs. rebase per team convention, but apply it consistently so history stays navigable.
6. Delete branches promptly after merge; treat a lingering unmerged branch older than the team's norm as a signal to finish, split, or abandon it.

## Decision rules
- If a branch has been open longer than roughly the team's sprint/iteration length without merging, actively resolve that rather than letting it sit.
- Prefer trunk-based short-lived branches over long-lived environment or feature branches that accumulate drift.
- Squash noisy WIP commit history before merge; preserve meaningful separate commits when each is independently useful for review or bisect.
- Resolve merge conflicts by re-integrating frequently, not in one large resolution at the end of a long-lived branch's life.

## Anti-patterns
- Long-lived environment branches (e.g., a persistent `develop` diverging from `main` for months) requiring painful periodic merge-backs.
- Rebasing shared, already-pushed branches that others have based work on, rewriting history out from under them.
- Commit messages that only restate the diff ("fix stuff," "wip") with no rationale.
- Avoiding merge to mainline because the branch "isn't done," instead of using a flag to merge incomplete-but-safe work continuously.

## Exceptions and trade-offs
- Some workflows (e.g., release branches for a shipped product with a support window) legitimately need longer-lived branches; scope and document their lifecycle explicitly rather than letting them become permanent forks.
- Rebase-heavy history rewriting is fine on solo/private branches but is a trade-off against shared-branch safety once others build on it.
- Squashing loses fine-grained history; keep separate commits when a bisect-relevant sequence is more valuable than a clean single-commit summary.

## Verification
- No active branch has diverged from mainline longer than the team's agreed threshold without a documented reason.
- History for merged work is either linear-and-bisectable or has clear merge-commit boundaries, per the team's chosen convention.
- Deleted or stale branches don't linger in the remote past their merge.
