---
name: prevent-dependency-cycles
description: "Detects and breaks cycles in the module or package dependency graph so components can be built, tested, and released independently. Use on a circular-import build error or lint warning, two modules whose cross-references keep growing as features touch both, or a component that cannot ship a hotfix alone because it is entangled with its dependents. Not when dependencies are acyclic but simply pointing the wrong way (see control-dependency-direction), or when the question is where the interface that would break the cycle should live (see invert-dependencies-around-stable-policy)."
license: MIT
---

# Prevent Dependency Cycles

## Intent
Keep component/module dependencies acyclic so components remain buildable, testable, releasable, and understandable.

## Procedure
1. Identify cycles in the dependency graph.
2. Find the conceptual reason the cycle exists.
3. Break it through dependency inversion, extraction of shared policy into a lower-level component, or relocation of the offending reference.
4. Re-run dependency checks after the change.

## Decision rules
- Prefer extracting the specific shared type or interface both sides need into a third, lower-level component over merging the two components.
- Prefer inverting one side's dependency (define the interface on the side that should be depended upon) over introducing a new shared module, when only one relationship is actually needed both ways.
- A cycle formed from many small back-and-forth calls between two components is often evidence they're really one component (see `group-components-by-cohesion`) rather than two that need decoupling.
- Fix the conceptual reason two components reference each other; don't just reverse one import to make the tool pass.

## Anti-patterns
- Suppressing cycle detection (annotations, tool config) without fixing the structure.
- Creating a dumping-ground shared module just to break a cycle.

## Exceptions and trade-offs
- Some language-level cyclic references may be harmless; the skill targets architectural cycles that impede independent build, test, and release.

## Verification
- Re-run the dependency/cycle checker (or redraw the graph) and confirm the specific cycle is gone, not just reduced in size.
- Confirm each formerly-cyclic component can now be built and unit-tested in isolation, in a single topological order.
- Check the fix didn't just move the cycle up a level (e.g., into a new shared "common" module that now depends back on one of the originals).
