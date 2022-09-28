from Crypto.Cipher import AES
import os

with open("test.txt", "rb") as file:
    data = file.read()

key = os.urandom(16)
print(key)

cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

# file_out = open("text.txt", "wb")
with open("test.txt", "wb") as file_out:
    for x in (cipher.nonce, tag, ciphertext):
        file_out.write(x) 
    file_out.close()