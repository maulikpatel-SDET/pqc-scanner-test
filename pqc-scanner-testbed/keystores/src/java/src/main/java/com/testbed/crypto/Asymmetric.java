package com.testbed.crypto;

import java.security.*;
import java.security.spec.ECGenParameterSpec;
import javax.crypto.Cipher;
import javax.crypto.KeyAgreement;

/** RSA, ECDSA, ECDH, DSA, DH. TEST ONLY. */
public class Asymmetric {

    public static byte[] rsaSign(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair kp = kpg.generateKeyPair();
        Signature sig = Signature.getInstance("SHA1withRSA");
        sig.initSign(kp.getPrivate());
        sig.update(data);
        return sig.sign();
    }

    public static byte[] rsaEncrypt(PublicKey pub, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("RSA/ECB/PKCS1Padding");
        c.init(Cipher.ENCRYPT_MODE, pub);
        return c.doFinal(data);
    }

    public static byte[] ecdsaSign(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
        kpg.initialize(new ECGenParameterSpec("secp256r1"));
        Signature sig = Signature.getInstance("SHA256withECDSA");
        sig.initSign(kpg.generateKeyPair().getPrivate());
        sig.update(data);
        return sig.sign();
    }

    public static byte[] ecdh(PrivateKey mine, PublicKey theirs) throws Exception {
        KeyAgreement ka = KeyAgreement.getInstance("ECDH");
        ka.init(mine);
        ka.doPhase(theirs, true);
        return ka.generateSecret();
    }

    public static byte[] dsaSign(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("DSA");
        kpg.initialize(2048);
        Signature sig = Signature.getInstance("SHA256withDSA");
        sig.initSign(kpg.generateKeyPair().getPrivate());
        sig.update(data);
        return sig.sign();
    }

    public static KeyPair dh() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("DiffieHellman");
        kpg.initialize(2048);
        return kpg.generateKeyPair();
    }
}
