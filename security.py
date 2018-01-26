import rsa

pubkey, privkey = rsa.newkeys(512)

def get_public_key():
    return pubkey.save_pkcs1()

def encrypt(message, keydata):
    key = rsa.PublicKey.load_pkcs1(keydata)
    return rsa.encrypt(message.encode('utf8'), key)

def decrypt(message):
    return rsa.decrypt(message, privkey).decode('utf8')

