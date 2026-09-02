---
name: build-knowledge-sharing-systems
description: "Turns tribal knowledge into durable, discoverable artifacts so the team's understanding does not depend on one person being reachable. Use when the same question gets answered in chat three times, a new hire must interrupt someone to learn how the deploy pipeline works, a system is understood only by the engineer who built it, or a doc has rotted until nobody trusts it. Not for a one-off explanation with no reuse value, growing a specific person's skill (see mentor-and-teach-through-engineering-work), review feedback norms (see create-healthy-review-and-feedback-culture), or writing one decision record or runbook (see document-decisions-and-system-context)."
license: MIT
---

# Build Knowledge-Sharing Systems

## Intent
Turn tribal knowledge into durable, discoverable artifacts so the team's collective understanding does not depend on any one person being reachable.

## Procedure
1. Find the knowledge bottleneck concretely: which question, decision, or procedure currently requires asking a specific person, and how often does that happen?
2. Identify why no durable source exists yet — never written down, written but stale, written but unfindable, or scattered across five places that disagree.
3. Choose the artifact type that matches how the knowledge will be consumed: a runbook for "what do I do when X happens," an architecture doc for "why does this system look this way," a decision log entry for "why did we choose this over the alternative," a README for "how do I get started."
4. Write it next to what it describes (in-repo docs, code comments for non-obvious invariants) rather than in a wiki that drifts out of sync, unless the team already has a working single source of truth elsewhere.
5. Assign an owner and a trigger for revisiting it — e.g., "review this doc whenever the deploy process changes" — so it does not silently rot.
6. Make it discoverable: link it from the README, the onboarding checklist, or the code path it explains, so people find it by navigating rather than only by search.
7. Retire or merge duplicate and contradicting sources once the canonical one exists; a second stale copy is worse than none.

## Decision rules
- Put the knowledge as close as possible to where it will be needed at the moment of need (code comment beats design doc beats wiki page, for knowledge tied to a specific line of logic).
- Prefer one canonical source per topic over several partial ones; if duplication is unavoidable, make one explicitly authoritative and link the rest to it.
- Write for the reader who has none of your context, not for your future self who already remembers.
- If a question has been asked more than twice, that is the threshold for writing it down instead of answering it again live.

## Anti-patterns
- Writing exhaustive documentation for a system that changes weekly, guaranteeing it goes stale faster than anyone can maintain it.
- Treating a Slack thread or a meeting recording as the canonical source — it is unsearchable and unmaintained the moment it ends.
- Building a knowledge base with no owner and no update trigger, so it fossilizes and becomes actively misleading.
- Documenting the "happy path" only and leaving failure modes and edge cases as tribal knowledge, which defeats the purpose for on-call and incident use.

## Exceptions and trade-offs
- For a system in active flux (prototype, pre-launch), heavy documentation investment is often wasted; favor lightweight, easily-updated notes over polished docs until the design stabilizes.
- Highly sensitive operational knowledge (credentials, security procedures) may need controlled access rather than open discoverability — apply the same durability principle within a restricted channel.
- A small team with high bus-factor tolerance may reasonably defer investment here in favor of shipping speed, provided that trade-off is a conscious choice, not a default.

## Verification
- Pick a real recent question that required asking a person; confirm someone with no prior context could now answer it from the artifact alone.
- Check that the artifact is linked from at least one place a newcomer would naturally land (README, onboarding doc, or the relevant code).
- Confirm there is a named owner or a clear trigger condition for revisiting the content, not just a creation date.
- Search for other sources on the same topic and confirm they either agree, are removed, or explicitly defer to the canonical one.
