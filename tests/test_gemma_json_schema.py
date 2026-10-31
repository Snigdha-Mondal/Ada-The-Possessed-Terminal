"""Tests for Gemma 2 JSON schema enforcement and graceful fallback on malformed response."""

from unittest.mock import patch, MagicMock
import httpx
from src.ai.gemma_client import diagnose_failure_with_gemma
from src.visual.renderer import OccultTier


def test_gemma_valid_json_response():
    """Verify that valid structured JSON from Gemma is properly parsed."""
    mock_payload = {
        "response": '{"diagnosis": "The spindle spins without thread. Babbage would lament such vacant calculation.", "fix": "pip install numpy"}'
    }

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = mock_payload

    with patch("httpx.Client.post", return_value=mock_resp):
        result = diagnose_failure_with_gemma("python script.py", "ModuleNotFoundError: No module named 'numpy'", 1)

    assert result.is_fallback is False
    assert "spindle" in result.diagnosis
    assert result.fix == "pip install numpy"


def test_gemma_fallback_on_invalid_json():
    """Verify that malformed JSON triggers deterministic fallback oracle."""
    mock_payload = {
        "response": 'Here is your advice: just run pip install!'  # Not valid JSON
    }

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = mock_payload

    with patch("httpx.Client.post", return_value=mock_resp):
        result = diagnose_failure_with_gemma("python script.py", "ModuleNotFoundError: No module named 'numpy'", 1)

    # Should gracefully fall back without throwing unhandled exceptions
    assert result.is_fallback is True
    assert "numpy" in result.diagnosis.lower()
    assert "pip install numpy" in result.fix


def test_gemma_fallback_on_network_timeout():
    """Verify that timeout automatically invokes fallback oracle."""
    with patch("httpx.Client.post", side_effect=httpx.TimeoutException("Connection timed out")):
        result = diagnose_failure_with_gemma("git merge", "error: you have divergent branches", 1)

    assert result.is_fallback is True
    assert result.tier == OccultTier.TIER_2
