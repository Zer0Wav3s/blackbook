# Divergence operators and working templates

Use these when the main workflow needs more ways to generate or test alternatives. Pick operators that challenge different assumptions.

| Operator | What It Changes | Prompt |
|----------|----------------|--------|
| **Inversion** | Flips the problem | "How would I *guarantee* the worst outcome? Now invert." |
| **Cross-Domain Analogy** | Imports from other fields | "Who solves this in biology / logistics / games / insurance?" |
| **Constraint Elimination** | Removes a restriction | "Which constraint is phantom? What's possible without it?" |
| **Subtraction** | Removes components | "What can be eliminated so the problem disappears?" |
| **Boundary Shift** | Moves the system edge | "Can this be solved upstream/downstream, outside the system?" |
| **Perspective Swap** | Changes viewpoint | "How would a beginner / adversary / end-user see this?" |
| **Scale Distortion** | Changes magnitude | "What works at 1000x? At 1/1000th? Infinite budget? Zero?" |
| **Sequence Reversal** | Changes order | "What if we did step 4 first?" |
| **Mechanism-Class Shift** | Changes solution type | "Could process / incentives / policy / defaults solve this instead?" |
| **Contrarianism** | Opposes conventional wisdom | "What's the strongest case the standard advice is wrong?" |
| **TRIZ Separation** | Resolves contradictions | "Separate in time / space / condition / scale" |
| **Bisociation** | Connects distant domains | "What's the core mechanism? Where else does it exist?" |


## Working templates

### Assumption Audit
```
Assumption: ...
Why it might be false: ...
If false, what changes: ...
Quick test: ...
```

### TRIZ Contradiction Template
```
We want to improve: ...
But it worsens: ...
Separation attempt:
  - in time: ...
  - in space: ...
  - by condition: ...
  - by scale: ...
IFR: "The system delivers ... while ... costs approach zero."
```

### Bisociation Template
```
Core mechanism we need: ...
Distant domains to consult: ...
Candidate analogies:
  - Domain → mechanism → mapping
Implementable translation: ...
```

---
