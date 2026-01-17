import numpy as np


def policy_health_report(stability_metrics):
    """
    Computes a governance-oriented health report for a MARL policy.

    Parameters
    ----------
    stability_metrics : list of dict
        Each dict must contain:
        - switch_rate
        - entropy
        - no_op_ratio

    Returns
    -------
    dict
        Governance-grade policy health summary.
    """

    if len(stability_metrics) == 0:
        return {
            "status": "NO_DATA",
            "message": "No stability metrics provided"
        }

    avg_switch_rate = float(
        np.mean([m["switch_rate"] for m in stability_metrics])
    )
    avg_entropy = float(
        np.mean([m["entropy"] for m in stability_metrics])
    )
    avg_no_op_ratio = float(
        np.mean([m["no_op_ratio"] for m in stability_metrics])
    )

    # --------------------------------------------------------------
    # Risk classification (rule-based, deterministic)
    # --------------------------------------------------------------
    if avg_switch_rate > 0.8:
        risk_level = "HIGH"
        interpretation = (
            "Policy exhibits frequent action switching, "
            "indicating potential oscillatory behavior."
        )
    elif avg_switch_rate > 0.5:
        risk_level = "MEDIUM"
        interpretation = (
            "Policy is reactive but remains within stable bounds. "
            "Monitoring recommended under high load or failures."
        )
    else:
        risk_level = "LOW"
        interpretation = (
            "Policy demonstrates stable control with limited oscillation."
        )

    # --------------------------------------------------------------
    # Abstention adequacy check
    # --------------------------------------------------------------
    if avg_no_op_ratio < 0.05:
        abstention_comment = (
            "Abstention behavior is rare; policy may be overconfident."
        )
    elif avg_no_op_ratio > 0.6:
        abstention_comment = (
            "High abstention frequency; policy may be overly conservative."
        )
    else:
        abstention_comment = (
            "Abstention frequency is balanced and appropriate."
        )

    # --------------------------------------------------------------
    # Final governance report
    # --------------------------------------------------------------
    report = {
        "avg_switch_rate": round(avg_switch_rate, 3),
        "avg_entropy": round(avg_entropy, 3),
        "avg_no_op_ratio": round(avg_no_op_ratio, 3),
        "risk_level": risk_level,
        "interpretation": interpretation,
        "abstention_assessment": abstention_comment,
        "governance_ready": True
    }

    return report
