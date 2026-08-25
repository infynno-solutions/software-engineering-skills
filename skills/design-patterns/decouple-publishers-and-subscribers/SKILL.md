---
name: decouple-publishers-and-subscribers
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Decouple producers of events or changes from consumers when consumers should evolve independently and the producer should not know their concrete implementations.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify a one-to-many dependency or event publication point.
2. Define the event/notification contract.
3. Register or compose consumers through an abstraction.
4. Keep publisher logic independent of concrete subscribers.
5. Define ordering, delivery, failure, and lifecycle semantics when they matter.
6. Prevent notification mechanics from becoming hidden control flow.

# Decision rules

- Observer is appropriate when consumers vary independently from the publisher.
- The notification abstraction should remain focused.
- Explicitly define synchronous/asynchronous semantics if they affect correctness.
- Avoid observers when a direct call makes the dependency clearer and stable.

# Anti-patterns

- Hidden observer graphs that make control flow impossible to trace.
- Subscriber side effects that depend on undocumented ordering.
- Notification as a replacement for every direct dependency.
- Global event buses used without ownership or lifecycle boundaries.

# Verification

- Can the publisher remain unchanged as consumers vary?
- Are delivery and failure semantics understandable?
- Can a reviewer trace important control flow without discovering hidden subscribers?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
