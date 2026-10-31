# ADR 0001: Local Gemma 2 and Python Subprocess Architecture

* **Status**: Accepted
* **Date**: 2026-10-31
* **Deciders**: Snigdha (Product Owner), Antigravity Agent (Engineer)

---

## Context

Developers face frequent terminal crashes and errors. Existing AI debugging utilities exfiltrate sensitive files, keys, and code snippets to cloud endpoints, while introducing multiple seconds of latency and subscription fees. We need a tool that can run cross-platform, execute natively inside the terminal, capture failures with zero overhead on successful commands, and provide instantaneous, privacy-preserving diagnoses.

---

## Decision

We have decided on the following core architectural choices:
1. **Python 3.10+ as the CLI Foundation**: Python provides first-class standard library support for cross-process lifecycle management (`subprocess.Popen`), signal propagation (`signal`, `atexit`), ANSI streams, and regex token replacement.
2. **Local Google Gemma 2 (2B) via Ollama (`http://localhost:11434`)**: Google's Gemma 2 (2B) is quantized and executed locally on the user's CPU/GPU. It provides superior reasoning capable of mastering the 1840s Byronic Victorian literary style while reliably producing structured JSON output.
3. **Deterministic Fallback Oracles**: If Ollama is offline or cold, in-memory pattern matching catches standard developer failure scenarios (Git divergence, port conflicts, Python/Node syntax errors) in 0ms, maintaining 100% developer reliability.
4. **Zero Overhead on Success**: If a command exits with code 0, `ada` leaves zero visual traces and introduces negligible runtime latency.
5. **Deterministic Pre-Prompt Sanitization**: All `stderr` buffers are stripped of AWS keys, Bearer tokens, GitHub/OpenAI API keys, and local home directory usernames *before* prompting local models.

---

## Consequences

* **Positive**:
  * Complete data privacy with zero cloud exfiltration.
  * Instantaneous sub-second feedback on developer machines.
  * Captivating user experience fusing Victorian history with modern development.
  * Full offline operability.
* **Negative**:
  * Requires local Ollama installation for full generative LLM diagnoses (mitigated by deterministic fallback oracles).
