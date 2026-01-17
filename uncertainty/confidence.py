# uncertainty/confidence.py
import numpy as np
from collections import Counter


def policy_entropy(actions):
    """
    Shannon entropy over discrete actions.
    Used as a proxy for policy uncertainty.
    """
    if len(actions) == 0:
        return 0.0

    counts = Counter(actions)
    probs = np.array(list(counts.values()), dtype=np.float32)
    probs = probs / probs.sum()

    entropy = -np.sum(probs * np.log(probs + 1e-8))
    return float(entropy)
