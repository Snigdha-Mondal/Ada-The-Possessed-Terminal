# Plan 001: Core CLI Build & Verification

* **Story Reference**: [`docs/stories/story-001-terminal-exorcism.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/stories/story-001-terminal-exorcism.md)
* **Backlog Phase**: Phase 1 & 2

---

## 1. Scope & Affected Files

* `pyproject.toml` — Package metadata, entrypoints, dependencies (`rich`, `httpx`).
* `src/core/runner.py` — Subprocess invocation, real-time stdout streaming, stderr buffering.
* `src/core/sanitizer.py` — Deterministic regex redacting for secrets and paths.
* `src/visual/glitch.py` — ANSI 350ms voltage flash and screen scanline tearing.
* `src/visual/ascii_art.py` — Veiled Lady Augusta Ada Lovelace ASCII portrait.
* `src/visual/renderer.py` — Rich panel rendering with TrueColor palettes and tier badges.
* `src/ai/prompts.py` — 1840s Byronic system prompt and JSON schema.
* `src/ai/gemma_client.py` — Ollama HTTP client (`gemma2:2b`).
* `src/ai/fallbacks.py` — In-memory deterministic fallback oracles.
* `src/ada.py` — Top-level CLI entrypoint.

---

## 2. Step-by-Step Implementation Slices

1. **Slice 1: Scaffolding & Subprocess Runner**
   * Build `src/core/runner.py` with `execute_command(cmd_args) -> ExecutionResult`.
   * Return `stdout`, `stderr`, `exit_code`.
   * Stream `stdout` live unless silenced.
2. **Slice 2: Secret & Path Sanitization**
   * Build `src/core/sanitizer.py` with `sanitize_trace(text: str) -> str`.
   * Mask cloud keys, auth headers, and user directories.
3. **Slice 3: ANSI Glitch & Terminal Protection**
   * Build `src/visual/glitch.py` with `trigger_crt_glitch()`.
   * Register clean terminal restoration handlers.
4. **Slice 4: Local AI Client & Deterministic Oracles**
   * Build `src/ai/prompts.py`, `src/ai/gemma_client.py`, `src/ai/fallbacks.py`.
   * Route failed runs to Gemma 2 if Ollama is accessible; fallback to oracles on timeout or disconnect.
5. **Slice 5: Rich Tomb UI Renderer & Main CLI**
   * Wire everything through `src/ada.py`.
   * Provide clean TrueColor terminal tomb panel.
6. **Slice 6: Automated Testing & Benchmark**
   * Build and run `pytest` test suite covering silent success, error capture, secret scrubbing, and oracles.
