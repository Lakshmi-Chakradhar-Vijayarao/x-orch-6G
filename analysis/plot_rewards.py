import json
import matplotlib.pyplot as plt
from pathlib import Path

baseline = json.load(open("results/baselines/baseline_rewards.json"))
ppo = json.load(open("results/ppo/rewards.json"))
marl = json.load(open("results/marl/system_rewards.json"))

plt.figure(figsize=(7,4))
plt.plot(baseline, label="Baseline", marker="o")
plt.plot(ppo, label="PPO", marker="o")
plt.plot(marl, label="MARL", marker="o")

plt.xlabel("Episode")
plt.ylabel("Total Reward")
plt.title("Reward Comparison Across Methods")
plt.legend()
plt.grid(True)
plt.tight_layout()

Path("figures").mkdir(exist_ok=True)
plt.savefig("figures/reward_comparison.png", dpi=300)
plt.show()
