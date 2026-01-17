import json
from pathlib import Path
from env.continuum_env import ContinuumEnv
from agents.ppo_agent import create_ppo_agent
from evaluation.metrics import compute_metrics


def run_ppo_training(total_timesteps=10_000, episodes=5):
    env = ContinuumEnv()
    model = create_ppo_agent(env)

    print("Training PPO agent...")
    model.learn(total_timesteps=total_timesteps)

    rewards = []

    for ep in range(episodes):
        obs, _ = env.reset()
        done = False
        total_reward = 0

        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, _, _ = env.step(action)
            total_reward += reward

        rewards.append(total_reward)
        print(f"PPO Episode {ep} | Total Reward: {total_reward:.2f}")

    metrics = compute_metrics(rewards)
    return rewards, metrics


if __name__ == "__main__":
    rewards, metrics = run_ppo_training()

    print("\nPPO Evaluation Metrics:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    Path("results/ppo").mkdir(parents=True, exist_ok=True)
    with open("results/ppo/rewards.json", "w") as f:
        json.dump(rewards, f, indent=2)

    with open("results/ppo/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
