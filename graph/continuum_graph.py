"""
graph/continuum_graph.py

Builds a deterministic, heterogeneous compute continuum graph
representing Cloud–Edge–Far-Edge (IoT) infrastructure.

This graph is used directly by the orchestration environment and
serves as a REAL system artifact (not a conceptual diagram).

Design principles:
- Interpretable node attributes
- Heterogeneous capacities and failure properties
- Deterministic construction for reproducibility
- No learned embeddings or opaque representations
"""

import networkx as nx
import random
from typing import Optional


def build_continuum_graph(
    num_cloud: int = 1,
    num_edge: int = 3,
    num_far_edge: int = 5,
    seed: int = 42,
) -> nx.DiGraph:
    """
    Constructs a directed compute continuum graph.

    Parameters
    ----------
    num_cloud : int
        Number of cloud nodes (high capacity, low mobility)
    num_edge : int
        Number of edge nodes (medium capacity)
    num_far_edge : int
        Number of far-edge / IoT nodes (low capacity, high mobility)
    seed : int
        Random seed for reproducibility

    Returns
    -------
    nx.DiGraph
        Directed graph with node and edge attributes
    """
    random.seed(seed)
    G = nx.DiGraph()
    node_id = 0

    # ------------------------------------------------------------
    # Internal helper for node creation
    # ------------------------------------------------------------
    def add_node(
        node_type: str,
        cpu_capacity: float,
        mem_capacity: float,
        energy_cost: float,
        failure_prob: float,
        mobility_sensitivity: float,
    ):
        nonlocal node_id
        G.add_node(
            node_id,
            type=node_type,
            cpu_capacity=cpu_capacity,
            mem_capacity=mem_capacity,
            cpu_used=0.0,
            mem_used=0.0,
            energy_cost=energy_cost,
            failure_prob=failure_prob,
            mobility_sensitivity=mobility_sensitivity,
        )
        node_id += 1

    # ------------------------------------------------------------
    # Cloud nodes (stable, high capacity)
    # ------------------------------------------------------------
    for _ in range(num_cloud):
        add_node(
            node_type="cloud",
            cpu_capacity=100.0,
            mem_capacity=100.0,
            energy_cost=3.0,
            failure_prob=0.01,
            mobility_sensitivity=0.0,
        )

    # ------------------------------------------------------------
    # Edge nodes (moderate capacity, moderate mobility)
    # ------------------------------------------------------------
    for _ in range(num_edge):
        add_node(
            node_type="edge",
            cpu_capacity=50.0,
            mem_capacity=50.0,
            energy_cost=2.0,
            failure_prob=0.03,
            mobility_sensitivity=0.2,
        )

    # ------------------------------------------------------------
    # Far-edge / IoT nodes (low capacity, high mobility)
    # ------------------------------------------------------------
    for _ in range(num_far_edge):
        add_node(
            node_type="far-edge",
            cpu_capacity=15.0,
            mem_capacity=15.0,
            energy_cost=1.0,
            failure_prob=0.08,
            mobility_sensitivity=0.6,
        )

    # ------------------------------------------------------------
    # Connectivity: fully connected directed graph
    # ------------------------------------------------------------
    # Rationale:
    # - Avoids topology bias in early-stage system studies
    # - Allows orchestration policies to reason about all options
    # - Latency and reliability encode practical constraints
    # ------------------------------------------------------------
    for src in G.nodes:
        for dst in G.nodes:
            if src == dst:
                continue

            latency = random.uniform(5.0, 50.0)        # milliseconds
            bandwidth = random.uniform(10.0, 100.0)    # Mbps (abstracted)
            reliability = random.uniform(0.90, 0.999)  # link success prob

            G.add_edge(
                src,
                dst,
                latency=latency,
                bandwidth=bandwidth,
                reliability=reliability,
            )

    return G


# ------------------------------------------------------------
# OPTIONAL: Visualization utility for Figure 2 (REAL OUTPUT)
# ------------------------------------------------------------
def visualize_continuum_graph(G: nx.DiGraph, seed: Optional[int] = 42):
    """
    Visualizes the compute continuum graph.

    This function is intended ONLY for inspection and figure generation.
    It does NOT affect the environment or experiments.

    Allowed edits for publication:
    - Node color coding
    - Legend
    - Cropping / resolution adjustments
    """
    import matplotlib.pyplot as plt

    random.seed(seed)

    pos = nx.spring_layout(G, seed=seed)

    node_colors = []
    for _, data in G.nodes(data=True):
        if data["type"] == "cloud":
            node_colors.append("tab:blue")
        elif data["type"] == "edge":
            node_colors.append("tab:green")
        else:
            node_colors.append("tab:orange")

    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=900,
        font_size=8,
        edge_color="gray",
        alpha=0.85,
    )

    plt.title("Compute Continuum Graph (Cloud–Edge–Far-Edge)")
    plt.tight_layout()
    plt.show()
