"""Tests for deterministic secret and private path sanitization."""

from src.core.sanitizer import sanitize_trace, mask_secret_tokens


def test_aws_key_masking():
    raw = "Error connecting to s3://mybucket with key AKIAIOSFODNN7EXAMPLE and secret"
    sanitized = mask_secret_tokens(raw)
    assert "AKIAIOSFODNN7EXAMPLE" not in sanitized
    assert "AKIA••••••••••••••••" in sanitized


def test_bearer_token_masking():
    raw = "Request failed: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    sanitized = mask_secret_tokens(raw)
    assert "eyJhbGci" not in sanitized
    assert "Bearer ••••••••••••" in sanitized


def test_github_token_masking():
    raw = "fatal: remote reject for token ghp_1234567890abcdef1234567890abcdef1234"
    sanitized = mask_secret_tokens(raw)
    assert "ghp_1234567890" not in sanitized
    assert "ghp_••••" in sanitized


def test_private_key_masking():
    raw = (
        "-----BEGIN RSA PRIVATE KEY-----\n"
        "MIIEowIBAAKCAQEA0Y1W9Z\n"
        "-----END RSA PRIVATE KEY-----"
    )
    sanitized = mask_secret_tokens(raw)
    assert "MIIEowIBAAKCAQEA0Y1W9Z" not in sanitized
    assert "[REDACTED_PRIVATE_KEY]" in sanitized


def test_user_path_masking():
    raw_win = r"Traceback in C:\Users\snigdha\Projects\secret\app.py line 42"
    sanitized_win = mask_secret_tokens(raw_win)
    assert r"C:\Users\snigdha" not in sanitized_win
    assert r"C:\Users\developer" in sanitized_win

    raw_unix = "/Users/alice/repo/auth.py failed on line 12"
    sanitized_unix = mask_secret_tokens(raw_unix)
    assert "/Users/alice" not in sanitized_unix
    assert "/home/developer" in sanitized_unix


def test_database_credential_masking():
    raw = "Failed connection to postgres://db_admin:SuperSecretPass123!@db.internal:5432/production"
    sanitized = mask_secret_tokens(raw)
    assert "SuperSecretPass123!" not in sanitized
    assert "db_admin:••••••••@" in sanitized
