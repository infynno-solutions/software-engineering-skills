---
name: communicate-trade-offs-and-context
description: "Makes the reasoning behind a technical choice legible to people who did not live through making it, so they can evaluate, build on, or safely revisit it. Use for a non-obvious architecture choice, a deliberate simplification trading correctness edge cases for delivery speed, a design doc proposing one of several viable approaches, a PR description a reviewer could reasonably question, or pushing back on a request. Not for routine changes where the code speaks for itself, the decision process itself (see make-and-revisit-technical-decisions), or winning adoption without authority (see lead-through-technical-influence)."
license: MIT
---

# Communicate Trade-offs and Context

## Intent
Make the reasoning behind a technical choice legible to people who did not live through the process of making it, so they can evaluate it, build on it, or safely revisit it later.

## Procedure
1. Name the goal the choice serves in one sentence — what outcome mattered enough to shape this decision.
2. List the real constraints in play: deadline, existing system shape, team size, an API you don't control, a performance floor. Distinguish hard constraints from assumed ones.
3. Name at least one alternative that was seriously considered and say concretely why it was not chosen — not "it was worse" but the specific cost or risk that ruled it out.
4. State what was given up by the chosen path (a cost, a limitation, a future migration now required) as plainly as what was gained.
5. Write the explanation for the reader's decision, not your defense: a reviewer or future maintainer needs enough to agree, disagree with grounds, or safely revisit — not a narrative of your effort.
6. Put the trade-off summary where the reader will actually encounter it — PR description, design doc summary, or a comment at the point of surprising code — not buried in a chat thread that will not survive.
7. When context is time-sensitive (this constraint is true today but may not be in six months), say so explicitly so it isn't mistaken for a permanent judgment.

## Decision rules
- If a reviewer or reader could reasonably ask "why not X instead," the trade-off write-up should already answer it before they ask.
- State costs and risks with the same weight as benefits; an explanation that only lists upside is advocacy, not context.
- Prefer concrete numbers or specifics ("adds ~40ms to p99," "couples this service to that schema") over vague hedges ("this might be slower").
- Match the depth of explanation to the size of the decision: a one-line rationale for a small choice, a structured section for an architectural one.

## Anti-patterns
- Presenting a decision as though it were the only option, hiding that alternatives existed and were rejected for specific reasons.
- Writing the trade-offs only in your head or in a since-deleted chat message, leaving the committed code as the sole record.
- Over-justifying trivial choices with lengthy trade-off essays, which trains reviewers to skim past the write-ups that actually matter.
- Framing a trade-off retrospectively as obviously correct once it worked out, erasing the genuine uncertainty that existed at decision time.

## Exceptions and trade-offs
- For fully reversible, low-stakes choices, a one-line rationale is proportionate; reserve full trade-off write-ups for decisions that are costly to unwind.
- Under real time pressure (incident response), a terse "why" now with a fuller write-up promised in the postmortem is better than delaying the fix to write it up first.
- When the audience already shares full context (a pair programming session), verbal trade-off discussion can substitute for written record, provided the outcome still gets captured somewhere durable if it will matter later.

## Verification
- Reread the write-up and confirm a reader with no background could state the goal, the main alternative, and the cost of the chosen path.
- Check that at least one real trade-off or limitation is named, not just benefits.
- Confirm the explanation lives in a place future readers will actually find (PR, doc, commit message) rather than only in live conversation.
- Ask whether someone who disagreed with the choice would say the write-up fairly represents the alternative they preferred.
