---
name: assign-responsibilities-to-the-right-object
description: "Picks which object should own a new or misplaced behavior, based on who holds the information and invariants it needs. Use when introducing a class or method, deciding where domain logic lives, moving behavior between objects, or tracing a bug to duplicated or misplaced logic. Not for splitting an object that has already accumulated unrelated duties (see keep-object-responsibilities-cohesive), hiding an object's fields (see encapsulate-representation), or performing the move mechanically under tests (see extract-and-recompose-responsibilities)."
license: MIT
---

# Assign Responsibilities to the Right Object

## Intent

Design objects around meaningful responsibilities rather than distributing behavior according to file layout, convenience, inheritance hierarchy, or the location of the first caller.

## Procedure

1. Identify the behavior being requested.
2. Identify the information needed to perform it.
3. Identify which object owns or naturally controls that information.
4. Check whether that object already has a cohesive responsibility related to the behavior.
5. Prefer ownership that reduces knowledge crossing object boundaries.
6. If the behavior is orchestration rather than domain responsibility, keep the coordinator thin and delegate real work to responsible objects.
7. Re-check the resulting design for duplicated knowledge, long parameter lists, or objects that merely forward everything.

## Decision rules

- Put behavior near the data and invariants it must protect when that improves cohesion.
- Do not create a class merely to make a method shorter; introduce a new responsibility boundary only when it improves understanding, changeability, or coupling.
- A coordinator may own workflow sequencing without owning all of the underlying work.
- If assigning a responsibility requires an object to know many unrelated details, reconsider the boundary.

## Anti-patterns

- "God object" that knows and does everything.
- Service classes that contain domain rules solely because they were convenient to create.
- Anemic objects surrounded by procedural code that manipulates their state directly.
- Moving behavior to the caller merely because the caller already exists.
- Splitting one coherent responsibility across many objects only to satisfy arbitrary class-size rules.

## Exceptions and trade-offs

- A thin application-service/coordinator object is legitimate when a use case spans several domain objects and no single one naturally owns the cross-cutting sequencing — don't force orchestration onto a domain object just to avoid a service class.
- Under real time pressure, placing a one-off behavior in a convenient-but-imperfect location and leaving a note is a reasonable trade-off; the risk is that "temporary" placement becomes permanent as more callers accumulate around it.
- Optimizing purely for "least knowledge crossing boundaries" can add indirection for a small, rarely-changed piece of logic that isn't worth the extra object — weigh the reasoning cost against how often the behavior actually changes.
- Framework conventions (a controller must expose a specific method shape, a job class must implement a fixed interface) sometimes force behavior into a location that isn't the ideal owner; isolate the framework-mandated shim from the real logic rather than letting the framework dictate the whole design.

## Verification

A reviewer should be able to answer:

- Can the object's responsibility be stated clearly?
- Does the object have the information required to perform the behavior without excessive asking of other objects?
- Does the placement reduce duplication and coordination complexity?
- Would a likely change affect one responsibility boundary or many unrelated objects?
