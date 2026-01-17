def policy_trace(state, action, reward_terms, outcome):
    """
    Produces a structured policy trace.
    """

    return {
        "state_summary": state.tolist(),
        "action": int(action),
        "reward_terms": reward_terms,
        "outcome": outcome
    }
