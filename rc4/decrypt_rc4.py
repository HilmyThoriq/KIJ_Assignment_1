from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

key = b"sapodkfpasokdfpakwp0ro2-o4-19-053c.=waxCAEr//.;\DQW/E]WQ["
msg = b'\x0e)\x92 '

decrypt = ARC4.new(key).decrypt(msg.decode('utf-8'))
print(decrypt)