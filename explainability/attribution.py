import numpy as np
import copy


def permutation_importance(env, agent, obs, num_trials=20):
    """
    Measures feature importance via permutation.

    Returns:
        dict: feature_index -> average reward drop
    """

    baseline_rewards = []

    for _ in range(num_trials):
        _, reward, _, _, _ = env.step(agent)
        baseline_rewards.append(reward)

    baseline = np.mean(baseline_rewards)
    importances = {}

    for i in range(len(obs)):
        perturbed_rewards = []

        for _ in range(num_trials):
            perturbed_obs = copy.deepcopy(obs)
            perturbed_obs[i] = np.random.uniform(0, 1)

            action, _ = agent.predict(perturbed_obs, deterministic=False)
            _, reward, _, _, _ = env.step(action)
            perturbed_rewards.append(reward)

        importances[f"feature_{i}"] = baseline - np.mean(perturbed_rewards)

    return importances
