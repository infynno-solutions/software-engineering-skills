---
name: recognize-recurring-design-forces
description: . Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Intent

Design-pattern use starts with recognizing a recurring design problem and the forces around it, not with searching for a pattern name. Inspect what varies, what must remain stable, who must know about whom, how objects collaborate, and what consequences the current structure creates.

# When to apply

Use when the recurring forces described below are present and a simpler design is insufficient.

# Procedure

1. Describe the problem without naming a pattern.
2. Identify the forces and constraints.
3. Identify what varies and what should remain stable.
4. Identify the collaborators and dependency relationships.
5. Look for a known pattern family only after the forces are clear.

# Decision rules

- A pattern is justified by a recurring problem and its forces, not novelty.
- Prefer the smallest known pattern that addresses the actual forces.
- If the problem is not recurring or the forces are weak, a simpler design may be better.
- Do not force a GoF pattern onto a problem merely because its name appears to fit.

# Anti-patterns

- Pattern-first design.
- Pattern-name matching without understanding consequences.
- Treating a pattern as a finished architecture.
- Assuming every variation deserves an abstraction.

# Verification

- Can the problem and forces be stated independently of the pattern name?
- Is there a clear reason the chosen structure addresses those forces?
- Are the pattern consequences explicit?

# Source basis

- GoF: *Design Patterns: Elements of Reusable Object-Oriented Software*
- Head First Design Patterns
- Code Complete
- Clean Architecture

**Synthesis note:** This skill expresses the underlying design force rather than prescribing a pattern by name. Specific GoF pattern names are included only as candidate techniques, because the books emphasize understanding when and how patterns apply rather than memorizing a catalog.
