---
name: use-automated-refactoring-tools-when-safe
description: "Prefers IDE, LSP, or compiler refactor commands over hand-editing text, while checking blind spots like reflection, string references, and dynamic typing. Use for a symbol rename across many files, an extract-method or extract-variable in a language with strong tooling, or a large mechanical signature change across a typed codebase. Not for how big each step should be or how to sequence them (see refactor-in-small-safe-steps), nor for treating compiler and lint diagnostics as everyday feedback (see use-compiler-and-static-feedback)."
license: MIT
---

# Use Automated Refactoring Tools When Safe

## Intent
Prefer syntax-aware, semantics-aware refactoring tools when they can safely express the intended change, while verifying tool limitations and running tests.

## Procedure
1. Before hand-editing for a mechanical change — rename, move, extract, inline, change signature — check whether the language's IDE, LSP, or compiler tooling offers an automated refactor command for it.
2. Confirm the tool operates on the language's actual syntax tree or type information, not text or regex search-replace, since that's what makes it trustworthy for this kind of change.
3. Run the automated refactor, then diff the result before committing — automated tools can still miss dynamic dispatch, reflection, string-based references such as a name in a config file, and generated code.
4. Run the test suite immediately after the automated change, same as for a manual refactor; automation reduces risk, it doesn't eliminate the need to verify.
5. For anything the tool flags as ambiguous or can't safely resolve, such as a rename colliding with an existing symbol, stop and resolve it manually rather than forcing the automated pass through.
6. When no reliable tool exists for the language or change, such as a cross-file rename in a dynamically-typed language with weak tooling, fall back to a manual small-safe-steps refactor rather than trusting a fragile automated pass.

## Decision rules
- Prefer the automated tool whenever it exists and the codebase's type or build setup lets it operate correctly — the project actually compiles or type-checks, so the tool has accurate information.
- Distrust automated renames or moves across string-based references — reflection, dependency-injection container names, serialized field names, dynamic imports — and grep for these separately even after an automated pass.
- In a dynamically-typed or loosely-typed codebase, treat automated "safe" refactors as a starting point, not a guarantee, since the tool's static analysis has weaker information to work with.
- Chain multiple automated refactor commands, such as extract then rename, as separate tool invocations you can inspect individually, rather than trusting one large multi-step automated operation blindly.

## Anti-patterns
- Doing a project-wide rename via text search-and-replace when the IDE or LSP has a proper semantic rename available, risking matches inside unrelated identifiers or comments.
- Trusting an automated refactor's output without running tests, on the assumption that "the tool guarantees correctness."
- Running an automated refactor on code that doesn't currently compile or type-check, where the tool's analysis is unreliable by definition.
- Ignoring the tool's own warnings or conflict dialogs and force-applying a refactor it flagged as ambiguous.

## Exceptions and trade-offs
- For a codebase without solid tooling — a weakly-typed language, no LSP support, a legacy IDE — the safety benefit of automation disappears; spend the effort on small manual steps and strong test coverage instead.
- Automated tools sometimes produce a mechanically-correct but stylistically poor result, such as an extracted method with an awkward generated name; it's fine to follow up with a manual cleanup pass as long as that pass is itself verified.

## Verification
- Confirm the automated tool's diff matches the intended change exactly, with no unrelated files touched and no unintended matches.
- Confirm the test suite passes after the automated change, not assumed passing because the tool is "safe."
- Grep separately for string-based or reflective references to the changed symbol that semantic tools cannot see, and update them by hand if found.
