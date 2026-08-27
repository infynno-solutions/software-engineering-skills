---
name: use-compiler-and-static-feedback
description: "Treats compiler, type-checker, and lint diagnostics as routine engineering feedback. Use before opening a review, running the type checker and linter locally rather than letting CI catch it first, and when deciding whether to add a suppression comment such as ts-ignore, noqa, or nolint versus fixing the underlying issue or configuring the rule properly. Not for invariants the toolchain cannot express - untrusted input, runtime state machines, cross-service contracts (see apply-defensive-programming) - and not for selecting and rolling out analysis tooling across a team (see use-static-analysis-in-the-core-workflow)."
license: MIT
---

# Use Compiler and Static Feedback

## Intent

Use compiler diagnostics, type checking, linters, static analysis, and automated code-quality checks as part of the normal development loop rather than as optional cleanup.

## Procedure

1. Run the repository's standard compiler/type checks and static analysis.
2. Treat diagnostics as engineering evidence, not noise.
3. Fix clear correctness issues before moving on.
4. Distinguish genuine issues from configured exceptions using repository policy.
5. Avoid weakening or bypassing checks to make a change pass unless the rule is demonstrably inappropriate and the repository process permits changing it.

## Decision rules

- Prefer machine-detectable correctness checks over relying on human memory.
- Keep static-analysis feedback integrated into the development workflow.
- Do not blindly obey every warning if the repository has an explicit, justified exception mechanism.
- Improve tooling when repeated human review effort can be made deterministic and reliable.

## Anti-patterns

- Disabling a lint or compiler check simply because it is inconvenient.
- Ignoring warnings until release.
- Flooding developers with low-value static-analysis findings.
- Treating tool output as more authoritative than the actual project contract when the rule is misconfigured.

## Exceptions and trade-offs

- A rule that produces many false positives against the repo's actual patterns is a case for fixing or disabling that specific rule through the project's exception mechanism, not for ignoring all static feedback.
- Early-stage prototypes or throwaway scripts may reasonably run with relaxed strictness; tighten it once the code is heading to production.
- Migrating an existing codebase to stricter settings (enabling a `strict` type-checking mode) is often a staged effort — don't block an unrelated fix on resolving every pre-existing warning.

## Verification

- Do standard checks pass?
- Were new warnings introduced?
- Are exceptions explicit and justified?
- Did automation catch issues that would otherwise depend on reviewer attention?
