"""ASCII artwork and portrait definitions conforming to DESIGN.md specification."""

from rich.text import Text


def build_lady_lovelace_portrait() -> Text:
    """
    Builds the exact monospace Lady Lovelace portrait with cyan spectral eyes
    as defined in DESIGN.md Section 4.
    """
    portrait_text = Text()
    portrait_text.append("     .---.     \n", style="bold #f87171")
    portrait_text.append("    /     \\    \n", style="bold #f87171")
    portrait_text.append("   | ", style="bold #f87171")
    portrait_text.append("() ()", style="bold #00f5d4")  # Phosphor Cyan spectral gaze
    portrait_text.append(" |   \n", style="bold #f87171")
    portrait_text.append("    \\  ^  /    \n", style="bold #f87171")
    portrait_text.append("   .-`---'-.   \n", style="bold #f87171")
    portrait_text.append("  /  .:::   \\  \n", style="bold #f87171")
    portrait_text.append(" /  /  ::   \\  \n", style="bold #f87171")
    portrait_text.append("   '    '   '  \n", style="bold #f87171")
    portrait_text.append(" † ADA BYRON † \n", style="bold #fca5a5")
    portrait_text.append("  (1815-1852)  ", style="dim #f87171")
    return portrait_text


LADY_LOVELACE_ASCII = """
     .---.
    /     \\
   | () () |
    \\  ^  /
   .-`---'-.
  /  .:::   \\
 /  /  ::   \\
   '    '   '
† ADA BYRON †
  (1815-1852)
"""

ADAS_SEAL = "†━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†"
