# env/continuum_env.py
import gymnasium as gym
import numpy as np
import random

from graph.continuum_graph import build_continuum_graph
from graph.semantics import SLICE_PROFILES, Workflow
from env.stress_models import StressModel


class ContinuumEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self, max_steps=100, seed=42, enable_stress=False):
        super().__init__()
        random.seed(seed)
        np.random.seed(seed)

        self.graph = build_continuum_graph(seed=seed)
        self.enable_stress = enable_stress
        self.stress_model = StressModel(seed) if enable_stress else None

        self.max_steps = max_steps
        self.time = 0
        self.control_node_id = 0
        self.active_workflows = []

        self.action_space = gym.spaces.Discrete(5)
        self.observation_space = gym.spaces.Box(
            low=0.0, high=1.0, shape=(10,), dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        self.time = 0
        self.active_workflows.clear()

        for _, node in self.graph.nodes(data=True):
            node["cpu_used"] = 0.0

        return self._get_obs(0.0, 0.0), {}

    def step(self, action):
        action = int(action)
        self.time += 1

        stress, failure = (0.0, 0.0)
        if self.enable_stress:
            stress, failure = self.stress_model.step(self.graph)

        # Workflow arrival (slice-aware)
        if random.random() < 0.3:
            slice_type = random.choice(list(SLICE_PROFILES.keys()))
            p = SLICE_PROFILES[slice_type]
            self.active_workflows.append(
                Workflow(
                    workflow_id=len(self.active_workflows),
                    slice_type=slice_type,
                    latency_budget=p["latency_budget"],
                    priority=p["priority"],
                )
            )

        node = self.graph.nodes[self.control_node_id]

        if action == 0:
            node["cpu_used"] += 5
        elif action == 1:
            node["cpu_used"] = max(0.0, node["cpu_used"] - 4)
        elif action == 2:
            node["cpu_used"] += 3
        elif action == 3:
            node["cpu_used"] = max(0.0, node["cpu_used"] - 3)

        latency = self._latency(node, failure)
        sla_violations = self._sla_violations(latency)

        reward = -latency - 10 * sla_violations
        done = self.time >= self.max_steps

        return self._get_obs(stress, failure), reward, done, False, {
            "latency": latency,
            "sla_violations": sla_violations,
        }

    def _latency(self, node, failure):
        return (
            random.uniform(10, 30)
            + (node["cpu_used"] / node["cpu_capacity"]) * 40
            + 80 * failure
        )

    def _sla_violations(self, latency):
        return sum(
            wf.priority
            for wf in self.active_workflows
            if latency > wf.latency_budget
        )

    def _get_obs(self, stress, failure):
        cpu_utils = [
            n["cpu_used"] / n["cpu_capacity"]
            for _, n in self.graph.nodes(data=True)
        ]

        return np.array(
            [
                np.mean(cpu_utils),
                np.max(cpu_utils),
                stress,
                failure,
                len(self.active_workflows) / 10,
                self.time / self.max_steps,
                0.0, 0.0, 0.0, 0.0,
            ],
            dtype=np.float32,
        )
