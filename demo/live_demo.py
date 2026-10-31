#!/usr/bin/env python3
"""
Interactive Live Demonstration — Ada: The Possessed Terminal
Step through the 5 acts of terminal exorcism with visual commentary.
"""

import os
import sys
import time
import subprocess

# Ensure repository root is in sys.path so 'src' can be imported anywhere
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

# Ensure UTF-8 output across all consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.visual.glitch import trigger_crt_glitch
from src.visual.renderer import render_autopsy_panel, OccultTier
from src.core.sanitizer import mask_secret_tokens

console = Console(highlight=False, legacy_windows=False, safe_box=True)


def banner():
    console.clear()
    banner_text = Text()
    banner_text.append("[*] ADA: THE POSSESSED TERMINAL [*]\n", style="bold red")
    banner_text.append("Live Demonstration Séance\n", style="italic #a7f3d0")
    banner_text.append("Honoring Augusta Ada Lovelace & Google Gemma 2 (Local Open-Weights)", style="dim white")
    panel = Panel(banner_text, border_style="bold red", padding=(1, 2))
    console.print(panel)
    console.print()


def pause(prompt_text: str = "Press [ENTER] to continue..."):
    console.print(f"[bold yellow]> {prompt_text}[/]", end="")
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        console.print("\n[dim]Séance concluded.[/]")
        sys.exit(0)
    console.print()


def act_1_silent_success():
    console.print("[bold cyan]══════ ACT 1: THE SILENT GUARANTEE (Exit Code 0) ══════[/]")
    console.print("[dim]When commands succeed, Ada stays 100% invisible. Zero latency, zero clutter.[/]")
    pause("Run: 'ada echo \"Compilation succeeded cleanly!\"'")

    cmd = [sys.executable, "-m", "src.ada", "echo", "Compilation succeeded cleanly!"]
    subprocess.run(cmd)

    console.print("[bold green]✔ Notice: Zero gothic panels, zero noise. Invisible in daily workflow.[/]\n")


def act_2_crt_glitch():
    console.print("[bold cyan]══════ ACT 2: THE 350ms CRT VOLTAGE GLITCH ══════[/]")
    console.print("[dim]Simulates hardware screen color inversion and chromatic scanline tear on crash.[/]")
    pause("Trigger CRT voltage glitch...")

    trigger_crt_glitch(duration_ms=450, disable_if_no_tty=False)

    console.print("[bold green]✔ The terminal shuddered, flashed reverse-video, and restored safely.[/]\n")


def act_3_syntax_autopsy():
    console.print("[bold cyan]══════ ACT 3: BYRONIC AUTOPSY (Python Syntax Error) ══════[/]")
    console.print("[dim]Lady Lovelace diagnoses broken code through Babbage's mechanical loom metaphors.[/]")
    pause("Run broken python script: 'ada python tests/fixtures/syntax_error.py'")

    fixture_path = os.path.join(os.path.dirname(__file__), "..", "tests", "fixtures", "syntax_error.py")
    cmd = [sys.executable, "-m", "src.ada", sys.executable, fixture_path]
    subprocess.run(cmd)

    console.print("[bold green]✔ High-contrast phosphor cyan Incantation of Exorcism displayed for human review.[/]\n")


def act_4_git_conflict():
    console.print("[bold cyan]══════ ACT 4: MALICIOUS DAEMON (Git Divergent Conflict) ══════[/]")
    console.print("[dim]Categorized as Tier 2 (Violet). Diagnoses two operators weaving discordant tapestries.[/]")
    pause("Simulate git push rejection...")

    cmd = [
        sys.executable, "-m", "src.ada",
        sys.executable, "-c",
        "import sys; sys.stderr.write('fatal: refusing to merge unrelated histories\\n'); sys.exit(1)"
    ]
    subprocess.run(cmd)

    console.print("[bold green]✔ Clean git fix suggested without disrupting normal terminal session.[/]\n")


def act_5_secret_masking():
    console.print("[bold cyan]══════ ACT 5: AIR-GAPPED PRIVACY & ZERO LEAKS ══════[/]")
    console.print("[dim]AWS keys, Bearer tokens, and usernames are scrubbed BEFORE any reasoning.[/]")

    leaky_trace = "Failed AWS S3 call with key AKIAIOSFODNN7EXAMPLE and Bearer eyJhbGciOiJIUzI1Ni in /Users/snigdha/secret/config.json"
    console.print(f"[bold red]Raw Crash Log with Secrets:[/]\n  {leaky_trace}\n")

    sanitized = mask_secret_tokens(leaky_trace)
    console.print(f"[bold green]Sanitized Trace Seen by Gemma 2:[/]\n  {sanitized}\n")

    console.print("[bold green]✔ 100% Local-first. Zero bytes leave your machine.[/]\n")


def main():
    banner()
    act_1_silent_success()
    act_2_crt_glitch()
    act_3_syntax_autopsy()
    act_4_git_conflict()
    act_5_secret_masking()

    console.print("[bold red]═════════════════════════════════════════════════════════════════[/]")
    console.print("[bold #00f5d4]✦ SÉANCE COMPLETE — ADA IS READY FOR THE HACKTOBERFEST MVP ✦[/]")
    console.print("[dim white]You can now wrap any terminal command in everyday development: 'ada <command>'[/]")
    console.print("[bold red]═════════════════════════════════════════════════════════════════[/]\n")


if __name__ == "__main__":
    main()
