import json
from pathlib import Path
from env.continuum_env import ContinuumEnv


def run_baselines(episodes: int = 5):
    env = ContinuumEnv()
    rewards = []

    for ep in range(episodes):
        obs, _ = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = env.action_space.sample()
            obs, reward, done, _, _ = env.step(action)
            total_reward += reward

        rewards.append(total_reward)
        print(f"Episode {ep} | Total Reward: {total_reward:.2f}")

    return rewards


if __name__ == "__main__":
    results = run_baselines()

    print("Finished baseline run:", results)

    Path("results/baselines").mkdir(parents=True, exist_ok=True)
    with open("results/baselines/baseline_rewards.json", "w") as f:
        json.dump(results, f, indent=2)
