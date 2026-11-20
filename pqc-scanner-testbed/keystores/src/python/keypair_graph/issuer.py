"""Key generation side of a keypair (for the keypair-graph feature). TEST ONLY."""
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class TokenIssuer:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def sign(self, data: bytes) -> bytes:
        return self.private_key.sign(data, padding.PKCS1v15(), hashes.SHA256())
