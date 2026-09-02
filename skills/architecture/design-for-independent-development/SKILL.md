---
name: design-for-independent-development
description: "Shapes component boundaries, interfaces, and ownership so separate teams can build, test, and ship their part in parallel without merge conflicts or cross-team blocking, and without simply mirroring the org chart. Use when merge conflicts cluster on the same files, PRs block waiting on another team's review, two owners must make synchronized edits to one module, a package split is being planned so ownership lines up with change boundaries, or a reorg prompts reshaping the architecture. Not for deciding whether the boundary is also a deployment boundary (see design-for-independent-deployment), which way dependencies cross it (see control-dependency-direction), what belongs on each side by cohesion (see group-components-by-cohesion), or team structure and staffing itself (see design-teams-and-work-for-scale)."
license: MIT
---

# Design for Independent Development

## Intent
Draw component and interface boundaries so that people working on different parts of the system can build, test, and change their part without waiting on or colliding with someone else's part — without simply copying the current org chart into the code structure.

## Procedure
1. Identify where developers are actually colliding: look at merge conflict frequency, PR review wait times, and which files show the most distinct authors touching overlapping lines in a short window.
2. For each collision hotspot, determine the cause: is it because the underlying code genuinely has one responsibility two teams both need to change (a real coupling problem, see `choose-boundaries-by-change-and-coupling`), or because the current boundary just happens to sit in the wrong place for how people work?
3. Define an explicit interface at the point where team ownership should change hands — a contract (API, event schema, function signature) that each side can implement or consume against without reading the other side's internals.
4. Check whether the proposed team-ownership boundary matches a boundary that also makes sense for change-reason and coupling. A boundary that's convenient for org purposes but incoherent for the code (splits a single business rule in half) will produce a bad interface no matter how it's drawn — don't let team topology override actual cohesion.
5. Give each side of the boundary its own test suite that can run and pass without needing the other side's implementation (a fake/stub/contract test standing in for the real dependency).
6. Where a reorg is driving the architecture discussion, keep the code boundary anchored to genuine change-reason/coupling patterns and let team assignment map onto that structure — not the reverse — unless there's a specific, named reason team structure should lead (see Exceptions).

## Decision rules
- Draw the ownership boundary at a point where the interface between the two sides is naturally narrow — if the "interface" needed between two teams' areas would have to expose most of each side's internals, the boundary is in the wrong place.
- Prefer stable, versioned interfaces at team boundaries over ad hoc cross-team edits to shared files — a team should be able to change its internals without asking another team's permission, as long as the interface contract is honored.
- Don't let current team structure single-handedly dictate the module boundary; use `choose-boundaries-by-change-and-coupling` to check the module boundary makes sense on its own merits, then align ownership to it.
- If two teams routinely need to change the same file for unrelated reasons, that's a boundary defect to fix, not a process problem to route around with more coordination meetings — split the file along their respective concerns.
- Prefer a contract test or published interface over "read the other team's source" as the coordination mechanism.
- Don't create an independently deployable unit purely for organizational reasons if it has no independent failure, scaling, or release need — the boundary must be technically real, not just political.

## Anti-patterns
- Copying the org chart into the module structure with no check on whether the resulting boundaries have a coherent, narrow interface between them (naive Conway's Law application).
- Leaving two teams sharing edit rights on the same core file indefinitely, treating repeated merge conflicts as a communication problem instead of a structural one.
- Defining a cross-team interface so wide (or so leaky) that consuming it still requires reading the other team's implementation, defeating the purpose of the boundary.
- Reorganizing the architecture every time the org chart changes, producing constant churn instead of a structure stable enough to absorb reorgs.
- Assigning ownership boundaries by seniority or convenience rather than by where the natural interface in the code actually is.
- Requiring cross-team review sign-off as a substitute for a real interface boundary.

## Exceptions and trade-offs
- In a very small team (everyone works on everything), formal ownership boundaries and interface contracts add overhead without benefit — apply this skill once the team is large enough that parallel, uncoordinated work is actually happening. Assuming every team needs an independently deployable service is itself a failure mode when coordination cost is already low.
- A platform or infrastructure team's boundary may legitimately be drawn to match their specialized skill set (e.g., "everything touching the deploy pipeline") even if that cuts across otherwise-cohesive business-logic boundaries — this is a deliberate exception, not a violation, as long as the interface is still kept narrow.
- During an active reorg, a temporary mismatch between team assignment and code boundary is normal; the fix is planned convergence, not an emergency architecture rewrite the same week.

## Verification
- Merge conflict and cross-team PR-wait metrics (if tracked) improve after the boundary/interface change, or there's a clear reason to expect they will.
- Each team can build and test its own area without checking out or running the other team's code, using a fake/stub for the interface.
- The interface contract at each team boundary is documented somewhere both sides can find it, not just known informally.
- Walk through the last few cross-team-coordinated changes and check whether the new boundary would have let them proceed independently.
- The chosen boundary also holds up under `choose-boundaries-by-change-and-coupling`'s change-reason test — it isn't purely an org-chart artifact.
