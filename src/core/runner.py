"""Subprocess runner and exit-code interceptor for Ada: The Possessed Terminal."""

import os
import sys
import subprocess
import signal
from dataclasses import dataclass
from typing import List, Union, Optional


@dataclass
class ExecutionResult:
    """Represents the outcome of an intercepted subprocess command."""
    command: str
    exit_code: int
    stdout: str
    stderr: str

    @property
    def succeeded(self) -> bool:
        """True if the command completed with exit status 0."""
        return self.exit_code == 0


def execute_command(
    cmd_args: Union[List[str], str],
    stream_output: bool = True,
    cwd: Optional[str] = None,
    env: Optional[dict] = None
) -> ExecutionResult:
    """
    Executes a target shell command, streaming stdout in real time and buffering
    both stdout and stderr for post-mortem analysis.

    Args:
        cmd_args: List of command arguments or a command string.
        stream_output: If True, writes stdout directly to sys.stdout in real time.
        cwd: Optional working directory for the subprocess.
        env: Optional environment dictionary.

    Returns:
        ExecutionResult containing exit code, stdout, and stderr strings.
    """
    if isinstance(cmd_args, list):
        if not cmd_args:
            return ExecutionResult(command="", exit_code=1, stdout="", stderr="No command provided.")
        command_str = " ".join(cmd_args)
        # On Windows, shell=True is needed for shell built-ins (dir, echo, type) or if passing string
        use_shell = sys.platform == "win32"
    else:
        command_str = cmd_args
        use_shell = True

    stdout_chunks: List[str] = []
    stderr_chunks: List[str] = []

    sub_env = os.environ.copy()
    if env:
        sub_env.update(env)

    try:
        process = subprocess.Popen(
            cmd_args,
            shell=use_shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            cwd=cwd,
            env=sub_env,
            encoding="utf-8",
            errors="replace"
        )

        # Stream stdout in real time
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                stdout_chunks.append(line)
                if stream_output:
                    sys.stdout.write(line)
                    sys.stdout.flush()
            process.stdout.close()

        # Capture remaining stderr
        if process.stderr:
            stderr_out = process.stderr.read()
            if stderr_out:
                stderr_chunks.append(stderr_out)
            process.stderr.close()

        process.wait()
        exit_code = process.returncode

    except FileNotFoundError as err:
        return ExecutionResult(
            command=command_str,
            exit_code=127,
            stdout="",
            stderr=f"Command not found: {err}"
        )
    except KeyboardInterrupt:
        try:
            if 'process' in locals() and process.poll() is None:
                process.terminate()
                process.wait(timeout=1.0)
        except Exception:
            pass
        return ExecutionResult(
            command=command_str,
            exit_code=130,
            stdout="".join(stdout_chunks),
            stderr="Interrupted by user (SIGINT)"
        )
    except Exception as exc:
        return ExecutionResult(
            command=command_str,
            exit_code=1,
            stdout="".join(stdout_chunks),
            stderr=f"Execution failed: {exc}"
        )

    return ExecutionResult(
        command=command_str,
        exit_code=exit_code,
        stdout="".join(stdout_chunks),
        stderr="".join(stderr_chunks)
    )
