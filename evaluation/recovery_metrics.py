# evaluation/recovery_metrics.py
from typing import List

def recovery_time(latencies: List[float], threshold: float = 80.0) -> int:
    """
    Time until latency returns below threshold after disturbance.
    """
    crossed = False
    for t, latency in enumerate(latencies):
        if latency > threshold:
            crossed = True
        if crossed and latency < threshold:
            return t
    return len(latencies)

def sla_violation_duration(latencies: List[float], threshold: float = 80.0) -> int:
    """
    Total duration of SLA violations.
    """
    return sum(1 for latency in latencies if latency > threshold)

def oscillation_count(actions: List[int]) -> int:
    """
    Counts control oscillations.
    """
    if len(actions) < 2:
        return 0
    return sum(
        1 for i in range(1, len(actions))
        if actions[i] != actions[i - 1]
    )
