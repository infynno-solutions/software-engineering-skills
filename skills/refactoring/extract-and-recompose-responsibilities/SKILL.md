---
name: extract-and-recompose-responsibilities
description: "Splits a function or class that does several unrelated things into cohesive units via Extract and Move refactorings. Use for a function that parses, validates, and persists in one body, or a class exhibiting feature envy on another class's data. Not for reducing branching complexity within one function (see simplify-conditionals-and-control-flow), eliminating copy-pasted logic across call sites (see remove-duplication-with-care), or deciding which object should own the behavior in the first place (see assign-responsibilities-to-the-right-object)."
license: MIT
---

# Extract and Recompose Responsibilities

## Intent
Use extraction, movement, and recomposition refactorings to restore cohesive functions and classes and clarify responsibility boundaries.

## Procedure
1. Name the distinct responsibilities inside the unit by describing what each block of code is "about" — e.g., "parses input," "computes total," "writes audit log."
2. For each candidate responsibility, check for a natural seam: does it use a distinct subset of the enclosing state or parameters, and could it be named as a verb phrase on its own?
3. Extract the smallest, most self-contained responsibility first, passing in only the data it actually needs.
4. If the extracted piece depends heavily on another class's data (feature envy), move it to that class instead of leaving it as a lonely extracted method.
5. Recompose: once several small units exist, look for a natural grouping — a new class, module, or strategy object — rather than leaving a flat pile of tiny functions.
6. Re-run the original entry point's tests after each extraction to confirm the seam did not change behavior.

## Decision rules
- Extract along a responsibility boundary that a domain expert would recognize by name, not an arbitrary line count.
- Prefer moving a method to the class whose data it primarily uses over adding a parameter to keep it where it is.
- Recompose into a new class or module only once at least two extracted pieces are cohesive together — don't create a one-method class speculatively.
- Keep the original function's public signature and observable behavior unchanged unless the task explicitly calls for a behavior change.

## Anti-patterns
- Extracting a method that still takes many parameters because the real cohesive boundary was ignored — a sign the split didn't follow responsibility.
- Creating a "Helpers" or "Utils" grab-bag class instead of naming the recomposed responsibility.
- Extracting for its own sake when the block has exactly one caller and no independent reason to change, which only adds indirection.
- Leaving a "God object" class in place while extracting from everything around it, so it still owns unrelated state after the refactor.

## Exceptions and trade-offs
- In a hot path, an extra function call from extraction is rarely worth avoiding, but profile before assuming it doesn't matter in genuinely performance-critical code.
- If two responsibilities always change together historically according to source history, leaving them combined may be more honest than forcing an artificial split.

## Verification
- Confirm each extracted unit has a single, nameable reason to change.
- Confirm the original caller's tests still pass unmodified.
- Confirm no extracted method needs an unusually long parameter list — if it does, the boundary is likely wrong.
- Check that recomposed classes or modules have cohesive fields, where most methods use most fields.
