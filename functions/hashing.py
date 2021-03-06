import hashlib
import base64


def hashing(message, type_hash):
    if type_hash == 'MD5':
        message = message.encode()
        message = hashlib.md5(message).hexdigest()
        return message
    if type_hash == 'SHA1':
        return hashlib.sha1(message.encode()).hexdigest()
    if type_hash == 'SHA256':
        return hashlib.sha256(message.encode()).hexdigest()


if __name__ == "__main__":
    # First let us encrypt secret message
    print(hashing('aaaaa', 'MD5'))
