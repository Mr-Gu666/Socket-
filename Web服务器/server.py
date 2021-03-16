from socket import *
from multiprocessing import *
from threading import Thread
import os
from _thread import *
from time import sleep

useThread = False
useProcess = True
sockeListenNum = 5

def serverAccpet_Process(connsocket):
    print("子进程的pid为{} 父进程的pid为{}".format(os.getpid(),os.getppid()))
    try:
        while True:
            sentence = connsocket.recv(1024)
            filename = sentence.split()[1]
            fp = open(filename[1:])
            output_data = fp.read()
            header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(output_data))
            connsocket.send(header.encode())
            '''
            for out in output_data:
                connsocket.send(out.encode())
            '''
            connsocket.send(output_data.encode())
    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        connsocket.send(header.encode())
    finally:
        fp.close()
        connsocket.close()    
    return


def serverAccpet_Thread(connsocket):
    try:
        while True:
            sentence = connsocket.recv(1024)
            filename = sentence.split()[1]
            fp = open(filename[1:])
            output_data = fp.read()
            header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(output_data))
            connsocket.send(header.encode())
            '''
            for out in output_data:
                connsocket.send(out.encode())
            '''
            connsocket.send(output_data.encode())
    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        connsocket.send(header.encode())
    finally:
        fp.close()
        connsocket.close()
    return

if __name__=="__main__":
    # server port
    serverPort = 12000
    # create socket
    serverSocket = socket(AF_INET,SOCK_STREAM)
    # socket bind port
    serverSocket.bind(('',serverPort))
    serverSocket.listen(sockeListenNum)
    print("server waiting for connect")
    while True:
        try:
            if useProcess:
                # get connect socket and client address
                connSocket, addr = serverSocket.accept()
                print("接收到请求，创建子进程")
                # create child process
                child_process = Process(target=serverAccpet_Process,args=(connSocket,))
                child_process.start()
                # sleep(1.0)
            elif useThread:
                connSocket, addr = serverSocket.accept()
                print("接收到请求，创建线程")
                # '''
                child_thread = Thread(target=serverAccpet_Thread,args=(connSocket,))
                child_thread.start()
                # '''
                # start_new_thread(serverAccpet_Thread,(connSocket,))
            else:
                connsocket, addr = serverSocket.accept()
                print("接收到请求，创建连接")
                try:
                    while True:
                        sentence = connsocket.recv(1024)
                        filename = sentence.split()[1]
                        fp = open(filename[1:])
                        output_data = fp.read()
                        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(output_data))
                        connsocket.send(header.encode())
                        '''
                        for out in output_data:
                            connsocket.send(out.encode())
                        '''
                        connsocket.send(output_data.encode())
                except IOError:
                    header = ' HTTP/1.1 404 Not Found'
                    connsocket.send(header.encode())
                finally:
                    fp.close()
                    connsocket.close()
        except:
            continue
    serverSocket.close()