import numpy as np


def action_disagreement(actions):
    """
    Measures disagreement among agents.
    0 → all agree
    1 → all different
    """
    if len(actions) <= 1:
        return 0.0

    unique = len(set(actions))
    return unique / len(actions)
