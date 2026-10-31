# Manual Test 001: CLI Crash Resurrection & Glitch Verification

* **Objective**: Manually verify visual fidelity, CRT voltage flash timing, Lady Lovelace portrait rendering, and clean exit codes in the terminal.

---

## Prerequisites
* Python 3.10+ installed.
* Terminal with ANSI TrueColor support (Windows Terminal, iTerm2, Kitty, Alacritty, or VS Code terminal).

---

## Test Cases

### TC-1: Silent Success
```powershell
python -m src.ada echo "Mechanical Engine Test"
```
* **Expected Result**:
  * Output prints: `Mechanical Engine Test`
  * No glitch, no gothic panel, no Ada message.
  * Exit code is `0`.

### TC-2: Syntax Error Autopsy
```powershell
python -m src.ada python -c "def bad(): print('unclosed"
```
* **Expected Result**:
  * Original python error prints.
  * 350ms CRT flash occurs (brief inversion & scanline jitter).
  * Blood-crimson / Amber tomb panel renders.
  * Lady Lovelace ASCII portrait displayed.
  * Witty Victorian commentary referencing mechanical calculation / punch cards.
  * High-contrast cyan fix command provided.
  * Exit code matches the failed command (`1`).

### TC-3: Secret Masking Verification
```powershell
python -m src.ada python -c "raise RuntimeError('Failed with AKIA1234567890ABCDEF and Bearer secret_token_xyz_1234567890')"
```
* **Expected Result**:
  * Tomb panel diagnosis never prints the raw AWS key or Bearer token.
  * Replaced by masked representations.
