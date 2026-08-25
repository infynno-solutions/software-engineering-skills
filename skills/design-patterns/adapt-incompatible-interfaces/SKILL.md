---
name: adapt-incompatible-interfaces
description: ". Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Intent

Introduce a compatibility boundary when two collaborators have useful behavior but incompatible interfaces, so existing code can work without invasive changes.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Identify the incompatible client and provider contracts.
2. Decide which side's interface should remain stable.
3. Introduce an adapter at the boundary.
4. Translate semantics explicitly rather than blindly mapping names.
5. Keep the translation localized.
6. Test edge cases where the contracts differ semantically.

# Decision rules

- Adapter should isolate incompatibility rather than spread translation code.
- Prefer semantic translation over mechanical forwarding when meanings differ.
- Keep adapters thin enough that they do not become a second domain model.
- Use adapters at architectural boundaries when integrating external systems.

# Anti-patterns

- Scattered conversions throughout callers.
- Adapters containing business policy.
- Assuming compatible method signatures mean compatible semantics.
- Adapter chains that hide ownership of transformation logic.

# Verification

- Is incompatibility confined to one boundary?
- Is semantic translation explicit?
- Can either side change internally without forcing unrelated callers to change?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
