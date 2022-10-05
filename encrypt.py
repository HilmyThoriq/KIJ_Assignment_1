from Crypto.Cipher import AES, DES, ARC4
from Crypto.Hash import SHA256
from Crypto import Random

key = Random.get_random_bytes(16)
iv = Random.get_random_bytes(8)
print(iv)

with open("text.txt", "rb") as file:
        msg = file.read()

def aes():
    cipher = AES.new(key, AES.MODE_CFB, iv)
    c_txt = cipher.encrypt(msg)

    with open("aes_enc.txt", "wb") as file_enc:
        file_enc.write(c_txt)

def des(): # Key must 16 length
    cipher = DES.new(key, DES.MODE_CFB, iv)
    c_txt = iv + cipher.encrypt(msg)
    print(c_txt)

    with open("des_enc.txt", "wb") as file_enc:
        file_enc.write(c_txt)

def rc4():
    nonce = Random.get_random_bytes(16)
    new_key = SHA256.new(key+nonce).digest()
    cipher = ARC4.new(new_key)
    print(new_key)
    c_txt = cipher.encrypt(msg)

    with open("rc4_enc.txt", "wb") as file_enc:
        file_enc.write(c_txt)


aes()
# des()
# rc4()