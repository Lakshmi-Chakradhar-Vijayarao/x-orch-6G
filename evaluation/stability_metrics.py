import numpy as np


def action_switch_rate(actions):
    """
    Measures how frequently actions change.
    High value = oscillatory policy.
    """
    switches = 0
    for i in range(1, len(actions)):
        if actions[i] != actions[i - 1]:
            switches += 1
    return switches / max(1, len(actions) - 1)


def no_op_ratio(actions, no_op_id=4):
    """
    Fraction of NO_OP actions.
    Indicates abstention / stability behavior.
    """
    return actions.count(no_op_id) / max(1, len(actions))


def action_entropy(actions, num_actions=5):
    """
    Entropy of action distribution.
    Measures uncertainty and policy spread.
    """
    counts = np.zeros(num_actions)
    for a in actions:
        counts[a] += 1

    probs = counts / np.sum(counts)
    probs = probs[probs > 0]

    return -np.sum(probs * np.log(probs))


def summarize_agent_stability(action_log):
    """
    Aggregate stability metrics for one agent.
    """
    return {
        "switch_rate": action_switch_rate(action_log),
        "no_op_ratio": no_op_ratio(action_log),
        "entropy": action_entropy(action_log)
    }
