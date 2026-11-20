"""Verifier in a different file with no crypto finding of its own:
cross-file keypair candidates (QP-39) should attach this to issuer.py."""
from .issuer import TokenIssuer


class TokenVerifier:
    def __init__(self, issuer: TokenIssuer):
        self.public_key = issuer.public_key

    def check(self, data: bytes, signature: bytes) -> bool:
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes
        self.public_key.verify(signature, data, padding.PKCS1v15(), hashes.SHA256())
        return True
