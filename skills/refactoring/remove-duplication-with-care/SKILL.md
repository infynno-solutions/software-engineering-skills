---
name: remove-duplication-with-care
description: "Unifies duplicated logic that encodes one real business rule, and deliberately leaves coincidental duplication alone. Use when the same logic - not merely the same shape - has been edited in more than one place for the same reason more than once, or two similar-looking blocks turn out to encode the same rule. Not merely because a copy-paste detector flagged a match, and not for splitting one oversized function or class (see extract-and-recompose-responsibilities)."
license: MIT
---

# Remove Duplication With Care

## Intent
Remove harmful duplication that creates divergent maintenance burden, but preserve intentional duplication when sharing would create stronger unwanted coupling.

## Procedure
1. For each duplicate found, ask what it represents: the same business rule or invariant, or two independent decisions that currently happen to compute the same thing?
2. Check the change history of both copies: have they been edited together in the past, or have they diverged even slightly, suggesting they evolve independently?
3. For duplication representing one true rule, extract a single shared implementation and update every call site to use it in the same refactoring pass.
4. For coincidental duplication — same code, different reasons to change — leave it duplicated, and consider a comment noting it's intentionally not shared.
5. When sharing would require a new abstraction with several conditional branches or flags to accommodate "almost duplicates," treat that as evidence the cases are not the same rule — don't force a shared implementation into the branches.
6. After deduplicating, verify all former call sites route through the new shared implementation and none still hold a stale copy.

## Decision rules
- Duplication that changes together historically — both copies edited in the same commits over time — is a strong signal to unify.
- Duplication that has already diverged in a small but meaningful way, such as slightly different rounding or an extra validation, is evidence the two are not the same rule; don't force-unify and paper over the difference with a flag.
- Prefer unifying at the smallest scope that removes the actual duplicated logic, not the largest scope that could plausibly reuse it.
- If unifying would couple two otherwise-independent modules, such as forcing a shared dependency between two bounded contexts, the coupling cost may outweigh the duplication cost.

## Anti-patterns
- Deduplicating two blocks that are only textually similar, a linter or copy-paste-detector match, without checking whether they represent the same business rule.
- Creating a shared utility function with a boolean flag or optional parameter to handle "almost the same" logic between two call sites, a sign the abstraction is forced.
- Introducing a shared dependency between two previously-independent modules purely to eliminate a few duplicated lines, coupling their release or deploy cadence.
- Leaving a shared abstraction in place after its call sites diverge in behavior over time, rather than re-splitting it when the "one rule" assumption breaks.

## Exceptions and trade-offs
- Test code often intentionally duplicates setup logic for readability and isolation even when a shared helper is possible — the coupling and indirection cost usually outweighs the DRY benefit in tests, unless the duplication is large and truly identical.
- Duplication across service or deployment boundaries, such as two microservices independently validating the same field, may be preferable to a shared library dependency that couples their deploys.

## Verification
- Confirm the unified implementation is exercised by tests covering the behavior of every former call site.
- Confirm no call site still holds a stale, un-migrated copy of the old logic after deduplication.
- For duplication left in place, confirm the decision is recorded, via comment or PR note, so a future reader doesn't "fix" it blindly.
