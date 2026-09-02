---
name: group-components-by-cohesion
description: "Decides which classes belong in the same releasable component, weighing what changes together, is reused together, and is released together. Use when choosing a package for a new class among several plausible ones, when a library ships a version bump to consumers who use none of the changed code, or when a shared component's classes have no relationship except being reusable. Not for which way dependencies between components point (see control-dependency-direction), what one client sees (see keep-interfaces-narrow-and-client-focused), or architecture-level boundary placement by change rate (see choose-boundaries-by-change-and-coupling)."
license: MIT
---

# Group Components by Cohesion

## Intent
Group classes into components according to shared change/reuse/release characteristics while respecting the tension between cohesion goals.

## Procedure
1. Identify classes that change together in practice.
2. Identify classes that are reused and released together.
3. Identify dependencies on individual classes that cause unnecessary release propagation to consumers.
4. Choose a component boundary balancing common closure, reuse, and release cost.

## Decision rules
- Classes that reliably change for the same reason belong in the same component, even if they serve different technical roles.
- Don't extract a class or two into a shared component before it has real, independent reuse — accept temporary duplication until reuse is real.
- If a component's releases force unrelated consumers to re-test or re-deploy, it's bundling unrelated reuse groups and should split.
- When cohesion goals conflict, favor common-closure for actively-developed code and reuse/release grouping for stable, externally-consumed code.

## Anti-patterns
- Maximizing any single cohesion principle blindly.
- Making components large solely to avoid duplication.
- Grouping classes purely by technical layer (all "validators" together) when they don't change or release together.

## Exceptions and trade-offs
- The optimal balance changes as a system and organization mature; revisit groupings rather than treating them as permanent.

## Verification
- For the last few real changes touching this component, confirm they stayed inside one component instead of forcing edits across several.
- Confirm the component's dependents don't need to upgrade on releases that touch none of the classes they use.
- Check that any class proposed for extraction into its own component already has more than one real, independent consumer.
