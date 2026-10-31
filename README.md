# 🕯️ Ada — The Possessed Terminal

### *The spirit of the world's first programmer, awakened by your compiler errors.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Gemma 2: 2B](https://img.shields.io/badge/AI-Google_Gemma_2_(2B)-orange.svg)](https://ai.google.dev/gemma)
[![Local-First](https://img.shields.io/badge/Privacy-100%25_Air--Gapped-green.svg)](https://github.com/Snigdha-Mondal/Ada-The-Possessed-Terminal)
[![DeftBench AI Loop](https://img.shields.io/badge/Specification-DeftBench_Compliant-purple.svg)](https://github.com/Snigdha-Mondal/Ada-The-Possessed-Terminal)

---

## 1. Overview

Developers live inside the command line, yet the terminal remains cold, unforgiving, and hazardous. Cryptic stack traces, unexpected panics, and merge conflicts break workflow focus. Worse, developers increasingly paste proprietary crash dumps and private file paths into cloud AI chatbots—leaking credentials, tokens, and corporate IP to remote servers.

**`ada`** is a **local-first, necromantic terminal resilience layer**. It wraps any shell command or terminal session and:

* **Stays 100% silent and invisible on successful execution (`exit code 0`)**;
* **Intercepts non-zero exit codes ($? \neq 0$)** before your shell prompt returns;
* **Masks sensitive tokens, credentials, and user home paths** deterministically;
* **Fires a 350ms physical CRT voltage surge and chromatic scanline tear** via raw ANSI escape sequences;
* **Summons the gothic ghost of Augusta Ada Lovelace** via local **Google Gemma 2 (2B)** to diagnose the mechanical root cause in aristocratic 1840s "Poetical Science" prose;
* **Renders an instant Incantation of Exorcism (the clean shell fix)** in high-contrast phosphor cyan (`#00f5d4`);
* **Operates 100% air-gapped** with zero cloud telemetry and sub-second deterministic fallback oracles.

```text
╭─────────── [*] ADA'S AUTOPSY — MINOR POLTERGEIST [Exit Status: 1] ───────────╮
│                                                                              │
│  ╭───────────────────────────── Ada Lovelace ─────────────────────────────╮  │
│  │       .---.                                                            │  │
│  │      /  _  \                                                           │  │
│  │     | (o)(o)|                                                          │  │
│  │     C   _>  D                                                          │  │
│  │      \ === /                                                           │  │
│  │      /`---'\                                                           │  │
│  │     / /| |\ \                                                          │  │
│  │    / / | | \ \                                                         │  │
│  │   (_/  |_|  \_)                                                        │  │
│  │    [1815-1852]                                                         │  │
│  ╰────────────────────────────────────────────────────────────────────────╯  │
│  Afflicted Cmd: python train.py                                              │
│                                                                              │
│  Diagnosis:     Your mathematical formula contains a discordant symbol. The  │
│                 grammar of your cards defies the mechanical logic of         │
│                 Babbage's mill.                                              │
│                                                                              │
│  Exorcism:      ╭──────── -- INCANTATION OF EXORCISM (THE FIX) -- ────────╮  │
│                 │  python -m py_compile train.py                          │  │
│                 ╰─────────────────────────────────────────────────────────╯  │
│                                                                              │
╰─ * 1843 Poetical Science | Google Gemma 2 (2B) Local Inference | Zero Cloud ─╯
```

---

## 2. Why Ada? (Honoring the First Programmer)

Built for **Hacktoberfest's *"Ghost in the Machine"*** and **Día de los Muertos**, `ada` honors **Augusta Ada King, Countess of Lovelace (1815–1852)**, the world's first computer programmer. 

Rather than treating historical pioneers as museum artifacts, `ada` resurrects her sharp Byronic wit, philosophical "Poetical Science," and deep conceptual insights into Babbage's Analytical Engine to fix modern software failures.

| Typical Tool / Cloud AI | `ada` (The Possessed Terminal) |
|---|---|
| Dumps cold, intimidating walls of red stack traces | Transforms crashes into an engaging, literary séance autopsy |
| Exfiltrates private traces to cloud servers | **100% air-gapped inference via Gemma 2** on local silicon |
| Clutters everyday commands | **100% silent on success**; triggers only on failure |
| Generic, robotic corporate tone | Authentic 1840s Byronic Victorian persona |
| Requires cloud subscriptions or API keys | **Free, open-weight, and offline-capable** |
| Multi-second network roundtrip latency | Sub-second inference & 0ms fallback oracles |

---

## 3. High-Level Architecture

```text
┌───────────────────────────────────────┐
│     User runs: ada <command>          │
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│      Subprocess Execution Layer       │  streams stdout live, buffers stderr
└──────────────────┬────────────────────┘
                   │
         Exit Code == 0? ──► YES ──► Exit cleanly & silently (0 overhead)
                   │
                   NO ($? != 0)
                   ▼
┌───────────────────────────────────────┐
│     Deterministic Secret Masker       │  strips API keys, paths, tokens
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│     ANSI CRT Glitch Engine (350ms)    │  voltage flash, chromatic scanline tear
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│      Local Gemma 2 Engine (Ollama)    │  HTTP http://localhost:11434/api/generate
└─────────┬───────────────────┬─────────┘  with gemma2:2b & 1843 Byronic system prompt
          │ (Success)         │ (Ollama down / timeout)
          v                   v
┌──────────────────┐  ┌─────────────────┐
│ JSON Parser      │  │ Fallback Oracle │  instant 0ms deterministic recovery
└─────────┬────────┘  └───────┬─────────┘
          │                   │
          └─────────┬─────────┘
                    v
┌───────────────────────────────────────┐
│      Gothic Tomb Terminal Panel       │  blood-red border, ASCII portrait
│      • Lady Lovelace Diagnosis        │  ectoplasm green (#a7f3d0)
│      • Incantation of Exorcism        │  clean phosphor cyan (#00f5d4)
└───────────────────────────────────────┘
```

---

## 4. Necromantic Severity Tiers

Failures are dynamically classified into 4 distinct occult severity tiers:

* **Tier 1 (Minor Poltergeist)**: Syntax errors, unclosed quotes, indentation mistakes. Visual motif: Amber scanline jitter (`#f59e0b`).
* **Tier 2 (Malicious Daemon)**: Port collisions (`EADDRINUSE`), lockfile conflicts, Git divergence, 404s. Visual motif: Violet spectral split (`#c084fc`).
* **Tier 3 (Demonic Possession)**: Null pointer dereferences, unwrapped Option panics, segfaults. Visual motif: Blood-crimson tomb (`#dc2626`).
* **Tier 4 (Abyssal Cataclysm)**: Out-of-memory (OOM), kernel panics, core dumps, CPU lockups. Visual motif: Phosphor invert flash + deep crypt runes (`#f43f5e`).

---

## 5. Quickstart & Installation

### Prerequisites
* **Python 3.10+**
* **Ollama** with Google Gemma 2 (2B):
  ```bash
  ollama run gemma2:2b
  ```

### Installation
Clone the repository and install in editable mode:
```bash
git clone https://github.com/Snigdha-Mondal/Ada-The-Possessed-Terminal.git
cd "Ada-The Possessed Terminal"
pip install -e .
```

### Usage Examples
```bash
# Wrap any command
ada python train.py
ada git push origin main
ada npm run build

# Direct module invocation
python -m src.ada python -c "1/0"

# Preview the gothic tomb panel
ada --test-tomb

# Force deterministic offline oracle (0ms latency)
ada --oracle python bad_syntax.py

# Disable the 350ms CRT glitch
ada --no-glitch node app.js
```

---

## 6. Shell Integration

Automatically wrap failed commands in your everyday terminal:

### PowerShell (`$PROFILE`)
```powershell
function Invoke-Ada {
    param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Cmd)
    python -m src.ada $Cmd
}
Set-Alias -Name ada -Value Invoke-Ada
```

### Bash / Zsh (`~/.bashrc` or `~/.zshrc`)
```bash
alias ada="python3 -m src.ada"
```

---

## 7. Privacy & Threat Model

* **Zero Cloud Network Calls**: All inference occurs over `http://localhost:11434` (Ollama) or in-memory fallback tables.
* **Deterministic Pre-Prompt Sanitization**: Automatically scrubs AWS access keys, Bearer tokens, GitHub/OpenAI tokens, private SSH keys, and system usernames (`/Users/<username>/` $\rightarrow$ `~developer/`).
* **Execution Safety**: Suggested commands are presented cleanly in TrueColor phosphor cyan for human review. `ada` **never** automatically executes suggested fixes.
* **Terminal Safety**: Registers `atexit` and signal handlers (`SIGINT`, `SIGTERM`) to guarantee cursor visibility (`\x1b[?25h`) and reset attributes (`\x1b[0m`) under all abort scenarios.

---

## 8. Agent Skill Bundle

`ada` includes a modular Agent Skill conforming to the **Agent Skills Open Standard**:
* Bundle: [`skills/terminal-exorcism/SKILL.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/skills/terminal-exorcism/SKILL.md)
* Historical Reference: [`skills/terminal-exorcism/references/lovelace-lore.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/skills/terminal-exorcism/references/lovelace-lore.md)

---

## 9. Verification & Testing Suite

Run the comprehensive automated test suite with `pytest`:
```bash
python -m pytest tests/
```

Test coverage includes:
* `tests/test_runner_silent_success.py`: Validates silent exit 0 on success.
* `tests/test_runner_error_catch.py`: Validates exit code preservation and stderr buffering.
* `tests/test_secret_masking.py`: Validates scrubbing of AWS, GitHub, Bearer, and user directory tokens.
* `tests/test_fallback_oracles.py`: Validates 0ms offline fallback accuracy.
* `tests/test_gemma_json_schema.py`: Validates structured JSON schema enforcement and recovery.

---

## 10. DeftBench AI Agent Framework Compliance

Following the **DeftBench AI Agent Loop** specification, the repository maintains explicit memory and operational files:

* [`AGENTS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/AGENTS.md) — Front door: 8 golden rules & locked tech choices
* [`ENGINEERING_PLAYBOOK.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ENGINEERING_PLAYBOOK.md) — Operating manual: 9-step loop, Ready/Done definitions
* [`PRD.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PRD.md) — Product specification & persona guidelines
* [`ARCHITECTURE.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ARCHITECTURE.md) — Technical specification & component breakdown
* [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md) — Phased tasks with verification checkboxes
* [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md) — Living session memory & decisions log
* [`docs/`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/) — Architecture decision records, stories, and manual test scripts

---

## 11. Final Word

> *"Proprietary cloud AI treats code as disposable corporate data. `ada` proves that with open-weight models like Google's Gemma 2, our development environments can stay completely private, blazingly fast, and rich with the memory of the pioneers who built the foundation of our craft."*

---

## License

Released under the [MIT License](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/LICENSE).
