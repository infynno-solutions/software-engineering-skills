---
name: separate-responsibilities-by-reason-to-change
description: "Splits a module along genuinely independent reasons or actors that drive its changes, keeping behavior together when it changes for one reason. Use when a change requested by finance and one requested by legal both land in the same method, or a manager/service class's history shows edits for several unrelated reasons over time. Not when one reason's change ripples elsewhere in the codebase (see keep-changes-localized), when adding an extension point instead of splitting (see design-for-extension-without-fragile-modification), when auditing one object's method set (see keep-object-responsibilities-cohesive), or when performing the split mechanically (see extract-and-recompose-responsibilities)."
license: MIT
---

# Separate Responsibilities by Reason to Change

## Intent
Separate responsibilities when they have materially different reasons for change. Identify the actors, policies, or concerns that can change independently and avoid forcing unrelated changes through the same module.

## Procedure
1. Identify plausible sources of change (actors, policies, external triggers).
2. Check whether those changes occur independently in practice, not just in theory.
3. Separate responsibilities only when the separation reduces change propagation or improves understanding.
4. Keep closely related behavior together when separation would add needless coupling.

## Decision rules
- Identify responsibilities by asking which actor or business rule would request a given change, not by counting methods or lines.
- Logic that always changes together for the same actor's reasons can stay in one module even if it looks like "different things" (e.g., validation and formatting for the same report).
- Split only when change history or a concrete roadmap shows the reasons actually diverge; a hypothetical future actor is not yet a reason to split.
- When splitting, name each resulting module after the responsibility or actor it now serves so the boundary stays legible later.

## Anti-patterns
- Splitting every class until each has one method.
- Treating "one thing" as a mechanical rule without considering reasons for change.

## Exceptions and trade-offs
- A module may legitimately coordinate several operations when orchestration is itself its responsibility.

## Verification
- Check the module's recent change history (or a walkthrough of upcoming changes) and confirm each commit maps to one identifiable actor or reason.
- Confirm a change driven by one actor's requirement can be made without touching code that exists only for a different actor.
- After splitting, confirm each resulting module still has a single, statable reason to change.
