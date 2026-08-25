---
name: evaluate-engineering-trade-offs
description: "Compare viable engineering alternatives explicitly instead of treating a preferred technique as universally correct. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Evaluate Engineering Trade-offs

## Intent

Compare viable engineering alternatives explicitly instead of treating a preferred technique as universally correct.

## Apply when

Use this skill when choices affect:

- performance versus simplicity
- delivery speed versus long-term maintainability
- isolation versus realism in tests
- abstraction versus directness
- consistency versus availability
- build speed versus infrastructure cost
- local complexity versus system-wide complexity
- short-term versus long-term engineering cost

## Procedure

1. List viable alternatives.
2. Identify the decision criteria.
3. Estimate measurable costs where possible.
4. Identify important hard-to-measure costs.
5. Include engineering time, operational cost, failure risk, opportunity cost, and future change cost where relevant.
6. State which option wins under the current context and why.
7. Record important deferred costs or assumptions.

## Decision rules

- Do not hide a trade-off behind “best practice.”
- Do not optimize only for runtime performance or only for developer convenience.
- If evidence is weak, state uncertainty explicitly.
- A decision can be reasonable even when it is not globally optimal, provided its context and deferred costs are understood.

## Anti-patterns

- “This is the standard approach” without context.
- Choosing the most feature-rich or technically sophisticated option.
- Ignoring engineering time because it is not an infrastructure bill.
- Treating measurable costs as the only real costs.

## Verification

A design decision is sufficiently reasoned when another engineer can see:

- the alternatives considered
- the criteria used
- the important evidence
- the principal trade-offs
- the decision and its assumptions


## Related skills

- ENG-04 Manage Essential vs Accidental Complexity
- ENG-06 Make Evidence-Based Engineering Decisions
- ENG-07 Defer Decisions When Uncertainty Is High
- ENG-08 Prefer the Simplest Adequate Solution
