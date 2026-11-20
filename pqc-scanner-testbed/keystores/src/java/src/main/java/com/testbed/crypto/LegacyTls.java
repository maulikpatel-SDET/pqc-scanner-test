package com.testbed.crypto;

import java.io.FileInputStream;
import java.security.KeyStore;
import javax.net.ssl.*;

/** TLS 1.0 / 1.1 contexts and a keystore reference. TEST ONLY. */
public class LegacyTls {

    public static SSLContext tls10() throws Exception {
        SSLContext ctx = SSLContext.getInstance("TLSv1");
        ctx.init(null, null, null);
        return ctx;
    }

    public static SSLServerSocket server(int port) throws Exception {
        KeyStore ks = KeyStore.getInstance("PKCS12");
        ks.load(new FileInputStream("keystores/server.p12"), "changeit".toCharArray());
        KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
        kmf.init(ks, "changeit".toCharArray());
        SSLContext ctx = SSLContext.getInstance("TLSv1.1");
        ctx.init(kmf.getKeyManagers(), null, null);
        SSLServerSocket s = (SSLServerSocket) ctx.getServerSocketFactory().createServerSocket(port);
        s.setEnabledProtocols(new String[] {"TLSv1", "TLSv1.1"});
        s.setEnabledCipherSuites(new String[] {"SSL_RSA_WITH_3DES_EDE_CBC_SHA", "TLS_RSA_WITH_RC4_128_SHA"});
        return s;
    }

    public static KeyStore jks() throws Exception {
        KeyStore ks = KeyStore.getInstance("JKS");
        ks.load(new FileInputStream("keystores/truststore.jks"), "changeit".toCharArray());
        return ks;
    }
}
