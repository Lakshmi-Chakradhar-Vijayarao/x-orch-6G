# experiments/run_stress_test.py
import json
from pathlib import Path
from collections import defaultdict

from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from evaluation.recovery_metrics import recovery_time


def run_stress_test():
    env = ContinuumEnv(enable_stress=True)
    marl = MARLController(env, num_agents=3)

    marl.train(timesteps=3000)

    obs, _ = env.reset()
    done = False

    # 🔑 Slice-specific latency tracking
    latencies_by_slice = defaultdict(list)

    while not done:
        actions = marl.select_actions(obs, episode_id=0)

        for agent_id, action in enumerate(actions):
            env.control_node_id = agent_id
            obs, _, done, _, info = env.step(action)

            latency = info["latency"]

            for wf in env.active_workflows:
                latencies_by_slice[wf.slice_type].append(latency)

            if done:
                break

    results = {}
    for slice_type, latencies in latencies_by_slice.items():
        results[slice_type] = {
            "recovery_time": recovery_time(latencies)
        }

    return results


if __name__ == "__main__":
    Path("results/stress").mkdir(parents=True, exist_ok=True)

    metrics = run_stress_test()

    with open("results/stress/slice_recovery.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))
