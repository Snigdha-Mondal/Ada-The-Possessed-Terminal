# AGENTS.md — The Front Door

> **READ FIRST**: Before performing any work or planning, read [`ENGINEERING_PLAYBOOK.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ENGINEERING_PLAYBOOK.md). It is our operating manual.

---

## 1. What This Project Is

**Ada — The Possessed Terminal** is a local-first, necromantic terminal resilience layer. When a command dies, `ada` intercepts the exit code, unleashes a brief physical CRT voltage glitch, and summons the gothic ghost of **Augusta Ada Lovelace** to diagnose the failure in 1840s "Poetical Science" prose and provide an instant, clean terminal fix—powered 100% locally by Google's **Gemma 2 (2B)** with zero cloud telemetry.

* **Product Requirements & Scope**: [`PRD.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PRD.md)
* **Technical Design & Architecture**: [`ARCHITECTURE.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ARCHITECTURE.md)
* **Master Specification**: [`MASTER_GUIDE.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/MASTER_GUIDE.md)

---

## 2. The 8 Golden Rules

1. **Small, verified slices**: Never leave the build broken. Build in thin vertical increments with verified tests.
2. **Evidence over assertion**: "Done" means you ran it and saw it work with your own eyes.
3. **Respect fixed decisions**: Locked tech choices require human approval to change.
4. **Use shared building blocks**: Gemma reasons and channels the spirit; deterministic code executes, glitches, and sanitizes.
5. **Never commit secrets or personal data**: Never exfiltrate code, weaken security, spend money, or add cloud telemetry.
6. **Stop and ask**: When things are unclear, sensitive, or high-risk, pause and ask with a clear recommendation.
7. **Keep docs in sync with code**: Code and docs ship in the same commit. Update [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md) every session.
8. **Verify without drowning in output**: Extract high-signal output. Do not flood context with raw binary or infinite logs.

---

## 3. Fixed Decisions

| Area | Decision | Rationale | Approval Needed to Change? |
| :--- | :--- | :--- | :--- |
| **Language & Runtime** | Python 3.10+ CLI (`src/ada.py`) | Native cross-platform subprocess handling, rich ecosystem, signal handling | Yes (🔒) |
| **Local AI Engine** | Google Gemma 2 (2B via Ollama `http://localhost:11434`) | High Byronic reasoning fidelity, sub-second quantized CPU inference, zero cost | Yes (🔒) |
| **Privacy / Telemetry** | 100% Local-first, Air-gapped, Zero Cloud Calls | Absolute zero exfiltration of code, stack traces, paths, or keys | Yes (🔒) |
| **Terminal UI / Styling** | Raw ANSI escape sequences + Rich library | 350ms CRT voltage flash & scanline tear, high-contrast phosphor tomb panels | Yes (🔒) |
| **Resilience / Fallback** | Deterministic in-memory Oracles | 0ms instant recovery when Ollama is offline or cold; developer is never blocked | Yes (🔒) |
| **Execution Safety** | Strictly manual review of suggested fixes | Never auto-execute suggestions without user consent | Yes (🔒) |
| **Subprocess Behavior** | 100% silent and invisible on exit code 0 | Zero overhead and zero clutter for successful everyday commands | Yes (🔒) |

---

## 4. Where to Find Things

| Need | Document / Location |
| :--- | :--- |
| **Operating Rules & Process** | [`ENGINEERING_PLAYBOOK.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ENGINEERING_PLAYBOOK.md) |
| **Product Scope & Requirements** | [`PRD.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PRD.md) |
| **System Architecture & Tech Choices**| [`ARCHITECTURE.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ARCHITECTURE.md) |
| **Current Tasks & Phase Roadmap** | [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md) |
| **Session Memory & Decisions Log** | [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md) |
| **Architecture Decision Records (ADRs)**| [`docs/adr/`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/adr/) |
| **Feature Stories & Requirements** | [`docs/stories/`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/stories/) |
| **Step-by-Step Implementation Plans** | [`docs/plans/`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/plans/) |
| **Human Verification Procedures** | [`docs/manual-tests/`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/docs/manual-tests/) |
| **Agent Skill Package** | [`skills/terminal-exorcism/SKILL.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/skills/terminal-exorcism/SKILL.md) |
