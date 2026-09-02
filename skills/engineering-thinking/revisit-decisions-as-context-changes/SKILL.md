---
name: revisit-decisions-as-context-changes
description: "Re-evaluates past decisions when requirements, workload, team structure, operational constraints, evidence, or system age materially change. Use when traffic has grown 10x since the original database choice, when a component deferred as we will build it properly later is now load-bearing, when a postmortem reveals a failure mode the original design never anticipated, or when a once-maintainable system's difficulty traces to a specific past decision. Not when the original decision was never recorded or reasoned through (apply make-evidence-based-engineering-decisions to the current choice instead), and not for a preference for newer technology with no material change in context."
license: MIT
---

# Revisit Decisions as Context Changes

## Intent

Treat engineering decisions as contextual rather than permanent truths. Re-evaluate them when requirements, workload, team structure, operational constraints, evidence, or system age materially changes.

## Procedure

1. Recover the original decision and rationale when possible.
2. Identify which assumptions have changed.
3. Re-measure or re-evaluate the current situation.
4. Determine whether the original trade-off still holds.
5. Preserve the decision if still justified; otherwise revise it incrementally where practical.
6. Record the new reasoning and any remaining uncertainty.

## Decision rules

- Do not retain a design merely because it was once approved.
- Do not rewrite a stable component solely because a theoretical improvement exists.
- Existing complexity is a reason to improve thoughtfully, not automatically to redesign everything.
- Revisit decisions when the cost of retaining them becomes material relative to the cost and risk of change.

## Anti-patterns

- “We have always done it this way.”
- Replacing a system solely because a newer technology exists.
- Ignoring evidence because a previous architecture decision is considered settled.
- Large rewrites when incremental migration could reduce risk.

## Exceptions and trade-offs

- Not every changed assumption warrants reopening a decision — revisit when the cost of leaving it stale is material relative to the cost of re-deciding, not on every drift.
- A decision can be re-affirmed as still correct; revisiting is not the same as committing to change something.
- Prefer incremental revision over a full redesign when the original decision is only partially invalidated — a full rewrite carries its own risk that a stale-but-working system did not have.

## Verification

A healthy decision lifecycle has:

- an identifiable reason for the original decision
- known assumptions
- observable signals that would trigger reevaluation
- an explicit current rationale
