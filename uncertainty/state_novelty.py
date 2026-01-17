import numpy as np


class StateNoveltyDetector:
    """
    Tracks state distribution and estimates novelty
    using Mahalanobis-style distance.
    """

    def __init__(self, state_dim):
        self.state_dim = state_dim
        self.mean = np.zeros(state_dim)
        self.cov = np.eye(state_dim)
        self.n = 0

    def update(self, state):
        self.n += 1
        delta = state - self.mean
        self.mean += delta / self.n
        self.cov += np.outer(delta, delta)

    def novelty_score(self, state):
        cov_inv = np.linalg.pinv(self.cov / max(self.n, 1))
        diff = state - self.mean
        return float(diff.T @ cov_inv @ diff)
