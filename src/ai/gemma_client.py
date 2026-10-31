"""Local Ollama client for Google Gemma 2 inference in Ada: The Possessed Terminal."""

import json
import re
import logging
from typing import Optional
import httpx

from .prompts import BYRONIC_SYSTEM_PROMPT, build_exorcism_prompt
from .fallbacks import ExorcismResult, get_fallback_exorcism, classify_occult_tier
from src.core.sanitizer import sanitize_trace

logger = logging.getLogger("ada.ai")


def diagnose_failure_with_gemma(
    command: str,
    stderr_trace: str,
    exit_code: int = 1,
    endpoint: str = "http://localhost:11434/api/generate",
    model: str = "gemma2:2b",
    timeout_seconds: float = 6.0
) -> ExorcismResult:
    """
    Invokes local Google Gemma 2 via Ollama to generate an authentic 1843 Byronic diagnosis
    and precise shell fix. If Ollama is offline or times out, seamlessly falls back to
    the deterministic fallback oracle.

    Args:
        command: The failed command string.
        stderr_trace: Raw standard error stream from the process.
        exit_code: Process exit code.
        endpoint: Ollama HTTP generation endpoint.
        model: Target model name (default: gemma2:2b).
        timeout_seconds: Maximum wait time before triggering instant fallback oracle.

    Returns:
        ExorcismResult containing diagnosis, fix, tier, and fallback flag.
    """
    sanitized_trace = sanitize_trace(stderr_trace)
    tier = classify_occult_tier(sanitized_trace, exit_code)
    user_prompt = build_exorcism_prompt(command, sanitized_trace)

    payload = {
        "model": model,
        "prompt": user_prompt,
        "system": BYRONIC_SYSTEM_PROMPT,
        "stream": False,
        "format": "json",
        "options": {
            "temperature": 0.3,
            "top_p": 0.9,
            "num_predict": 150
        }
    }

    try:
        with httpx.Client(timeout=timeout_seconds) as client:
            response = client.post(endpoint, json=payload)
            if response.status_code == 200:
                data = response.json()
                raw_response = data.get("response", "").strip()

                # Parse and validate structured JSON
                diagnosis = ""
                fix = ""

                # Strip possible markdown code fence wrappers
                cleaned_json = raw_response
                if cleaned_json.startswith("```"):
                    cleaned_json = re.sub(r"^```(?:json)?\s*", "", cleaned_json)
                    cleaned_json = re.sub(r"\s*```$", "", cleaned_json)

                try:
                    parsed = json.loads(cleaned_json)
                    diagnosis = parsed.get("diagnosis", "").strip()
                    fix = parsed.get("fix", "").strip()
                except json.JSONDecodeError:
                    # Attempt regex extraction if JSON is slightly malformed
                    diag_match = re.search(r'"diagnosis"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"', raw_response)
                    fix_match = re.search(r'"fix"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"', raw_response)
                    if diag_match:
                        diagnosis = diag_match.group(1).encode().decode('unicode_escape')
                    if fix_match:
                        fix = fix_match.group(1).encode().decode('unicode_escape')

                # Clean markdown from fix if model generated it
                if fix:
                    fix = re.sub(r"^```[a-z]*\n?", "", fix).strip("` \n")

                if diagnosis and fix:
                    return ExorcismResult(
                        diagnosis=diagnosis,
                        fix=fix,
                        tier=tier,
                        is_fallback=False
                    )

    except (httpx.ConnectError, httpx.TimeoutException, httpx.RequestError) as err:
        logger.debug(f"Ollama local connection failed or timed out ({err}); invoking deterministic oracle.")
    except (json.JSONDecodeError, KeyError, ValueError) as json_err:
        logger.debug(f"Gemma output schema validation error ({json_err}); invoking deterministic oracle.")
    except Exception as exc:
        logger.debug(f"Unexpected AI client error ({exc}); invoking deterministic oracle.")

    # Seamless instant fallback oracle
    return get_fallback_exorcism(command, sanitized_trace, exit_code)
