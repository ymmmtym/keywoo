import hashlib
import hmac

from werkzeug.security import check_password_hash as werkzeug_check_password_hash
from werkzeug.security import generate_password_hash as werkzeug_generate_password_hash


def generate_password_hash(password):
    # Keep the encoded hash within the existing VARCHAR(100) password column.
    return werkzeug_generate_password_hash(
        password, method="pbkdf2:sha256:1000000", salt_length=8
    )


def is_legacy_hash(password_hash):
    return password_hash.startswith("sha256$")


def check_password_hash(password_hash, password):
    if password is None:
        return False
    if is_legacy_hash(password_hash):
        parts = password_hash.split("$")
        if len(parts) != 3 or not parts[1]:
            return False
        _, salt, expected = parts
        # Werkzeug's former sha256 method used HMAC with the salt as its key.
        # The weak hash is required to match the legacy format and only verifies
        # existing hashes; accounts are rehashed with PBKDF2 on the next login.
        # codeql[py/weak-sensitive-data-hashing]
        actual = hmac.new(salt.encode("utf-8"), password.encode("utf-8"), hashlib.sha256)
        return hmac.compare_digest(actual.hexdigest(), expected)
    return werkzeug_check_password_hash(password_hash, password)
