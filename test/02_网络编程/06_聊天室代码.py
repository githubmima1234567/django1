from socket import *
def test():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(("",7788))#绑定接收方的端口
    while True:
        recvData = udpsocket.recvfrom(1024)#接收最大消息的
        content,addr = recvData
        print("内容是：%s"%str(content.decode("gb2312"))+"ip:%s"%str(addr))
    udpsocket.close

test()



