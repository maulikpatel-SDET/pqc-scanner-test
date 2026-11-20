// RSA, ECDSA, ECDH, DH, DES/3DES, RC4, MD5, SHA-1 with Node crypto. TEST ONLY.
const crypto = require('crypto');

function rsaKeys() {
  return crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
}

function rsaSign(data, privateKey) {
  return crypto.createSign('RSA-SHA1').update(data).sign(privateKey);
}

function ecdsaKeys() {
  return crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' });
}

function ecdh() {
  const a = crypto.createECDH('secp256k1');
  const b = crypto.createECDH('secp256k1');
  a.generateKeys(); b.generateKeys();
  return a.computeSecret(b.getPublicKey());
}

function dh() {
  const a = crypto.createDiffieHellman(2048);
  a.generateKeys();
  return a;
}

function dsaKeys() {
  return crypto.generateKeyPairSync('dsa', { modulusLength: 2048, divisorLength: 256 });
}

function des3(key, iv, data) {
  const c = crypto.createCipheriv('des-ede3-cbc', key, iv);
  return Buffer.concat([c.update(data), c.final()]);
}

function des(key, data) {
  const c = crypto.createCipheriv('des-ecb', key, null);
  return Buffer.concat([c.update(data), c.final()]);
}

function rc4(key, data) {
  const c = crypto.createCipheriv('rc4', key, '');
  return c.update(data);
}

const md5 = (d) => crypto.createHash('md5').update(d).digest('hex');
const sha1 = (d) => crypto.createHash('sha1').update(d).digest('hex');

module.exports = { rsaKeys, rsaSign, ecdsaKeys, ecdh, dh, dsaKeys, des3, des, rc4, md5, sha1 };
