import os
import rsa


PRIVATE_KEY_FILE = 'private.pem'


def initialize():
    if not os.path.exists(PRIVATE_KEY_FILE):
        ans = raw_input('Private key not found. Generate a new one? (Y/n)')
        if ans.lower() != 'n':
            public_key, private_key = rsa.newkeys(512)
        else:
            print 'Bye.'
            exit()
