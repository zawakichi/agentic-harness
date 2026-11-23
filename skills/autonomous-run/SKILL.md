---
name: autonomous-run
description: Execute coding tasks autonomously, using acceptance criteria and verification to continue until complete or genuinely blocked.
---

# Autonomous run

Use this workflow when the user requests autonomous execution or a task that should be carried through to completion.

1. Read applicable repository instructions, inspect the current state, and identify the intended outcome. Preserve unrelated changes.
2. Form concrete acceptance criteria and a verification strategy. Make reasonable, reversible decisions without interrupting the user. Request essential missing information early and continue independent work.
3. Implement in small steps. Run relevant checks, inspect failures, and fix them. Keep working while meaningful progress is possible.
4. Verify the acceptance criteria with evidence. Report the changes, checks, and any remaining blockers accurately. Do not claim completion when verification fails or required work remains.

Respect user instructions, runtime permissions, approval requirements, and external effects. This skill does not grant permissions, schedule work, or guarantee autonomous execution when a host stops a session.
