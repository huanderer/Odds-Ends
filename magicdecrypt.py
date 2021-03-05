import sys
import os
import hashlib
from des import des, CBC, PAD_PKCS5


def decrypt(filename):
    k = des(b"87629ae8", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    with open(filename,"rb") as file:
        encrypted_data=file.read()
    
    decrypted_data=k.decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)

decrypt(sys.argv[1])
