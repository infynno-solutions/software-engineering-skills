---
name: mentor-and-teach-through-engineering-work
description: "Turns everyday engineering work into opportunities that leave a specific person more capable afterward, not just the code more correct. Use when reviewing code from someone earlier in their growth on this codebase, pairing on something unfamiliar to them, walking through the reasoning behind a design choice so they can make a similar call independently, or noticing a teammate repeat the same category of mistake across PRs. Not for building a reusable artifact aimed at anyone who encounters it later (see build-knowledge-sharing-systems), or general review etiquette that applies regardless of experience level (see create-healthy-review-and-feedback-culture)."
license: MIT
---

# Mentor and Teach Through Engineering Work

## Intent
Turn the everyday work of building software into opportunities that leave a specific person more capable afterward, not just the code more correct.

## Procedure
1. Identify what this specific person doesn't yet have — a concept, a piece of codebase context, a debugging technique — rather than assuming the gap is generic "junior-ness."
2. Choose the teaching moment to match the stakes: pair live on something consequential or unfamiliar; leave a review comment with reasoning for something lower-stakes they can absorb asynchronously.
3. When reviewing, explain the reasoning behind a requested change, not just the change itself, so the same judgment transfers to their next PR without your review.
4. Let them do the work rather than doing it for them — in pairing, resist taking the keyboard to "just fix it faster"; the point is the rep, not the shortest path to a merged PR.
5. Calibrate the size of the stretch: assign or review work that's slightly past their current comfort zone, not so far past it that they can't productively engage with feedback.
6. Use worked examples from the real codebase over abstract advice — show the actual pattern elsewhere in the system rather than describing a principle in the void.
7. After a mistake repeats, name the pattern explicitly ("this is the third time we've hit an off-by-one here — let's talk about the general case") rather than only fixing each instance individually.
8. Check back later whether the concept transferred — did their next independent PR show the pattern, or did you just supply the fix again.

## Decision rules
- Prefer explaining the reasoning over supplying the answer whenever the person has the time and standing to absorb it; supply the answer directly only under real time pressure.
- Match teaching intensity to stakes and unfamiliarity: high-stakes and unfamiliar work gets live pairing; low-stakes and familiar work gets a written note.
- If the same mistake has recurred more than once, address the underlying concept explicitly rather than continuing to fix instances silently.
- Let the mentee drive the actual typing/decisions whenever the cost of a slower pace is affordable; take over only when the cost of not shipping now outweighs the teaching value.

## Anti-patterns
- Rewriting someone's PR yourself and merging it rather than reviewing it with them, which fixes the code but teaches nothing.
- Giving only the correct answer with no reasoning ("just do it this way"), which produces compliance on this instance without transferable understanding.
- Assigning stretch work with no support and calling it mentorship — a growth opportunity with no feedback loop is just being thrown in the deep end.
- Reserving all teaching moments for formal 1:1s instead of the actual code and design work where the context is freshest and most concrete.
- Treating a repeated mistake as a discipline problem before checking whether it's actually a knowledge gap that hasn't been named yet.

## Exceptions and trade-offs
- Under genuine deadline or incident pressure, it's reasonable to fix it yourself now and teach the concept afterward rather than slow down a live situation to preserve a teaching moment.
- Some skills are best built through independent struggle with light guardrails rather than close pairing — judge by the person's stated preference and the cost of them getting stuck, not a fixed formula.
- Not every interaction needs to be a teaching moment; treating every code review as a lesson can read as condescending to a peer who doesn't need it on this particular change.

## Verification
- After a mentoring interaction, check whether the person can articulate the reasoning back in their own words, not just the fix that was applied.
- Look at their next independent piece of similar work and confirm the pattern actually transferred rather than the fix being supplied again.
- Confirm review comments aimed at teaching included the "why," not only the "what."
- If a stretch assignment was made, confirm support was actually available when they got stuck, not just implied.
