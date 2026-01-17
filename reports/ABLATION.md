# Ablation Study: NO_OP Action

This ablation evaluates the role of the NO_OP (abstention) action.

---

## Experimental Setup

Two configurations were tested:
1. NO_OP enabled
2. NO_OP disabled

All other parameters were identical.

---

## Observations

With NO_OP enabled:
- Higher no-op ratios
- Controlled switch rates
- Lower oscillatory behavior

Without NO_OP:
- Increased action entropy
- Higher switching frequency
- Reduced stability under load

---

## Conclusion

NO_OP is a **first-class stabilizing action**, not a convenience.
Its removal degrades policy stability even when reward appears similar.

This validates abstention as a necessary design choice.
