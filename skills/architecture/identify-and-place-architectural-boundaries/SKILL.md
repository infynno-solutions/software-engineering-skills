---
name: identify-and-place-architectural-boundaries
description: "Decides whether a seam deserves a real boundary - interface, port, inverted dependency - or should stay a direct call, weighing cost against the volatility it protects. Use before adding a port, gateway, provider, or plugin interface, or when changes keep rippling because no boundary exists. Not for which way dependencies then point (see control-dependency-direction), what goes on each side (see choose-boundaries-by-change-and-coupling), or removing an abstraction that stopped paying (see manage-abstraction-debt)."
license: MIT
---

# Identify and Place Architectural Boundaries

## Intent
Put a real architectural boundary — an interface plus inverted dependency, isolated data models, a controlled crossing point — exactly where independent change, ownership, testability, or deployment genuinely justify the cost, and use a plain direct call everywhere else.

## Procedure
1. Name the specific seam under discussion: two components, a component and an external system, or a component and a UI/delivery mechanism.
2. Ask what would have to change on one side for the other side to be unaffected, if a full boundary existed here: a different database vendor, a different UI, a different external API provider, a different team owning one side, a need to test one side without the other.
3. Check whether that variation is realistic and likely in this system's actual lifetime — not hypothetical "someday we might swap X." Look for existing evidence: has this dependency actually changed before, is there a second implementation already needed, is there a concrete near-term plan to swap it.
4. If the variation is real, place a boundary: define an interface in the more-stable side's vocabulary, invert the dependency so the volatile side implements it, and keep data crossing the boundary in a form that doesn't leak the volatile side's internal model.
5. If the variation is not real or not likely, do not add a boundary — call the collaborator directly. Note this explicitly as a decision (not an oversight) so a future reviewer doesn't assume it was missed.
6. For an existing un-abstracted seam that is now causing pain (frequent ripple effects, blocked tests, inability to swap a vendor), retrofit the boundary using the same test: confirm the pain is real and current, not anticipated, before investing in the retrofit.
7. Verify the new boundary is minimal — expose only what the consuming side actually needs, not the full surface of the underlying implementation.

## Decision rules
- Place a boundary where at least one of these is concretely true: the two sides need to be independently testable, independently deployable, independently owned by different teams, or one side is genuinely expected to have multiple/changing implementations.
- Don't place a boundary just because "good architecture has boundaries" — an abstraction with a single, never-varying implementation and no independent-testing need is pure overhead.
- When retrofitting a missing boundary, let the actual pain (a real incident, a real blocked test, a real vendor swap) drive the decision, not a general sense that "this should have been abstracted."
- A boundary's interface should be shaped by what the consumer needs, not by what the provider happens to expose — narrow, purpose-built interfaces age better than one mirroring the provider's full API.
- The number of boundaries in a system should track its actual volatility and team/deployment structure — a small, single-team, single-deployment system needs far fewer boundaries than a large multi-team, multi-service one.

## Anti-patterns
- Wrapping every collaborator behind an interface "for good practice" regardless of whether it ever has more than one implementation, adding a permanent layer of indirection with no corresponding benefit.
- Leaving a genuinely volatile dependency (a specific vendor's SDK, a specific database's query dialect) called directly from deep inside business logic, so every change to that dependency ripples through many files.
- Introducing a boundary only after being burned once, but drawing it in the wrong place because the retrofit was done under incident pressure without re-checking where the actual volatility lives.
- Building a boundary whose interface exactly mirrors the underlying implementation's full API surface, so swapping implementations still requires wide changes on the consumer side.
- Confusing "this is a different technical layer" with "this needs a boundary" — layering alone doesn't justify indirection if nothing on either side varies independently.

## Exceptions and trade-offs
- Boundaries around anything crossing an organizational trust line (external vendor, another team's service, a public API) are usually worth their cost even with only one current implementation, because control over the other side is limited regardless of technical volatility.
- In an early prototype, deliberately skip boundaries even where they'd eventually be justified, and note where they'll likely need to be added once the design stabilizes — see `avoid-premature-distribution` for the parallel reasoning at the deployment-topology level.
- A boundary that turns out to be unnecessary is usually cheap to remove (delete the interface, call directly); a missing boundary that turns out to be necessary is usually expensive to retrofit under pressure — when genuinely uncertain and the cost of the abstraction is low, that asymmetry can tip the decision toward adding it.

## Verification
- For each boundary in the design under review, there's a stated concrete reason (testability, deployability, ownership, real multiple-implementation need) — not just "it's cleaner."
- For each seam without a boundary, check that no real, current volatility is leaking across it uncontrolled.
- Each existing boundary's interface is shaped around what the consumer actually needs, not the full provider API.
- Recently added boundaries can be pointed to an actual event (a swap, a test need, a team split) that justified them, if asked.
