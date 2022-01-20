import os
import hashlib
import base64


def hash_password(password):
    salt = os.urandom(32)
    password = password.encode()
    password = hashlib.pbkdf2_hmac('sha256', password, salt, 10000)
    password = password
    return base64.b64encode(password).decode('utf-8')


if __name__ == "__main__":
    print(hash_password('essia'))
