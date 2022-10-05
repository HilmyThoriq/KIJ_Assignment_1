from Crypto.Cipher import AES,DES, ARC4

key = b"OX\xc4Ky\xf1_\x1b_`u\xc4\xeb\xac\xec\xa7\x0c\x100\xf1\xf5\x1c\xf8Z\x0c\xb5\xaf\xe5_\xc1\x92'" # Changeable
iv = b'4\xbe\x87\x8d\x13\xbed\x07' # Changeable

def aes():
    with open("aes_enc.txt", "rb") as file_enc:
        c_txt = file_enc.read()

    cipher = AES.new(key, AES.MODE_CFB, iv)
    p_txt = cipher.decrypt(c_txt)

    with open("aes_dec.txt", "wb") as file_dec:
        file_dec.write(p_txt)

def des():
    with open("des_enc.txt", "rb") as file_enc:
        c_txt = file_enc.read()

    cipher = DES.new(key, DES.MODE_CFB, iv)
    p_txt = cipher.decrypt(c_txt)
    p_txt = p_txt[8:16]

    with open("des_dec.txt", "wb") as file_dec:
        file_dec.write(p_txt)

def rc4():
    with open("rc4_enc.txt", "rb") as file_enc:
        c_txt = file_enc.read()

    cipher = ARC4.new(key)
    p_txt = cipher.decrypt(c_txt)

    with open("rc4_dec.txt", "wb") as file_dec:
        file_dec.write(p_txt)

# aes()
# des ()
rc4()