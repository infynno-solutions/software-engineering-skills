# Software Engineering Best-Practice Skills

A collection of reusable software-engineering skills for AI coding agents.

This repository contains 141 agent-oriented skills synthesized into 12 engineering categories. The skills are written as operational guidance: when to apply a practice, how to reason about it, decision rules, anti-patterns, trade-offs, and verification criteria.

## Repository layout

```text
skills/
  <category>/
    <skill-name>/
      SKILL.md
```

Each published skill has exactly one `SKILL.md` entrypoint. Skill names are lowercase kebab-case and match their containing directory.

## Categories

- `engineering-thinking` — 10 skills
- `code-construction` — 15 skills
- `object-oriented-design` — 11 skills
- `design-principles-and-modularity` — 13 skills
- `design-patterns` — 12 skills
- `refactoring` — 12 skills
- `architecture` — 12 skills
- `testing` — 11 skills
- `reliability` — 11 skills
- `data-and-distributed-systems` — 12 skills
- `engineering-process-and-delivery` — 12 skills
- `technical-leadership` — 10 skills

## Installation

Install the complete collection with the skills CLI:

```bash
npx skills add <owner>/software-engineering-skills
```

Install selected skills:

```bash
npx skills add <owner>/software-engineering-skills --skill frame-the-problem
```

For a large repository, installing an exact skill path is also supported.

## Validation

Run the local validator:

```bash
python3 scripts/validate-skills.py
```

Before publishing a GitHub release, validate against the Agent Skills publishing checks:

```bash
gh skill publish --dry-run
```

Then publish a versioned release with:

```bash
gh skill publish --tag v1.0.0
```

## Design principles

- Prefer engineering behaviors over named concepts.
- Prefer decision rules over slogans.
- Avoid unconditional `always` / `never` advice unless justified by context.
- Preserve trade-offs and exceptions.
- Separate diagnosis, design, execution, and verification where useful.
- Keep each skill focused on one reusable engineering capability.

## Notes

This repository intentionally does not embed book citations or source-provenance sections in the runtime skills. The skill files are optimized for direct agent consumption.
