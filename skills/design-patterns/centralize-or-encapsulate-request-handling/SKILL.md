---
name: centralize-or-encapsulate-request-handling
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Represent requests, coordination, or responsibility transfers explicitly when they need to be queued, logged, composed, undone, routed, or mediated.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify request handling that is becoming coupled to the caller or receiver.
2. Determine whether the request itself needs a stable representation.
3. Encapsulate the request as an object or route it through a focused mediator/chain.
4. Keep receivers focused on executing their responsibility.
5. Add composition, queuing, undo, logging, or routing only when required.
6. Verify that control flow remains traceable.

# Decision rules

- Command is appropriate when requests need to be represented independently of invocation.
- Chain of Responsibility is useful when handlers should process or pass requests without a fixed caller-to-handler binding.
- Mediator is useful when many peers would otherwise become tightly connected.
- These patterns should simplify coordination, not hide it.

# Anti-patterns

- Command objects created solely to rename method calls.
- Mediators becoming god objects.
- Chains with ambiguous handler ownership.
- Hidden queues or asynchronous execution that change semantics without explicit design.

# Verification

- Can request flow be traced?
- Does the abstraction solve real coordination pressure?
- Are responsibilities still localized?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
