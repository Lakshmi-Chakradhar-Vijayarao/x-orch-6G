# experiments/run_governance_ablation.py

import json
from pathlib import Path

from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from evaluation.recovery_metrics import recovery_time, sla_violation_duration
from governance.risk_gate import RiskAwareGate


def run(governance_enabled: bool, strict: bool = False):
    env = ContinuumEnv(enable_stress=True)
    marl = MARLController(env, num_agents=3)

    # IMPORTANT: identical training across all runs
    marl.train(timesteps=3000)

    gate = None
    if governance_enabled:
        gate = RiskAwareGate(
            uncertainty_threshold=0.25 if strict else 0.7
        )

    obs, _ = env.reset()
    latencies = []

    done = False
    while not done:
        actions = marl.select_actions(obs, episode_id=0)

        for agent_id, raw_action in enumerate(actions):
            env.control_node_id = agent_id
            final_action = raw_action

            # 🔒 GOVERNANCE (POST-POLICY, EXECUTION-ONLY)
            if gate is not None:
                uncertainty = obs[3]  # failure / stress proxy
                final_action = gate.gate(raw_action, uncertainty)

            obs, _, done, _, info = env.step(final_action)
            latencies.append(info["latency"])

            if done:
                break

    return {
        "governance": governance_enabled,
        "strict": strict,
        "recovery_time": recovery_time(latencies),
        "sla_violation_duration": sla_violation_duration(latencies),
    }


if __name__ == "__main__":
    Path("results/governance").mkdir(parents=True, exist_ok=True)

    results = {
        "marl_no_governance": run(False),
        "marl_governance": run(True),
        "marl_governance_strict": run(True, strict=True),
    }

    with open("results/governance/governance_ablation.json", "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
