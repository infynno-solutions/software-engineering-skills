---
name: evaluate-engineering-trade-offs
description: "Compares two or more viable alternatives explicitly instead of treating a preferred technique as universally correct. Use when a library switch, sync versus async, or SQL versus NoSQL choice must be justified; when a decision pits performance against simplicity or consistency against availability; when a reviewer asks why not just use X; or when a proposal cites best practice as its entire justification. Not when only one option has been identified (see iterate-design-before-committing first), when the question is how much complexity one design should carry (see manage-essential-vs-accidental-complexity), or whether to decide now at all (see defer-decisions-when-uncertainty-is-high)."
license: MIT
---

# Evaluate Engineering Trade-offs

## Intent

Compare viable engineering alternatives explicitly instead of treating a preferred technique as universally correct.

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

## Exceptions and trade-offs

- A full trade-off table is overkill for a reversible, low-stakes choice — reserve the explicit comparison for decisions with real cost or blast radius.
- When alternatives are close, documented judgment calls are acceptable; don't manufacture false precision to make one option look decisively better.
- Two engineers can weigh the same trade-offs differently and both be reasonable — the goal is a visible comparison, not a single "correct" answer.

## Verification

A design decision is sufficiently reasoned when another engineer can see:

- the alternatives considered
- the criteria used
- the important evidence
- the principal trade-offs
- the decision and its assumptions
