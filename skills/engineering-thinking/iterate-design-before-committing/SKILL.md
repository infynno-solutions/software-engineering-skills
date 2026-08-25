---
name: iterate-design-before-committing
description: Treat design as an iterative engineering activity: explore alternatives, compare them, test important assumptions, and refine the solution before making an expensive commitment. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Iterate Design Before Committing

## Intent

Treat design as an iterative engineering activity: explore alternatives, compare them, test important assumptions, and refine the solution before making an expensive commitment.

## Apply when

Use this skill when:

- a design has multiple plausible solutions
- requirements are still evolving
- a change has high blast radius
- the design introduces new abstractions or boundaries
- there is a meaningful risk that the first solution will encode the wrong assumptions

## Procedure

1. Produce at least two plausible approaches for material design decisions.
2. Compare them against explicit criteria.
3. Identify assumptions that can be tested cheaply.
4. Prototype, benchmark, spike, or inspect the codebase as appropriate.
5. Choose the smallest design that survives the evaluation.

## Decision rules

- Do not treat the first workable design as automatically good.
- The amount of design exploration should be proportional to the cost of being wrong.
- Prefer cheap experiments over prolonged speculation when practical.
- Iteration does not justify endlessly postponing implementation.

## Anti-patterns

- Coding the first idea immediately for a large architectural change.
- Generating many designs with no decision criteria.
- Prototyping without converting findings into a decision.
- Designing everything up front when small feedback cycles would reveal more information.

## Verification

For a non-trivial design, retain a brief record of:

- alternatives considered
- important assumptions
- evaluation performed
- selected approach
- rejected alternatives and why


## Related skills

- ENG-01 Frame the Problem Before Designing the Solution
- ENG-05 Evaluate Engineering Trade-offs
- ENG-06 Make Evidence-Based Engineering Decisions
- ENG-10 Revisit Decisions as Context Changes
