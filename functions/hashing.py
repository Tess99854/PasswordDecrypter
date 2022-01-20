import hashlib
import base64

def hashing(message, typeOfHash) :
    if typeOfHash == 'MD5':
        message = message.encode()
        message = hashlib.md5(message).digest()
        return base64.b64encode(message).decode('utf-8')
    if typeOfHash == 'SHA1':
        return hashlib.sha1(message.encode()).digest()
    if typeOfHash == 'SHA256' :
        return hashlib.sha256(message.encode()).digest()

if __name__=="__main__":
    # First let us encrypt secret message
    print(hashing('aaaaa','MD5'))