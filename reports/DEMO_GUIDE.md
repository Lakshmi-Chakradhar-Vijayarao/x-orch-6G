# Demo Guide: X-ORCH-6G

This guide explains how to run demonstrations of X-ORCH-6G and interpret
their outputs.

The demos are designed for **understanding system behavior**, not for
benchmarking performance.

---

## 1. Quick Demo

Runs a short MARL episode with stress enabled.

```bash
python demos/demo_quick.py
Purpose:

Verify environment setup

Observe basic orchestration behavior

Confirm reproducibility

## 2. Full Demo

Runs a longer experiment with logging and metrics.

python demos/demo_full.py


Purpose:

Observe recovery under stress

Inspect stability metrics

Generate plots for analysis

3. What to Watch For

During demos, pay attention to:

Action switching frequency

NO_OP usage under stress

Latency spikes and recovery

SLA violation patterns

These behaviors illustrate why abstention and governance are necessary.

4. What the Demo Is Not

Not a real deployment

Not a performance showcase

Not tuned for maximum reward

The demo exists to surface system dynamics, not hide them.


---
