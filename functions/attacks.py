import hashlib
import base64


def use_dictionnary():
    with open("./functions/dictionnary.txt", "r") as f:
        for i in f.readlines():
            yield i


def attacks(message, hash_type):
    if hash_type == 'MD5':
        for i in use_dictionnary():
            if hashlib.md5(i.strip().encode()).hexdigest() == message:
                return i
        return 'message not found'
    if hash_type == 'SHA1':
        for i in use_dictionnary():
            if hashlib.sha1(i.strip().encode()).hexdigest() == message:
                return i
        return 'message not found'
    if hash_type == 'SHA256':
        for i in use_dictionnary():
            if hashlib.sha256(i.strip().encode()).hexdigest() == message:
                return i
        return 'message not found'


if __name__ == "__main__":
    # First let us encrypt secret message
    print(attacks('594f803b380a41396ed63dca39503542', 'MD5'))
