"""RSA key held in a TPM. TEST ONLY."""
from tpm2_pytss import ESAPI, TPM2B_PUBLIC, TPM2_ALG


def create_tpm_rsa_key():
    with ESAPI() as ectx:
        template = TPM2B_PUBLIC.parse("rsa2048:rsassa-sha256")
        return ectx.create_primary(None, in_public=template)


def tpm_ecc_key():
    with ESAPI() as ectx:
        return ectx.create_primary(None, in_public=TPM2B_PUBLIC.parse("ecc256:ecdsa-sha256"))


ALG = TPM2_ALG.RSA
