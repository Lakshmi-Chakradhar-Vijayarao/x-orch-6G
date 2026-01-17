# governance/risk_gate.py

from graph.semantics import get_action_risk


class RiskAwareGate:
    """
    Risk-aware uncertainty gate.

    Governance is strictly POST-POLICY:
    - Never alters learning
    - Never feeds back into the agent
    - Only constrains execution under risk

    Enforcement rule:
    - If uncertainty exceeds threshold
    - AND action risk exceeds acceptable level
    → Abstain (NO_OP)
    """

    def __init__(
        self,
        uncertainty_threshold: float = 0.8,
        max_acceptable_risk: int = 2,  # MEDIUM
    ):
        self.uncertainty_threshold = uncertainty_threshold
        self.max_acceptable_risk = max_acceptable_risk

    def gate(self, action: int, uncertainty: float) -> int:
        """
        Apply governance gating.

        Parameters
        ----------
        action : int
            Raw action selected by policy
        uncertainty : float
            System uncertainty estimate (e.g., failure/stress proxy)

        Returns
        -------
        int
            Final executable action
        """
        action_risk = get_action_risk(action)

        if (
            uncertainty > self.uncertainty_threshold
            and action_risk > self.max_acceptable_risk
        ):
            return 4  # NO_OP (explicit abstention)

        return action
