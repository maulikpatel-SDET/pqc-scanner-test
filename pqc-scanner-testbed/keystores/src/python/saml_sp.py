"""SAML signing and encryption with RSA-SHA1. TEST ONLY."""
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.constants import OneLogin_Saml2_Constants
import xmlsec

SECURITY = {
    "authnRequestsSigned": True,
    "wantAssertionsEncrypted": True,
    "signatureAlgorithm": OneLogin_Saml2_Constants.RSA_SHA1,
    "digestAlgorithm": OneLogin_Saml2_Constants.SHA1,
}


def sign_xml(node, key_file: str):
    ctx = xmlsec.SignatureContext()
    ctx.key = xmlsec.Key.from_file(key_file, xmlsec.constants.KeyDataFormatPem)
    sig = xmlsec.template.create(node, xmlsec.constants.TransformExclC14N,
                                 xmlsec.constants.TransformRsaSha1)
    ctx.sign(sig)
    return sig


def encrypt_assertion(node, cert_file: str):
    manager = xmlsec.KeysManager()
    manager.add_key(xmlsec.Key.from_file(cert_file, xmlsec.constants.KeyDataFormatCertPem))
    enc = xmlsec.EncryptionContext(manager)
    enc.key = xmlsec.Key.generate(xmlsec.constants.KeyDataDes, 192, xmlsec.constants.KeyDataTypeSession)
    return enc
