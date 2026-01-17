# Experimental Results

This document summarizes the empirical results obtained from the X-ORCH-6G simulator.

All numerical results are generated reproducibly and stored under `results/`.

---

## 1. Baseline Performance

Baseline heuristics were evaluated under identical environment settings.

**Observations:**
- High variance across episodes
- No stability guarantees
- No awareness of long-term system health

Baseline rewards consistently ranged between **-550 to -610**, indicating inefficient orchestration under dynamic workloads.

---

## 2. Single-Agent PPO Performance

A single PPO agent controlling orchestration decisions was trained for comparison.

**Key Results:**
- Mean reward improved to approximately **-503**
- Reduced variance compared to baselines
- Still susceptible to oscillatory behavior

This demonstrates that learning-based control improves performance but does not fully address stability.

---

## 3. Multi-Agent Reinforcement Learning (MARL)

Independent PPO agents were trained to control orchestration decisions.

**Key Observations:**
- Comparable reward to single-agent PPO
- No catastrophic collapse under multi-agent contention
- Stability metrics reveal controlled but non-trivial switching behavior

MARL performance confirms that decentralized learning is viable under bounded orchestration constraints.

---

## 4. Summary

| Method      | Mean Reward | Stability Awareness |
|------------|------------|---------------------|
| Baselines  | Poor       | None                |
| PPO        | Moderate   | Partial             |
| MARL       | Moderate   | Explicitly Measured |

The results support the thesis that **stability-aware orchestration is as important as raw reward optimization**.
