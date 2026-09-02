---
name: recognize-code-smells
description: "Names structural code smells - Long Method, Feature Envy, Shotgun Surgery - with concrete evidence, then decides whether deeper work is warranted. Use during code review, when triaging a legacy module before changing it, or when picking where to start a refactoring pass. This skill stops at diagnosis: hand off to extract-and-recompose-responsibilities, simplify-conditionals-and-control-flow, or remove-duplication-with-care to actually treat the smell."
license: MIT
---

# Recognize Code Smells

## Intent
Identify structural symptoms that make code harder to understand, test, or change, and use them as triggers for deeper investigation rather than automatic refactoring targets.

## Procedure
1. Scan the unit under review against a working checklist of named smells: Long Method, Large Class, Long Parameter List, Feature Envy, Data Clumps, Primitive Obsession, type-code switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man.
2. For each smell found, name it explicitly and point to concrete evidence — e.g., "Feature Envy: `computeTax` reads five fields off `order` and none of its own class's state."
3. Check whether the smell is actually costing something now — has it caused a bug, slowed a recent change, or made the current task harder — versus being merely cosmetic.
4. Rank the smells that intersect with the current task; note the rest without acting on them.
5. Hand off ranked, evidenced smells to the appropriate targeted refactoring skill rather than fixing everything found at once.

## Decision rules
- A smell is a prompt to investigate, not a mandate to refactor — escalate only smells that intersect with the current change or demonstrably increase risk or cost.
- Prefer smells with concrete, recent evidence, such as a bug it caused or a PR forced to touch many files, over smells that are merely aesthetically displeasing.
- Distinguish "this class is large" from "this class has low cohesion" — size alone is not a smell if the class is genuinely cohesive, such as a generated parser.
- When a smell is pervasive across a legacy codebase, flag it once as a systemic issue rather than as an action item for every file.

## Anti-patterns
- Filing a refactoring ticket for every long method in a codebase without checking whether any of them are actually being changed or causing problems.
- Treating "smell" as synonymous with "bug" or "must fix before merge" in code review, blocking unrelated work over cosmetic structure.
- Missing smells that lack snappy names, such as unclear temporal coupling between two calls, because a checklist mentality replaces actually reading the code.
- Naming a smell to justify a refactor the reviewer already wanted to do, rather than genuinely evidencing it.

## Exceptions and trade-offs
- Generated code, vendored code, or code slated for imminent deletion can carry smells that are correctly left alone.
- A smell in code not being touched and not on the current task's critical path is worth noting, perhaps as a follow-up ticket, but not worth blocking the current change.

## Verification
- Confirm each flagged smell cites specific code — file and function — not a vague impression.
- Confirm each flagged smell is connected to an actual or plausible cost — bug risk, change cost, test difficulty — rather than a style preference.
- Confirm the diagnosis stops short of prescribing a specific refactor; that decision belongs to the targeted skill.
