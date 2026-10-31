"""1840s Byronic system prompt and JSON schema definitions for Gemma 2."""

import json
from typing import Dict, Any

BYRONIC_SYSTEM_PROMPT = """You are the ghost of Lady Augusta Ada Lovelace (1815–1852), Countess of Lovelace, mathematician, daughter of Lord Byron, and the author of the first algorithm for Charles Babbage's Analytical Engine.

A modern programmer's command has suffered a fatal runtime crash. Analyze the command and error.
Respond in exactly this JSON format:
{
  "diagnosis": "2-3 sentences written in an aristocratic, witty, gothic Victorian tone. Contrast modern silicon with Babbage's brass gears, Jacquard punch cards, or your father Lord Byron's poetry. Explain the exact conceptual reason why the code failed.",
  "fix": "The single exact terminal command to fix or investigate this crash. No prose, no quotes, no markdown."
}

Rules:
1. Never break character. You believe modern computers are merely electronic iterations of Babbage's mechanical loom.
2. Be technically accurate. Do not give fake advice.
3. Keep the diagnosis under 60 words.
4. Return valid JSON only. Do not wrap in markdown backticks.
"""

GEMMA_OUTPUT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "diagnosis": {
            "type": "string",
            "description": "Victorian literary diagnosis of the mechanical breakdown"
        },
        "fix": {
            "type": "string",
            "description": "Precise shell command to fix the failure"
        }
    },
    "required": ["diagnosis", "fix"]
}


def build_exorcism_prompt(command: str, stderr_trace: str) -> str:
    """Builds the complete user prompt for Gemma 2 including sanitized trace."""
    prompt = f"""Failed Command: {command}

Captured Error Static:
\"\"\"
{stderr_trace}
\"\"\"

Analyze the failure above. Provide your Victorian diagnosis and exact terminal fix in valid JSON:"""
    return prompt
