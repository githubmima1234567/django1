#coding=utf-8
from socket import *
import codecs

# 1.创建socket
serverSocket = socket(AF_INET,SOCK_STREAM)
# 2.绑定ip和端口
serverSocket.bind(("",8898))
# 3.监听
serverSocket.listen(5)
while True:
	# 4.等待新客户端到来
	clientsocket,clientaddr = serverSocket.accept()
	# 5.信息长度为空，则关闭客户端，否则打印输出
	try:
		while True:
			# 6.客户端接收信息
			recvData = clientsocket.recv(1024)
			if len(recvData)>0:
				print("%s：%s"%(str(clientaddr[0]),recvData))
			else:
				print("%s 客户端已关闭"%clientaddr[0])
				breakS
	finally:
		clientsocket.close()

serverSocket.close()