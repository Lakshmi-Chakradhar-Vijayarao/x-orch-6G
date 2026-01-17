# graph/workflow_builder.py

import networkx as nx
import random
from graph.semantics import ServiceSemantic, WorkflowSemantic


def generate_workflow_dag(workflow_id: int, seed: int = None):
    if seed is not None:
        random.seed(seed)

    dag = nx.DiGraph(id=workflow_id)

    services = [
        ServiceSemantic("sensor", 5, 20, criticality=0.9, stateful=False),
        ServiceSemantic("preprocess", 10, 30, criticality=0.7, stateful=False),
        ServiceSemantic("inference", 20, 40, criticality=1.0, stateful=True),
        ServiceSemantic("aggregation", 8, 20, criticality=0.6, stateful=False),
    ]

    for svc in services:
        dag.add_node(
            svc.name,
            cpu_demand=svc.cpu_demand,
            latency_budget=svc.latency_budget,
            criticality=svc.criticality,
            stateful=svc.stateful
        )

    dag.add_edges_from([
        ("sensor", "preprocess"),
        ("preprocess", "inference"),
        ("inference", "aggregation"),
    ])

    semantic = WorkflowSemantic(
        workflow_id=workflow_id,
        services=services,
        sla_latency_budget=sum(s.latency_budget for s in services),
        user_priority=random.uniform(0.3, 1.0)
    )

    dag.graph["semantic"] = semantic
    return dag
