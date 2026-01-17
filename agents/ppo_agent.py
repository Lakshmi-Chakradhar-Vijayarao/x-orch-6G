from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

def create_ppo_agent(env):
    model = PPO(
        policy="MlpPolicy",
        env=env,
        learning_rate=3e-4,
        n_steps=256,
        batch_size=64,
        gamma=0.99,
        gae_lambda=0.95,
        ent_coef=0.01,   # entropy = exploration
        clip_range=0.2,
        verbose=0,
        seed=42
    )
    return model
