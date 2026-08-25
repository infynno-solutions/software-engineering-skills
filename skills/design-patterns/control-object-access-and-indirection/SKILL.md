---
name: control-object-access-and-indirection
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Introduce controlled indirection when direct access to an object needs isolation, lazy behavior, protection, remote access, caching, or another stable access policy.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify the access concern that should be separated from the target object.
2. Preserve the target interface where transparency is useful.
3. Place access policy in a proxy or facade-like boundary.
4. Keep the target unaware of unnecessary caller concerns.
5. Make latency, caching, authorization, or remote semantics explicit where they matter.
6. Avoid indirection that provides no concrete value.

# Decision rules

- Proxy is useful when access control, deferred loading, remote access, caching, or similar concerns vary independently.
- Facade is useful when the goal is a simpler interface over a subsystem rather than transparent substitution.
- Keep the indirection observable where behavior such as latency or failures changes semantics.

# Anti-patterns

- Proxy used as a generic wrapper for every object.
- Facades that absorb business logic.
- Hiding remote calls behind apparently local semantics without documenting consequences.
- Multiple layers of indirection with no distinct responsibility.

# Verification

- Is the access concern isolated?
- Is the additional indirection worth its complexity?
- Are changed semantics visible to callers?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
