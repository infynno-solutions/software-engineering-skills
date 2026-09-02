---
name: create-healthy-review-and-feedback-culture
description: "Makes code review a place where feedback improves the code and grows the author instead of feeling arbitrary, personal, or defensive. Use when writing review comments on someone else's change, responding to comments on your own, defining a team's review checklist or PR template, or when a thread degrades - comments getting terser, a contributor going quiet, the same disagreement looping. Not for what technical decision to make (see make-and-revisit-technical-decisions), teaching a broader concept outside the review (see mentor-and-teach-through-engineering-work), or the technical substance of comments on one PR (see conduct-effective-code-reviews)."
license: MIT
---

# Create Healthy Review and Feedback Culture

## Intent
Make code review a place where feedback improves the code and grows the author, instead of a gate that feels arbitrary, personal, or purely defensive.

## Procedure
1. Before commenting, decide whether the issue is a blocking correctness/design problem, a strong preference, or a nitpick — and label it as such so the author can triage effort correctly.
2. Write comments about the code's behavior or structure, not the author's competence: "this drops the error on retry" rather than "you forgot error handling."
3. Give the reasoning, not just the verdict — say why a pattern is a problem here, so the comment teaches something reusable rather than issuing a fiat.
4. When proposing an alternative, be concrete enough to act on (a snippet, a named pattern, a link) rather than "this could be cleaner."
5. Distinguish "this must change to merge" from "consider this, your call" explicitly, so authors aren't left guessing which comments are gates.
6. As the author, respond to the substance of each comment (accept, push back with reasoning, or ask for clarification) rather than silently resolving or silently ignoring.
7. When a thread disagrees past two exchanges without converging, move it to a synchronous conversation and record the resolution back in the thread, rather than letting it become a text-based standoff.
8. Periodically check whether review turnaround time and comment tone are trending toward rubber-stamping or toward gatekeeping, and recalibrate the team's norms if so.

## Decision rules
- If a comment could be read as being about the person rather than the code, rewrite it before posting.
- Reserve "must fix" framing for correctness, security, and maintainability issues; mark style and preference as optional.
- A comment with no actionable next step ("this feels off") is not yet ready to post — find the specific concern first.
- Praise specific good decisions in the diff, not just flag problems — a review that only ever finds fault reads as adversarial regardless of intent.

## Anti-patterns
- Rewriting the author's code in the comment as the only acceptable version, rather than explaining the concern and leaving room for their solution.
- Blocking a PR on personal style preference with no stated technical reason, dressed up as a "must fix."
- Approving without reading, which erodes both the safety net and the credibility of future approvals.
- Letting seniority substitute for justification — "just do it this way" from a senior reviewer with no reasoning, which teaches deference instead of judgment.
- Going silent on a thread instead of explicitly resolving disagreement, leaving the author unsure whether they're blocked.

## Exceptions and trade-offs
- Under incident or deadline pressure, it's reasonable to compress review to correctness and safety only, explicitly deferring style and design commentary to a follow-up.
- For a trusted, high-context pair (e.g., two senior engineers who've worked together for years), terser comments can carry the same meaning that would need spelling out for a newer teammate — calibrate verbosity to the relationship, not just the rule.
- A junior author may need more explicit "why," while a senior author reviewing a junior's work may need to consciously add more of it than they would for a peer.

## Verification
- Reread your own comments before posting and confirm each names the code issue, not the person.
- Confirm blocking comments are distinguishable from optional ones, either by label or by clear phrasing.
- Check that any comment proposing a change gives enough detail (why, and ideally how) that the author isn't left guessing.
- For a thread that stalled, confirm it ended in an explicit resolution recorded in writing, not silence.
