# Product Requirements Document (PRD) — Ada: The Possessed Terminal

> **Tagline**: *The spirit of the world's first programmer, awakened by your compiler errors.*

---

## 1. Executive Summary & Vision

Developers spend hours wrestling with unforgiving compiler errors, obscure stack traces, and unhelpful exit codes. When modern developers paste private error traces into cloud AI chatbots, they risk leaking credentials, internal file paths, and proprietary algorithms—all while incurring high latency and recurring subscription costs.

**Ada: The Possessed Terminal** is a local-first, privacy-preserving terminal resilience utility. It intercepts non-zero exit codes, triggers a 350ms physical CRT glitch, and summons the ghost of **Augusta Ada Lovelace** to diagnose the failure in authentic 1840s "Poetical Science" prose and provide an instant, clean terminal fix—powered 100% locally by Google's **Gemma 2 (2B)** with zero cloud telemetry.

---

## 2. Target Users & Personas

1. **Everyday CLI Developers (Python, Node.js, Rust, Go)**:
   * Pain: Stack traces, unhandled panics, missing dependencies, syntax typos.
   * Value: Instant diagnosis and copyable fix without leaving the terminal context.
2. **DevOps & Systems Engineers**:
   * Pain: Diverged Git branches, port collisions (`EADDRINUSE`), broken Docker bindings, permission traps.
   * Value: Fast actionable command fixes without leaking internal hostnames or keys.
3. **Hackathon Participants, Students & Educators**:
   * Pain: Intimidating walls of red error text; coding late in low-connectivity or air-gapped settings.
   * Value: Engaging literary learning experience; 100% offline-capable on local silicon.

---

## 3. Product Features & MVP Scope

### 3.1 Subprocess Interceptor
* Invoked via CLI: `ada <command> [args...]` or `python -m src.ada <command> [args...]`.
* Streams standard output in real-time.
* **Silent Success**: If exit code is `0`, `ada` exits cleanly and silently with zero terminal overhead.
* **Failure Trigger**: If exit code is non-zero ($? \neq 0$), captures standard error and activates the necromantic pipeline.

### 3.2 Deterministic Secret & Path Masker
* Evaluates `stderr` through deterministic regex rules *before* passing to the AI engine.
* Redacts AWS access keys (`AKIA...`), OpenAI/Anthropic/GitHub tokens (`sk-...`, `ghp_...`), Bearer tokens, private SSH keys (`-----BEGIN PRIVATE KEY-----`).
* Sanitizes local file system paths: `/Users/<username>/` and `C:\Users\<username>\` $\rightarrow$ `~user/`.

### 3.3 ANSI CRT Glitch Engine (~350ms)
* Emulates vintage hardware voltage surge using raw ANSI escape codes:
  * 60ms screen color inversion flash (`\x1b[7m\x1b[38;5;196m`).
  * Chromatic scanline tearing and jitter characters.
  * Clean settling into a blood-crimson or obsidian tomb panel without residual cursor or screen corruption.

### 3.4 Necromantic Diagnostic Classification
Errors are categorized into 4 occult severity tiers:
* **Tier 1 (Minor Poltergeist)**: Syntax errors, unclosed quotes, indentation mistakes. Visual motif: Amber scanlines (`#f59e0b`).
* **Tier 2 (Malicious Daemon)**: Port collisions (`EADDRINUSE`), file locks, network timeouts. Visual motif: Violet spectral split (`#c084fc`).
* **Tier 3 (Demonic Possession)**: Null pointer dereferences, Rust unwrap panics, segfaults. Visual motif: Blood-crimson tomb (`#dc2626`).
* **Tier 4 (Abyssal Cataclysm)**: OOM, core dumps, CPU lockups. Visual motif: Phosphor invert flash + deep crypt runes.

### 3.5 Lady Lovelace Diagnosis (Local Gemma 2 Engine)
* Direct HTTP request to local Ollama instance (`http://localhost:11434/api/generate` with `gemma2:2b`).
* System prompt channels Countess Ada Lovelace (1815–1852):
  * Aristocratic, witty, gothic Victorian voice.
  * Conceptual analogies to Babbage's Analytical Engine, Jacquard loom punch cards, brass gears, and Lord Byron's poetry.
  * Maximum 60 words for snappy terminal reading.
  * Strict JSON output schema: `{"diagnosis": "...", "fix": "..."}`.

### 3.6 The Incantation of Exorcism (The Fix)
* The single exact terminal command required to resolve or investigate the crash.
* Rendered in high-contrast TrueColor phosphor cyan (`#00f5d4`).
* Never auto-executed; cleanly highlighted for instant human copying or verification.

### 3.7 Offline-First Resilience (Deterministic Fallback Oracles)
* Built-in deterministic pattern matcher for common failure modes (Git conflicts, port in use, ModuleNotFoundError, syntax errors, permission errors).
* If Ollama is offline or times out (>3.5s), falls back in 0ms so the user is never left without guidance.

---

## 4. Non-Functional Requirements & Security Guarantees

* **Zero Cloud Telemetry**: Absolute prohibition of external network calls. All reasoning is on `localhost`.
* **Sub-Second Performance**: Total post-crash latency under 800ms on CPU.
* **Terminal Cleanliness**: Guaranteed restoration of ANSI text attributes, cursor visibility (`\x1b[?25h`), and terminal echo even on `SIGINT` (Ctrl+C).
* **Safe Suggested Execution**: Strictly manual review. Never pipe fixes to shell execution automatically.

---

## 5. Out of Scope for MVP

* Multi-turn conversational terminal chat (reserved for future `ada-shell`).
* Remote multi-agent orchestration.
* Automatic binary patching of corrupted source files.
