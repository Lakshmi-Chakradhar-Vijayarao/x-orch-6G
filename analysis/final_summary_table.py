# analysis/final_summary_table.py
import json
import pandas as pd

gov = json.load(open("results/governance/governance_ablation.json"))
slice_rec = json.load(open("results/governance/slice_recovery.json"))

rows = []

rows.append({
    "Scenario": "MARL + Governance",
    "Recovery Time": gov["with_governance"]["recovery_time"],
    "SLA Violations": gov["with_governance"]["sla_violation_duration"],
})

rows.append({
    "Scenario": "MARL (No Governance)",
    "Recovery Time": gov["without_governance"]["recovery_time"],
    "SLA Violations": gov["without_governance"]["sla_violation_duration"],
})

for slice_type, rt in slice_rec.items():
    rows.append({
        "Scenario": f"Slice: {slice_type}",
        "Recovery Time": rt,
        "SLA Violations": "N/A",
    })

df = pd.DataFrame(rows)
print(df)
df.to_csv("results/governance/final_summary_table.csv", index=False)
