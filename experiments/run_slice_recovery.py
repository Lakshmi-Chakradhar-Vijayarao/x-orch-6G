# experiments/run_slice_recovery.py
import json
from pathlib import Path
from collections import defaultdict

from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from evaluation.recovery_metrics import recovery_time

def run_slice_recovery():
    env = ContinuumEnv(enable_stress=True)
    marl = MARLController(env, num_agents=3)

    marl.train(timesteps=3000)

    obs, _ = env.reset()
    done = False

    slice_latencies = defaultdict(list)

    while not done:
        actions = marl.select_actions(obs, episode_id=0)
        for agent_id, action in enumerate(actions):
            env.control_node_id = agent_id
            obs, _, done, _, info = env.step(action)

            for wf in env.active_workflows:
                slice_latencies[wf.slice_type].append(info["latency"])

            if done:
                break

    results = {
        slice_type: recovery_time(latencies)
        for slice_type, latencies in slice_latencies.items()
    }

    return results

if __name__ == "__main__":
    Path("results/governance").mkdir(parents=True, exist_ok=True)

    results = run_slice_recovery()

    with open("results/governance/slice_recovery.json", "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
