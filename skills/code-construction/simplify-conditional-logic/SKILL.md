---
name: simplify-conditional-logic
description: Reduce difficult-to-read branching by simplifying predicates, clarifying cases, extracting decisions, or changing the design when repeated variation indicates a deeper abstraction problem. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Simplify Conditional Logic

## Intent

Reduce difficult-to-read branching by simplifying predicates, clarifying cases, extracting decisions, or changing the design when repeated variation indicates a deeper abstraction problem.

## Apply when

Use this skill when you encounter:

- long `if/else` chains
- deeply nested conditionals
- repeated predicates
- duplicated branch logic
- flags controlling multiple behaviors
- repeated `switch`/`case` logic

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

## Verification

- Is the decision expressed once where possible?
- Are cases easy to enumerate?
- Can a reader explain the normal and exceptional paths quickly?
- Has the redesign reduced repetition without hiding domain behavior?


## Related skills

- CODE-05 Minimize Function and Class Complexity
- CODE-07 Keep Control Flow Understandable
- OO-04 Encapsulate What Varies
- MOD-03 Design for Extension Without Fragile Modification
