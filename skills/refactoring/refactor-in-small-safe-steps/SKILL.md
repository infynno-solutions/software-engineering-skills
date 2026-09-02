---
name: refactor-in-small-safe-steps
description: "Sequences a refactor as small, verifiable moves that keep the code compiling and tests passing, instead of one all-or-nothing change. Use for any multi-step refactor, especially one touching widely-used code or likely to be interrupted part-way. Not for whether tests exist to catch regressions at all (see use-tests-to-enable-refactoring), nor for choosing automated tooling over manual editing (see use-automated-refactoring-tools-when-safe); this skill governs step sizing and sequencing."
license: MIT
---

# Refactor in Small Safe Steps

## Intent
Perform refactoring as a sequence of small, reversible structural changes so the code spends little time in a broken or incoherent state.

## Procedure
1. Break the target transformation into an ordered list of individually-named refactoring moves — rename, extract, inline, move, change signature — each small enough to hold in your head and review in isolation.
2. Order the steps so that after every single step the code compiles or runs and existing tests pass; never leave a step that depends on the next step to be correct.
3. For a signature or interface change, use expand/contract: add the new form alongside the old, migrate callers one at a time, then remove the old form as its own final step.
4. Commit, or at least checkpoint, after each step so any step can be reverted independently without unwinding the whole sequence.
5. Run the test suite, or the fastest reliable subset, after each step, not only at the end of the whole sequence.
6. If a step turns out to be bigger than expected once inside it, stop and split it further rather than pushing through.

## Decision rules
- A step that can't be described in one short sentence, such as "rename X to Y" or "extract this block into a function," is too big — split it.
- Prefer a longer chain of trivial, obviously-correct steps over a shorter chain of steps that require heavy reasoning.
- When a step would require touching many call sites at once, use a temporary shim so call sites can migrate independently across multiple steps or PRs.
- If interrupted mid-sequence, the code at the last completed step must still be shippable — that is the definition of "safe."

## Anti-patterns
- A single commit that renames a class, changes its constructor signature, and moves several methods out of it all at once, making any one failure hard to bisect.
- Leaving the codebase in a non-compiling or test-failing state "temporarily" between steps of a multi-step refactor.
- Batching unrelated small refactors into one step because they're each individually trivial — batch only genuinely dependent steps.
- Skipping test runs between steps to save time, discovering the break only after several more steps compound it.

## Exceptions and trade-offs
- Some refactorings, such as a rename across hundreds of files via a single automated tool run, are safe as one large step precisely because the tool guarantees mechanical correctness — see `use-automated-refactoring-tools-when-safe` for when that substitutes for manual step-splitting.
- Under extreme time pressure, a slightly larger step may be pragmatic, but only when the fallback of a git revert is genuinely cheap and the step is still test-verified.

## Verification
- Confirm the code compiles or type-checks and the relevant test suite passes after every individual step, not only at the end.
- Confirm each step's diff matches its one-sentence description, with no incidental extra changes riding along.
- Confirm the sequence could be safely paused after any step — that is, that step's state is shippable.
