---
name: revisit-process-rules-using-evidence
description: "Treats engineering rules as hypotheses to be re-justified as technologies, costs, and observed outcomes change. Use when a rule causes repeated friction and nobody can explain why it exists, when proposing a new mandatory process rule, or when a retrospective surfaces a process pain point. Not for deciding whether a specific check should be automated as a gate right now (see automate-quality-gates-and-delivery), or for revisiting a technical or architectural decision (see revisit-decisions-as-context-changes)."
license: MIT
---

# Revisit Process Rules Using Evidence

## Intent
Treat engineering rules as hypotheses that should be revisited when technologies, costs, and observed outcomes change.

## Procedure
1. When a rule causes friction, ask when and why it was introduced; find the original incident, decision, or context if possible.
2. Gather evidence on the rule's actual effect: how often has it caught a real problem vs. how often has it been overridden, waived, or worked around.
3. Estimate the rule's ongoing cost — time, review latency, cognitive load — against that evidence of benefit.
4. If the rule's originating conditions have changed (new tooling now catches the same issue automatically, team size changed, the risky pattern stopped occurring), propose relaxing or removing it.
5. Change process rules the way you'd change code: propose, get input from people it affects, roll out, and monitor the effect.
6. Record the outcome — kept, relaxed, removed — and why, so the next person doesn't have to redo the investigation.

## Decision rules
- A rule with no one able to state its rationale is a candidate for review, not automatically for removal — investigate before changing.
- Prefer replacing a manual rule with automated enforcement (or vice versa) over deleting it outright, when the underlying risk it addressed is still real.
- Treat "we've always done it this way" as a hypothesis to check against current evidence, not as sufficient justification on its own.
- Remove or change a rule because evidence shows the cost now exceeds the benefit, not solely because it's inconvenient.

## Anti-patterns
- Keeping a rule indefinitely purely because changing it feels risky, without ever checking whether its original justification still holds.
- Silently ignoring or working around an inconvenient rule instead of formally revisiting it, so it stays on the books unenforced.
- Removing a rule reactively right after one instance of friction, without checking what it was preventing.
- Treating every process rule as permanent policy rather than a decision with a context that can expire.

## Exceptions and trade-offs
- Rules tied to external compliance or regulatory requirements aren't unilaterally revisable by engineering judgment alone, even with good internal evidence.
- Some rules are cheap insurance against rare catastrophic failure; low observed trigger frequency doesn't automatically justify removal if the tail risk is severe.
- Revisiting every rule constantly has its own overhead; prioritize the rules with the highest friction or the least-remembered rationale.

## Verification
- Each active process rule can be traced to a stated rationale, even if written down after the fact during this review.
- Changed or removed rules have a recorded decision and the evidence behind it.
- Outcomes (defect rate, incident rate, review latency) are monitored after a rule change, watching for regression.
