import base64
import hashlib
import math
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import DES
 
COMMON_ENCRYPTION_KEY='asdjk@15r32r1234asdsaeqwe314SEFT'
COMMON_16_BYTE_IV_FOR_AES='IVIVIVIVIVIVIVIV'
COMMON_ENCRYPTION_KEY_DES='asdjk@15'

def encrypt(message, encType):
    if encType == 'AES' :
        aes = AES.new(COMMON_ENCRYPTION_KEY, AES.MODE_CBC, COMMON_16_BYTE_IV_FOR_AES)
        cleartext_length = len(message)
        next_multiple_of_16 = 16 * math.ceil(cleartext_length/16)
        padded_cleartext = message.rjust(next_multiple_of_16)
        raw_ciphertext = aes.encrypt(padded_cleartext)
        return base64.b64encode(raw_ciphertext).decode('utf-8')
    if encType == 'DES' :
        des1 = DES.new(COMMON_ENCRYPTION_KEY_DES, DES.MODE_ECB)
        cleartext_length = len(message)
        next_multiple_of_8 = 8 * math.ceil(cleartext_length/8)
        padded_cleartext = message.rjust(next_multiple_of_8)
        raw_ciphertext = des1.encrypt(padded_cleartext)
        return base64.b64encode(raw_ciphertext).decode('utf-8')
 
def decrypt(enc, encType):
    if encType == 'AES' :
        aes = AES.new(COMMON_ENCRYPTION_KEY, AES.MODE_CBC, COMMON_16_BYTE_IV_FOR_AES)
        raw_ciphertext = base64.b64decode(enc)
        decrypted_message_with_padding = aes.decrypt(raw_ciphertext)
        return decrypted_message_with_padding.decode('utf-8').strip()
    if encType == 'DES' :
        des1 = DES.new(COMMON_ENCRYPTION_KEY_DES, DES.MODE_ECB)
        raw_ciphertext = base64.b64decode(enc)
        decrypted_message_with_padding = des1.decrypt(raw_ciphertext)
        return decrypted_message_with_padding.decode('utf-8').strip()
 

if __name__=="__main__":
    # First let us encrypt secret message
    encrypted = encrypt("This is a secret message", 'AES')
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, 'AES')
    print(decrypted)

    # First let us encrypt secret message
    encrypted = encrypt("This is a secret message", 'DES')
    print(encrypted)
    
    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, 'DES')
    print(decrypted)