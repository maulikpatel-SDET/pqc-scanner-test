package com.testbed.crypto;

import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/** DES, 3DES, RC4, MD5, SHA-1. TEST ONLY. */
public class SymmetricAndHashes {

    public static byte[] des(byte[] key, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("DES/ECB/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(key, "DES"));
        return c.doFinal(data);
    }

    public static byte[] tripleDes(byte[] key, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("DESede/CBC/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(key, "DESede"));
        return c.doFinal(data);
    }

    public static byte[] rc4(byte[] key, byte[] data) throws Exception {
        Cipher c = Cipher.getInstance("ARCFOUR");
        c.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(key, "RC4"));
        return c.doFinal(data);
    }

    public static byte[] md5(byte[] data) throws Exception {
        return MessageDigest.getInstance("MD5").digest(data);
    }

    public static byte[] sha1(byte[] data) throws Exception {
        return MessageDigest.getInstance("SHA-1").digest(data);
    }

    public static byte[] hmacSha1(byte[] key, byte[] data) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA1");
        mac.init(new SecretKeySpec(key, "HmacSHA1"));
        return mac.doFinal(data);
    }
}
