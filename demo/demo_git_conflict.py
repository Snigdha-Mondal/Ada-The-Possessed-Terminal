#!/usr/bin/env python3
"""
Demonstration Script 2: Git Divergent Conflict Exorcism
Simulates a git failure and runs Ada to exorcise the conflict.
"""

import subprocess
import sys
import os

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=================================================================")
print("  [*] ADA: THE POSSESSED TERMINAL -- DEMO 2: GIT DIVERGENT MERGE")
print("  Simulating git rejected push or merge conflict...")
print("=================================================================\n")

# Run simulated git divergence error through ada
simulated_git_cmd = [
    sys.executable, "-m", "src.ada",
    sys.executable, "-c",
    "import sys; sys.stderr.write('fatal: refusing to merge unrelated histories\\nerror: failed to push some refs to remote\\n'); sys.exit(1)"
]

proc = subprocess.run(simulated_git_cmd, cwd=repo_root)
sys.exit(proc.returncode)
