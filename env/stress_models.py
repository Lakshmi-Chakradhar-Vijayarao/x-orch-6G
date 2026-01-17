# env/stress_models.py
import random

class StressModel:
    """
    Exogenous stress + failure generator.
    """

    def __init__(self, seed=42):
        random.seed(seed)
        self.failure_timer = 0

    def step(self, graph):
        stress = random.random()

        failure = 0.0
        if stress > 0.7 and random.random() < 0.2:
            self.failure_timer = random.randint(5, 15)

        if self.failure_timer > 0:
            failure = 1.0
            self.failure_timer -= 1

        return stress, failure
