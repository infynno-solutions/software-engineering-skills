---
name: design-teams-and-work-for-scale
description: "Partitions problem spaces and decision-making so teams keep moving independently as headcount and system complexity grow. Use when defining or redrawing team boundaries, deciding which team owns a new service or shared library, writing a team charter, or diagnosing scale failure - one team bottlenecking unrelated work, a change requiring five codebases owned by five teams, an on-call rotation that cannot reason about what it is paged for. Not for day-to-day technical decisions within a team's remit (see make-and-revisit-technical-decisions), influence inside well-drawn boundaries (see lead-through-technical-influence), or shaping code boundaries for parallel work (see design-for-independent-development)."
license: MIT
---

# Design Teams and Work for Scale

## Intent
Partition problem spaces and decision-making so that as headcount or system complexity grows, teams can still move independently instead of coordinating on everything.

## Procedure
1. Identify the actual coupling in the system today — which changes currently require touching multiple teams' code or getting multiple teams' sign-off — before proposing a new boundary.
2. Draw team and service boundaries along seams where coupling is naturally low (a clear API, a bounded domain) rather than along org-chart convenience or headcount alone.
3. For each proposed boundary, assign explicit decision rights: who can approve a change to this component without asking elsewhere, and who must be consulted versus merely informed.
4. Check the boundary against Conway's Law in both directions: will the team structure you're proposing produce the system architecture you actually want, and does the current architecture already imply a different team shape than the one proposed?
5. Define the interface between teams (API contract, SLA, escalation path) as deliberately as the internal design of either team's system — an ambiguous interface reproduces the coordination cost you were trying to remove.
6. Size the boundary to what one team can actually own end-to-end (build, operate, be on call for) — a team that owns a slice of a system it can't operate independently hasn't actually gained autonomy.
7. Revisit the boundary when its cost shows up as evidence: repeated cross-team blocking, duplicated logic reinvented on both sides, or an on-call team paged for a system it doesn't control.

## Decision rules
- Draw the boundary where coupling is already lowest, not where the org chart is most convenient to redraw.
- A team should not own more surface area than it can operate and be on call for.
- Every shared interface needs an explicit owner and contract; "shared ownership" without a named decision-maker becomes no ownership.
- Prefer fewer, clearer decision rights over broad consensus requirements — a change that needs five approvals will move at the speed of the slowest approver.

## Anti-patterns
- Splitting teams along org-chart or reporting-line convenience while leaving the underlying code tightly coupled, which just moves the coordination cost into cross-team meetings.
- Creating a boundary with no clear owner for the seam between two teams, so integration bugs become nobody's job.
- Scaling a team by adding headcount to an already-overloaded single team instead of asking whether the work should split into independently ownable pieces.
- Copying another company's team topology wholesale without checking whether it matches this org's actual coupling and skill distribution.

## Exceptions and trade-offs
- For a small team or early-stage system, formal boundaries and decision rights are often premature overhead — a single team owning everything can be the right scale-appropriate choice.
- Some coupling is essential (a shared core domain model) and should stay owned by one team as a deliberate dependency, not be artificially split for autonomy's sake.
- Reorganizing has a real cost in lost context and momentum; the benefit of a cleaner boundary must outweigh the disruption of redrawing it, which is not automatic.

## Verification
- Trace a recent real change and confirm it would now require sign-off from fewer teams under the proposed boundary, not more.
- Confirm every proposed boundary has a named owner for both sides and for the interface between them.
- Check the boundary against actual system coupling (imports, API calls, shared data) rather than only against the org chart.
- Ask whether each team, once split, could operate its piece independently — build, deploy, and be on call for it — without routine cross-team dependency.
