# graph/semantics.py
from dataclasses import dataclass
from typing import Dict, List

# ============================================================
# Risk encoding
# ============================================================

RISK_LEVELS = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
}

# ============================================================
# 6G SLICE PROFILES (ETSI / 3GPP-ALIGNED)
# ============================================================

SLICE_PROFILES = {
    "eMBB": {
        "latency_budget": 100,
        "priority": 1.0,
    },
    "URLLC": {
        "latency_budget": 30,
        "priority": 3.0,
    },
    "mMTC": {
        "latency_budget": 200,
        "priority": 0.5,
    },
}

# ============================================================
# Workflow Model (USED BY ENV)
# ============================================================

@dataclass
class Workflow:
    workflow_id: int
    slice_type: str
    latency_budget: float
    priority: float

# ============================================================
# Action Semantics
# ============================================================

ACTION_SEMANTICS: Dict[int, Dict] = {
    0: {"name": "DEPLOY_LOCAL", "risk": "LOW"},
    1: {"name": "MIGRATE_NEIGHBOR", "risk": "MEDIUM"},
    2: {"name": "SCALE_UP", "risk": "LOW"},
    3: {"name": "SCALE_DOWN", "risk": "MEDIUM"},
    4: {"name": "NO_OP", "risk": "LOW"},
}

def describe_action(action_id: int) -> Dict:
    return ACTION_SEMANTICS.get(
        action_id,
        {"name": "UNKNOWN", "risk": "HIGH"},
    )

def get_action_risk(action_id: int) -> int:
    meta = describe_action(action_id)
    return RISK_LEVELS.get(meta["risk"], RISK_LEVELS["HIGH"])
