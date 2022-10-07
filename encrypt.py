from Crypto.Cipher import AES, DES, ARC4
from Crypto import Random
from var import *

with open("test_gambar.jpg", "rb") as file:
        msg = file.read()

def aes(): # Key can 16/24/32
    cipher = AES.new(key_16, AES.MODE_CFB, iv_aes)
    c_txt = cipher.encrypt(msg)

    with open("enc.jpg", "wb") as file_enc:
        file_enc.write(c_txt)

def des(): # Key must 8 length
    cipher = DES.new(key_8, DES.MODE_CFB, iv_des)
    c_txt = iv_des + cipher.encrypt(msg)
    with open("enc.jpg", "wb") as file_enc:
        file_enc.write(c_txt)

def rc4(new_key_rc4):
    cipher = ARC4.new(new_key_rc4)
    c_txt = cipher.encrypt(msg)
    with open("enc.jpg", "wb") as file_enc:
        file_enc.write(c_txt)

# aes()
# des()
# rc4()