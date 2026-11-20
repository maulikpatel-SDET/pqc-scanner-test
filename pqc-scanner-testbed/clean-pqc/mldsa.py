"""Post-quantum signatures with ML-DSA / SLH-DSA via liboqs. Expected: no findings."""
import hashlib
import oqs


def sign(message: bytes) -> bytes:
    with oqs.Signature("ML-DSA-65") as signer:
        signer.generate_keypair()
        return signer.sign(message)


def sign_hash_based(message: bytes) -> bytes:
    with oqs.Signature("SLH-DSA-SHA2-128s") as signer:
        signer.generate_keypair()
        return signer.sign(message)


def kem():
    with oqs.KeyEncapsulation("ML-KEM-768") as k:
        pk = k.generate_keypair()
        return k.encap_secret(pk)


def digest(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()
