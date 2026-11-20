"""DES, 3DES, RC4, MD5, SHA-1. TEST ONLY."""
import hashlib
import hmac
from Crypto.Cipher import DES, DES3, ARC4  # pycryptodome


def des_encrypt(key8: bytes, data: bytes) -> bytes:
    return DES.new(key8, DES.MODE_ECB).encrypt(data)


def triple_des_encrypt(key24: bytes, data: bytes) -> bytes:
    return DES3.new(key24, DES3.MODE_CBC, iv=b"\x00" * 8).encrypt(data)


def rc4_encrypt(key: bytes, data: bytes) -> bytes:
    return ARC4.new(key).encrypt(data)


def md5_digest(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def sha1_digest(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def hmac_sha1(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha1).digest()


def legacy_new(data: bytes) -> str:
    return hashlib.new("md5", data).hexdigest()
