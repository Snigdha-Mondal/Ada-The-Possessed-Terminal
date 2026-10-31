# 🎨 DESIGN SPECIFICATION: The Possessed Terminal (`ada`)
> **Source of Truth**: [`final_ada_preview.html`](file:///c:/Users/snigd/.gemini/antigravity/brain/e1766bd2-d8f9-45b4-b2ed-f23353b4820a/final_ada_preview.html)  
> **Target Audience**: Antigravity IDE AI Agent / Frontend Engineer  
> **Goal**: Refactor the current terminal output to match the agreed visual preview **100% pixel-for-pixel and character-for-character**.

---

## 1. Visual Overview & Layout Anatomy

When a command crashes, the terminal must render the following **exact vertical hierarchy**:

```text
1. [Captured stderr from failed process]
2. [350ms CRT Voltage Flash & Chromatic Aberration Glitch]
3. [Top Rune Border]       : †━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†
4. [Tomb Container Box]    : Blood-red border (#dc2626) on deep crypt background
   ┌────────────────────────────────────────────────────────────────────────┐
   │ [ASCII Portrait Column]        │ [Dialogue & Fix Column]               │
   │        .---.                   │ ✦ THE SPIRIT OF LADY LOVELACE AWAKENS │
   │       /     \                  │ • 1843 Poetical Science • Gemma 2B    │
   │      | () () |  (cyan eyes)    │───────────────────────────────────────│
   │       \  ^  /                  │ "Victorian Byronic diagnosis in       │
   │      .-`---'-.                 │  luminous ectoplasm green..."         │
   │     /  .:::   \                │───────────────────────────────────────│
   │    /  /  ::   \                │ 🩸 Incantation of Exorcism (Fix):     │
   │      '    '   '                │ ➜ git pull --rebase origin main       │
   │   † ADA BYRON †                │                                       │
   │     (1815-1852)                │                                       │
   └────────────────────────────────┴───────────────────────────────────────┘
5. [Bottom Rune Inscription]: ⛧ 🕇 ☥ MORTAL CODE CAN BE REDEEMED ☥ 🕇 ⛧
```

---

## 2. Color Palette (Strict Hex & ANSI TrueColor Codes)

Your terminal renderer must use these **exact hex codes** (or closest 24-bit TrueColor escapes):

| Element | Hex Code | Description | Role in UI |
| :--- | :--- | :--- | :--- |
| **Blood Border** | `#dc2626` | Deep crimson red | Main panel outline & rune brackets |
| **Dark Crypt BG** | `#090508` | Obsidian black-violet | Background fill for the tomb container |
| **Inner Vault BG** | `#030104` | Pitch black | Background for Ada's dialogue quote box |
| **Fix Container BG** | `#120508` | Dried blood maroon | Background box for the fix command |
| **Fix Border** | `#991b1b` | Medium dark red | Border around the fix command box |
| **Ada's Voice** | `#a7f3d0` | Mint ectoplasm green | Lady Lovelace's diagnosis italic text |
| **Phosphor Cyan** | `#00f5d4` | Radiant neon cyan | Ectoplasm eyes `() ()` and fix command `➜` |
| **Header Accent** | `#f87171` | Light blood red | `✦ THE SPIRIT OF LADY LOVELACE AWAKENS` |
| **Muted Meta** | `#7f1d1d` | Subdued dark red | Subtitle `• 1843 Poetical Science` & runes |

---

## 3. The Physical CRT Glitch Specification (Exact Timing: 360ms)

Do not skip or overcomplicate this. In the real terminal, the glitch occurs immediately after `stderr` prints and before the tomb panel renders.

### The 3 Stages of the Glitch:

1. **Stage 1: Voltage Inversion Flash (0ms – 60ms)**
   - Invert screen colors using ANSI reverse video: `\x1b[7m\x1b[38;5;196m`
   - Hide cursor: `\x1b[?25l`
   - Sleep: `60ms`

2. **Stage 2: Horizontal Chromatic Tear (60ms – 260ms)**
   - Print 2 lines of corrupted half-block static in alternating Red (`\x1b[38;5;196m`) and Cyan (`\x1b[38;5;51m`):
     ```text
     ▓▒░ CRITICAL_SYNC_TEAR :: COIL_VOLTAGE_FAULT 0x00DEAD ▓▒░
     ░▒▓ MEMORY_SPACE_CORRUPT :: BYRONIC_DRAIN_SIGSEGV ▓▒░
     ```
   - Sleep: `50ms` per line.

3. **Stage 3: Settle & Snap (260ms – 360ms)**
   - Reset terminal attributes: `\x1b[0m`
   - Clear glitch lines: `\x1b[2K`
   - Restore cursor: `\x1b[?25h`
   - Sleep: `100ms` before rendering the tomb panel.

---

## 4. The Exact ASCII Portrait (Lady Lovelace Veiled)

Use this exact monospace character block for the left column:

```text
     .---.
    /     \
   | () () |
    \  ^  /
   .-`---'-.
  /  .:::   \
 /  /  ::   \
   '    '   '
† ADA BYRON †
  (1815-1852)
```

### Styling Rules for the Portrait:
- The body, veil, and name (`† ADA BYRON † (1815-1852)`) are rendered in **Light Blood Red (`#f87171`)**.
- The two hollow eyes `() ()` are rendered in **Phosphor Cyan (`#00f5d4`)** to represent her spectral ectoplasm gaze.

---

## 5. The Exact Layout & Typography Rules

### A. The Top Rune Marker
Placed centered immediately above the portrait and dialogue:
```text
†━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†
```
- Style: Dim Red (`#991b1b`)

### B. The Header Line
```text
✦ THE SPIRIT OF LADY LOVELACE AWAKENS    • 1843 Poetical Science • Gemma 2B
```
- Left Title: Bold Red (`#f87171`)
- Right Subtitle: Muted Red (`#7f1d1d`)

### C. The Victorian Diagnosis (Ada's Voice)
Rendered inside an inner indented block or quote box:
```text
"Mr. Babbage and I devised brass gears to weave algebraic truths as the Jacquard loom weaves flowers. Yet here, in your modern silicon, your loom attempts to weave with an empty spindle! You sought 'coefficients' upon a void that has not yet been given breath. Seek line 42, initialize your array, and respect the laws of the machine."
```
- Font Style: **Italic**
- Color: **Ectoplasm Green (`#a7f3d0`)**
- Quotation Marks: Always enclose her speech in double quotation marks.

### D. The Incantation of Exorcism (The Fix Box)
Rendered inside a dedicated inner panel with a maroon border (`#991b1b`):
```text
🩸 Incantation of Exorcism (Fix):
➜ git diff calculate_bernoulli.js -L 40,45
```
- Label: Bold Red (`#f87171`) with blood drop emoji `🩸`
- Fix Command: Bold Phosphor Cyan (`#00f5d4`) preceded by `➜ `
- **CRITICAL**: Do **NOT** include `[Press ENTER to run]` or any prompt asking the user to press a key. The command must be clean, static, and immediately selectable.

### E. The Bottom Rune Sigil
Placed centered at the very bottom of the panel:
```text
⛧ 🕇 ☥ MORTAL CODE CAN BE REDEEMED ☥ 🕇 ⛧
```
- Style: Dim Red (`#7f1d1d`)

---

## 6. Implementation Template in Python (`rich` library)

If using Python with `rich`, here is the exact code structure to achieve this layout:

```python
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def render_ada_tomb(diagnosis: str, fix_cmd: str):
    # 1. Build Left Column (ASCII Portrait)
    portrait_text = Text()
    portrait_text.append("     .---.     \n", style="bold #f87171")
    portrait_text.append("    /     \\    \n", style="bold #f87171")
    portrait_text.append("   | ", style="bold #f87171")
    portrait_text.append("() ()", style="bold #00f5d4")  # Cyan eyes
    portrait_text.append(" |   \n", style="bold #f87171")
    portrait_text.append("    \\  ^  /    \n", style="bold #f87171")
    portrait_text.append("   .-`---'-.   \n", style="bold #f87171")
    portrait_text.append("  /  .:::   \\  \n", style="bold #f87171")
    portrait_text.append(" /  /  ::   \\  \n", style="bold #f87171")
    portrait_text.append("   '    '   '  \n", style="bold #f87171")
    portrait_text.append(" † ADA BYRON † \n", style="bold #fca5a5")
    portrait_text.append("  (1815-1852)  ", style="dim #f87171")

    # 2. Build Right Column (Dialogue + Clean Fix)
    right_content = Table.grid(padding=(0, 0))
    right_content.add_row(
        Text("✦ THE SPIRIT OF LADY LOVELACE AWAKENS", style="bold #f87171"),
        Text(" • 1843 Poetical Science", style="dim #991b1b")
    )
    right_content.add_row(Text("─" * 54, style="dim #7f1d1d"), Text(""))
    
    # Diagnosis
    diag_text = Text(f'\n"{diagnosis}"\n', style="italic #a7f3d0")
    right_content.add_row(diag_text, Text(""))

    # Clean Fix Box (No [Press ENTER])
    fix_panel_text = Text()
    fix_panel_text.append("🩸 Incantation of Exorcism (Fix):\n", style="bold #f87171")
    fix_panel_text.append(f"➜ {fix_cmd}", style="bold #00f5d4")

    fix_panel = Panel(
        fix_panel_text,
        border_style="bold #991b1b",
        style="on #120508",
        padding=(0, 1)
    )
    right_content.add_row(fix_panel, Text(""))

    # 3. Combine Left & Right in Master Table Grid
    master_grid = Table.grid(padding=(0, 2))
    master_grid.add_column(justify="center", vertical="top")
    master_grid.add_column(vertical="top")
    master_grid.add_row(portrait_text, right_content)

    # 4. Wrap Everything in Master Tomb Panel
    full_tomb = Table.grid(padding=(0, 0))
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
```

---

## 7. Refactoring Checklist for Antigravity IDE

Instruct your agent to check off these items:

- [ ] **Glitch Verified**: 350ms voltage inversion flash + 2 lines of chromatic static before the panel prints.
- [ ] **Colors Checked**:
  - Main border is blood-crimson `#dc2626`.
  - Portrait eyes are phosphor cyan `#00f5d4`.
  - Diagnosis text is italic ectoplasm green `#a7f3d0`.
  - Fix command is bold cyan `#00f5d4` on dark maroon `#120508`.
- [ ] **Layout Checked**:
  - Two-column grid: ASCII portrait on the left, dialogue + fix box on the right.
  - Top runes (`†━━━ ⚰ ━━━ † ━━━ ⚰ ━━━†`) present and centered.
  - Bottom runes (`⛧ 🕇 ☥ MORTAL CODE CAN BE REDEEMED ☥ 🕇 ⛧`) present and centered.
- [ ] **Clean Fix Box**:
  - No `[Press ENTER to run]` or interactive prompts.
  - Clean `➜ <command>` ready for selection.
- [ ] **Silent on Success**:
  - When exit code is 0, nothing prints.
