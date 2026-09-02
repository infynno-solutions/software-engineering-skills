---
name: remove-team-roadblocks
description: "Identifies the structural constraints actually preventing engineers from making progress and removes them, rather than asking people to push harder. Use when a team repeatedly cites the same blocker in standups or retros - flaky CI, a slow deploy pipeline, a review queue sitting for days; when routine work needs an approval chain disproportionate to its risk; when a shared system has no owner so nobody will touch it; or when someone is blocked on access or another team with no escalation path. Not for a one-off task that is hard for legitimate reasons, a single person's skill gap (see mentor-and-teach-through-engineering-work), or re-justifying an existing process rule (see revisit-process-rules-using-evidence)."
license: MIT
---

# Remove Team Roadblocks

## Intent
Identify the specific constraints actually preventing engineers from making progress, and remove or reduce them rather than asking people to push harder against them.

## Procedure
1. Collect the actual friction points from the people experiencing them (standup complaints, retro items, support requests) rather than guessing at what's slowing the team down.
2. For each candidate roadblock, quantify it if possible — how often it recurs, how much time it costs, how many people it affects — so effort goes to the highest-leverage fix first.
3. Distinguish a roadblock from a hard-but-necessary constraint: a slow security review that catches real risk is not the same problem as a slow approval that exists only out of process inertia.
4. Trace each roadblock to its root cause rather than patching the symptom — a flaky test suite people route around with reruns is a signal to fix the flakiness, not just add more retries.
5. Fix what's within your authority directly; for what isn't, identify who owns the constraint and make a specific, scoped ask rather than a general complaint.
6. When removing a process gate, replace it with the minimum safeguard that still covers the real risk it existed for, rather than removing the safeguard along with the friction.
7. Close the loop with the people who reported the blocker — tell them what changed, even if the answer is "not yet, here's why."
8. Watch for the roadblock's return; a fixed flaky test can regress, a shortened approval chain can silently regrow.

## Decision rules
- Prioritize roadblocks by frequency times cost times number of people affected, not by whichever one is loudest this week.
- Never remove a safeguard without understanding what risk it was covering; replace it with a smaller safeguard, don't just delete it.
- If a blocker's root cause is outside your control, escalate it explicitly to its owner rather than absorbing it as your team's permanent tax.
- A roadblock reported more than once by more than one person outranks a roadblock reported once by one person, all else equal.

## Anti-patterns
- Treating chronic friction as a motivation problem ("just push through it") instead of investigating whether it's a structural constraint worth fixing.
- Fixing the visible symptom (adding a retry, a workaround script) while leaving the underlying cause (a flaky dependency, an unowned service) untouched, so the cost keeps recurring.
- Removing a review or approval gate entirely to speed things up, without replacing the risk coverage it provided.
- Collecting roadblock complaints in retros repeatedly with no follow-through, which teaches the team that reporting friction is pointless.
- Solving a roadblock for your own team while quietly pushing the same friction onto another team via the interface between you.

## Exceptions and trade-offs
- Some friction is inherent to the risk it's guarding against (a genuinely careful release process for a regulated system) and removing it would trade real safety for speed — the goal is the smallest sufficient safeguard, not zero friction.
- A roadblock affecting one person occasionally may not warrant systemic investment; a direct workaround for that individual can be the proportionate response.
- Fixing root causes (rewriting flaky infra, renegotiating a process with another team) often takes longer than the team can wait; a temporary workaround plus a tracked follow-up is a legitimate interim state, not a failure to solve it properly.

## Verification
- Confirm the roadblock's frequency or cost was measured or estimated before deciding how much effort to spend removing it.
- After a fix, check with the people who reported it whether the friction actually decreased, rather than assuming the fix worked.
- For any safeguard removed or shortened, confirm the risk it covered is still addressed some other way.
- Revisit previously "fixed" roadblocks periodically to confirm they haven't silently regrown.
