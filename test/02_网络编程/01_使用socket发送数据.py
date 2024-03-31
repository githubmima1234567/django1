from socket import *
udpsocket = socket(AF_INET,SOCK_DGRAM)
udpsocket.sendto(b"haha",("192.168.10.9",8080))#python2中不需要加b
