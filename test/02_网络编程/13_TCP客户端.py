from socket import *
clientsocket = socket(AF_INET,SOCK_STREAM)
clientsocket.connect(("192.168.10.9",8989))
clientsocket.send("haha".encode("gb2312"))
recv = clientsocket.recv(1024)
print("recv:%s"%recv)
clientsocket.close()
