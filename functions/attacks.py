import hashlib
import base64


def use_dictionnary():
    with open("./functions/dictionnary.txt", "r") as f:
        for i in f.readlines():
            yield i


def attacks(message, hash_type):
    if hash_type == 'MD5':
        for i in use_dictionnary():
            if base64.b64encode(hashlib.md5(i.encode()).digest()).decode('utf-8') == message:
                return i
        return 'message not found'
    if hash_type == 'SHA1':
        for i in use_dictionnary():
            if hashlib.sha1(i.encode()).hexdigest() == message:
                return i
        return 'message not found'
    if hash_type == 'SHA256':
        for i in use_dictionnary():
            if hashlib.sha256(i.encode()).hexdigest() == message:
                return i
        return 'message not found'


if __name__ == "__main__":
    # First let us encrypt secret message
    print(attacks('WU+AOzgKQTlu1j3KOVA1Qg==', 'MD5'))
