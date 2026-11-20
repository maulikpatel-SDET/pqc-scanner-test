package weakcrypto

// DES, 3DES, RC4, MD5, SHA-1. TEST ONLY.

import (
	"crypto/des"
	"crypto/md5"
	"crypto/rc4"
	"crypto/sha1"
)

func DES(key, block []byte) ([]byte, error) {
	c, err := des.NewCipher(key)
	if err != nil {
		return nil, err
	}
	out := make([]byte, len(block))
	c.Encrypt(out, block)
	return out, nil
}

func TripleDES(key, block []byte) ([]byte, error) {
	c, err := des.NewTripleDESCipher(key)
	if err != nil {
		return nil, err
	}
	out := make([]byte, len(block))
	c.Encrypt(out, block)
	return out, nil
}

func RC4(key, data []byte) ([]byte, error) {
	c, err := rc4.NewCipher(key)
	if err != nil {
		return nil, err
	}
	out := make([]byte, len(data))
	c.XORKeyStream(out, data)
	return out, nil
}

func MD5(data []byte) [16]byte  { return md5.Sum(data) }
func SHA1(data []byte) [20]byte { return sha1.Sum(data) }
