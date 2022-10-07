import socket
from encrypt import *
# Initialize Socket Instance
sock = socket.socket()
print ("Socket created successfully.")

# Defining port and host
port = 8800
host = 'localhost'

# binding to the host and port
sock.bind((host, port))

# Accepts up to 10 connections
sock.listen(10)
print('Socket is listening...')

while True:
    # Establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    data = con.recv(1024)
    print(data.decode())
    # Read File in binary
    # aes()
    # des()

    key_rc4 = b"super strong key" # Changeable from 5 to 256
    new_key_rc4 = SHA256.new(key_rc4+nonce).digest()
    con.send(new_key_rc4)
    rc4(new_key_rc4)
    
    file = open("enc.jpg","rb")
    data = file.read()
    # Keep sending data to the client
    while(data):
        con.send(data)
        data = file.read()
    
    print('File has been transferred successfully.')

    con.close()
    break

    