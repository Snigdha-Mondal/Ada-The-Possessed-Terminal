# Story 001: Terminal Exorcism & Subprocess Intercept

* **Backlog Reference**: Phase 1 & Phase 2
* **Epic**: Core CLI & Resilience Layer

---

## Story Statement

As a **CLI developer working on complex applications**,
I want to **wrap any command in `ada <cmd>` and have successful runs be silent, but have failures trigger an authentic CRT glitch and an instant Victorian diagnosis with a clean fix**,
So that **I never leak secrets to cloud LLMs, avoid frustrating red stack traces, and recover from failures in seconds**.

---

## Acceptance Criteria

1. **Silent Success**:
   * Given a command that completes with exit code `0` (e.g. `ada echo "OK"`),
   * When executed,
   * Then standard output is streamed directly and no glitch, header, or tomb panel is rendered.
2. **Crash Intercept & Preserved Exit Status**:
   * Given a command that fails with a non-zero exit code (e.g. `ada non_existent_cmd` or `ada python3 -c "1/0"`),
   * When executed,
   * Then `ada` catches the failure, triggers the 350ms glitch, outputs Lady Lovelace's diagnosis and fix, and exits with the original process exit code.
3. **Secret Masking Guarantee**:
   * Given stderr containing `AKIAIOSFODNN7EXAMPLE` or `Bearer eyJhbGci...` or `/Users/snigd/`,
   * When `ada` processes the trace,
   * Then all tokens are masked (`AKIA••••••••••••••••`, `Bearer ••••`, `~user/`) before any model prompt or terminal display.
4. **Terminal Integrity**:
   * Even if the user terminates `ada` during execution with `Ctrl+C`,
   * Terminal cursor visibility and standard text colors are guaranteed to be restored.
