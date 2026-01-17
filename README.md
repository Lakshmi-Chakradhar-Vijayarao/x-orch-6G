
# **X-ORCH-6G**

## **Uncertainty-Aware, Explainable, and Governance-Driven Orchestration for 6G Compute Continuums**

---

## 📌 Overview

**X-ORCH-6G** is a **system-level research simulator** for studying **autonomous orchestration under uncertainty** in future **6G cloud–edge–far-edge compute continuums**.

Unlike most AI-driven orchestration systems that focus solely on optimization, this project explicitly investigates:

> **When an autonomous system should abstain from acting instead of making risky decisions.**

The system integrates **multi-agent reinforcement learning (MARL)** with **stability control, uncertainty awareness, failure modeling, explainability, and governance**, while remaining:

* fully reproducible,
* CPU-only,
* interpretable by design,
* and suitable for PhD-level research and evaluation.

This repository is **not a demo** and **not a product**.
It is a **research platform** for studying decision legitimacy and safety in autonomous networked systems.

---

## 🎯 Core Research Question

> **How can an autonomous orchestration system detect when its learned policy is operating outside its reliable knowledge regime, and enforce safe abstention instead of aggressive optimization?**

This reframes orchestration from *“always act optimally”* to:

* stability first,
* uncertainty-aware decision making,
* governance-constrained autonomy.

---

## 🔒 Explicit Scope (Non-Negotiable)

### ✅ What This Project Is

* System-level orchestration simulator
* Graph-modeled compute continuum (cloud / edge / far-edge)
* Workflow-aware service orchestration
* Multi-agent reinforcement learning (PPO-based)
* Stability, oscillation, and recovery analysis
* Uncertainty-aware abstention (NO_OP)
* Governance and policy health monitoring
* Explainability and post-hoc auditability
* Fully deterministic and reproducible experiments

### ❌ What This Project Is Not

* No PHY / MAC / waveform modeling
* No ns-3, O-RAN, or radio-level simulators
* No real operator traffic traces
* No LLMs in the control loop
* No production deployment claims
* No state-of-the-art performance claims

These exclusions are **deliberate design choices**, not limitations.

---

## 🧠 System Architecture (High-Level)

```
Workflow Requests
(latency, priority, slice)
        ↓
Graph-Based Compute Continuum
(Cloud / Edge / Far-Edge)
        ↓
Workflow-Aware State Encoder
(interpretable features)
        ↓
Multi-Agent RL (PPO)
(independent agents)
        ↓
Uncertainty & Abstention Logic
(entropy, novelty, failure)
        ↓
Governance Risk Gate
(post-policy safety)
        ↓
Execution & Simulation
(latency, SLA, recovery)
        ↓
Explainability & Audit
(traces, attribution, reports)
```

**Key principle:**

> RL controls actions.
> Governance constrains actions.
> Explainability explains actions.
> Nothing else interferes.

---

## 🌐 Compute Continuum Modeling

### Node Types

* **Cloud** – high capacity, higher latency
* **Edge** – medium capacity, low latency
* **Far-Edge / IoT** – low capacity, intermittent

### Graph Representation

Implemented using **NetworkX** with:

* node capacities,
* utilization,
* latency edges,
* failure sensitivity.

No deep graph embeddings are used to preserve interpretability.

---

## 🔗 Workflow-Aware Services

Workflows are modeled as **end-to-end services**, not isolated tasks.

Each workflow includes:

* latency budget,
* priority,
* slice type (eMBB / URLLC / mMTC).

This enforces realistic **end-to-end reasoning**, consistent with 6G service pipelines.

---

## 🧩 State Representation (Explainable by Design)

Each agent observes a fixed-size, engineered state vector including:

* local and global CPU utilization,
* workflow load indicators,
* stress and failure signals,
* time progression.

No learned embeddings → stable, auditable behavior.

---

## 🎛 Action Space

Each agent can choose:

| Action           | Description                    |
| ---------------- | ------------------------------ |
| DEPLOY_LOCAL     | Place or retain workload       |
| MIGRATE_NEIGHBOR | Move workload to adjacent node |
| SCALE_UP         | Increase allocated resources   |
| SCALE_DOWN       | Reduce allocated resources     |
| **NO_OP**        | Abstain from action            |

**NO_OP is mandatory** and treated as a first-class safety mechanism.

---

## 🎯 Reward Function

Multi-objective reward with explicit logging:

* latency penalty
* SLA violation penalty
* migration cost
* stability considerations

Each component is logged separately for analysis and ablation.

---

## 🤖 Learning Framework

* Independent PPO agents (Stable-Baselines3)
* CPU-only training
* Fixed random seeds
* Deterministic experiments

Centralized critics and parameter sharing are intentionally deferred.

---

## ⚠️ Uncertainty, Abstention & Failures

### Uncertainty Signals

* Policy entropy
* State novelty
* Failure indicators

### Abstention Logic

If uncertainty exceeds a threshold → **force NO_OP**

### Failure Modeling

* Node overload
* Capacity degradation
* Latency inflation

The system is evaluated for **graceful degradation**, not peak performance.

---

## 🧾 Governance & Explainability

### Governance Layer

* Risk-aware gating of actions
* Monitors long-term policy health
* Enforces conservative behavior under uncertainty

### Explainability

* Policy traces
* Attribution analysis
* Counterfactual reasoning

### Optional LLM Usage

* Post-hoc explanation only
* Zero control authority
* Used for audit and human interpretation

---

## 📊 Experiments & Evaluation

### Baselines

* Random
* Heuristic placement
* PPO
* MARL

### Metrics

* Latency
* SLA violations
* Recovery time
* Oscillation count
* Abstention frequency
* Policy stability

### Key Findings

* Abstention reduces oscillations
* Governance improves safety
* Recovery time is environment-limited

---

## 📁 Repository Structure

```
agents/          PPO & MARL controllers
env/             Gym environment & stress models
graph/           Continuum & workflow builders
experiments/     Reproducible experiment scripts
evaluation/      Metrics & recovery analysis
analysis/        Plotting & summary tables
explainability/  Attribution & traces
governance/      Risk gating & policy health
uncertainty/     Entropy, novelty, aggregation
reports/         Markdown & CSV reports
figures/         Publication-ready plots
```

---

## 🧪 Reproducibility

* Fixed seeds
* Deterministic graph generation
* Scripted experiments
* CPU-only execution

All reported results are reproducible.

---

## 🏁 Final Statement

**X-ORCH-6G** is a foundational research platform that treats **abstention, uncertainty, and governance** as core primitives in autonomous orchestration.

It does not claim optimality.
It claims **legitimacy, stability, and rigor**.

---

## 👤 Author

**Lakshmi Chakradhar Vijayarao**
AI / Systems / Networks Research
MS Computer Science

---


