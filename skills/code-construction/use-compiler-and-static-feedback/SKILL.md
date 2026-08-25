---
name: use-compiler-and-static-feedback
description: Use compiler diagnostics, type checking, linters, static analysis, and automated code-quality checks as part of the normal development loop rather than as optional cleanup. Use when the engineering task, code review, design change, refactoring, incident, or implementation materially involves this concern.
---

# Use Compiler and Static Feedback

## Intent

Use compiler diagnostics, type checking, linters, static analysis, and automated code-quality checks as part of the normal development loop rather than as optional cleanup.

## Apply when

Use this skill whenever modifying typed or statically analyzed code and whenever repository tooling provides automated feedback.

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

## Verification

- Do standard checks pass?
- Were new warnings introduced?
- Are exceptions explicit and justified?
- Did automation catch issues that would otherwise depend on reviewer attention?


## Related skills

- CODE-13 Apply Defensive Programming
- PROC-06 Use Static Analysis
- TEST-06 Create Fast Feedback Loops
