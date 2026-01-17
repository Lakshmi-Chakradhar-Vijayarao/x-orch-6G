import json
from pathlib import Path
from env.continuum_env import ContinuumEnv
from agents.marl_controller import MARLController
from evaluation.stability_metrics import summarize_agent_stability


def run_marl(num_agents=3, episodes=5, timesteps=5_000):
    env = ContinuumEnv()
    marl = MARLController(env, num_agents=num_agents)

    print("\n=== Training MARL Agents ===")
    marl.train(timesteps=timesteps)

    system_rewards = []
    stability_logs = []

    for ep in range(episodes):
        obs, _ = env.reset()
        done = False
        total_reward = 0

        while not done:
            actions = marl.select_actions(obs, episode_id=ep)
            for agent_id, action in enumerate(actions):
                env.control_node_id = agent_id
                obs, reward, done, _, _ = env.step(action)
                total_reward += reward
                if done:
                    break

        system_rewards.append(total_reward)
        print(f"Episode {ep} | Total System Reward: {total_reward:.2f}")

    for (agent_id, ep), log in marl.action_logs.items():
        metrics = summarize_agent_stability(log)
        stability_logs.append(
            {"agent": agent_id, "episode": ep, **metrics}
        )

    return system_rewards, stability_logs


if __name__ == "__main__":
    rewards, stability = run_marl()

    Path("results/marl").mkdir(parents=True, exist_ok=True)

    with open("results/marl/system_rewards.json", "w") as f:
        json.dump(rewards, f, indent=2)

    with open("results/marl/stability_metrics.json", "w") as f:
        json.dump(stability, f, indent=2)
