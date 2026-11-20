// MD5 / SHA-1 / 3DES in a React component via crypto-js. TEST ONLY.
import React from 'react';
import CryptoJS from 'crypto-js';
import NodeRSA from 'node-rsa';

export default function Fingerprint({ value }) {
  const md5 = CryptoJS.MD5(value).toString();
  const sha1 = CryptoJS.SHA1(value).toString();
  const enc = CryptoJS.TripleDES.encrypt(value, 'test-secret').toString();
  const rc4 = CryptoJS.RC4.encrypt(value, 'test-secret').toString();
  const rsa = new NodeRSA({ b: 1024 });
  return <pre>{md5} {sha1} {enc} {rc4} {rsa.encrypt(value, 'base64')}</pre>;
}
