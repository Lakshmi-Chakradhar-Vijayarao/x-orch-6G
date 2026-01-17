# experiments/run_no_op_ablation.py

import json
from pathlib import Path

from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from evaluation.stability_metrics import summarize_agent_stability


def run_ablation(allow_no_op: bool):
    env = ContinuumEnv()
    marl = MARLController(env, num_agents=3)

    marl.train(timesteps=3_000)

    obs, _ = env.reset()
    done = False

    while not done:
        actions = marl.select_actions(obs, episode_id=0)

        filtered = []
        for a in actions:
            if not allow_no_op and a == 4:
                filtered.append(0)
            else:
                filtered.append(a)

        for agent_id, action in enumerate(filtered):
            env.control_node_id = agent_id
            obs, _, done, _, _ = env.step(action)
            if done:
                break

    metrics = {}
    for (agent_id, _), log in marl.action_logs.items():
        metrics[f"agent_{agent_id}"] = summarize_agent_stability(log)

    return metrics


if __name__ == "__main__":
    Path("results/ablations").mkdir(parents=True, exist_ok=True)

    enabled = run_ablation(True)
    disabled = run_ablation(False)

    with open("results/ablations/no_op_enabled.json", "w") as f:
        json.dump(enabled, f, indent=2)

    with open("results/ablations/no_op_disabled.json", "w") as f:
        json.dump(disabled, f, indent=2)
