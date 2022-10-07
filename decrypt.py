from Crypto.Cipher import AES,DES, ARC4
from var import *

def aes(data):
    cipher = AES.new(key_16, AES.MODE_CFB, iv_aes)
    p_txt = cipher.decrypt(data)
    return p_txt

def des(data):
    cipher = DES.new(key_8, DES.MODE_CFB, iv_des)
    p_txt = cipher.decrypt(data)
    p_txt = p_txt[8:]

    return p_txt

def rc4(new_key_rc4,data):
    cipher = ARC4.new(new_key_rc4)
    p_txt = cipher.decrypt(data)
    return p_txt

# aes()
# des()
# rc4()