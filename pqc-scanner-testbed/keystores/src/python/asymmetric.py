"""RSA, ECDSA, ECDH, DSA, Diffie-Hellman. TEST ONLY."""
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa, dh, padding
from cryptography.hazmat.primitives import hashes


def rsa_sign(data: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.sign(data, padding.PKCS1v15(), hashes.SHA256())


def rsa_encrypt(data: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
    return key.public_key().encrypt(
        data, padding.OAEP(mgf=padding.MGF1(hashes.SHA1()), algorithm=hashes.SHA1(), label=None))


def ecdsa_sign(data: bytes) -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    return key.sign(data, ec.ECDSA(hashes.SHA256()))


def ecdh_shared_secret() -> bytes:
    a = ec.generate_private_key(ec.SECP384R1())
    b = ec.generate_private_key(ec.SECP384R1())
    return a.exchange(ec.ECDH(), b.public_key())


def dsa_sign(data: bytes) -> bytes:
    key = dsa.generate_private_key(key_size=2048)
    return key.sign(data, hashes.SHA256())


def diffie_hellman() -> bytes:
    params = dh.generate_parameters(generator=2, key_size=2048)
    a = params.generate_private_key()
    b = params.generate_private_key()
    return a.exchange(b.public_key())
