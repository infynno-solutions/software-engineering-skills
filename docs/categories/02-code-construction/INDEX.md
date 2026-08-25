# Category 02 — Code Construction & Code Quality

Code-construction skills govern how an agent turns a design into readable, maintainable, reliable source code.

The category is intentionally broader than formatting or style. It covers the construction-level practices that reduce cognitive load, make behavior explicit, expose defects early, and keep code changeable.

## Skills

| ID | Skill | Primary role |
|---|---|---|
| CODE-01 | Write Code at the Level of Intent | readability and abstraction |
| CODE-02 | Name for Meaning | readability and communication |
| CODE-03 | Design Cohesive Functions | routine design |
| CODE-04 | Design Cohesive Classes | class design |
| CODE-05 | Minimize Function and Class Complexity | complexity control |
| CODE-06 | Make Dependencies Explicit | dependency reasoning |
| CODE-07 | Keep Control Flow Understandable | control-flow design |
| CODE-08 | Simplify Conditional Logic | complexity reduction |
| CODE-09 | Minimize State and Side Effects | state management |
| CODE-10 | Encapsulate Implementation Details | information hiding |
| CODE-11 | Write for the Maintainer | maintainability |
| CODE-12 | Use Comments for Missing Context | documentation and intent |
| CODE-13 | Apply Defensive Programming | correctness and failure handling |
| CODE-14 | Use Compiler and Static Feedback | defect prevention |
| CODE-15 | Continuously Improve Code Quality | ongoing code stewardship |

## Category operating rule

When implementing or modifying code, the agent should continuously ask:

1. Can a reader understand the intent without reconstructing hidden assumptions?
2. Does each function or class have a cohesive purpose?
3. Are dependencies, control flow, state, and side effects visible?
4. Is the implementation more complicated than the problem requires?
5. Are names, interfaces, and comments communicating the right information?
6. Are invalid states, unexpected inputs, and failure paths handled deliberately?
7. Can compiler, static-analysis, tests, or review feedback expose a mistake early?
8. Does the change leave the code easier—not harder—to understand and modify?

Do not impose arbitrary line counts, naming styles, abstraction layers, or formatting rules when the repository already has established conventions. Local project rules take precedence over generic style preferences, while the engineering principles in these skills govern the reasoning behind those rules.
