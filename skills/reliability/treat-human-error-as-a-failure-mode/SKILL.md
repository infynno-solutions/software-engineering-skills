---
name: treat-human-error-as-a-failure-mode
description: "Designs dangerous operator actions and tools assuming a human will eventually make a mistake using them, by constraining the action and building recovery paths for when it happens. Use when a CLI command, admin panel action, or script can delete, overwrite, or mass-modify production data with operator care as its only safeguard; when a production action has no undo, no blast-radius-scaled confirmation, and no distinction between a scoped and a wildcard target; or when a postmortem root cause is a mistyped argument or the wrong environment. Not for replacing manual steps with tooling (see automate-reliability-work) or adding operator controls generally (see make-systems-operable)."
license: MIT
---

# Treat Human Error as a Failure Mode

## Intent
Design dangerous operator actions and tools assuming a human will eventually make a mistake using them, by constraining the action, and by building recovery paths for when the mistake happens anyway — rather than relying solely on operator care and training.

## Procedure
1. Identify actions where a single human mistake (wrong argument, wrong environment, wrong target, fat-fingered command) causes disproportionate damage — deletion, mass update, permission change, irreversible migration.
2. For each, add friction proportional to blast radius: require explicit confirmation that echoes back what will be affected (not a generic "are you sure?"), require naming the target explicitly rather than accepting a wildcard/empty filter by default, and make the scariest actions require a second reviewer or a two-step confirm.
3. Make the default behavior of ambiguous or missing arguments safe — a missing filter should mean "operate on nothing," never "operate on everything."
4. Build a recovery path for when the mistake happens anyway: soft-delete with a grace period, versioned/reversible changes, point-in-time restore — matched to how catastrophic and how frequent the mistake plausibly is.
5. After any incident whose root cause is an operator mistake, ask "what would have prevented this specific slip" and fix the tool/constraint, not only the person's process — the same slip will recur under time pressure otherwise.

## Decision rules
- Scale confirmation friction to blast radius: a single-resource, reversible action needs little friction; a bulk, irreversible, cross-tenant action needs an explicit target list echoed back and possibly a second approver.
- Default to the safe interpretation of ambiguous input — an empty/missing filter argument should be rejected or scoped to nothing, never silently interpreted as "all rows"/"all resources."
- Prefer reversible-by-default actions (soft delete, versioned config, snapshot before mutate) for anything destructive, so a mistake is a recoverable incident rather than a permanent loss.
- When the same dangerous manual action is performed repeatedly, replace it with a narrower, purpose-built tool that can't express the dangerous general case — a scoped tool is safer than a general one used carefully.

## Anti-patterns
- A delete/update command whose filter argument defaults to "match everything" when omitted, so a missing `--where` clause wipes an entire table.
- A "type yes to confirm" prompt that doesn't show what will actually be affected, so the operator confirms blind and the confirmation step provides no real safety.
- Blaming the individual in a postmortem ("should have double-checked") without also changing the tool or process that let one keystroke cause irreversible damage.
- Giving broad, unscoped production access as the default for routine tasks that only ever need a narrow permission, increasing the blast radius of any single mistake.

## Exceptions and trade-offs
- Excess friction on routine, low-risk actions slows operators down and encourages workarounds that bypass the safeguard entirely (e.g., scripting around a confirmation prompt); reserve heavy friction for genuinely high-blast-radius actions.
- Reversibility (soft delete, snapshots) has a real storage/complexity cost and sometimes conflicts with requirements like GDPR-style hard deletion — those constraints need explicit handling, not a blanket "always reversible" rule.
- Requiring a second approver for dangerous actions adds latency that's unacceptable during a live incident; consider a break-glass path with after-the-fact audit for genuine emergencies rather than removing the safeguard outright.

## Verification
- Confirm every action capable of large-scale or irreversible damage requires explicit, scoped confirmation that reflects the actual target, not a generic prompt.
- Confirm ambiguous or missing filter/target arguments fail safe (affect nothing / require explicit input) rather than defaulting to the broadest scope.
- Confirm a recovery mechanism exists and has been tested for the most damaging plausible mistake (accidental bulk delete, wrong-environment run).
- Confirm postmortems with a human-error root cause produced a tool or constraint change, not solely a process/training action item.
