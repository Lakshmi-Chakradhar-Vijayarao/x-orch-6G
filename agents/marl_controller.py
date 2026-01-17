# agents/marl_controller.py
from stable_baselines3 import PPO
from collections import defaultdict
import numpy as np


class MARLController:
    """
    Independent PPO agents with stability-first design.

    Design principles:
    - No implicit coordination
    - Deterministic logging
    - Governance handled externally (risk gates, audits)
    """

    def __init__(self, env, num_agents: int):
        self.env = env
        self.num_agents = num_agents

        self.agents = []
        self.action_logs = defaultdict(list)

        for agent_id in range(num_agents):
            model = PPO(
                policy="MlpPolicy",
                env=env,
                learning_rate=3e-4,
                n_steps=256,
                batch_size=64,
                gamma=0.99,
                ent_coef=0.01,
                verbose=0,
                seed=42 + agent_id,
            )
            self.agents.append(model)

    def train(self, timesteps: int = 5_000):
        """
        Train each agent independently.
        """
        for agent_id, agent in enumerate(self.agents):
            print(f"Training agent {agent_id}")
            agent.learn(total_timesteps=timesteps)

    def select_actions(self, obs, episode_id: int):
        """
        Select actions for all agents at the current timestep.
        """
        actions = []

        for agent_id, agent in enumerate(self.agents):
            action, _ = agent.predict(obs, deterministic=False)

            if isinstance(action, np.ndarray):
                action = int(action.item())

            self.action_logs[(agent_id, episode_id)].append(action)
            actions.append(action)

        return actions
