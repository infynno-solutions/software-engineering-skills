---
name: automate-quality-gates-and-delivery
description: "Turns repeatable verification and release steps into unattended, enforced gates. Use when adding a new required CI check, building or changing a release pipeline, replacing a manual pre-merge checklist or Slack sign-off with a script, or setting up branch protection rules. Not for how reviewers give feedback on a PR (see conduct-effective-code-reviews), deciding which checks run early versus late for latency reasons (see optimize-for-fast-feedback), or re-justifying a rule that already exists (see revisit-process-rules-using-evidence)."
license: MIT
---

# Automate Quality Gates and Delivery

## Intent
Automate repeatable verification and release steps so delivery relies less on manual memory and intervention.

## Procedure
1. Enumerate every manual step currently performed before merge or release (checklist items, Slack sign-offs, "ask X to eyeball this").
2. For each step, decide whether it can be expressed as a scripted, deterministic check (exit code 0/1) or whether it genuinely requires human judgment.
3. Wire deterministic checks into the pipeline as blocking gates tied to merge/release, not advisory jobs someone can ignore.
4. Give each gate a single clear failure output (what failed, why, how to reproduce locally) so failures are self-service.
5. Version and roll out the pipeline definition itself like code (PR review, staged rollout of new gates) so a bad gate doesn't lock out the whole team at once.
6. Instrument gates: track pass/fail rate, run time, and false-positive rate so a broken gate can be distinguished from a real regression.
7. Automate the release mechanics that follow a green pipeline — version bump, changelog, artifact publish, deploy — rather than leaving them as manual runbook steps.

## Decision rules
- A check a human currently performs from memory before every merge/release is a candidate for gate automation.
- A gate must fail deterministically and reproducibly; if two people can run it and get different answers, fix the gate before making it blocking.
- New gates should land non-blocking/warn-only first, then flip to blocking once teams have had a chance to fix pre-existing violations.
- Normal (non-incident) releases should run unattended end-to-end; a human should intervene only by exception.

## Anti-patterns
- Adding a new blocking gate with no grace period, breaking every open PR at once.
- Gates that are advisory in output but treated as blocking "by convention" with no enforcement.
- A release process only one person knows how to run by hand.
- Gating on flaky checks, which trains people to re-run until green instead of trusting the gate.

## Exceptions and trade-offs
- Judgment calls that require domain knowledge (e.g., "is this UX change acceptable") should stay manual review steps, not be forced into automated gates.
- Emergency hotfix paths may need an explicit, audited bypass distinct from routinely skipping gates.
- Very early-stage or throwaway projects may not yet warrant the investment in full gate automation.

## Verification
- Each blocking gate can be reproduced locally with the same result as CI.
- A deliberately broken change is actually blocked by the gate, not just flagged.
- The release path has been exercised end-to-end (e.g., staging or dry-run) since its last change.
- Gate run time is checked against the team's feedback-latency budget.
