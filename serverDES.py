import socket
from datetime import datetime
from encrypt import *

# Initialize Socket 
sock = socket.socket()
print ("Socket created successfully.")

# Define host and port
port = 8700
host = 'localhost'

# bind host and port
sock.bind((host, port))

# Accept Connection
sock.listen(10)
print('Socket is listening...')

while True:
    # Establish Connection
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    data = con.recv(1024)
    print(data.decode())
    
    start = datetime.now() 
    # key_rc4 = b"super strong key" # Changeable from 5 to 256
    # new_key_rc4 = SHA256.new(key_rc4+nonce).digest() 
    # con.send(new_key_rc4)
    # aes() 
    des()
    # rc4(new_key_rc4)
    
    file = open("enc.jpg","rb")
    data = file.read()
    # Keep sending data to the client
    while(data):
        con.send(data)
        data = file.read()
    
    print('File has been transferred successfully.')
    print('Duration: {}'.format(datetime.now() - start))

    con.close()
    break