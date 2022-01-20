from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import base64
import sys
sys.path.append('ELGAMAL')
import elgamal

key = RSA.generate(2048)
privateKey = key.exportKey('PEM')
publicKey = key.publickey().exportKey('PEM')
_elgamal_keys = elgamal.generate_keys(128)
elgamal_pubkey = _elgamal_keys["publicKey"]
elgamal_privkey = _elgamal_keys["privateKey"]

def rsaenc(message):
    message = str.encode(message)
    RSApublicKey = RSA.importKey(publicKey)
    OAEP_cipher = PKCS1_OAEP.new(RSApublicKey)
    encryptedMsg = OAEP_cipher.encrypt(message)
    return base64.b64encode(encryptedMsg).decode('utf-8')

def rsadec(message):
    RSAprivateKey = RSA.importKey(privateKey)
    OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
    message = base64.b64decode(message)
    decryptedMsg = OAEP_cipher.decrypt(message)
    return decryptedMsg.decode('utf-8').strip()

def elGamalEnc(message):
    cipher = elgamal.encrypt(elgamal_pubkey, message)
    return cipher

def elGamalDec(message):
    plaintext = elgamal.decrypt(elgamal_privkey, message)
    return plaintext


if __name__=="__main__":
    # First let us encrypt secret message
    encrypted = rsaenc("This is a secret message")
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = rsadec(encrypted)
    print(decrypted)

    encrypted = elGamalEnc("This is a secret message")
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = elGamalDec(encrypted)
    print(decrypted)

