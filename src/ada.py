#!/usr/bin/env python3
"""
Ada: The Possessed Terminal — Main CLI Entrypoint
The spirit of Augusta Ada Lovelace, awakened by your compiler errors.
"""

import sys
import os
import argparse
from typing import List

# Ensure UTF-8 output encoding across all platforms (particularly Windows legacy consoles)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from src import __version__
from src.core.runner import execute_command
from src.visual.glitch import trigger_crt_glitch, restore_terminal_state
from src.visual.renderer import render_autopsy_panel, OccultTier
from src.ai.gemma_client import diagnose_failure_with_gemma
from src.ai.fallbacks import get_fallback_exorcism


def build_parser() -> argparse.ArgumentParser:
    """Builds CLI argument parser for Ada."""
    parser = argparse.ArgumentParser(
        prog="ada",
        description="The spirit of the world's first programmer, awakened by your compiler errors.",
        add_help=False
    )
    parser.add_argument(
        "--help", "-h",
        action="store_true",
        help="Show this help message and exit."
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"ada (The Possessed Terminal) v{__version__}"
    )
    parser.add_argument(
        "--no-glitch",
        action="store_true",
        help="Disable the 350ms ANSI CRT hardware voltage glitch animation."
    )
    parser.add_argument(
        "--oracle",
        action="store_true",
        help="Force deterministic offline fallback oracle without contacting local Gemma 2."
    )
    parser.add_argument(
        "--test-tomb",
        action="store_true",
        help="Render a demonstration gothic tomb panel and exit."
    )
    return parser


def run_test_tomb():
    """Renders a sample autopsy panel for demonstration and visual testing."""
    render_autopsy_panel(
        diagnosis=(
            "Your calculation reached into the ether expecting a brass cylinder, yet grasped upon a vacant void. "
            "A spindle in the Jacquard loom was summoned before thread was spun for it; Babbage himself wept over such empty columns."
        ),
        fix="node --inspect app.js",
        tier=OccultTier.TIER_3,
        command="node server.js",
        exit_code=1,
        is_fallback=False
    )


def main(argv: List[str] = None) -> int:
    """Main CLI execution loop."""
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()

    # If no arguments provided, display help
    if not argv:
        parser.print_help()
        print("\nUsage example:")
        print("  ada python broken.py")
        print("  ada git push origin main")
        print("  ada npm run build")
        return 0

    # Handle known diagnostic flags
    known_flags = ["--help", "-h", "--test-tomb", "--version", "-v"]
    if any(arg in known_flags for arg in argv[:2]):
        parsed, remaining = parser.parse_known_args(argv)
        if parsed.help:
            parser.print_help()
            return 0
        if parsed.test_tomb:
            run_test_tomb()
            return 0

    # Parse optional tool flags that may precede the target command
    skip_glitch = False
    force_oracle = False
    cmd_index = 0

    while cmd_index < len(argv) and argv[cmd_index].startswith("--"):
        flag = argv[cmd_index]
        if flag == "--no-glitch":
            skip_glitch = True
            cmd_index += 1
        elif flag == "--oracle":
            force_oracle = True
            cmd_index += 1
        elif flag in ["--help", "-h"]:
            parser.print_help()
            return 0
        elif flag == "--test-tomb":
            run_test_tomb()
            return 0
        else:
            break

    target_cmd = argv[cmd_index:]
    if not target_cmd:
        parser.print_help()
        return 0

    # 1. Execute target command and stream stdout in real-time
    result = execute_command(target_cmd, stream_output=True)

    # 2. Silent success: If exit code is 0, exit immediately with zero output
    if result.succeeded:
        return 0

    # 3. Intercept failure: Trigger 350ms ANSI CRT Glitch
    if not skip_glitch:
        trigger_crt_glitch(duration_ms=350)

    # 4. Perform diagnosis (via local Gemma 2 or fallback oracle)
    if force_oracle:
        exorcism = get_fallback_exorcism(result.command, result.stderr, result.exit_code)
    else:
        exorcism = diagnose_failure_with_gemma(
            command=result.command,
            stderr_trace=result.stderr,
            exit_code=result.exit_code
        )

    # 5. Render Gothic Tomb Terminal Panel
    render_autopsy_panel(
        diagnosis=exorcism.diagnosis,
        fix=exorcism.fix,
        tier=exorcism.tier,
        command=result.command,
        exit_code=result.exit_code,
        is_fallback=exorcism.is_fallback
    )

    # 6. Ensure terminal state is clean and propagate exit code
    restore_terminal_state()
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
