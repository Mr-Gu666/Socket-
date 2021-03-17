from socket import *
from time import sleep, time

if __name__=="__main__":
    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverPort = 12000
    serverSocket.bind(('',serverPort))
    while True:
        print("server")
        try:
            message, addr = serverSocket.recvfrom(1024)
            print(message.decode())
            server_message = "Server alive"
            serverSocket.sendto(server_message.encode(),addr)
            serverSocket.settimeout(1)
        except timeout:
            print("client message lost")
        sleep(1)