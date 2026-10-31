"""Unit tests for deterministic fallback oracles and occult tier classification."""

from src.ai.fallbacks import classify_occult_tier, get_fallback_exorcism
from src.visual.renderer import OccultTier


def test_classify_tier_syntax_error():
    tier = classify_occult_tier("SyntaxError: invalid syntax", 1)
    assert tier == OccultTier.TIER_1


def test_classify_tier_port_in_use():
    tier = classify_occult_tier("Error: listen EADDRINUSE: address already in use :::3000", 1)
    assert tier == OccultTier.TIER_2


def test_classify_tier_null_pointer():
    tier = classify_occult_tier("TypeError: Cannot read properties of undefined (reading 'calculate')", 1)
    assert tier == OccultTier.TIER_3


def test_classify_tier_oom_crash():
    tier = classify_occult_tier("FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory", 137)
    assert tier == OccultTier.TIER_4


def test_fallback_git_merge_conflict():
    exorcism = get_fallback_exorcism("git merge feature", "error: you have divergent branches and need to specify how to reconcile them", 1)
    assert exorcism.is_fallback is True
    assert "warp" in exorcism.diagnosis.lower() or "babbage" in exorcism.diagnosis.lower()
    assert "rebase" in exorcism.fix.lower() or "status" in exorcism.fix.lower()


def test_fallback_missing_python_module():
    exorcism = get_fallback_exorcism("python train.py", "ModuleNotFoundError: No module named 'torch'", 1)
    assert exorcism.is_fallback is True
    assert "torch" in exorcism.diagnosis.lower()
    assert "pip install torch" in exorcism.fix


def test_fallback_command_not_found():
    exorcism = get_fallback_exorcism("non_existent_tool run", "bash: non_existent_tool: command not found", 127)
    assert exorcism.is_fallback is True
    assert exorcism.tier == OccultTier.TIER_1
    assert "non_existent_tool" in exorcism.diagnosis
