# Category 05 — Design Patterns

Design patterns are reusable responses to recurring design problems and forces. The goal of this category is not pattern-name matching. Agents should first diagnose the design force, then select a pattern or simpler alternative based on consequences. GoF defines a pattern in terms of a recurring problem, its context, the solution, and its consequences; Head First emphasizes that many patterns address change and allow parts of a system to vary independently.

## Skill inventory

| ID | Skill | Candidate GoF / related techniques |
|---|---|---|
| PAT-01 | Recognize Recurring Design Forces | All patterns; pattern discovery |
| PAT-02 | Select Patterns by Forces and Consequences | All patterns |
| PAT-03 | Encapsulate Object Creation | Factory Method, Abstract Factory, Builder, Prototype |
| PAT-04 | Encapsulate Algorithmic Variation | Strategy, Template Method |
| PAT-05 | Represent State-Dependent Behavior Explicitly | State |
| PAT-06 | Decouple Publishers and Subscribers | Observer |
| PAT-07 | Compose and Augment Object Behavior | Decorator, Composite |
| PAT-08 | Adapt Incompatible Interfaces | Adapter |
| PAT-09 | Separate Abstraction from Implementation | Bridge |
| PAT-10 | Control Object Access and Indirection | Proxy, Facade |
| PAT-11 | Centralize or Encapsulate Request Handling | Command, Chain of Responsibility, Mediator |
| PAT-12 | Compose Patterns Without Pattern Accumulation | Pattern combinations / refactoring |

## Pattern-selection rule

Do not introduce a pattern because its name appears to match the problem. State the problem, identify the forces and variation points, compare a simpler solution with relevant pattern families, then choose the smallest structure that gives the required flexibility.

## Source synthesis

GoF presents patterns as named, motivated recurring solutions and emphasizes programming to interfaces, composition, delegation, and pattern combinations. Head First emphasizes identifying what varies, encapsulating it, loose coupling, composition, and learning when patterns are appropriate. Code Complete contributes simplicity, iterative design, standard techniques, and avoidance of exotic solutions. Clean Architecture contributes dependency direction, boundaries, and keeping stable policy independent of details.
