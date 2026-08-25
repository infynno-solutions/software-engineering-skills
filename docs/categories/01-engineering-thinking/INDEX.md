# Category 01 — Engineering Thinking & Problem Solving

Engineering thinking skills govern how an agent reasons before changing a codebase.

## Skills

| ID | Skill | Primary role |
|---|---|---|
| ENG-01 | Frame the Problem Before Designing the Solution | Establish the real problem and outcome |
| ENG-02 | Identify Requirements and Constraints | Separate requirements, constraints, assumptions, and unknowns |
| ENG-03 | Identify the Shape of Change | Determine what is volatile and what should remain stable |
| ENG-04 | Manage Essential vs. Accidental Complexity | Minimize unnecessary cognitive and structural complexity |
| ENG-05 | Evaluate Engineering Trade-offs | Compare alternatives explicitly |
| ENG-06 | Make Evidence-Based Engineering Decisions | Prefer evidence, estimates, experiments, and precedent over preference |
| ENG-07 | Defer Decisions When Uncertainty Is High | Keep volatile options open without speculative architecture |
| ENG-08 | Prefer the Simplest Adequate Solution | Avoid unnecessary machinery and speculative flexibility |
| ENG-09 | Iterate Design Before Committing | Explore alternatives and use feedback before locking in design |
| ENG-10 | Revisit Decisions as Context Changes | Reassess decisions as requirements, scale, or evidence changes |

## Category operating rule

Before implementing a non-trivial change, the agent should determine:

1. What problem is actually being solved?
2. What constraints and acceptance conditions exist?
3. What is likely to change?
4. What complexity is essential versus self-inflicted?
5. What alternatives exist and what trade-offs separate them?
6. What evidence is available?
7. Which decisions need to remain reversible?
8. What is the simplest solution that adequately addresses the known problem?

Do not force a design conclusion when the source material does not support one. Record uncertainty and identify what evidence would change the decision.
