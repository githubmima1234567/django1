from socket import *
from multiprocessing import Process
def fun(clientsocket):
    # 接收客户端信息
    recvData = clientsocket.recv()
    print(recvData)
    clientsocket.close()


# 解析客户端信息

# 解析客户端信息请求方法

# 解析客户端信息路径
    try:
        #打开文件
        path = "./html/index.html"
        f = open(path,)
        contentdata = f.read()
        # 发信息给客户端
        clientsocket.send(contentdata)
        f.close()

    except IOError:
        print("404,notfind")
def main():
    # 创建socket
    serversocket = socket(AF_INET,SOCK_STREAM)
    # 绑定ip和端口
    serversocket.bind("",8899)
    # 监听
    serversocket.listen(5)
    try:
        while True:
            # 接收客户端的socket
            clientsocket,clientadd = serversocket.accept()
            #创建新进程给新客户端
            p = Process(target=fun,args=clientsocket)
            p.start()
            clientsocket.close()
    except:
        serversocket.close()

if __name__ == "__main__":
    main()


