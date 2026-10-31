"""Deterministic secret, credential, and path sanitizer for Ada: The Possessed Terminal."""

import re
from typing import Pattern, List, Tuple

# Pre-compiled sanitization patterns with their replacement templates
SANITIZATION_RULES: List[Tuple[Pattern[str], str]] = [
    # 1. Private Keys (RSA, EC, DSA, OPENSSH, PGP)
    (
        re.compile(r"-----BEGIN (?:[A-Z0-9_-]+ )?PRIVATE KEY-----[\s\S]+?-----END (?:[A-Z0-9_-]+ )?PRIVATE KEY-----", re.MULTILINE),
        "[REDACTED_PRIVATE_KEY]"
    ),

    # 2. AWS Access Key IDs
    (
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "AKIA••••••••••••••••"
    ),

    # 3. GitHub Tokens (Personal Access Token, OAuth)
    (
        re.compile(r"\bghp_[a-zA-Z0-9]{36}\b"),
        "ghp_••••••••••••••••••••••••••••••••••••"
    ),
    (
        re.compile(r"\bgithub_pat_[a-zA-Z0-9_]{40,}\b"),
        "github_pat_••••••••••••••••••••••••"
    ),

    # 4. Standard API Secret Keys (OpenAI, Anthropic, Stripe, HuggingFace)
    (
        re.compile(r"\b(?:sk|hf|live)_[a-zA-Z0-9]{20,}\b"),
        "sk_••••••••••••••••••••"
    ),

    # 5. Bearer / Authorization HTTP Headers
    (
        re.compile(r"(?i)\bBearer\s+[a-zA-Z0-9_\-\.]{20,}\b"),
        "Bearer ••••••••••••"
    ),

    # 6. Database / HTTP URLs with embedded credentials (e.g., postgres://user:password@host)
    (
        re.compile(r"([a-zA-Z][a-zA-Z0-9+.-]*://)([^:\s]+):([^@\s]+)@"),
        r"\1\2:••••••••@"
    ),

    # 7. User Home Paths (Windows: C:\Users\<user>\...)
    (
        re.compile(r"(?i)[a-z]:\\users\\[a-z0-9_\-\.]+", re.IGNORECASE),
        r"C:\\Users\\developer"
    ),

    # 8. User Home Paths (Unix/macOS: /Users/<user>/ or /home/<user>/)
    (
        re.compile(r"/(?:Users|home)/[a-zA-Z0-9_\-\.]+"),
        "/home/developer"
    ),
]


def mask_secret_tokens(text: str) -> str:
    """Masks high-entropy keys, passwords, and tokens within the given text."""
    if not text:
        return ""
    sanitized = text
    for pattern, replacement in SANITIZATION_RULES:
        sanitized = pattern.sub(replacement, sanitized)
    return sanitized


def sanitize_trace(text: str, max_chars: int = 4000) -> str:
    """
    Cleanses sensitive tokens, paths, and limits buffer length to prevent
    context window flooding.

    Args:
        text: Raw trace or error string.
        max_chars: Maximum character limit for downstream prompts.

    Returns:
        Sanitized, safe string suitable for local model consumption.
    """
    if not text:
        return ""

    cleaned = mask_secret_tokens(text)

    # Truncate if extreme length (e.g. multi-megabyte core dumps)
    if len(cleaned) > max_chars:
        half = max_chars // 2
        cleaned = (
            cleaned[:half]
            + f"\n\n... [TRUNCATED {len(cleaned) - max_chars} CHARACTERS OF LOG STATIC] ...\n\n"
            + cleaned[-half:]
        )

    return cleaned
