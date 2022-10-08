import socket
from decrypt import *

# Initialize Socket 
sock = socket.socket()
print ("Socket created successfully.")

# Define port and host
port = 8700
host = 'localhost'

# Connect socket 
sock.connect((host, port))
print('Connection Established.')
# Test if data sended
sock.send('A message from the client'.encode())

# Write Decrypted file destination
file = open('received_test.jpg', 'wb')

# Receive key for rc4 only
# new_key_rc4 = sock.recv(2048)

data = sock.recv(99999)

while(data):
    file.write(aes(data))
    # file.write(des(data))
    # file.write(rc4(new_key_rc4,data))
    data = sock.recv(99999)

print('File has been received successfully.')

file.close()
sock.close()
print('Connection Closed.')