---
name: autonomous-run
description: Pursue coding and engineering tasks autonomously with quality-driven decisions, preserved contracts, understandable outcomes, and independent verification.
---

# Autonomous run

Pursue the user's intended outcome within the host's instructions, permissions, and approval policy. Choose the approach and level of process appropriate to the task; these are objectives, not mandatory sequential stages or required artifacts.

- Understand the relevant existing behavior, intended outcome, acceptance criteria, constraints, and applicable functional contracts before changing them; preserve unrelated changes. Preserve preconditions, invariants, normal and failure postconditions unless a change is authorized. Do not treat invalid external input as an impossible precondition when it must be handled.
- Identify the authoritative source for each affected requirement or contract. Update that source when its meaning changes; link to it rather than creating a competing copy. Distinguish observed behavior from intended specification.
- Let quality attributes, risk, and lifecycle cost guide decisions. Explain consequential alternatives and tradeoffs, including how a person can understand the behavior, rationale, residual risks, and evidence. Use QAW, ADD, ATAM, CBAM, threat modeling, or formal methods selectively when useful; a lightweight analysis is not a full formal method.
- Make reversible, low-risk decisions autonomously and continue useful independent work when information is missing. Honor explicit authorization and platform security boundaries; do not infer access from this skill. Escalate only when necessary under the governing instructions.
- Verify against acceptance criteria and existing authoritative contracts, preferably using independent checks or independently maintained acceptance evidence. Do not weaken criteria, tests, permissions, or validation merely to pass. If a legitimate change requires changing a criterion, explain it and retain appropriate independent evidence. Report failures and limitations honestly.
- Report the outcome, important decisions, verification evidence, and unresolved risks in terms the responsible human can understand. Reassess whether harness instructions and components add measurable value as models and environments change.

Optional references when useful: [functional contract](references/functional-contract.md), [quality attribute scenario](references/quality-attribute.md), [architecture decision](references/architecture-decision.md), and [harness evaluation](references/harness-evaluation.md). Existing project sources take precedence; templates do not become new sources of truth unless explicitly adopted.
