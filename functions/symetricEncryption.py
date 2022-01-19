import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import DES
 
def dopad(BLOCK_SIZE, s):
    return  s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
def dounpad(BLOCK_SIZE, s):
    return s[:-ord(s[len(s) - 1:])]
 
password = '01234567'

def encrypt(raw, encType):
    if encType == 'AES' :
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        raw = dopad(16,raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))
    if encType == 'DES' :
        iv = Random.get_random_bytes(8)
        des1 = DES.new(password.encode(), DES.MODE_CFB, iv)
        raw = dopad(8, raw)
        return des1.encrypt(raw)

 
 
def decrypt(enc, encType):
    if encType == 'AES' :
        private_key = hashlib.sha256(password.encode("utf-8")).digest()
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(private_key, AES.MODE_CBC, iv)
        return dounpad(16 , cipher.decrypt(enc[16:]))
    if encType == 'DES' :
        enc = base64.b64decode(enc)
        iv = enc[:8]
        des1 = DES.new(password.encode(), DES.MODE_CFB, iv)
        return dounpad(8 , des1.decrypt(enc[8:]))
 

if __name__=="__main__":
    # First let us encrypt secret message
    encrypted = encrypt("This is a secret message", 'AES')
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, 'AES')
    print(bytes.decode(decrypted))

    # First let us encrypt secret message
    encrypted = encrypt("This is a secret message", 'DES')
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, 'DES')
    print(decrypted)