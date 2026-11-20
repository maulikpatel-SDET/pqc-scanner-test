// Post-quantum key encapsulation with ML-KEM (Go 1.24 crypto/mlkem). Expected: no findings.
package cleanpqc

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/mlkem"
	"crypto/sha256"
	"crypto/tls"
)

func Encapsulate() ([]byte, []byte, error) {
	dk, err := mlkem.GenerateKey768()
	if err != nil {
		return nil, nil, err
	}
	shared, ct := dk.EncapsulationKey().Encapsulate()
	return shared, ct, nil
}

func Seal(key, nonce, msg []byte) ([]byte, error) {
	block, err := aes.NewCipher(key) // 32-byte key: AES-256
	if err != nil {
		return nil, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	return gcm.Seal(nil, nonce, msg, nil), nil
}

func Digest(b []byte) [32]byte { return sha256.Sum256(b) }

var ServerTLS = &tls.Config{
	MinVersion:       tls.VersionTLS13,
	CurvePreferences: []tls.CurveID{tls.X25519MLKEM768},
}
