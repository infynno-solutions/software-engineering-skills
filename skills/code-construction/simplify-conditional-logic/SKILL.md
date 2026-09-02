---
name: simplify-conditional-logic
description: "Simplifies hard-to-read branching in code being authored now, by clarifying predicates or redesigning around repeated variation. Use when the same predicate is copy-pasted across three modules, or a switch on a type code keeps growing a new case every time a related feature is added. Not when the real issue is the ordering of happy path versus error handling (see keep-control-flow-understandable), when a class or function has taken on too many responsibilities (see design-cohesive-functions, design-cohesive-classes), or when restructuring existing conditionals under tests (see simplify-conditionals-and-control-flow)."
license: MIT
---

# Simplify Conditional Logic

## Intent

Reduce difficult-to-read branching by simplifying predicates, clarifying cases, extracting decisions, or changing the design when repeated variation indicates a deeper abstraction problem.

## Procedure

1. Identify the decision being made.
2. Name complicated predicates when doing so improves comprehension.
3. Remove duplicated branch behavior.
4. Separate normal and exceptional cases.
5. Extract cohesive decisions or operations.
6. If the same variation is repeated throughout the system, consider whether a polymorphic or data-driven design is more appropriate.
7. Verify that the new structure still reflects the domain behavior clearly.

## Decision rules

- Simplify before introducing a pattern.
- Repeated conditionals across multiple locations are a stronger signal for redesign than one isolated conditional.
- Do not replace a clear conditional with polymorphism merely because a pattern exists.
- Preserve explicitness when the number of cases is small and stable.

## Anti-patterns

- Pattern-for-pattern's-sake polymorphism.
- Nested conditions whose purpose is unclear.
- One routine performing multiple distinct operations selected by flags.
- Duplicating the same business predicate across several modules.

## Exceptions and trade-offs

- A small, stable number of cases (three enum values that will never grow) is often clearer as an explicit conditional than as a polymorphic hierarchy.
- Introducing a strategy or polymorphism pattern adds indirection and extra types; it's only justified once the variation is genuinely repeated across the codebase, not for a single occurrence.
- Extracting a named predicate can obscure a condition that was actually simpler read inline — verify the extraction is a net readability win, not just fewer characters at the call site.

## Verification

- Is the decision expressed once where possible?
- Are cases easy to enumerate?
- Can a reader explain the normal and exceptional paths quickly?
- Has the redesign reduced repetition without hiding domain behavior?
