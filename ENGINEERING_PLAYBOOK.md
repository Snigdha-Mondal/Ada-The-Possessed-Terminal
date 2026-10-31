# Engineering Playbook — The Operating Manual

> *"You don't carry memory between sessions. The docs do."*
> This playbook acts as the engineering manager for **Ada: The Possessed Terminal**. It governs how we pick work, build it, test it, verify it, and record memory.

---

## 1. The 3 Roles

| Role | Who | What They Own |
| :--- | :--- | :--- |
| **Product Owner** | Human Developer (`Snigdha`) | Priorities, feature scope approvals, aesthetic direction, and anything risky or externally visible. Has the final say. |
| **Engineering Manager** | The Playbook (`ENGINEERING_PLAYBOOK.md`) | The processes, standards, checklists, stop signs, and architectural rules. |
| **Engineer** | The AI Agent | Planning, building, testing, verifying, reviewing, and keeping memory docs up to date. |

---

## 2. How Every Session Starts

A fresh session starts with zero memory. Read these files in order before doing any work:

1. **Front Door**: [`AGENTS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/AGENTS.md) (golden rules & locked decisions).
2. **Operating Manual**: [`ENGINEERING_PLAYBOOK.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ENGINEERING_PLAYBOOK.md) (this file).
3. **Session Memory**: [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md) (what's done, what's broken, notes for next time).
4. **Current Backlog**: [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md) (pick the next unblocked task in the active phase).
5. **Touch Specs Only**: Read only the specs and docs relevant to the chosen task via the *Where to Find Things* table.

---

## 3. The 9-Step Loop

Every slice of work follows this cycle. Never do a "big bang" implementation.

```
       [ 1. ORIENT ] ──► [ 2. SELECT ] ──► [ 3. PLAN ]
             ▲                                    │
             │                                    ▼
       [ 9. REFLECT ]                      [ 4. BUILD ]
             ▲                                    │
             │                                    ▼
       [ 8. COMMIT ]  ◄── [ 7. RECORD ] ◄── [ 5. TEST & VERIFY ]
                               ▲                  │
                               └──── [ 6. REVIEW ]┘
```

1. **Orient**: Read the Playbook, [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md), and the current active phase in [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md).
2. **Select**: Pick the next unblocked item. Respect phase boundaries. Stop at any item marked with 🔒 for human approval.
3. **Plan**: Write a concise plan: what files change, what functions are added, and how it will be verified with live evidence.
4. **Build**: Write the smallest, cleanest increment of code that fulfills the requirement.
5. **Test & Verify**: Write and execute automated tests (`pytest`). Then run the CLI tool for real and observe actual output.
6. **Review**: Inspect code against standards: zero data leaks, proper signal handling, cursor restoration, strict JSON validation.
7. **Record**: Update [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md) with exact evidence (command output, timings) and log any technical decision in the Decisions Log.
8. **Commit**: Git commit with a concise, descriptive message. Keep the build green.
9. **Reflect**: Check for newly discovered bugs, risks, or follow-ups. Log them into [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md).

---

## 4. Source of Truth Hierarchy

When documents or code disagree, resolve conflicts strictly using this ranking:

1. **What the Human Product Owner says right now** *(Highest authority)*
2. **[`PRD.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PRD.md)** *(Product intent and feature scope)*
3. **[`ARCHITECTURE.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ARCHITECTURE.md)** *(System architecture and locked tech choices)*
4. **[`ENGINEERING_PLAYBOOK.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/ENGINEERING_PLAYBOOK.md)** *(Engineering process & standards)*
5. **[`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md)** *(Concrete task slices)*
6. **Existing code and comments** *(May be stale or contain bugs)*

*Rules*:
* Never quietly pick one side of a conflict. Inform the human and recommend a fix.
* If a detail is missing, propose the addition rather than making an unwritten assumption.
* Once a decision is logged in the Decisions Log or ADR, do not re-argue settled decisions.

---

## 5. Ready and Done Checklists

### ✔ Definition of Ready (Before starting a task)
- [ ] The outcome and acceptance criteria are specific and measurable.
- [ ] All prerequisite tasks and dependencies are already merged and tested.
- [ ] The task fits into one focused working session.
- [ ] The relevant spec and architecture documents have been read.

### ✔ Definition of Done (Before marking complete)
- [ ] Meets all acceptance criteria of the task.
- [ ] Automated tests pass (`pytest`).
- [ ] Executed live in the terminal and witnessed working with real evidence.
- [ ] Zero secrets, tokens, or private paths exposed.
- [ ] ANSI cursor visibility and terminal echo guaranteed under normal and abort conditions.
- [ ] Docs, [`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md), and [`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md) updated in the same commit.
- [ ] Git commit created with a clean message.

---

## 6. Stop Signs & Escalation Rules

| Signal | Category | Allowed Actions |
| :--- | :--- | :--- |
| 🟢 **GO** | Autonomous | Pick next unblocked task; write and run tests; implement scoped logic; update docs and progress; log low-level decisions. |
| 🟡 **PAUSE** | Checkpoint | Changes to CLI argument schema; modifications to Ollama prompt schemas; adding new error categories; ambiguous user intent. Pause and propose a recommendation. |
| 🔴 **NEVER** | Forbidden without human sign-off | Auto-executing suggested fix commands; sending telemetry or logs to cloud endpoints; committing credentials or personal files; adding unapproved heavy dependencies; altering locked architectural decisions. |

### When Stuck (The Two-Try Rule)
If a command, test, or edit fails twice with the same blocker:
* **Stop immediately**. Do not loop blindly or keep editing in circles.
* Isolate the root cause, summarize the evidence, and propose clear options with a recommended fix.

---

## 7. Memory & Record Keeping

Every completed slice produces updates to:
1. **[`PROGRESS.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/PROGRESS.md)**:
   * **Dated Session Entry**: What was done, what was verified with real output, and what is still open (marked with 🔴).
   * **Decisions Log**: One row per non-trivial choice (`Date · Decision · Rationale`). Major choices get an ADR in `docs/adr/`.
   * **Notes for the Next Iteration**: Clear handover note telling the next session exactly where to resume.
2. **[`BACKLOG.md`](file:///c:/Users/snigd/OneDrive/Documents/Projects/Ada-The%20Possessed%20Terminal/BACKLOG.md)**: Check off the completed item with a short verification note; append newly identified tasks.
