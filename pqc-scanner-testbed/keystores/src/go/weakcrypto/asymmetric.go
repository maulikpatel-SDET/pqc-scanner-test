// Package weakcrypto: RSA, ECDSA, ECDH, DSA. TEST ONLY.
package weakcrypto

import (
	"crypto"
	"crypto/dsa"
	"crypto/ecdh"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
)

func RSASign(data []byte) ([]byte, error) {
	key, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		return nil, err
	}
	h := sha256.Sum256(data)
	return rsa.SignPKCS1v15(rand.Reader, key, crypto.SHA256, h[:])
}

func RSAEncrypt(pub *rsa.PublicKey, msg []byte) ([]byte, error) {
	return rsa.EncryptPKCS1v15(rand.Reader, pub, msg)
}

func ECDSASign(data []byte) ([]byte, error) {
	key, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, err
	}
	h := sha256.Sum256(data)
	return ecdsa.SignASN1(rand.Reader, key, h[:])
}

func ECDH() ([]byte, error) {
	a, _ := ecdh.P256().GenerateKey(rand.Reader)
	b, _ := ecdh.P256().GenerateKey(rand.Reader)
	return a.ECDH(b.PublicKey())
}

func X25519() ([]byte, error) {
	a, _ := ecdh.X25519().GenerateKey(rand.Reader)
	b, _ := ecdh.X25519().GenerateKey(rand.Reader)
	return a.ECDH(b.PublicKey())
}

func DSAKey() (*dsa.PrivateKey, error) {
	var params dsa.Parameters
	if err := dsa.GenerateParameters(&params, rand.Reader, dsa.L2048N256); err != nil {
		return nil, err
	}
	priv := &dsa.PrivateKey{PublicKey: dsa.PublicKey{Parameters: params}}
	return priv, dsa.GenerateKey(priv, rand.Reader)
}
