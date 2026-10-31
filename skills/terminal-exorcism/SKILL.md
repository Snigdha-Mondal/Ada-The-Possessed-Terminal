---
name: terminal-exorcism
description: Diagnoses catastrophic terminal and compiler failures using local open-weight AI (Gemma 2). Channels the historical persona of Ada Lovelace to explain the mechanical root cause in 1840s Poetical Science prose, delivering an exact shell command to fix the crash.
license: MIT
compatibility: Requires Python 3.10+, ANSI TrueColor terminal, and local Ollama instance running gemma2:2b (or uses built-in fallbacks).
metadata:
  author: Ada Lovelace Contributors
  version: "1.0.0"
---

# Terminal Exorcism Skill

## Procedure

1. Intercept the failed command string and captured standard error stream.
2. Sanitize and mask all API keys, bearer tokens, passwords, and private file paths.
3. Fire a 350ms non-blocking ANSI CRT voltage glitch to signal hardware failure.
4. Pass the sanitized context to the local Gemma 2 model using the 1843 Byronic system prompt.
5. If the model is unreachable within 3.5 seconds, invoke the built-in deterministic fallback oracle.
6. Parse and validate the JSON schema containing `diagnosis` and `fix`.
7. Render the blood-crimson gothic tomb panel, veiled ASCII portrait, and clean fix code.

## Hard Rules

- NEVER trigger on commands that exit with status 0.
- NEVER send terminal telemetry, paths, or errors to external network endpoints.
- NEVER execute the suggested fix command automatically; present it cleanly for human review.
- Mask all potential secrets before LLM inference.
- Ensure the terminal cursor is restored and terminal echo is preserved under all abort scenarios.
