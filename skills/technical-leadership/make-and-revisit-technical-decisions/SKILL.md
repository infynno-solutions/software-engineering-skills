---
name: make-and-revisit-technical-decisions
description: "Moves a decision forward at a speed matched to how hard it would be to undo, and builds in a way to notice when it should be revisited. Use when a team is stuck debating an architectural choice without converging, when deciding under incomplete information where further delay has its own cost, when writing an ADR, or when a months-old decision rested on an assumption current evidence contradicts. Not for explaining the reasoning to others once made (see communicate-trade-offs-and-context), getting buy-in without authority (see lead-through-technical-influence), or the individual reasoning technique itself (see evaluate-engineering-trade-offs, revisit-decisions-as-context-changes)."
license: MIT
---

# Make and Revisit Technical Decisions

## Intent
Move a decision forward at a speed matched to how hard it would be to undo, and build in a way to notice when it should be revisited instead of letting it calcify.

## Procedure
1. Classify the decision by reversibility before debating its merits: is this a one-way door (expensive or impossible to undo — a public API shape, a data model, a vendor lock-in) or a two-way door (cheap to reverse — an internal library choice, a config default)?
2. For two-way doors, decide quickly with the best available evidence and move on; further analysis has a cost that usually exceeds the risk of being wrong.
3. For one-way doors, gather the evidence that would actually change the answer, not evidence in general — identify what you don't know that matters before spending time on what's merely uncertain.
4. Name the assumptions the decision rests on explicitly, especially the ones likely to stop being true (scale, team size, a vendor's pricing, a regulatory environment).
5. Record the decision, its reasoning, the alternatives considered, and its assumptions somewhere durable (an ADR or equivalent) at the time it's made, not reconstructed later from memory.
6. Set an explicit trigger for revisiting it — a condition ("if traffic exceeds X"), not just a calendar date — so the decision gets reopened because reality changed, not because everyone forgot it existed.
7. When revisiting, evaluate against the original assumptions and current evidence, not against nostalgia for the old choice or sunk cost in what's already built on it.
8. When a decision deadlocks a team without converging, make the call explicitly (name who decides) rather than letting indecision become the default by attrition.

## Decision rules
- Match analysis effort to reversibility: shallow and fast for two-way doors, deep and evidence-driven for one-way doors.
- A decision with no recorded assumption and no revisit trigger is not finished, even if it's shipped.
- When new evidence contradicts a stated assumption, that alone is grounds to reopen the decision — no additional justification needed.
- If a debate has repeated the same arguments without new evidence for two rounds, that's the signal to decide and move rather than continue deliberating.

## Anti-patterns
- Treating every decision as a one-way door and demanding exhaustive analysis for reversible, low-stakes choices, which stalls the team on things that don't warrant it.
- Making an irreversible decision under artificial urgency when the actual deadline pressure was negotiable.
- Never writing down the reasoning, so revisiting the decision later means re-deriving from scratch or defending it purely from memory.
- Revisiting a decision endlessly without new evidence, which is indecision wearing the costume of diligence.
- Treating "we already built on top of it" as proof the original decision was correct, rather than as sunk cost that shouldn't dictate the next choice.

## Exceptions and trade-offs
- Under genuine incident time pressure, decide with the best guess available and explicitly flag it for post-incident review rather than pausing to gather full evidence.
- A decision made by a clear technical authority (an owning team's lead, on a matter within their remit) doesn't need full team consensus — legitimate authority is itself a valid decision mechanism.
- Some decisions are worth deliberately delaying (a "not yet" is a real decision) when the cost of choosing wrong now exceeds the cost of the delay itself — distinguish that from indecision by naming what you're waiting to learn.

## Verification
- For the decision at hand, confirm you can state in one sentence whether it's a one-way or two-way door and that the effort spent matches that classification.
- Confirm the reasoning, alternatives, and key assumptions are written down somewhere durable, not only known to the people in the room.
- Check that a concrete revisit trigger exists (a condition, not just "someday") for any decision resting on an assumption that could change.
- If reopening a past decision, confirm the trigger condition (not just discomfort with the outcome) is what's driving the reopening.
