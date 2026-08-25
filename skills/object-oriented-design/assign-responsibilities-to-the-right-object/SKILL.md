---
name: assign-responsibilities-to-the-right-object
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Design objects around meaningful responsibilities rather than distributing behavior according to file layout, convenience, inheritance hierarchy, or the location of the first caller.

# When to apply

Use when:

- introducing new classes or methods;
- deciding where domain logic should live;
- moving behavior between objects;
- reviewing an object that has accumulated unrelated behavior;
- deciding whether a collaborator should own data, validation, transformation, or coordination.

# Procedure

1. Identify the behavior being requested.
2. Identify the information needed to perform it.
3. Identify which object owns or naturally controls that information.
4. Check whether that object already has a cohesive responsibility related to the behavior.
5. Prefer ownership that reduces knowledge crossing object boundaries.
6. If the behavior is orchestration rather than domain responsibility, keep the coordinator thin and delegate real work to responsible objects.
7. Re-check the resulting design for duplicated knowledge, long parameter lists, or objects that merely forward everything.

# Decision rules

- Put behavior near the data and invariants it must protect when that improves cohesion.
- Do not create a class merely to make a method shorter; introduce a new responsibility boundary only when it improves understanding, changeability, or coupling.
- A coordinator may own workflow sequencing without owning all of the underlying work.
- If assigning a responsibility requires an object to know many unrelated details, reconsider the boundary.

# Anti-patterns

- "God object" that knows and does everything.
- Service classes that contain domain rules solely because they were convenient to create.
- Anemic objects surrounded by procedural code that manipulates their state directly.
- Moving behavior to the caller merely because the caller already exists.
- Splitting one coherent responsibility across many objects only to satisfy arbitrary class-size rules.

# Verification

A reviewer should be able to answer:

- Can the object's responsibility be stated clearly?
- Does the object have the information required to perform the behavior without excessive asking of other objects?
- Does the placement reduce duplication and coordination complexity?
- Would a likely change affect one responsibility boundary or many unrelated objects?

# Source basis

Code Complete treats classes as cohesive, well-defined responsibilities and routines as intellectual tools for reducing complexity. GoF and Head First emphasize responsibility assignment through object collaboration, composition, and delegation. Clean Architecture adds the requirement that important business rules remain independent of volatile details.
