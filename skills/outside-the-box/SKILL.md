---
name: outside-the-box
description: Generate and test alternatives with different underlying mechanisms when the user asks for unconventional ideas, lateral thinking, or help with a problem where conventional approaches have failed.
metadata:
  version: "2.1.0"
---

# OUTBOX Protocol

Find a useful alternative by challenging assumptions, then compare it with the strongest conventional solution. Novelty earns consideration, not preference.

Use this for open-ended problems that need a different approach. A routine implementation, factual lookup, or request for standard practice does not need this workflow.

## Frame the problem

State the desired outcome, the conventional approach, and what has already failed. Separate the user's goal from the proposed mechanism without substituting a different goal.

Classify constraints using evidence:

- **Hard:** explicit requirements, budget limits, deadlines, or physical constraints.
- **Negotiable:** preferences the user has indicated can change.
- **Assumed:** restrictions introduced by the agent or inherited from the usual solution.

Treat an explicit requirement as binding unless the user agrees to change it. An interesting alternative that violates it can be mentioned as conditional, but cannot be the recommended solution.

## Generate alternatives

Temporarily set aside the baseline mechanism during ideation. Keep the baseline for the final comparison.

For a quick request, aim for three distinct mechanisms. For a substantial investigation, explore five or more using the [operator table and templates](references/operators.md). Useful starting moves are subtraction, inversion, upstream changes, and an analogy from another domain.

Include a way to change the mechanism and, where plausible, a way to remove the need for the problem. Do not force an irrelevant analogy to meet a quota. Explain the causal mechanism behind an analogy rather than borrowing its vocabulary.

For each candidate, identify:

- What changes and which assumption it challenges.
- Why it could work and what evidence is missing.
- The main cost, dependency, or failure mode.

Merge ideas that are the same mechanism with different labels. Do not claim branches are independent agents unless separate agents actually ran.

## Prove the idea left the box

For each serious candidate, write one compact comparison against the baseline:

> We normally [mechanism] because we assume [premise]. This option instead [different mechanism]. It works only if [condition]. We can check that by [observation].

Use the original OUTBOX search radius to distinguish distance from value:

| Radius | What changed |
|---|---|
| R0 | The baseline got better |
| R1 | A different tactic uses the same mechanism |
| R2 | A different mechanism produces the outcome |
| R3 | The need for the original task changes or disappears |

Seek an R2 and an R3 when the brief allows them. If neither survives the constraints, say what prevented the move. Never relabel an R1 idea to make the set look more creative.

Run a substitution check. Replace the tool or vendor names in two ideas with neutral nouns. If the same causal explanation now describes both, merge them. For the surviving alternatives, identify the observation that would favor one over the other. An experiment should help choose between mechanisms, not merely show that one prototype can run.

Example: a slow report can be accelerated by query tuning (R0), served from a precomputed snapshot (R2), or replaced with exception alerts when users only need to know what changed (R3). Alerts are conditional on that user need; they cannot replace an explicitly required full report. The distinguishing check is whether users need arbitrary full-history queries or only exceptions. Measure that need before replacing the report.

## Compare and choose

Compare the baseline and alternatives against the user's success criteria. Consider expected benefit, feasibility, effort, and reversibility. Distinguish evidence from estimates; avoid numeric scores without a meaningful scale.

Discard ideas that violate hard constraints or are worse than the baseline without a compensating benefit. A conventional winner is a valid result. Recommend one option and explain the tradeoff; include a bolder alternative only when it is useful.

For the recommendation, provide the cheapest informative test, an observable success signal, a stop condition, and the next step. Do not invent performance numbers. Define proposed thresholds as proposals.

## Optional independent perspectives

If available and authorized, delegate bounded perspectives such as conventional optimizer, simplifier, and cross-domain analyst. Give each the same goal and constraints, and collect proposals before sharing critiques. Use actual host capabilities; this skill does not require another skill or a named orchestration tool. With no delegation, do the comparison locally and describe it accurately.

## Delivery check

The reader should be able to identify the baseline, the different mechanisms, the binding constraints, the recommended option, and a test that could disprove it. Scale the answer to the request; do not dump the working templates into a short answer.

## Credits

OUTBOX builds on lateral-thinking methods, including TRIZ and bisociation. Its workflow compares different mechanisms and asks for a test that can distinguish them.
