---
name: evolve-architecture-incrementally
description: "Moves architecture through small, shippable steps instead of a big-bang rewrite. Use when a boundary is crossed on every third feature, several teams must all touch one module to ship independent work, or a strangler-fig migration off a legacy system or datastore is planned. Not for restructuring a single function or class (see extract-and-recompose-responsibilities), deciding whether a pattern is warranted inside one module (see refactor-toward-patterns-when-justified), or deciding where the target boundary should sit (see identify-and-place-architectural-boundaries)."
license: MIT
---

# Evolve Architecture Incrementally

## Intent
Improve architectural structure through bounded, incremental changes informed by real experience rather than waiting for a perfect redesign.

## Procedure
1. Identify the recurring pain point in the current architecture concretely — e.g., a specific boundary crossed on every third feature — not a checklist of "best practices."
2. Define the target shape, but commit only to the next boundary-clarifying step, not the full migration plan.
3. Introduce a seam (interface, façade, event boundary) alongside the existing structure — strangler pattern — without removing the old path yet.
4. Migrate call sites or traffic incrementally behind the seam, keeping both old and new paths releasable at every step.
5. Once all consumers use the new path, remove the old path and the seam scaffolding.
6. Re-evaluate the target shape after each increment against what was actually learned; an architecture that "improves" through blind adherence to an upfront diagram is not incremental evolution.

## Decision rules
- Let a currently-felt cost (duplicated logic across services, a change that requires touching many unrelated modules, an incident traceable to a boundary) drive which boundary moves next, not a diagram.
- Keep every intermediate architecture state deployable and rollback-able; avoid leaving the system half-migrated across a release boundary.
- Prefer a parallel-run or dual-write period over a hard cutover when the new path's risk is unproven.
- Stop when the pain that motivated the change is resolved, even if the target architecture is not "finished."

## Anti-patterns
- Freezing feature work for a multi-month architectural rewrite instead of evolving the boundary alongside delivered features.
- Introducing a new architectural layer (event bus, service boundary, generic plugin system) speculatively, before a second real consumer exists.
- Big-bang cutovers that switch all traffic or callers to a new boundary in one release with no fallback.
- Letting an incremental migration stall halfway, leaving two competing implementations live indefinitely with no plan to finish.

## Exceptions and trade-offs
- A genuinely broken foundation (a datastore that cannot scale, a security model that must change) may justify a bounded, time-boxed rewrite of a subsystem rather than incremental strangling — but scope and exit criteria must be explicit up front.
- Regulatory or contractual deadlines may force a faster cutover with less parallel-run time than ideal.

## Verification
- After each increment, confirm the system is fully deployable and both old and new paths, if coexisting, are exercised by tests or real traffic.
- Confirm the specific pain point that motivated the change is measurably reduced — fewer cross-module PRs, faster change lead time, or similar.
- Confirm no consumer is left silently depending on scaffolding intended to be temporary.
