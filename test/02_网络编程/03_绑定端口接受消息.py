from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(('',7788))
recvData = udpsocket.recvfrom(1024)
print(recvData)
udpsocket.close()
