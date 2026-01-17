import copy


def counterfactual_action(agent, obs, feature_index, delta):
    """
    Tests if action changes when a feature is perturbed.
    """

    base_action, _ = agent.predict(obs, deterministic=False)

    modified_obs = copy.deepcopy(obs)
    modified_obs[feature_index] = min(1.0, modified_obs[feature_index] + delta)

    new_action, _ = agent.predict(modified_obs, deterministic=False)

    return {
        "original_action": int(base_action),
        "counterfactual_action": int(new_action),
        "changed": base_action != new_action
    }
