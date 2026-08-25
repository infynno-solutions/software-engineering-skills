---
name: keep-object-responsibilities-cohesive
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Prevent objects from accumulating unrelated responsibilities merely because they share access to data or happen to be used by the same caller.

# When to apply

Use when:

- a class grows repeatedly for unrelated reasons;
- methods operate on unrelated parts of state;
- the class has many collaborators for different concerns;
- changing one behavior regularly requires touching unrelated methods;
- the class name requires "and" to describe everything it does.

# Procedure

1. List the object's responsibilities.
2. Group them by the reason they exist and change.
3. Identify responsibilities that do not share meaningful data, invariants, or conceptual purpose.
4. Extract a new object only when the extracted responsibility forms a coherent boundary.
5. Keep collaboration between the resulting objects explicit.
6. Re-check whether the split reduced complexity or merely created pass-through objects.

# Decision rules

- Cohesion is about related responsibility, not a target number of methods or lines.
- Multiple methods may belong together when they form one coherent abstraction.
- Do not split an object merely because it is large; split when responsibilities have distinct reasons to change or understandability improves.
- Avoid extracting utility classes that have no coherent ownership.

# Anti-patterns

- God objects.
- "Utils" classes containing unrelated business behavior.
- One class responsible for validation, persistence, formatting, messaging, and orchestration merely because it owns a database model.
- Excessive micro-classes with no meaningful responsibility.

# Verification

- The class has one understandable conceptual purpose.
- Related behavior and state are kept together.
- Changes to one responsibility do not routinely require changes to unrelated responsibilities.
- The resulting object graph remains understandable.

# Source basis

Code Complete describes a class as a cohesive, well-defined responsibility and emphasizes minimizing the portion of the program a developer must reason about at once. GoF describes composition as helping classes remain encapsulated and focused. Clean Architecture applies the same reasoning through the Single Responsibility Principle and component cohesion.
