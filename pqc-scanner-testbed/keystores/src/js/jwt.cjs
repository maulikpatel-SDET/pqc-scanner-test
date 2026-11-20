// JWT signing with RS256 / ES256 (CommonJS). TEST ONLY.
const jwt = require('jsonwebtoken');
const fs = require('fs');

const privateKey = fs.readFileSync('keys/rsa_private.pem');

exports.issue = (sub) => jwt.sign({ sub }, privateKey, { algorithm: 'RS256', expiresIn: '1h' });
exports.issueEc = (sub, ecKey) => jwt.sign({ sub }, ecKey, { algorithm: 'ES256' });
exports.verify = (t, pub) => jwt.verify(t, pub, { algorithms: ['RS256', 'ES256'] });
