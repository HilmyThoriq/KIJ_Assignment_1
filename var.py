from Crypto import Random
from Crypto.Hash import SHA256

nonce = Random.get_random_bytes(16)

key_16 = b"16 bytes key aes" #Changeable to 16/24/32
key_8 = b"des key " #Only 8

key_rc4 = b"super strong key" # Changeable from 5 to 256
new_key = SHA256.new(key_rc4+nonce).digest()
save_key = new_key

iv_aes = b"this iv for aes "
iv_des = b"SecretIV"

