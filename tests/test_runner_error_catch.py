"""Tests for subprocess error capturing and exit-code propagation."""

import sys
from src.core.runner import execute_command


def test_runner_catches_runtime_error():
    """Verify that a failing command returns non-zero code and captures stderr."""
    cmd = [sys.executable, "-c", "import sys; sys.stderr.write('Fatal gear misalignment'); sys.exit(42)"]
    result = execute_command(cmd, stream_output=False)

    assert result.exit_code == 42
    assert result.succeeded is False
    assert "Fatal gear misalignment" in result.stderr


def test_runner_catches_invalid_syntax():
    """Verify that a syntax error yields non-zero exit code."""
    cmd = [sys.executable, "-c", "def unclosed():"]
    result = execute_command(cmd, stream_output=False)

    assert result.exit_code != 0
    assert result.succeeded is False
    assert ("SyntaxError" in result.stderr) or ("IndentationError" in result.stderr)
