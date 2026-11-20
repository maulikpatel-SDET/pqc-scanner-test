# Cloud key definitions with quantum-vulnerable algorithms. TEST ONLY.

resource "aws_kms_key" "signer" {
  description              = "RSA signing key"
  customer_master_key_spec = "RSA_2048"
  key_usage                = "SIGN_VERIFY"
}

resource "aws_kms_key" "ecc_signer" {
  customer_master_key_spec = "ECC_NIST_P256"
  key_usage                = "SIGN_VERIFY"
}

resource "azurerm_key_vault_key" "rsa" {
  name         = "testbed-rsa"
  key_vault_id = var.key_vault_id
  key_type     = "RSA"
  key_size     = 2048
  key_opts     = ["sign", "verify", "encrypt", "decrypt"]
}

resource "azurerm_key_vault_key" "ec" {
  name         = "testbed-ec"
  key_vault_id = var.key_vault_id
  key_type     = "EC"
  curve        = "P-256"
  key_opts     = ["sign", "verify"]
}

resource "google_kms_crypto_key" "rsa_signer" {
  name     = "rsa-signer"
  key_ring = var.key_ring_id
  purpose  = "ASYMMETRIC_SIGN"
  version_template {
    algorithm = "RSA_SIGN_PKCS1_2048_SHA256"
  }
}

resource "google_kms_crypto_key" "ec_signer" {
  name     = "ec-signer"
  key_ring = var.key_ring_id
  purpose  = "ASYMMETRIC_SIGN"
  version_template {
    algorithm = "EC_SIGN_P256_SHA256"
  }
}

resource "vault_transit_secret_backend_key" "rsa" {
  backend = "transit"
  name    = "rsa-signer"
  type    = "rsa-2048"
}

resource "vault_transit_secret_backend_key" "ecdsa" {
  backend = "transit"
  name    = "ecdsa-signer"
  type    = "ecdsa-p256"
}
