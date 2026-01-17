# analysis/generate_summary_table.py

import json
import pandas as pd
from pathlib import Path


def load_json(path):
    with open(path) as f:
        return json.load(f)


def main():
    # Load only what is actually used
    stress = load_json("results/stress/marl_under_stress.json")
    gov = load_json("results/governance/governance_ablation.json")

    rows = [
        {
            "Method": "PPO",
            "Governance": "No",
            "Recovery Time": "N/A",
            "SLA Violations": "N/A",
        },
        {
            "Method": "MARL",
            "Governance": "No",
            "Recovery Time": stress["recovery_time"],
            "SLA Violations": stress["sla_violation_duration"],
        },
        {
            "Method": "MARL",
            "Governance": "Yes",
            "Recovery Time": gov["marl_governance"]["recovery_time"],
            "SLA Violations": gov["marl_governance"]["sla_violation_duration"],
        },
        {
            "Method": "MARL",
            "Governance": "Strict",
            "Recovery Time": gov["marl_governance_strict"]["recovery_time"],
            "SLA Violations": gov["marl_governance_strict"]["sla_violation_duration"],
        },
    ]

    df = pd.DataFrame(rows)

    Path("reports").mkdir(exist_ok=True)
    df.to_csv("reports/final_summary_table.csv", index=False)

    print(df)


if __name__ == "__main__":
    main()
