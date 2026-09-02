---
name: choose-boundaries-by-change-and-coupling
description: "Decides which classes and files belong inside one component versus apart, by rate of change and coupling rather than layer or file type. Use when defining a package structure, placing a new top-level directory, or merging components that always change together. Not for whether the boundary is a network or deployment boundary (see avoid-premature-distribution), whether a seam needs an interface (see identify-and-place-architectural-boundaries), or splitting one class (see extract-and-recompose-responsibilities)."
license: MIT
---

# Choose Boundaries by Change and Coupling

## Intent
Group code into components based on who changes it, why, and how tightly it is coupled — so that a single business reason to change touches one component, not several, and unrelated reasons to change don't get bundled into one.

## Procedure
1. For the code in question, ask: what stakeholder, business rule, or reason-to-change does each piece serve? Group pieces that change together for the same business reason (the Common Closure Principle) — a change request should map to edits in one component, not a shotgun spread across many.
2. Check reuse: do external consumers depend on some classes in the component but not others? If a component is reused as a whole but only part of it is ever actually reused, split out the unused part (the Common Reuse Principle) — consumers should not need to redeploy or retest because of changes to code they don't use.
3. Check the mix of stability and volatility: components with many incoming dependents should change rarely; if such a component is also volatile (frequently modified), that's a structural risk — either stabilize it or reduce how many things depend on it.
4. Look for cyclic dependencies between candidate components. If A and B depend on each other, they are really one component pretending to be two — merge them or extract the shared, cycle-breaking piece.
5. Re-evaluate the grouping against real change history, not just conceptual similarity: pull recent commits/PRs and check whether the proposed component boundaries actually match where changes clustered.
6. Name the resulting component boundary in terms of the business capability or change-reason it encapsulates, not the technical role of the code inside it.

## Decision rules
- Two pieces of code that always change together for the same reason belong in the same component, even if they look structurally different (e.g., a validator and the rule it validates).
- Two pieces of code that change for independent reasons belong in different components, even if they look structurally similar (e.g., two validators serving unrelated business rules).
- Don't group by technical kind alone ("all the validators," "all the DTOs") if the members of that group have unrelated reasons to change — this produces low cohesion behind a superficially tidy folder.
- Prefer fewer, coarser components while a system is small; split further only once real churn or reuse evidence justifies it — this skill is not a license to over-fragment on day one (see `avoid-premature-distribution` for the deployment-level version of that caution).
- A cyclic dependency between two proposed components is evidence they were split in the wrong place.

## Anti-patterns
- Organizing top-level folders by technical layer only (`controllers/`, `services/`, `models/`) with no regard for which business capability each file serves, so implementing one feature requires touching one file in each of five folders.
- Splitting a component purely because it has "too many files," without checking whether those files share a change-reason.
- Merging two components that happen to be small, even though they serve unrelated stakeholders and change on unrelated schedules.
- Leaving a widely-depended-on component volatile because splitting it "would take too long," while every dependent absorbs the churn.
- Choosing a boundary based on which team currently owns the code, if ownership doesn't track actual change/reuse patterns (see `design-for-independent-development` for the org-alignment question specifically).

## Exceptions and trade-offs
- Very early in a project, before change patterns are known, it's reasonable to start with a coarser, guessed grouping and refactor boundaries once real churn data exists — don't over-invest in boundary precision before there's evidence.
- Optimizing purely for reuse (CRP) and purely for closure (CCP) can pull a boundary in opposite directions; when they conflict, prefer grouping by change-reason for actively-developed code and by reuse for stable, widely-consumed libraries.
- A temporary grouping violation introduced under deadline pressure is acceptable if it's flagged and the follow-up split is tracked — silently living with it long-term is not.

## Verification
- Pick three recent feature changes and check whether each touched a small, contained set of components rather than being scattered across many.
- Check for dependency cycles between the chosen components; none should exist.
- For any component with many dependents, confirm its change frequency is low; if it's high, flag it as a stabilization risk.
- Confirm no component mixes code serving clearly unrelated stakeholders under one name.
