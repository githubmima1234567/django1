from socket import *

udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(('',7788))
recvData = udpsocket.recvfrom(1024)
content,addr = recvData
print("内容是：%s"%str((content.decode("gb2312")))+"地址是：%s"%str(addr))
udpsocket.close()
