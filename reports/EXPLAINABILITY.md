# Explainability Analysis

X-ORCH-6G integrates explainability as a diagnostic layer, not a control mechanism.

---

## Feature Attribution

Permutation importance reveals that:
- Load-related features dominate decisions
- Time-dependent features influence scaling actions

This confirms that policies respond to meaningful system variables.

---

## Counterfactual Reasoning

Example:
- Increasing CPU load by +20% causes action flip from SCALE_UP to MIGRATE

This demonstrates causal sensitivity rather than memorization.

---

## Policy Tracing

Each decision can be traced as:
State → Action → Reward Components → Outcome

This enables full auditability of orchestration behavior.
