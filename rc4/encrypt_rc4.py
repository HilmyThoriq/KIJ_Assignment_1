from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

msg = "test"
key = b"sapodkfpasokdfpakwp0ro2-o4-19-053c.=waxCAEr//.;\DQW/E]WQ["
nonce = get_random_bytes(16)

key = SHA256.new(key+nonce).digest()
encrypt = ARC4.new(key).encrypt(msg.encode('utf-8'))

print(encrypt)