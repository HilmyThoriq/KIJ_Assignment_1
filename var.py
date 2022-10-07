from Crypto import Random

nonce = Random.get_random_bytes(16)

key_16 = b"16 bytes key aes" #Changeable to 16/24/32
key_8 = b"des key " #Only 8

iv_aes = b"this iv for aes "
iv_des = b"SecretIV"
