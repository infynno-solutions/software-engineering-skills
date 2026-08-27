---
name: use-inheritance-only-for-genuine-subtyping
description: "The substitutability test to run whenever inheritance is actually on the table: is the subclass a valid instance of the base contract, or does it silently violate its preconditions, postconditions, or invariants. Use when modeling a polymorphic type family, designing a framework extension point, or reviewing a subclass that exists for code reuse. Not when the goal is reuse rather than modeling a type family (see prefer-composition-for-behavioral-reuse), nor for checking substitutability of interface implementations at module level (see preserve-behavioral-substitutability)."
license: MIT
---

# Use Inheritance Only for Genuine Subtyping

## Intent

Prevent inheritance hierarchies from becoming implementation-sharing mechanisms that violate substitutability or expose fragile dependencies.

## Procedure

1. Identify the base type's externally visible contract.
2. Identify what every subtype must preserve.
3. Check preconditions, postconditions, invariants, and semantic expectations.
4. Determine whether the subclass is genuinely substitutable for the base type.
5. If substitution fails or requires caller-specific knowledge, do not use inheritance for that relationship.
6. Prefer composition or another abstraction mechanism for pure implementation reuse.

## Decision rules

- Inheritance should express a stable subtype relationship, not just "shares code with."
- A subclass should preserve the expectations clients have of the base abstraction.
- Prefer inheriting from small, stable abstractions over depending heavily on mutable implementation details.
- Deep hierarchies require stronger justification because inherited behavior propagates dependencies.

## Anti-patterns

- "X extends Y" because Y contains convenient helper methods.
- Subclasses that disable or throw for inherited operations.
- Base classes whose protected state becomes an accidental shared data protocol.
- Hierarchies where every feature adds another subclass and behavior becomes difficult to locate.

## Exceptions and trade-offs

- A sealed/closed hierarchy used purely as a tagged union — a small, fixed set of result variants matched exhaustively — can use inheritance or sealed classes for representation convenience even when classic behavioral substitutability isn't the primary concern; the compiler-checked exhaustiveness is the actual benefit being sought there.
- Framework base classes (test-case base classes, UI widget base classes) frequently violate strict substitutability in minor, framework-sanctioned ways; following the framework's own extension contract is pragmatic even when it wouldn't pass a from-scratch LSP review.
- Disabling one inherited method with an explicit, documented "not supported" exception is sometimes an acceptable narrow violation when the base abstraction is otherwise a very strong fit and the unsupported operation is rare — but treat that as a signal to revisit the hierarchy, not a pattern to repeat elsewhere.

## Verification

Ask:

- Can existing clients safely use the subtype as the base type?
- Does the subtype honor the abstraction's behavioral meaning?
- Would a change in the base implementation unexpectedly break subclasses?
- Would composition communicate the design intent more clearly?
