"""Rich TrueColor gothic tomb terminal renderer conforming to DESIGN.md specification."""

import sys
from enum import Enum
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .ascii_art import build_lady_lovelace_portrait

# Force UTF-8 stream reconfigure on Windows consoles to support rune glyphs
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


class OccultTier(Enum):
    """Occult failure classification tiers."""
    TIER_1 = (1, "Minor Poltergeist", "#f59e0b", "✦")
    TIER_2 = (2, "Malicious Daemon", "#c084fc", "❖")
    TIER_3 = (3, "Demonic Possession", "#dc2626", "☠")
    TIER_4 = (4, "Abyssal Cataclysm", "#f43f5e", "⚡")

    def __init__(self, level: int, title: str, color_hex: str, symbol: str):
        self.level = level
        self.tier_title = title
        self.color_hex = color_hex
        self.symbol = symbol


# Shared Console instance configured for TrueColor
console = Console(highlight=False, legacy_windows=False)


def render_autopsy_panel(
    diagnosis: str,
    fix: str,
    tier: Optional[OccultTier] = None,
    command: Optional[str] = None,
    exit_code: int = 1,
    is_fallback: bool = False
) -> None:
    """
    Renders the exact tomb container layout specified in DESIGN.md:
    - Top Rune Border: †━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†
    - Blood-red container border (#dc2626) on obsidian crypt background (#090508)
    - Left column: Veiled Ada Byron ASCII portrait with phosphor cyan spectral eyes
    - Right column: Header, italic ectoplasm green diagnosis, and clean fix panel
    - Bottom Rune Sigil: ⛧ 🕇 ☥ MORTAL CODE CAN BE REDEEMED ☥ 🕇 ⛧
    """
    # 1. Build Left Column (ASCII Portrait)
    portrait_text = build_lady_lovelace_portrait()

    # 2. Build Right Column (Dialogue + Clean Fix)
    header_line = Text()
    header_line.append("✦ THE SPIRIT OF LADY LOVELACE AWAKENS", style="bold #f87171")
    header_line.append("  • 1843 Poetical Science • Gemma 2B", style="dim #991b1b")

    right_content = Table.grid(padding=(0, 0), expand=True)
    right_content.add_column(ratio=1)
    right_content.add_row(header_line)
    right_content.add_row(Text("─" * 60, style="dim #7f1d1d"))

    # Diagnosis: enclosed in quotes, italic ectoplasm green (#a7f3d0)
    clean_diag = diagnosis.strip().strip('"')
    diag_text = Text(f'\n"{clean_diag}"\n', style="italic #a7f3d0")
    right_content.add_row(diag_text)

    # Clean Fix Box (No [Press ENTER] or interactive clutter)
    fix_panel_text = Text()
    fix_panel_text.append("🩸 Incantation of Exorcism (Fix):\n", style="bold #f87171")
    fix_cmd = fix.strip()
    fix_panel_text.append(f"➜ {fix_cmd}", style="bold #00f5d4")

    fix_panel = Panel(
        fix_panel_text,
        border_style="bold #991b1b",
        style="on #120508",
        padding=(0, 1)
    )
    right_content.add_row(fix_panel)

    # 3. Combine Left & Right in Master Table Grid
    master_grid = Table.grid(padding=(0, 2), expand=True)
    master_grid.add_column(width=18, justify="center", vertical="top")
    master_grid.add_column(ratio=1, vertical="top")
    master_grid.add_row(portrait_text, right_content)

    # 4. Wrap Everything in Master Tomb Panel with Runes
    full_tomb = Table.grid(padding=(0, 0), expand=True)
    full_tomb.add_column(ratio=1)
    full_tomb.add_row(Text("†━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†\n", style="dim #991b1b", justify="center"))
    full_tomb.add_row(master_grid)
    full_tomb.add_row(Text("\n⛧ 🕇 ☥ MORTAL CODE CAN BE REDEEMED ☥ 🕇 ⛧", style="dim #7f1d1d", justify="center"))

    main_panel = Panel(
        full_tomb,
        title="[bold red]☠ SÉANCE OF THE ANALYTICAL VOID ☠[/bold red]",
        subtitle="[dim red]Gemma-2 Open-Weights • Zero Cloud Telemetry[/dim red]",
        border_style="bold #dc2626",
        style="on #090508",
        padding=(1, 2)
    )

    console.print()
    console.print(main_panel)
    console.print()
