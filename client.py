import socket
from decrypt import *

# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# Connect socket to the host and port
sock.connect((host, port))
print('Connection Established.')
# Send a greeting to the server
sock.send('A message from the client'.encode())

# Write File in binary
file = open('received_test.jpg', 'wb')

# Keep receiving data from the server
data = sock.recv(99999)

while(data):
    file.write(aes(data))
    data = sock.recv(99999)

print('File has been received successfully.')

file.close()
sock.close()
print('Connection Closed.')