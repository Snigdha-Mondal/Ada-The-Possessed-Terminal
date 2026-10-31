#!/usr/bin/env python3
"""
Demonstration Script 1: Syntax Crash Exorcism
Runs Ada against an invalid Python syntax fixture.
"""

import subprocess
import sys
import os

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fixture = os.path.join(repo_root, "tests", "fixtures", "syntax_error.py")

print("=================================================================")
print("  [*] ADA: THE POSSESSED TERMINAL -- DEMO 1: SYNTAX CRASH")
print("  Simulating developer running a broken script...")
print("=================================================================\n")

cmd = [sys.executable, "-m", "src.ada", sys.executable, fixture]
proc = subprocess.run(cmd, cwd=repo_root)
sys.exit(proc.returncode)
