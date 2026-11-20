// Certificate fingerprint pinning (SHA-1) and HPKP header. TEST ONLY.
import tls from 'node:tls';
import crypto from 'node:crypto';

const PIN = 'AB:CD:EF:01:23:45:67:89:AB:CD:EF:01:23:45:67:89:AB:CD:EF:01';

export function checkServerIdentity(host: string, cert: tls.PeerCertificate) {
  if (cert.fingerprint !== PIN) return new Error('pin mismatch');
  const sha1 = crypto.createHash('sha1').update(cert.raw).digest('hex');
  return sha1 ? undefined : new Error('no cert');
}

export const HPKP_HEADER = 'Public-Key-Pins: pin-sha256="d6qzRu9zOECb90Uez27xWltNsj0e1Md7GkYYkVoZWmM="; max-age=5184000';
