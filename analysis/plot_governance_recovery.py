import json
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# Load governance ablation results
# ------------------------------------------------------------
with open("results/governance/governance_ablation.json") as f:
    data = json.load(f)

# ------------------------------------------------------------
# Extract metrics
# ------------------------------------------------------------
labels = ["Recovery Time", "SLA Violation Duration"]

no_gov = [
    data["marl_no_governance"]["recovery_time"],
    data["marl_no_governance"]["sla_violation_duration"],
]

gov = [
    data["marl_governance"]["recovery_time"],
    data["marl_governance"]["sla_violation_duration"],
]

gov_strict = [
    data["marl_governance_strict"]["recovery_time"],
    data["marl_governance_strict"]["sla_violation_duration"],
]

# ------------------------------------------------------------
# Plot configuration
# ------------------------------------------------------------
x = range(len(labels))
width = 0.25

plt.figure(figsize=(8, 4))

plt.bar(
    [i - width for i in x],
    no_gov,
    width,
    label="No Governance",
)

plt.bar(
    x,
    gov,
    width,
    label="Governance",
)

plt.bar(
    [i + width for i in x],
    gov_strict,
    width,
    label="Strict Governance",
)

plt.xticks(x, labels)
plt.ylabel("Timesteps")
plt.title("Governance Impact on Recovery and SLA Violations")
plt.legend()
plt.grid(axis="y", alpha=0.4)
plt.tight_layout()

# ------------------------------------------------------------
# Save figure
# ------------------------------------------------------------
Path("figures").mkdir(exist_ok=True)
plt.savefig(
    "figures/governance_recovery_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
