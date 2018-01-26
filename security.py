# -*- coding: utf-8 -*-
import rsa

pubkey, privkey = rsa.newkeys(512)

def get_public_key():
    return pubkey.save_pkcs1()

def encrypt(message, keydata):
    key = rsa.PublicKey.load_pkcs1(keydata)
    return rsa.encrypt(message, key)

def decrypt(message):
    return rsa.decrypt(message, privkey)

# s = "中文"
# t = encrypt(s, get_public_key())
# print t
# d = decrypt(t)
# print '-'
# print d
