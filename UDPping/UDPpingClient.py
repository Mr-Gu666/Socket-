from socket import *
import time

if __name__=="__main__":
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    min_rtt = 2
    max_rtt = -1
    ave_rrt = 0
    timeout_num = 0
    for i in range(1,11):
        try:
            send_time = time.time()*1000
            message = "Ping Sequence: {} Time: {}"
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            clientSocket.sendto(message.format(i,local_time).encode(),(serverName,serverPort))
            clientSocket.settimeout(1)
            recv_message,serverAddr = clientSocket.recvfrom(1024)
            recv_time = time.time()*1000
            cur_rtt = recv_time - send_time
            print(recv_message.decode(),"RTT: {:.2f}ms".format(cur_rtt))
            if min_rtt>cur_rtt:
                min_rtt = cur_rtt
            if max_rtt<cur_rtt:
                max_rtt = cur_rtt
            ave_rrt = (ave_rrt+cur_rtt)/(i-timeout_num)
            print("MIN_RTT: {:.2f}ms  MAX_RTT: {:.2f}ms  Average_RTT: {:.2f}ms".format(min_rtt,max_rtt,ave_rrt))
        except timeout:
            print("Request time out")
            timeout_num += 1
    clientSocket.close()
    print("丢包率: {:.2f}% ".format((timeout_num/10)*100))