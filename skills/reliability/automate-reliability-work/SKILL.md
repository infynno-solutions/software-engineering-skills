---
name: automate-reliability-work
description: "Turns manual operational procedures that must be executed correctly under stress into tested, repeatable automation. Use when a runbook is prose steps a human copies commands from, when a deploy, rollback, failover, backup/restore, or key rotation is performed by hand more than once, or when an incident retro finds the fix was someone running a script from their laptop. Not for the failure-handling logic itself - timeouts, retries, circuit breaking (see use-timeouts-and-deadlines, make-retries-safe-and-bounded, isolate-failures-and-limit-blast-radius) - and not for delivery pipelines generally (see automate-quality-gates-and-delivery)."
license: MIT
---

# Automate Reliability Work

## Intent
Turn manual operational procedures that must be executed correctly under stress into tested, repeatable automation, so correctness does not depend on an operator remembering the right steps at 3am.

## Procedure
1. Inventory the manual steps currently required to perform the operation (deploy, failover, restore, rotate, scale) and note which ones are order-dependent or easy to skip.
2. Identify which steps are read-only checks (safe to script freely) versus state-changing actions (need guardrails: dry-run mode, confirmation, idempotency).
3. Encode the procedure as a script, pipeline job, or tool invocation that takes explicit inputs (target environment, version, resource IDs) rather than relying on operator memory or shell history.
4. Add a dry-run or plan-only mode when the action is destructive or hard to reverse (schema migration, mass deletion, failover).
5. Wire the automation into the same path used during incidents — do not let the automated version and the "break glass" manual version diverge.
6. Rehearse the automation in a non-production environment or game day before trusting it in a real incident.

## Decision rules
- Automate first the operations that are both frequent and error-prone (deploy, rollback, cache flush) before rare-but-catastrophic ones (full region failover) — but do not skip the rare ones, since that is exactly when human error is costliest.
- If a step requires judgment (deciding *whether* to fail over), automate the mechanics and leave the decision to a human with the data surfaced; don't hide a judgment call inside a fully automatic action unless the blast radius of a wrong call is small.
- Prefer a single automated path over "automated happy path + manual escape hatch that nobody tests" — an escape hatch that isn't rehearsed is not a reliable fallback.
- When automation itself can fail (network partition during automated failover), design it to fail toward a safe, observable state, not silently retry forever.

## Anti-patterns
- A wiki page of shell commands labeled "runbook" that has never been executed end-to-end outside a real incident.
- Automation that only works on the author's machine because it depends on local credentials, aliases, or uncommitted scripts.
- Scripts that mutate production state with no dry-run, no confirmation, and no audit trail of what was run and by whom.
- Automating the common case but leaving the rollback/undo path manual, so recovery is slower and riskier than the original mistake.

## Exceptions and trade-offs
- For genuinely one-off migrations, full automation may not be worth building — but still script the mechanical parts and keep a written, reviewed procedure for the rest.
- Over-automating novel or ambiguous incidents can remove the human judgment needed to handle a situation the automation wasn't designed for; keep manual override paths for out-of-band cases.
- Automation adds a new artifact that itself needs maintenance and testing — weigh that ongoing cost against the frequency and risk of the manual task it replaces.

## Verification
- Confirm the automation has been executed successfully at least once outside a real incident (staging, game day, or scheduled DR drill).
- Confirm state-changing automation has a dry-run/plan mode and that destructive actions require an explicit, hard-to-fumble confirmation.
- Confirm the automated path and the incident-response path are the same script/tool, not two versions that can drift apart.
- Confirm failures of the automation itself are visible (logged, alerted) rather than silently swallowed.
