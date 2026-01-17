# analysis/plot_recovery.py
import json
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_FILE = "results/stress/marl_under_stress.json"
OUTPUT_FILE = "figures/recovery_metrics.png"

def plot_recovery_metrics():
    if not Path(INPUT_FILE).exists():
        raise FileNotFoundError(
            f"Expected recovery metrics at {INPUT_FILE}"
        )

    metrics = json.load(open(INPUT_FILE))

    recovery_time = metrics["recovery_time"]
    sla_duration = metrics["sla_violation_duration"]

    plt.figure()
    plt.bar(
        ["Recovery Time", "SLA Violation Duration"],
        [recovery_time, sla_duration]
    )
    plt.ylabel("Timesteps")
    plt.title("Failure Recovery & SLA Impact")

    Path("figures").mkdir(exist_ok=True)
    plt.savefig(OUTPUT_FILE)
    plt.close()

    print(f"Recovery plot saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    plot_recovery_metrics()
