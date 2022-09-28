from Crypto.Cipher import AES

file_in = open("test.txt", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

key = b'U\x94\xea\xf3g\x9f0Jjf\xc9\x9c\x8c\xb0\x11`'
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))