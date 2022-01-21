import os
import hashlib


def hash_password(password):
    salt = os.urandom(32)
    password = password.encode('utf-8')
    password = hashlib.pbkdf2_hmac('sha256', password, salt, 10000)
    password = password + salt
    return password


def verifyPassword(passToCheck, password, salt):
    new_key = hashlib.pbkdf2_hmac('sha256', passToCheck.encode('utf-8'),salt, 100000)
    if new_key == password:
        return True
    else:
        return False

if __name__ == "__main__":
    print(hash_password('essia'))
