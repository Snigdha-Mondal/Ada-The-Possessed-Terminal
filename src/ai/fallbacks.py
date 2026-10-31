"""Deterministic fallback oracles and occult tier classifier for Ada: The Possessed Terminal."""

import re
from dataclasses import dataclass
from typing import Optional
from src.visual.renderer import OccultTier


@dataclass
class ExorcismResult:
    """Diagnostic autopsy and fix incantation produced by AI or fallback oracle."""
    diagnosis: str
    fix: str
    tier: OccultTier
    is_fallback: bool = False


def classify_occult_tier(stderr_trace: str, exit_code: int) -> OccultTier:
    """Classifies terminal failures into distinct necromantic tiers based on error signatures."""
    trace_lower = stderr_trace.lower()

    # Tier 4: Abyssal Cataclysm
    if any(k in trace_lower for k in ["out of memory", "oom", "core dump", "kernel panic", "sigkill", "stack overflow"]):
        return OccultTier.TIER_4

    # Tier 3: Demonic Possession
    if any(k in trace_lower for k in [
        "cannot read propert", "nullpointer", "null pointer", "undefined is not",
        "unwrap() on a none value", "panicked at", "sigsegv", "typeerror",
        "attributeerror", "segmentation fault"
    ]):
        return OccultTier.TIER_3

    # Tier 2: Malicious Daemon
    if any(k in trace_lower for k in [
        "eaddrinuse", "port ", "address already in use", "connection refused",
        "merge conflict", "divergent branches", "permission denied", "eacces",
        "lockfile", "resource temporarily unavailable"
    ]):
        return OccultTier.TIER_2

    # Tier 1: Minor Poltergeist (Syntax / Indentation / Typos)
    if any(k in trace_lower for k in [
        "syntaxerror", "indentationerror", "unexpected token", "unclosed",
        "missing semicolon", "invalid syntax", "command not found"
    ]) or exit_code in [127, 2]:
        return OccultTier.TIER_1

    # Default based on exit code severity
    if exit_code > 128:
        return OccultTier.TIER_3
    return OccultTier.TIER_2


def get_fallback_exorcism(command: str, stderr_trace: str, exit_code: int) -> ExorcismResult:
    """
    Provides an instant (0ms latency) deterministic Byronic diagnosis and shell fix
    when the local Gemma model is cold, unreachable, or times out.
    """
    tier = classify_occult_tier(stderr_trace, exit_code)
    trace_lower = stderr_trace.lower()

    # 1. Git Divergent Branches / Merge Conflicts
    if "conflict" in trace_lower or "non-fast-forward" in trace_lower or "divergent" in trace_lower:
        return ExorcismResult(
            diagnosis="Two willful operators have woven discordant patterns upon the same warp. Babbage's engine cannot reconcile such divided intentions without an orderly re-threading of the commits.",
            fix="git status && git pull --rebase origin main",
            tier=OccultTier.TIER_2,
            is_fallback=True
        )

    # 2. Port Collisions (EADDRINUSE)
    port_match = re.search(r":(\d{2,5})\b", stderr_trace)
    port_str = port_match.group(1) if port_match else "8080"
    if "eaddrinuse" in trace_lower or "address already in use" in trace_lower:
        return ExorcismResult(
            diagnosis=f"A phantom process already occupies port {port_str}. One cannot seat two spirits upon the same velvet stool without unseating the squatter first.",
            fix=f"netstat -ano | findstr :{port_str}" if "win" in stderr_trace.lower() else f"lsof -i :{port_str}",
            tier=OccultTier.TIER_2,
            is_fallback=True
        )

    # 3. Python ModuleNotFoundError
    mod_match = re.search(r"No module named ['\"]([^'\"]+)['\"]", stderr_trace)
    if mod_match:
        mod_name = mod_match.group(1)
        return ExorcismResult(
            diagnosis=f"A spindle in your loom calls for a thread of '{mod_name}' not present in your basket. Your engine searches in vain for an unspun module.",
            fix=f"pip install {mod_name}",
            tier=OccultTier.TIER_1,
            is_fallback=True
        )

    # 4. Python IndentationError / SyntaxError
    if "indentationerror" in trace_lower:
        return ExorcismResult(
            diagnosis="The punch card is mis-drilled; an unindented row has disrupted the harmony of the Analytical Engine's teeth.",
            fix="python -m py_compile " + (command.split()[-1] if command else "app.py"),
            tier=OccultTier.TIER_1,
            is_fallback=True
        )

    if "syntaxerror" in trace_lower:
        return ExorcismResult(
            diagnosis="Your mathematical formula contains a discordant symbol. The grammar of your cards defies the mechanical logic of Babbage's mill.",
            fix=f"python -m py_compile {command.split()[-1] if command else 'main.py'}",
            tier=OccultTier.TIER_1,
            is_fallback=True
        )

    # 5. JavaScript / Node.js Null or Undefined Dereference
    if "cannot read propert" in trace_lower or "undefined is not" in trace_lower:
        return ExorcismResult(
            diagnosis="Your calculation reached into the ether expecting a brass cylinder, yet grasped upon a vacant void. A variable was queried before existence was bestowed upon it.",
            fix="node --inspect " + (command if command else "index.js"),
            tier=OccultTier.TIER_3,
            is_fallback=True
        )

    # 6. Command Not Found (Exit code 127)
    if exit_code == 127 or "command not found" in trace_lower or "is not recognized" in trace_lower:
        cmd_first = command.split()[0] if command else "command"
        return ExorcismResult(
            diagnosis=f"You utter the incantation '{cmd_first}', but no lever in this operating chamber answers to that name. Verify whether this tool is installed upon your system's PATH.",
            fix=f"where {cmd_first}" if "win" in stderr_trace.lower() else f"which {cmd_first}",
            tier=OccultTier.TIER_1,
            is_fallback=True
        )

    # 7. Permission Denied
    if "permission denied" in trace_lower or "eacces" in trace_lower:
        return ExorcismResult(
            diagnosis="The iron gate remains firmly barred against your advance. The chamber demands higher authority or an altered key before admitting your instructions.",
            fix=f"chmod +x {command.split()[-1]}" if "/" in command else f"runas /user:Administrator {command}",
            tier=OccultTier.TIER_2,
            is_fallback=True
        )

    # 8. Out of Memory
    if "out of memory" in trace_lower or "oom" in trace_lower:
        return ExorcismResult(
            diagnosis="The storehouse of memory has overflowed its banks. Babbage's brass columns cannot accommodate this torrent of data without expanded physical apparatus.",
            fix="top -o %MEM" if "/" in command else "Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5",
            tier=OccultTier.TIER_4,
            is_fallback=True
        )

    # Generic Fallback
    return ExorcismResult(
        diagnosis="The machine shuddered and threw its calculating gears out of alignment. A discordance in the arithmetic sequence halted the mill without yielding its secret.",
        fix=f"{command} --verbose" if command else "git status",
        tier=tier,
        is_fallback=True
    )
