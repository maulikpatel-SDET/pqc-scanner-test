"""Certificate fingerprint pinning with SHA-1. TEST ONLY."""
import hashlib
import ssl

PINNED_SHA1 = "3a:5f:9c:11:2b:7e:44:d0:91:aa:bc:de:f0:12:34:56:78:9a:bc:de"


def check_pin(host: str) -> bool:
    der = ssl.get_server_certificate((host, 443))
    fp = hashlib.sha1(ssl.PEM_cert_to_DER_cert(der)).hexdigest()
    return fp == PINNED_SHA1.replace(":", "")
