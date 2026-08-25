---
name: revisit-decisions-as-context-changes
description: "Treat engineering decisions as contextual rather than permanent truths. Re-evaluate them when requirements, workload, team structure, operational constraints, evidence, or system age materially changes. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Revisit Decisions as Context Changes

## Intent

Treat engineering decisions as contextual rather than permanent truths. Re-evaluate them when requirements, workload, team structure, operational constraints, evidence, or system age materially changes.

## Apply when

Review existing decisions when:

- scale changes substantially
- a previous assumption becomes false
- a new failure mode appears
- a system becomes difficult to maintain
- new evidence contradicts the original reasoning
- a previously deferred cost becomes material

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

## Verification

A healthy decision lifecycle has:

- an identifiable reason for the original decision
- known assumptions
- observable signals that would trigger reevaluation
- an explicit current rationale


## Related skills

- ENG-05 Evaluate Engineering Trade-offs
- ENG-06 Make Evidence-Based Engineering Decisions
- ENG-07 Defer Decisions When Uncertainty Is High
- ENG-09 Iterate Design Before Committing
