---
name: frame-the-problem
description: "Understand the problem, desired outcome, and relevant context before selecting an implementation. The agent should solve the stated engineering problem rather than prematurely optimizing for a particular implementation, pattern, framework, or technology. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern."
license: MIT
---

# Frame the Problem Before Designing the Solution

## Intent

Understand the problem, desired outcome, and relevant context before selecting an implementation.

The agent should solve the stated engineering problem rather than prematurely optimizing for a particular implementation, pattern, framework, or technology.

## Apply when

Use this skill for:

- feature work with ambiguous requirements
- bug fixes where symptoms may not equal the root problem
- architectural changes
- performance work
- refactoring proposals
- new abstractions or infrastructure
- changes whose blast radius is unclear

## Procedure

1. State the problem in domain terms.
2. State the desired observable outcome.
3. Identify the affected users, components, workflows, and operational constraints.
4. Separate known facts from assumptions.
5. Identify what is explicitly required versus merely suggested by the current implementation.
6. Identify important unknowns.
7. Only then enumerate candidate solutions.

## Decision rules

- Do not start from a preferred technology and retrofit a problem around it.
- Do not treat an existing implementation detail as a requirement without evidence.
- If the problem definition is unstable, prefer an incremental investigation over a large irreversible design.
- A problem that cannot yet be stated clearly may need exploration before implementation.

## Anti-patterns

- Jumping directly from ticket text to code changes.
- Choosing a pattern because it is familiar rather than because the forces require it.
- Treating the current architecture as the definition of the problem.
- Designing for hypothetical requirements that have not been established.

## Verification

Before implementation, the agent should be able to answer:

- What exact problem is being solved?
- What observable result determines success?
- What constraints matter?
- Which assumptions remain uncertain?

If these cannot be answered, continue analysis rather than making a large design commitment.


## Related skills

- ENG-02 Identify Requirements and Constraints
- ENG-03 Identify the Shape of Change
- ENG-05 Evaluate Engineering Trade-offs
- ENG-09 Iterate Design Before Committing
