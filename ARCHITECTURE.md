# System Architecture & Technical Design — Ada: The Possessed Terminal

> **Architectural Philosophy**: *Gemma reasons and channels the spirit; deterministic code executes, glitches, and sanitizes.*

---

## 1. High-Level Data Flow

```text
┌───────────────────────────────────────┐
│     User runs: ada <command>          │
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│      Subprocess Execution Layer       │  streams stdout, buffers stderr
└──────────────────┬────────────────────┘
                   │
         Exit Code == 0? ──► YES ──► Exit cleanly & silently (0 overhead)
                   │
                   NO ($? != 0)
                   ▼
┌───────────────────────────────────────┐
│     Deterministic Secret Masker       │  regex redacting of API keys, tokens, paths
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│     ANSI CRT Glitch Engine (350ms)    │  voltage flash, chromatic tear, jitter
└──────────────────┬────────────────────┘
                   │
                   v
┌───────────────────────────────────────┐
│      Local Gemma 2 Engine (Ollama)    │  HTTP POST http://localhost:11434/api/generate
└─────────┬───────────────────┬─────────┘  with gemma2:2b & 1843 Byronic system prompt
          │ (Success)         │ (Ollama down / timeout > 3.5s)
          v                   v
┌──────────────────┐  ┌─────────────────┐
│ JSON Schema      │  │ Fallback Oracle │  deterministic regex-based diagnostics & fixes
│ Validator        │  └───────┬─────────┘
└─────────┬────────┘          │
          │                   │
          └─────────┬─────────┘
                    v
┌───────────────────────────────────────┐
│      Gothic Tomb Terminal Panel       │  Rich TrueColor console panel
│      • Lady Lovelace Portrait         │  ASCII shaded character art
│      • Occult Tier Header             │  Tier 1..4 color palette
│      • Lady Lovelace Diagnosis        │  Ectoplasm green (#a7f3d0)
│      • Incantation of Exorcism        │  Clean phosphor cyan (#00f5d4)
└───────────────────────────────────────┘
```

---

## 2. Component Breakdown

### 2.1 Subprocess & Runner (`src/core/runner.py`)
* Manages child process lifecycle using Python's `subprocess.Popen`.
* Handles real-time stdout streaming to stdout console.
* Buffers stderr in memory for autopsy processing.
* Preserves and forwards process exit codes accurately.
* Intercepts `SIGINT` (Ctrl+C) to prevent zombie processes and restore terminal state cleanly.

### 2.2 Sanitizer & Privacy Engine (`src/core/sanitizer.py`)
* Applies deterministic compiled regular expressions before stderr leaves memory.
* Patterns covered:
  * AWS Secret / Access Keys (`AKIA[0-9A-Z]{16}`)
  * Generic Bearer / Auth tokens (`Bearer [a-zA-Z0-9_\-\.]{20,}`)
  * OpenAI / GitHub / Anthropic API keys (`sk-[a-zA-Z0-9]{32,}`, `ghp_[a-zA-Z0-9]{36}`)
  * Private Keys (`-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----`)
  * User home paths (`/Users/<username>/`, `C:\Users\<username>\`, `/home/<username>/`)

### 2.3 Visual & ANSI Glitch Engine (`src/visual/glitch.py`, `src/visual/renderer.py`)
* **CRT Glitch**: Emits non-blocking raw ANSI escape codes:
  * Invert screen video: `\x1b[7m\x1b[38;5;196m`
  * Reset video: `\x1b[0m`
  * Noise jitter & chromatic tear rows for 300–350ms total.
* **Terminal Safety**: Registers `atexit` and signal handlers (`SIGINT`, `SIGTERM`) to guarantee `\x1b[?25h` (show cursor) and `\x1b[0m` (reset styling) are emitted under all circumstances.
* **Rich Tomb Panel**: Uses `rich.panel.Panel`, `rich.columns.Columns`, and TrueColor formatting for the Lady Lovelace ASCII portrait, diagnosis, and fix incantation.

### 2.4 Local AI Client (`src/ai/gemma_client.py`)
* Connects via `httpx.Client` or `urllib.request` to `http://localhost:11434/api/generate`.
* Parameters:
  * Model: `gemma2:2b`
  * Temperature: `0.3` (factual precision with literary flair)
  * Format: `json`
  * Timeout: `3.5s`
* Strictly validates JSON output:
  ```json
  {
    "diagnosis": "string",
    "fix": "string"
  }
  ```

### 2.5 Fallback Oracles (`src/ai/fallbacks.py`)
* Provides instantaneous (0ms) zero-dependency fallbacks if Ollama is unreachable or timeout expires.
* Handles:
  * Git diverged branches / merge conflicts
  * Port in use (`EADDRINUSE`)
  * Python `ModuleNotFoundError`, `IndentationError`, `SyntaxError`
  * Node `Cannot read property of undefined`
  * Permission denied (`EACCES`, `chmod`)
  * Command not found

---

## 3. Locked Technical Decisions

1. **Python 3.10+**: Core implementation language.
2. **Local Ollama (`gemma2:2b`)**: Primary intelligence engine.
3. **Air-Gap Architecture**: Zero outbound external HTTP calls.
4. **ANSI + Rich**: Terminal graphics without heavy GUI frameworks.
5. **No Auto-Execution**: Suggested fixes remain strictly actionable strings for human copying.
