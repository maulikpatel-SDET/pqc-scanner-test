// JWT verification and SAML settings in a TSX component. TEST ONLY.
import React from 'react';
import { jwtVerify, importSPKI } from 'jose';

const SAML = { signatureAlgorithm: 'http://www.w3.org/2000/09/xmldsig#rsa-sha1' };

export async function verify(token: string, spki: string) {
  const key = await importSPKI(spki, 'RS256');
  return jwtVerify(token, key, { algorithms: ['RS256'] });
}

export const LoginForm: React.FC = () => <form data-alg={SAML.signatureAlgorithm} />;
