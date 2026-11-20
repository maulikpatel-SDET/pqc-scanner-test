// Legacy TLS server (ES module). TEST ONLY.
import https from 'node:https';
import fs from 'node:fs';

const server = https.createServer({
  key: fs.readFileSync('keys/rsa_private.pem'),
  cert: fs.readFileSync('certs/rsa_server.cert'),
  minVersion: 'TLSv1',
  maxVersion: 'TLSv1.1',
  ciphers: 'DES-CBC3-SHA:RC4-SHA:AES128-SHA',
  secureProtocol: 'TLSv1_method',
}, (req, res) => res.end('ok'));

server.listen(8443);
