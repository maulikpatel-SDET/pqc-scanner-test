package weakcrypto

// Legacy TLS server and client. TEST ONLY.

import (
	"crypto/tls"
	"net/http"
)

func LegacyServer() error {
	cfg := &tls.Config{
		MinVersion: tls.VersionTLS10,
		MaxVersion: tls.VersionTLS11,
		CipherSuites: []uint16{
			tls.TLS_RSA_WITH_3DES_EDE_CBC_SHA,
			tls.TLS_RSA_WITH_RC4_128_SHA,
			tls.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,
		},
	}
	srv := &http.Server{Addr: ":8443", TLSConfig: cfg}
	return srv.ListenAndServeTLS("certs/rsa_server.cert", "keys/rsa_private.pem")
}

func InsecureClient() *http.Client {
	return &http.Client{Transport: &http.Transport{TLSClientConfig: &tls.Config{
		MinVersion:         tls.VersionTLS10,
		InsecureSkipVerify: true,
	}}}
}
