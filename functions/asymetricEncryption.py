import json

from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import new
from Crypto.Hash import SHA256

from app.utils.encoder import decode, encode


class AsymSecurity:

    @staticmethod
    def from_key(key):
        return AsymSecurity(key)

    @staticmethod
    def get_instance():
        key=""
        with open("key.pem", "r") as f:
            key = RSA.importKey(f.read())
        return AsymSecurity(key)

    def __init__(self, key):
        self.key = key

    @staticmethod
    def generate_key():
        rsa_result = RSA.generate(3072)
        key = rsa_result.exportKey()
        return key

    def sign(self, data):
        sig = new(self.key)
        data_encoded = json.dumps(data, sort_keys=True, ensure_ascii=True).encode("utf-8")
        return sig.sign(SHA256.new(data_encoded))

    def verify(self, data: dict, signature):
        verifier = new(self.key)
        data_encoded = json.dumps(data, sort_keys=True, ensure_ascii=True).encode("utf-8")
        verifier.verify(SHA256.new(data_encoded), signature)

    def get_public_key(self):
        return encode(self.key.publickey().export_key())
