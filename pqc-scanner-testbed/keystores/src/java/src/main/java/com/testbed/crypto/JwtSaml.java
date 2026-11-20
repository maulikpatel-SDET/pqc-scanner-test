package com.testbed.crypto;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.security.PrivateKey;
import org.opensaml.xmlsec.signature.support.SignatureConstants;
import org.apache.xml.security.signature.XMLSignature;

/** JWT RS256 / ES256 and SAML RSA-SHA1 signing. TEST ONLY. */
public class JwtSaml {

    public static String rs256(PrivateKey key) {
        return Jwts.builder().setSubject("test").signWith(key, SignatureAlgorithm.RS256).compact();
    }

    public static String es256(PrivateKey key) {
        return Jwts.builder().setSubject("test").signWith(key, SignatureAlgorithm.ES256).compact();
    }

    public static final String SAML_SIG_ALG = SignatureConstants.ALGO_ID_SIGNATURE_RSA_SHA1;
    public static final String XML_SIG_ALG = XMLSignature.ALGO_ID_SIGNATURE_RSA_SHA1;
}
