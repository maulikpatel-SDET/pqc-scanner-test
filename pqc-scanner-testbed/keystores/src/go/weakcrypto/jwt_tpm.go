package weakcrypto

// JWT RS256/ES256 and a TPM-held RSA key. TEST ONLY.

import (
	"crypto/rsa"

	"github.com/golang-jwt/jwt/v5"
	"github.com/google/go-tpm/legacy/tpm2"
)

func IssueRS256(key *rsa.PrivateKey) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodRS256, jwt.MapClaims{"sub": "test"}).SignedString(key)
}

func IssueES256(key interface{}) (string, error) {
	return jwt.NewWithClaims(jwt.SigningMethodES256, jwt.MapClaims{"sub": "test"}).SignedString(key)
}

var TPMRSATemplate = tpm2.Public{
	Type:       tpm2.AlgRSA,
	NameAlg:    tpm2.AlgSHA1,
	Attributes: tpm2.FlagSign | tpm2.FlagSensitiveDataOrigin | tpm2.FlagUserWithAuth,
	RSAParameters: &tpm2.RSAParams{
		Sign:    &tpm2.SigScheme{Alg: tpm2.AlgRSASSA, Hash: tpm2.AlgSHA1},
		KeyBits: 2048,
	},
}
