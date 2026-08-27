---
name: keep-object-responsibilities-cohesive
description: "Audits an object that has already piled up unrelated responsibilities and regroups its methods around one coherent reason to change. Use when a class grows repeatedly for unrelated reasons, its methods operate on unrelated parts of state, changing one behavior forces edits to unrelated methods, or its name needs the word and. Not for picking the owner of new behavior in the first place (see assign-responsibilities-to-the-right-object), designing a fresh class (see design-cohesive-classes), splitting a module by actor (see separate-responsibilities-by-reason-to-change), or executing the split (see extract-and-recompose-responsibilities)."
license: MIT
---

# Keep Object Responsibilities Cohesive

## Intent

Prevent objects from accumulating unrelated responsibilities merely because they share access to data or happen to be used by the same caller.

## Procedure

1. List the object's responsibilities.
2. Group them by the reason they exist and change.
3. Identify responsibilities that do not share meaningful data, invariants, or conceptual purpose.
4. Extract a new object only when the extracted responsibility forms a coherent boundary.
5. Keep collaboration between the resulting objects explicit.
6. Re-check whether the split reduced complexity or merely created pass-through objects.

## Decision rules

- Cohesion is about related responsibility, not a target number of methods or lines.
- Multiple methods may belong together when they form one coherent abstraction.
- Do not split an object merely because it is large; split when responsibilities have distinct reasons to change or understandability improves.
- Avoid extracting utility classes that have no coherent ownership.

## Anti-patterns

- God objects.
- "Utils" classes containing unrelated business behavior.
- One class responsible for validation, persistence, formatting, messaging, and orchestration merely because it owns a database model.
- Excessive micro-classes with no meaningful responsibility.

## Exceptions and trade-offs

- Splitting increases the number of objects and collaboration points; for a small, rarely-touched class, tolerating mild incohesion can be cheaper than the added indirection of extraction.
- Two responsibilities that always change together in practice — even if conceptually distinct on paper — may be fine to keep combined; judge cohesion by actual change history and coupling, not by abstract taxonomy.
- Extracting responsibilities purely to satisfy a line-count or method-count lint rule can produce pass-through classes that reduce, rather than improve, understandability — the split must earn its keep in clarity, not just in metrics.

## Verification

- The class has one understandable conceptual purpose.
- Related behavior and state are kept together.
- Changes to one responsibility do not routinely require changes to unrelated responsibilities.
- The resulting object graph remains understandable.
