import hashlib

def hashing(message, typeOfHash) :
    if typeOfHash == 'MD5':
        message = message.encode()
        message = hashlib.md5(message).digest()
        return message
    if typeOfHash == 'SHA1':
        return hashlib.sha1(message.encode()).digest()
    if typeOfHash == 'SHA256' :
        return hashlib.sha256(message.encode()).digest()