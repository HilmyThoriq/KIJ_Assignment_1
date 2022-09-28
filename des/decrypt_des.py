from Crypto.Cipher import DES

key = b'-8B key ' 
msg = b'\xaf\xbe\x93\xda>k\xc9~\x006\x17\xaf\xbeB\x19(\x00'

cipher = DES.new(key, DES.MODE_OFB)
msg = cipher.decrypt(msg)

print (msg)
