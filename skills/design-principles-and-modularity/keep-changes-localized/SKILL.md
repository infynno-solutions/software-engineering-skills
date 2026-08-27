---
name: keep-changes-localized
description: "Structures responsibilities so one recurring kind of change - a new field, business rule, or format - touches one cohesive place instead of rippling across unrelated files. Use when a PR touches many files to add one enum value with a near-identical switch case in each, or when planning ahead of a repeating change type such as a new locale or currency. Not for splitting a module that changes for several unrelated reasons (see separate-responsibilities-by-reason-to-change), or for adding a seam for future variants rather than tracing an existing ripple (see design-for-extension-without-fragile-modification)."
license: MIT
---

# Keep Changes Localized

## Intent
Structure code so common changes touch a small, coherent region rather than rippling through unrelated modules.

## Procedure
1. Trace a representative change through the dependency graph.
2. Find unrelated modules affected by the same change.
3. Group or decouple responsibilities to localize the change.
4. Verify the resulting change path with tests and dependency analysis.

## Decision rules
- Before restructuring, confirm the change is one that recurs — don't localize for a change that happens once.
- Prefer consolidating the repeated logic (e.g., one lookup table or registry keyed by the new dimension) over scattering the same conditional across call sites.
- When localizing requires a new abstraction, weigh its ongoing cost against the change frequency it saves.
- Keep the localized change path discoverable — one clearly-named place a future editor will find, not merely fewer scattered edits.

## Anti-patterns
- Creating abstractions that merely move a change through many layers instead of removing the ripple.
- Splitting code without reducing change propagation.

## Exceptions and trade-offs
- Some duplication can be cheaper than coupling when it preserves independence between modules that shouldn't know about each other.

## Verification
- Re-apply (or simulate) the same class of change again and count the files/modules touched; confirm it dropped to the intended small set.
- Confirm the localized region has a test that fails if the change is forgotten there.
- Check that consolidating the change didn't merge genuinely unrelated concerns into one place just to reduce file count.
