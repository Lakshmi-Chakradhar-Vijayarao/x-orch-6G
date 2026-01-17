import numpy as np

def compute_metrics(rewards):
    return {
        "mean_reward": np.mean(rewards),
        "reward_variance": np.var(rewards),
        "episodes": len(rewards)
    }
