# analysis/plot_slice_recovery.py
import json
import matplotlib.pyplot as plt

data = json.load(open("results/governance/slice_recovery.json"))

slices = list(data.keys())
recovery = list(data.values())

plt.bar(slices, recovery)
plt.ylabel("Recovery Time (timesteps)")
plt.title("Slice-Specific Recovery (6G Semantics)")

plt.tight_layout()
plt.savefig("figures/slice_recovery.png")
print("Saved figures/slice_recovery.png")
