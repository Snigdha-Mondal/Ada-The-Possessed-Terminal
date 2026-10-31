"""Tests for silent success behavior in the runner."""

import sys
from src.core.runner import execute_command


def test_runner_silent_success():
    """Verify that a successful command returns exit code 0 and stdout."""
    # Use python executable to ensure cross-platform execution
    cmd = [sys.executable, "-c", "print('Engine Operational')"]
    result = execute_command(cmd, stream_output=False)

    assert result.exit_code == 0
    assert result.succeeded is True
    assert "Engine Operational" in result.stdout
    assert result.stderr == ""


def test_runner_silent_empty_command():
    """Verify handling of empty command list."""
    result = execute_command([], stream_output=False)
    assert result.exit_code != 0
    assert result.succeeded is False
