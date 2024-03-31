#coding=utf-8
from socket import *
from threading import Thread

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
    # 2.绑定ip和端口
    serverSocket.bind(("", 8899))
    # 3.监听
    serverSocket.listen(5)
    try:
        while True:
            # 4.等待新客户端到来
            clientsocket, clientaddr = serverSocket._sock.accept()
            t1 = Thread(target=user,args=(clientsocket,clientaddr))
            t1.start()
            # clientsocket.close()
    finally:
        serverSocket.close()

if __name__ == "__main__":
    main()