#coding=utf-8
from socket import *
#给服务端创建套接字
service_socket = socket(AF_INET,SOCK_STREAM)
#绑定ip和端口
service_socket.bind(("",8889))
#监听
service_socket.listen(5)
#接受客户端消息
newsocket,clientaddr = service_socket._accept()
print(clientaddr)
#客户端创建套接字
recvData = newsocket.recv(1024)
print("接收的数据为：%s:%s"%(str(clientaddr),str(recvData)))
newsocket.send("Thank you!")
newsocket.close()
service_socket.close()
