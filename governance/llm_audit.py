# governance/llm_audit.py

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# ------------------------------------------------------------------
# Secure environment setup
# ------------------------------------------------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise RuntimeError(
        "OPENAI_API_KEY not found. "
        "Please set it in a .env file at the project root."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

# ------------------------------------------------------------------
# LLM Governance Audit (STRICTLY POST-HOC)
# ------------------------------------------------------------------

def llm_policy_audit(
    state_summary: dict,
    action: str,
    reward_terms: dict,
    uncertainty: float,
    policy_health: str,
    model: str = "gpt-4o-mini"
) -> str:
    """
    Post-hoc governance explanation using an LLM.

    HARD CONSTRAINTS (REVIEWER-CRITICAL):
    - This function NEVER influences control decisions
    - No outputs are fed back into learning or action selection
    - Advisory, human-readable, auditable only
    - Suitable for safety-critical / regulated AI systems

    Parameters
    ----------
    state_summary : dict
        High-level summary of observed system state
    action : str
        Human-readable action name
    reward_terms : dict
        Reward decomposition (latency, SLA, penalties)
    uncertainty : float
        Composite uncertainty estimate
    policy_health : str
        Policy stability classification
    model : str
        OpenAI model identifier

    Returns
    -------
    str
        Governance audit explanation
    """

    prompt = f"""
You are a conservative AI governance auditor.

Context:
- Multi-Agent Reinforcement Learning (MARL)
- 6G cloud–edge–IoT orchestration simulator
- The LLM has ZERO control authority

Observed State Summary:
{json.dumps(state_summary, indent=2)}

Action Executed:
{action}

Reward Decomposition:
{json.dumps(reward_terms, indent=2)}

Uncertainty Estimate:
{uncertainty:.3f}

Policy Health Assessment:
{policy_health}

Tasks:
1. Explain why the chosen action is reasonable given the observed state
2. Evaluate whether abstention (NO_OP) could have reduced risk
3. Identify any stability, safety, or governance concerns
4. Keep analysis factual, conservative, and evidence-based
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are an AI governance auditor. You do not make decisions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
