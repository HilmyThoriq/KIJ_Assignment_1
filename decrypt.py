from Crypto.Cipher import AES,DES, ARC4
from var import *

def aes(data):
    cipher = AES.new(key_16, AES.MODE_CFB, iv_aes)
    p_txt = cipher.decrypt(data)
    return p_txt

def des():
    with open("des_enc.txt", "rb") as file_enc:
        c_txt = file_enc.read()

    cipher = DES.new(key_8, DES.MODE_CFB, iv_des)
    p_txt = cipher.decrypt(c_txt)
    p_txt = p_txt[8:]

    with open("des_dec.txt", "wb") as file_dec:
        file_dec.write(p_txt)

def rc4():
    # with open("rc4_enc.txt", "rb") as file_enc:
    #     c_txt = file_enc.read()

    # cipher = ARC4.new(new_key)
    # p_txt = cipher.decrypt(c_txt)

    cipher = ARC4.new(dec_key)
    p_txt = cipher.decrypt(b'\x1b\xa4\xe6\xc1B\xcf\xe2|\x02\xc3\xad<\x10\xe5r\xfc\x05\xeb\xe5v\x04\xf4\xaa')
    print(p_txt)
    # with open("rc4_dec.txt", "wb") as file_dec:
    #     file_dec.write(p_txt)

# aes()
# des()
# rc4()