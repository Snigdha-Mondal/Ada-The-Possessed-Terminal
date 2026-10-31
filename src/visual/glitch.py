"""ANSI CRT Hardware Glitch Engine conforming to DESIGN.md specification."""

import os
import sys
import time
import atexit
import signal

_TERMINAL_RESTORED = False


def restore_terminal_state() -> None:
    """Restores normal terminal attributes, resets styling, and ensures cursor visibility."""
    global _TERMINAL_RESTORED
    if _TERMINAL_RESTORED:
        return
    try:
        sys.stdout.write("\x1b[0m\x1b[?25h")
        sys.stdout.flush()
    except Exception:
        pass
    _TERMINAL_RESTORED = True


def _signal_handler(signum, frame):
    """Handles SIGINT/SIGTERM gracefully during glitch execution."""
    restore_terminal_state()
    sys.exit(130 if signum == signal.SIGINT else 143)


atexit.register(restore_terminal_state)
try:
    signal.signal(signal.SIGINT, _signal_handler)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, _signal_handler)
except Exception:
    pass


def trigger_crt_glitch(duration_ms: int = 360, disable_if_no_tty: bool = True) -> None:
    """
    Executes the exact 3-stage CRT physical glitch specified in DESIGN.md:
    1. Voltage Inversion Flash (0ms - 60ms)
    2. Horizontal Chromatic Tear (60ms - 260ms)
    3. Settle & Snap (260ms - 360ms)
    """
    if disable_if_no_tty:
        if not sys.stdout.isatty() or os.getenv("CI") or os.getenv("NO_COLOR"):
            return

    global _TERMINAL_RESTORED
    _TERMINAL_RESTORED = False

    try:
        # Stage 1: Voltage Inversion Flash (0ms - 60ms)
        # Hide cursor & invert screen colors (reverse video with crimson)
        sys.stdout.write("\x1b[?25l\x1b[7m\x1b[38;5;196m")
        sys.stdout.flush()
        time.sleep(0.06)

        # Stage 2: Horizontal Chromatic Tear (60ms - 260ms)
        sys.stdout.write("\x1b[0m\n")
        # Line 1: Corrupted red/cyan static
        sys.stdout.write("\x1b[38;5;196m▓▒░ \x1b[38;5;51mCRITICAL_SYNC_TEAR :: COIL_VOLTAGE_FAULT 0x00DEAD \x1b[38;5;196m▓▒░\x1b[0m\n")
        sys.stdout.flush()
        time.sleep(0.05)

        # Line 2: Memory space corruption
        sys.stdout.write("\x1b[38;5;51m░▒▓ \x1b[38;5;196mMEMORY_SPACE_CORRUPT :: BYRONIC_DRAIN_SIGSEGV \x1b[38;5;51m▓▒░\x1b[0m\n")
        sys.stdout.flush()
        time.sleep(0.05)

        # Stage 3: Settle & Snap (260ms - 360ms)
        # Clear glitch lines and reset
        sys.stdout.write("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\r\x1b[0m\x1b[?25h")
        sys.stdout.flush()
        time.sleep(0.10)

    except Exception:
        pass
    finally:
        restore_terminal_state()
