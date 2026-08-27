---
name: design-for-extension-without-fragile-modification
description: "Adds a stable seam - interface, strategy, extension point - at a genuine recurring variation point so new behavior can be added without editing code that already works. Use when a switch gains a case every release for a new payment type, file format, or notification channel, or when every past change to a module forced a regression pass across unrelated callers. Not for a subclass violating its base contract (see preserve-behavioral-substitutability), choosing the concrete pattern (see encapsulate-algorithmic-variation), or introducing the seam into existing code (see refactor-toward-patterns-when-justified)."
license: MIT
---

# Design for Extension Without Fragile Modification

## Intent
Use stable seams to accommodate foreseeable variation when modifying existing behavior repeatedly would spread risk.

## Procedure
1. Identify a genuine variation point, not a hypothetical one.
2. Estimate how often and how independently it is likely to change.
3. Choose an extension mechanism that keeps stable policy intact — prefer the narrowest one that fits.
4. Reject the abstraction if the variation is speculative or the seam costs more than it saves.

## Decision rules
- Require at least two real variants, or a concretely planned third, before introducing an extension seam.
- Put the seam where the variation actually recurs (e.g., per-format serialization), not one level up or down from it.
- Prefer a function parameter or strategy object before an inheritance hierarchy or plugin framework.
- If using the seam still requires the caller to know which concrete variant to construct, the abstraction hasn't removed the coupling — it only moved it.

## Anti-patterns
- Adding factories or interfaces for every possible future feature.
- Using the open/closed principle as a mandate for inheritance-heavy frameworks.

## Exceptions and trade-offs
- Small, stable systems may be better served by direct code until variation becomes real.
- If the current change is the first observed variation, it's often cheaper to make the direct edit now and extract the seam when a second variant actually appears.

## Verification
- Add or simulate a new variant and confirm it can be introduced by adding code, without editing the existing stable module's body.
- Confirm existing variants and their tests still pass unmodified after the seam is introduced.
- Check that the extension mechanism has more than one real implementation, or a concrete second use planned, not just the original case wrapped in an interface.
