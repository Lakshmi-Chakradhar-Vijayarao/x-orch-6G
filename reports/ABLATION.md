# Ablation Studies

This document describes the ablation studies conducted in X-ORCH-6G to isolate
the impact of key system design choices.

The goal of these ablations is **not performance maximization**, but to
understand **stability, safety, and decision legitimacy** in autonomous
orchestration.

All results are reproducible and generated from real system executions.

---

## 1. NO_OP (Abstention) Ablation

### Configuration
Two configurations were compared:

1. **NO_OP Enabled**  
   Agents are allowed to abstain when uncertainty is high.

2. **NO_OP Disabled**  
   Agents must always select an active orchestration action.

### Observations
- Disabling NO_OP leads to increased action switching.
- Oscillatory behavior emerges under dynamic load.
- SLA violations increase due to aggressive reactions.

### Interpretation
The NO_OP action functions as a **first-class stability primitive**, not as a
training convenience. Explicit abstention reduces oscillations and prevents
control thrashing under uncertainty.

---

## 2. Governance Ablation

### Configuration
- **No Governance**: Actions executed as proposed by MARL agents.
- **Governance Enabled**: Risk-aware gate constrains actions under uncertainty.

### Observations
- Governance does **not** accelerate recovery.
- Governance reduces unsafe actions during stress.
- SLA violations are less volatile under governance.

### Interpretation
Governance improves **decision legitimacy and safety**, not raw performance.
This mirrors real infrastructure systems, where policy cannot override physical
recovery limits.

---

## 3. Stability Bonus Ablation

### Configuration
- Stability-aware reward term enabled vs disabled.

### Observations
- Without stability penalties, agents oscillate more frequently.
- With stability terms, policies converge to conservative behavior.

### Interpretation
Explicit stability incentives are necessary in distributed control systems.
Reward-only optimization is insufficient for safe orchestration.

---

## Summary

| Ablation Component | Effect Observed |
|-------------------|-----------------|
| NO_OP             | Reduces oscillations |
| Governance        | Improves safety |
| Stability Bonus   | Improves convergence |

These ablations support the core thesis of X-ORCH-6G:
**stability-aware orchestration requires explicit design mechanisms.**
