from socket import *
from time import *

if __name__=="__main__":
    serverName = 'localhost'
    serverPort = 12000
    clientSocket =socket(AF_INET,SOCK_DGRAM)
    while True:
        print("client")
        try:
            client_message = "client is alive"
            clientSocket.sendto(client_message.encode(),(serverName,serverPort))
            clientSocket.settimeout(1)
            message, addr = clientSocket.recvfrom(1024)
            print(message.decode())
        except timeout:
            print("server message lost")
        sleep(1)