# 📄 `reports/EXPLAINABILITY.md`

```markdown
# Explainability in X-ORCH-6G

Explainability in X-ORCH-6G is **architectural**, not cosmetic.

The system is designed to be interpretable by construction.

---

## 1. Design Philosophy

Explainability is used to:
- Audit decisions
- Understand uncertainty
- Diagnose instability

Explainability is **never** used to control actions.

---

## 2. Interpretable State Design

All agent observations are:
- Fixed-size
- Engineered
- Human-readable

No learned embeddings or opaque representations are used.

---

## 3. Policy Traces

Each decision can be traced as:



State → Action → Reward Components → Outcome


This enables:
- Post-hoc auditing
- Failure analysis
- Governance inspection

---

## 4. Counterfactual Reasoning

Counterfactuals answer questions such as:
- Would migration occur if latency increased?
- Would abstention trigger if failure persisted longer?

These analyses support **decision legitimacy**, not justification.

---

## 5. Optional LLM Usage

LLMs may be used:
- Post-hoc
- Read-only
- For human interpretation

LLMs have **zero authority** over control decisions.

This separation aligns with governance best practices.
