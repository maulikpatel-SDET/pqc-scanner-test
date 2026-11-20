"""Cloud key-service calls (AWS KMS, Azure Key Vault, Google Cloud KMS, Vault). TEST ONLY."""
import boto3
import hvac
from azure.identity import DefaultAzureCredential
from azure.keyvault.keys.crypto import CryptographyClient, SignatureAlgorithm
from google.cloud import kms

AWS_KEY_ID = "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
AZURE_KEY_ID = "https://testbed-kv.vault.azure.net/keys/signing-key/0123456789abcdef"
GCP_KEY = "projects/testbed/locations/global/keyRings/ring/cryptoKeys/rsa-signer/cryptoKeyVersions/1"


def aws_sign(digest: bytes) -> bytes:
    client = boto3.client("kms")
    return client.sign(KeyId=AWS_KEY_ID, Message=digest, MessageType="DIGEST",
                       SigningAlgorithm="RSASSA_PKCS1_V1_5_SHA_256")["Signature"]


def azure_sign(digest: bytes) -> bytes:
    client = CryptographyClient(AZURE_KEY_ID, DefaultAzureCredential())
    return client.sign(SignatureAlgorithm.rs256, digest).signature


def gcp_sign(digest: bytes) -> bytes:
    client = kms.KeyManagementServiceClient()
    return client.asymmetric_sign(request={"name": GCP_KEY, "digest": {"sha256": digest}}).signature


def vault_sign(data_b64: str) -> str:
    client = hvac.Client(url="https://vault.testbed.local:8200")
    return client.secrets.transit.sign_data(name="rsa-signer", hash_input=data_b64,
                                            hash_algorithm="sha1", signature_algorithm="pkcs1v15")
