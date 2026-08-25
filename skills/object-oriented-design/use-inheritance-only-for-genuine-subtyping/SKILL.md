---
name: use-inheritance-only-for-genuine-subtyping
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Prevent inheritance hierarchies from becoming implementation-sharing mechanisms that violate substitutability or expose fragile dependencies.

# When to apply

Evaluate inheritance when:

- modeling a polymorphic family of types;
- designing a framework extension point;
- considering subclass-based reuse;
- replacing a large conditional with polymorphism;
- reviewing whether a subclass truly "is a" valid instance of the abstraction.

# Procedure

1. Identify the base type's externally visible contract.
2. Identify what every subtype must preserve.
3. Check preconditions, postconditions, invariants, and semantic expectations.
4. Determine whether the subclass is genuinely substitutable for the base type.
5. If substitution fails or requires caller-specific knowledge, do not use inheritance for that relationship.
6. Prefer composition or another abstraction mechanism for pure implementation reuse.

# Decision rules

- Inheritance should express a stable subtype relationship, not just "shares code with."
- A subclass should preserve the expectations clients have of the base abstraction.
- Prefer inheriting from small, stable abstractions over depending heavily on mutable implementation details.
- Deep hierarchies require stronger justification because inherited behavior propagates dependencies.

# Anti-patterns

- "X extends Y" because Y contains convenient helper methods.
- Subclasses that disable or throw for inherited operations.
- Base classes whose protected state becomes an accidental shared data protocol.
- Hierarchies where every feature adds another subclass and behavior becomes difficult to locate.

# Verification

Ask:

- Can existing clients safely use the subtype as the base type?
- Does the subtype honor the abstraction's behavioral meaning?
- Would a change in the base implementation unexpectedly break subclasses?
- Would composition communicate the design intent more clearly?

# Source basis

GoF distinguishes interface inheritance from implementation inheritance and warns that implementation inheritance can break encapsulation. Clean Architecture uses the Liskov Substitution Principle to guide inheritance. Head First repeatedly contrasts inheritance with composition when behavior needs to vary.
