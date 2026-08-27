---
name: document-decisions-and-system-context
description: "Records rationale, constraints, interfaces, and operational context where future engineers would otherwise need tribal knowledge. Use when making an architecture decision with real alternatives such as choosing a datastore or reversing a prior approach, writing a runbook for an on-call scenario, or documenting why a non-obvious workaround exists. Not for process-rule rationale (see revisit-process-rules-using-evidence), usage docs for an internal tool (see treat-tooling-as-an-engineering-product), in-code context (see use-comments-for-missing-context), or building the team's discoverability system (see build-knowledge-sharing-systems)."
license: MIT
---

# Document Decisions and System Context

## Intent
Record rationale, constraints, interfaces, and operational context where future engineers would otherwise need tribal knowledge.

## Procedure
1. Identify decisions that are non-obvious from reading the code alone — the chosen alternative, the rejected ones, and why.
2. Write an ADR (or equivalent) at decision time, not retroactively: context, decision, consequences, alternatives considered.
3. Keep system-context docs (README, architecture diagram, runbook) next to the code they describe, not in a wiki that drifts out of sync.
4. Record operational knowledge that would otherwise require paging someone: how to deploy, how to roll back, what alerts mean, known failure modes.
5. Link decisions to their consequences: when a later change contradicts or supersedes a prior ADR, mark the old one superseded rather than deleting it.
6. Review docs for staleness whenever the described system changes materially.

## Decision rules
- Document a decision if a reasonable engineer joining later would ask "why was it done this way?" and the code/tests don't answer it.
- Prefer a short ADR for a single bounded decision; use a fuller design doc when multiple interacting decisions are involved.
- Operational runbook content belongs where the on-call engineer will actually look during an incident, not buried in a design doc.
- Update or supersede a doc once its recommendation stops matching reality; a wrong doc is worse than no doc.

## Anti-patterns
- Writing extensive documentation for self-evident code instead of the actual non-obvious rationale.
- Letting the "why" live only in a closed PR discussion, chat thread, or someone's memory.
- Documentation that describes the intended system rather than the one that actually shipped.
- One giant wiki page trying to cover architecture, runbook, and decisions at once, so nothing in it stays current.

## Exceptions and trade-offs
- Exploratory or throwaway spikes don't need ADR-level rigor; document only if the outcome will inform a later real decision.
- Small, easily reversible decisions don't warrant a decision record.
- Documentation effort should scale with team size and expected system lifetime — a short-lived internal script needs far less than a shared platform.

## Verification
- A new team member can answer "why is it built this way" for major decisions using the docs alone.
- Runbook steps have actually been executed, or dry-run, by someone other than the author.
- Superseded decisions are marked as such, not left presented as current.
