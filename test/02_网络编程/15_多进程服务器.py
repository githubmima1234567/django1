#coding=utf-8
from socket import *
from multiprocessing import *

def user(clientsocket,clientaddr):
    while True:
        # 6.客户端接收信息
        recvData = clientsocket.recv(1024)
        if len(recvData) > 0:
            print("%s：%s" % (str(clientaddr[0]), recvData))
        else:
            print("%s 客户端已关闭" % clientaddr[0])
            break
    clientsocket.close()
def main():
    # 1.创建socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 2.绑定ip和端口
    serverSocket.bind(("", 8898))
    # 3.监听
    serverSocket.listen(5)
    try:
        while True:

        # 4.等待新客户端到来
            clientsocket, clientaddr = serverSocket.accept()

            p1 = Process(target=user,args=(clientsocket,clientaddr))
            p1.start()
            clientsocket.close()
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()