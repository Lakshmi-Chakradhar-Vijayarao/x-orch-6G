import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def normalize_metrics(raw):
    """
    Normalize ablation metrics into a list of metric dicts.

    Supports:
    - list[dict]
    - dict[str, dict]
    """
    if isinstance(raw, list):
        return raw

    if isinstance(raw, dict):
        return list(raw.values())

    raise ValueError("Unsupported metrics format in ablation file")


def aggregate(metrics):
    return {
        "avg_switch_rate": np.mean([m["switch_rate"] for m in metrics]),
        "avg_entropy": np.mean([m["entropy"] for m in metrics]),
        "avg_no_op_ratio": np.mean([m["no_op_ratio"] for m in metrics]),
    }


# --------------------------------------------------
# Load raw ablation results
# --------------------------------------------------
enabled_raw = json.load(open("results/ablations/no_op_enabled.json"))
disabled_raw = json.load(open("results/ablations/no_op_disabled.json"))

enabled_metrics = normalize_metrics(enabled_raw)
disabled_metrics = normalize_metrics(disabled_raw)

enabled = aggregate(enabled_metrics)
disabled = aggregate(disabled_metrics)

# --------------------------------------------------
# Plot
# --------------------------------------------------
labels = ["Switch Rate", "Entropy", "NO_OP Ratio"]

enabled_vals = [
    enabled["avg_switch_rate"],
    enabled["avg_entropy"],
    enabled["avg_no_op_ratio"],
]

disabled_vals = [
    disabled["avg_switch_rate"],
    disabled["avg_entropy"],
    disabled["avg_no_op_ratio"],
]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(7, 4))
plt.bar(x - width / 2, enabled_vals, width, label="NO_OP Enabled")
plt.bar(x + width / 2, disabled_vals, width, label="NO_OP Disabled")

plt.xticks(x, labels)
plt.ylabel("Value")
plt.title("NO_OP Ablation Study")

plt.legend()
plt.grid(axis="y")
plt.tight_layout()

# --------------------------------------------------
# Save
# --------------------------------------------------
Path("figures").mkdir(exist_ok=True)
plt.savefig("figures/no_op_ablation.png", dpi=300)
plt.show()
