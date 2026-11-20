"""JWT / JWE with RSA and EC. TEST ONLY."""
import jwt  # PyJWT
from jose import jwe  # python-jose

with open("keys/rsa_private.pem") as fh:
    PRIVATE_KEY = fh.read()


def issue_rs256(claims: dict) -> str:
    return jwt.encode(claims, PRIVATE_KEY, algorithm="RS256")


def issue_es256(claims: dict, ec_key: str) -> str:
    return jwt.encode(claims, ec_key, algorithm="ES256")


def verify(token: str, public_key: str) -> dict:
    return jwt.decode(token, public_key, algorithms=["RS256", "ES256", "HS256"])


def encrypt_jwe(payload: bytes, public_key: str) -> bytes:
    return jwe.encrypt(payload, public_key, algorithm="RSA-OAEP", encryption="A128CBC-HS256")


def encrypt_jwe_rsa15(payload: bytes, public_key: str) -> bytes:
    return jwe.encrypt(payload, public_key, algorithm="RSA1_5", encryption="A128GCM")
