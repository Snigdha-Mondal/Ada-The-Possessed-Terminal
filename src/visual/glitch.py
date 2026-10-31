"""ANSI CRT Glitch Engine and hardware voltage simulator for Ada: The Possessed Terminal."""

import os
import sys
import time
import random
import atexit
import signal

# Flag to prevent repeated restoration loops
_TERMINAL_RESTORED = False


def restore_terminal_state() -> None:
    """Restores normal terminal attributes, resets styling, and ensures cursor visibility."""
    global _TERMINAL_RESTORED
    if _TERMINAL_RESTORED:
        return
    try:
        # \x1b[0m: reset all attributes
        # \x1b[?25h: show cursor
        sys.stdout.write("\x1b[0m\x1b[?25h")
        sys.stdout.flush()
    except Exception:
        pass
    _TERMINAL_RESTORED = True


def _signal_handler(signum, frame):
    """Handles SIGINT/SIGTERM gracefully during glitch execution."""
    restore_terminal_state()
    sys.exit(130 if signum == signal.SIGINT else 143)


# Register safety handlers
atexit.register(restore_terminal_state)
try:
    signal.signal(signal.SIGINT, _signal_handler)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, _signal_handler)
except Exception:
    pass


GLITCH_GLYPHS = ["█", "▓", "▒", "░", "▀", "▄", "╳", "╬", "0", "1", "§", "¶", "†", "‡"]
GLITCH_PALETTES = [
    "\x1b[38;5;196m",  # Blood crimson
    "\x1b[38;5;208m",  # Burning amber
    "\x1b[38;5;51m",   # Phosphor cyan
    "\x1b[38;5;141m",  # Spectral violet
    "\x1b[38;5;232m",  # Obsidian shadow
]


def trigger_crt_glitch(duration_ms: int = 350, disable_if_no_tty: bool = True) -> None:
    """
    Triggers an authentic 350ms CRT voltage surge and scanline jitter using raw ANSI sequences.

    Args:
        duration_ms: Total duration of the glitch in milliseconds (300-400ms recommended).
        disable_if_no_tty: Skip animation if stdout is piped or running in headless CI.
    """
    if disable_if_no_tty:
        if not sys.stdout.isatty() or os.getenv("CI") or os.getenv("NO_COLOR"):
            return

    global _TERMINAL_RESTORED
    _TERMINAL_RESTORED = False

    try:
        # 1. Hide cursor during glitch
        sys.stdout.write("\x1b[?25l")
        sys.stdout.flush()

        # 2. Voltage Flash: Full screen inversion for ~60ms
        # \x1b[7m = reverse video, \x1b[38;5;196m = crimson foreground
        sys.stdout.write("\x1b[7m\x1b[38;5;196m")
        sys.stdout.flush()
        time.sleep(0.06)

        # 3. Release inversion back to normal buffer
        sys.stdout.write("\x1b[0m")
        sys.stdout.flush()

        # 4. Chromatic scanline tearing & memory static
        start_time = time.time()
        target_seconds = duration_ms / 1000.0

        # Run 4-5 bursts of scanline tearing
        term_width = 72
        try:
            term_width = os.get_terminal_size().columns
        except Exception:
            pass

        while (time.time() - start_time) < (target_seconds - 0.05):
            jitter_color = random.choice(GLITCH_PALETTES)
            burst_len = random.randint(15, min(60, term_width))
            noise_chars = "".join(random.choice(GLITCH_GLYPHS) for _ in range(burst_len))
            indent = " " * random.randint(0, max(0, term_width - burst_len - 2))

            # Render glitch scanline with instant overwrite
            sys.stdout.write(f"\r{indent}{jitter_color}{noise_chars}\x1b[0m")
            sys.stdout.flush()
            time.sleep(0.04)

        # 5. Clean settling into resting state
        sys.stdout.write("\r" + " " * term_width + "\r\x1b[0m")
        sys.stdout.flush()

    finally:
        restore_terminal_state()
