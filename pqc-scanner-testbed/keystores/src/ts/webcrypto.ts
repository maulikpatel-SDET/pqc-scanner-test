// WebCrypto RSA, ECDSA, ECDH and SHA-1. TEST ONLY.
export async function rsaOaepKeys(): Promise<CryptoKeyPair> {
  return crypto.subtle.generateKey(
    { name: 'RSA-OAEP', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-1' },
    true, ['encrypt', 'decrypt']);
}

export async function rsaPssKeys(): Promise<CryptoKeyPair> {
  return crypto.subtle.generateKey(
    { name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1, 0, 1]), hash: 'SHA-256' },
    true, ['sign', 'verify']);
}

export async function ecdsaKeys(): Promise<CryptoKeyPair> {
  return crypto.subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
}

export async function ecdhKeys(): Promise<CryptoKeyPair> {
  return crypto.subtle.generateKey({ name: 'ECDH', namedCurve: 'P-384' }, true, ['deriveKey']);
}

export async function sha1(data: ArrayBuffer): Promise<ArrayBuffer> {
  return crypto.subtle.digest('SHA-1', data);
}
