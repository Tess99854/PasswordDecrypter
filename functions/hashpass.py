#from dao.User import User
import os
import hashlib




def hashPassw(password) :
    salt = os.urandom(32)
    password = password.encode()
    password = hashlib.pbkdf2_hmac('sha256', password, salt, 10000)
    password = password
    print(password)
    return password


if __name__=="__main__":
   print (hashPassw('essia'))