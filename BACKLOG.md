# Task Backlog — Ada: The Possessed Terminal

> **Rule**: Build in phases. Each item is a small, testable slice. Items requiring human sign-off are marked with 🔒. Check off items only when verified with live evidence.

---

## Phase 1: Core Subprocess & Intercept Layer
*Exit Goal*: `ada` runs any command, stays completely silent on exit code `0`, captures errors on non-zero exit codes, sanitizes credentials, and exits with the target command's status.

- [x] **1.1 Project Scaffolding & Packaging**: Setup `pyproject.toml`, directory hierarchy (`src/core`, `src/visual`, `src/ai`), and `LICENSE`.
- [x] **1.2 Subprocess Runner**: Implement `src/core/runner.py` with real-time stdout streaming, stderr capture, signal handling, and exact exit code return.
- [x] **1.3 Deterministic Sanitizer**: Implement `src/core/sanitizer.py` with regex masking for AWS keys, Bearer tokens, GitHub/OpenAI keys, and user home paths.
- [x] **1.4 Verification Tests for Phase 1**:
  - `tests/test_runner_silent_success.py` (Verified: silent output and exit code 0).
  - `tests/test_runner_error_catch.py` (Verified: captured stderr and preserved exit code).
  - `tests/test_secret_masking.py` (Verified: all 6 secret classes properly masked).
- [x] 🔒 **Phase 1 Human Review**: Verified live in terminal.

---

## Phase 2: ANSI CRT Glitch & Gothic Terminal UI
*Exit Goal*: A 350ms authentic CRT voltage flash and chromatic scanline tear followed by an immaculate Rich gothic tomb panel displaying Lady Lovelace's portrait and tier badge.

- [x] **2.1 ANSI Hardware Glitch Engine**: Implement `src/visual/glitch.py` with 60ms screen invert flash, noise scanlines, and guaranteed cursor/attribute restoration.
- [x] **2.2 Lady Lovelace ASCII Art**: Implement `src/visual/ascii_art.py` with compact high-fidelity shaded ASCII portrait.
- [x] **2.3 Gothic Tomb Renderer**: Implement `src/visual/renderer.py` using Rich panels, TrueColor borders, and necromantic tier color schemes (Amber, Violet, Blood-crimson, Abyssal).
- [x] **2.4 Terminal Safety & Signal Handlers**: Ensure `atexit` and `SIGINT` cleanly restore the cursor (`\x1b[?25h`) even if aborted mid-glitch.
- [x] **2.5 Verification Tests for Phase 2**: Verified with `python -m src.ada --test-tomb` and cross-platform terminal rendering.
- [x] 🔒 **Phase 2 Human Review**: Visual approval of CRT glitch timing and tomb aesthetics.

---

## Phase 3: Gemma 2 Local AI Integration & Fallback Oracles
*Exit Goal*: Full integration with local `gemma2:2b` via Ollama for 1840s Byronic diagnosis and clean shell fixes, with 0ms fallback oracles when offline.

- [x] **3.1 Byronic System Prompt & JSON Schema**: Implement `src/ai/prompts.py` enforcing Countess Lovelace character, Babbage/Loom metaphors, and strict JSON format.
- [x] **3.2 Local Ollama Client**: Implement `src/ai/gemma_client.py` using HTTP requests to `http://localhost:11434/api/generate` with timeout, JSON repair, and fallback logic.
- [x] **3.3 Deterministic Fallback Oracles**: Implement `src/ai/fallbacks.py` with instant offline rules for Git conflicts, syntax errors, missing modules, port collisions.
- [x] **3.4 Occult Tier Classifier**: Implement error analyzer mapping stderr patterns to Tiers 1–4.
- [x] **3.5 Verification Tests for Phase 3**:
  - `tests/test_fallback_oracles.py` (7 tests passed).
  - `tests/test_gemma_json_schema.py` (3 tests passed).
- [x] 🔒 **Phase 3 Human Review**: Verified live with Ollama `gemma2:2b`.

---

## Phase 4: CLI Integration, Agent Skill & Verification Benchmark
*Exit Goal*: The unified `ada` CLI tool installed and validated against the 30-scenario test suite, packaged with `skills/terminal-exorcism/SKILL.md`.

- [x] **4.1 Unified CLI Entrypoint**: Implement `src/ada.py` wiring together runner, sanitizer, glitch, AI client, and renderer.
- [x] **4.2 Agent Skill Bundle**: Created `skills/terminal-exorcism/SKILL.md` conforming to the Agent Skills Open Standard and `skills/terminal-exorcism/references/lovelace-lore.md`.
- [x] **4.3 Test Fixtures & Synthetic Benchmark**: Created test fixtures in `tests/fixtures/` and verified end-to-end.
- [x] **4.4 Demo Scripts**: Provided `demo/demo_syntax_crash.py` and `demo/demo_git_conflict.py` verified live.
- [x] 🔒 **Phase 4 Human Review**: Run demo scripts live in terminal.

---

## Phase 5: Documentation & Presentation
*Exit Goal*: Comprehensive `README.md`, MIT `LICENSE`, and release packaging ready for GitHub and Hacktoberfest submission.

- [x] **5.1 Public README.md**: Complete with architecture diagram, installation guide, theme explanation, and visual previews.
- [x] **5.2 Final Audit**: Verified zero committed secrets, clean git history, and up-to-date `PROGRESS.md`.
- [x] 🔒 **Phase 5 Human Sign-off**: Final approval and pushed to `origin/main`.
