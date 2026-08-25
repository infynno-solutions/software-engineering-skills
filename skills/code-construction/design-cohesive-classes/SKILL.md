---
name: design-cohesive-classes
description: "Organize data and behavior into classes that have a focused, well-defined responsibility and an interface that allows consumers to ignore unnecessary internals. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Design Cohesive Classes

## Intent

Organize data and behavior into classes that have a focused, well-defined responsibility and an interface that allows consumers to ignore unnecessary internals.

## Apply when

Use this skill when:

- introducing a class or module
- deciding whether behavior belongs together
- reviewing a class that has grown substantially
- designing a public interface
- splitting responsibilities during refactoring

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

## Verification

- Can the class responsibility be stated in one or two precise sentences?
- Are most methods and fields directly related to that responsibility?
- Can consumers use it without understanding its internal representation?
- Do unrelated changes require changing the same class?


## Related skills

- CODE-03 Design Cohesive Functions
- CODE-10 Encapsulate Implementation Details
- MOD-01 Separate Responsibilities by Reason to Change
- MOD-02 Keep Changes Localized
