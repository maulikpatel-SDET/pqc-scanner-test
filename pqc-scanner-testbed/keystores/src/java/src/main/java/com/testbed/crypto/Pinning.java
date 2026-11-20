package com.testbed.crypto;

import okhttp3.CertificatePinner;
import okhttp3.OkHttpClient;

/** OkHttp certificate pinning. TEST ONLY. */
public class Pinning {
    public static OkHttpClient client() {
        CertificatePinner pinner = new CertificatePinner.Builder()
            .add("api.testbed.local", "sha1/BOGUSPINVALUE0000000000000=")
            .add("api.testbed.local", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
            .build();
        return new OkHttpClient.Builder().certificatePinner(pinner).build();
    }
}
