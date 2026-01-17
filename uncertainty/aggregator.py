# uncertainty/aggregator.py

def should_force_no_op(entropy: float, threshold: float) -> bool:
    """
    Decide whether uncertainty is high enough
    to override action selection with NO_OP.
    """
    return entropy >= threshold
