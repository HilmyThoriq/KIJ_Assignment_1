from Crypto.Cipher import DES

key = b'-8B key '
cipher = DES.new(key, DES.MODE_OFB)
txt = b'hello all'
msg = cipher.iv + cipher.encrypt(txt)

print (msg)