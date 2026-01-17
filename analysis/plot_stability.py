import json
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Load MARL stability metrics (LIST of dicts)
# --------------------------------------------------
metrics = json.load(open("results/marl/stability_metrics.json"))

switch_rates = [m["switch_rate"] for m in metrics]
entropies = [m["entropy"] for m in metrics]

# --------------------------------------------------
# Plot
# --------------------------------------------------
plt.figure(figsize=(7, 4))
plt.scatter(
    switch_rates,
    entropies,
    alpha=0.7,
    edgecolor="black"
)

plt.xlabel("Switch Rate")
plt.ylabel("Action Entropy")
plt.title("MARL Stability Distribution")

plt.grid(True)
plt.tight_layout()

# --------------------------------------------------
# Save figure
# --------------------------------------------------
Path("figures").mkdir(exist_ok=True)
plt.savefig("figures/stability_scatter.png", dpi=300)
plt.show()
