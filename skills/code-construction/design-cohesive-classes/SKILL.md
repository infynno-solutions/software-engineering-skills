---
name: design-cohesive-classes
description: "Gives a class one focused responsibility and a minimal interface. Use when deciding whether two pieces of behavior belong in the same class, or when a class has accumulated persistence, orchestration, and presentation duties that each change for different reasons. Not for hiding internal representation on an otherwise well-scoped class (see encapsulate-implementation-details), a single function rather than a class (see design-cohesive-functions), auditing an existing overloaded object (see keep-object-responsibilities-cohesive), or performing the split under tests (see extract-and-recompose-responsibilities)."
license: MIT
---

# Design Cohesive Classes

## Intent

Organize data and behavior into classes that have a focused, well-defined responsibility and an interface that allows consumers to ignore unnecessary internals.

## Procedure

1. Identify the responsibility or service the class provides.
2. Group data and operations that directly support that responsibility.
3. Identify unrelated responsibilities that should move elsewhere.
4. Define the smallest useful public interface.
5. Hide representation and implementation details that consumers do not need.
6. Check whether callers need to understand the class's internal mechanics.

## Decision rules

- A class should provide a cohesive set of responsibilities or services.
- Prefer interfaces that allow callers to ignore most internal details.
- Split a class when distinct responsibilities change for different reasons or create unrelated dependencies.
- Do not split a class merely because it contains several methods; cohesion matters more than method count.

## Anti-patterns

- "God classes" that own unrelated business, persistence, orchestration, and presentation responsibilities.
- Public exposure of internal state because it is convenient for callers.
- Classes whose only commonality is that they happen to be used together.

## Exceptions and trade-offs

- A small data-holder class (a DTO or value object) does not need elaborate cohesion analysis — this matters most as responsibilities and state accumulate.
- Splitting responsibilities always adds an interface and coordination cost; do not split a stable, rarely-changed class purely for theoretical purity.
- Framework-mandated shapes (a controller base class, an ORM entity) may force technically unrelated methods together; judge cohesion against the part of the design that is actually within your control.

## Verification

- Can the class responsibility be stated in one or two precise sentences?
- Are most methods and fields directly related to that responsibility?
- Can consumers use it without understanding its internal representation?
- Do unrelated changes require changing the same class?
