# experiments/run_uncertainty_stress.py

import json
from pathlib import Path

from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from uncertainty.confidence import policy_entropy
from governance.risk_gate import RiskAwareGate


def run_uncertainty_stress(
    num_agents: int = 3,
    horizon: int = 50,
    entropy_window: int = 10,
    entropy_threshold: float = 0.8,
):
    """
    Uncertainty-driven stress test with governance gating.
    """

    env = ContinuumEnv(enable_stress=True)
    marl = MARLController(env, num_agents=num_agents)
    gate = RiskAwareGate(uncertainty_threshold=entropy_threshold)

    obs, _ = env.reset()

    action_history = []
    final_actions = []
    forced_no_op_count = 0

    for t in range(horizon):
        actions = marl.select_actions(obs, episode_id=0)
        proposed_action = actions[0]

        recent = action_history[-entropy_window:]
        entropy = policy_entropy(recent)

        final_action = gate.gate(proposed_action, entropy)

        if final_action == 4 and proposed_action != 4:
            forced_no_op_count += 1

        obs, _, done, _, _ = env.step(final_action)

        action_history.append(final_action)
        final_actions.append(final_action)

        if done:
            break

    total = len(final_actions)

    results = {
        "uncertainty_threshold": entropy_threshold,
        "total_actions": total,
        "raw_no_op_ratio": final_actions.count(4) / total,
        "forced_no_op_ratio": forced_no_op_count / total,
        "effective_no_op_ratio": final_actions.count(4) / total,
    }

    Path("results/ablations").mkdir(parents=True, exist_ok=True)
    with open("results/ablations/no_op_behavior.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Uncertainty stress results:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    run_uncertainty_stress()
