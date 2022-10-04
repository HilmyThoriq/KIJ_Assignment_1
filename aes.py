# Advance Encryption Standard using CTR mode
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

BLOCK_SIZE = 16 # Bytes
key = get_random_bytes(16) # can change to 16/24/32 

with open("test.txt", "rb") as file:
    msg = file.read()

start = time.time()

cipher = AES.new(key, AES.MODE_CTR)
msg = cipher.encrypt(pad(msg, BLOCK_SIZE))

end = time.time()
total = end - start

with open("test_encrypted.txt", "wb") as file_dec:
    file_dec.write(msg)

print("\n"+str(total))
