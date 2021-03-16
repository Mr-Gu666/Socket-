# UDPPingerServer.py 
# We will need the following module to generate randomized lost packets import random 
from socket import * 
import random
from sys import meta_path

# Create a UDP socket  
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
serverSocket.bind(('', 12000)) 

while True:
    try:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(2048)
        print("receive message")
        message = message.decode()
        message = '127.0.0.1:12000 ' + message
        if rand < 4:
            continue
        serverSocket.sendto(message.encode(), address)
    except:
        print("server error happened")
serverSocket.close()