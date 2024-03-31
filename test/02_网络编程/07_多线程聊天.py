from socket import *
from threading import Thread

#1、触发键盘，发送消息
#2、接收消息
#3、使用多线程实现发送接收消息同步

def sendInfo():
    while True:
        sendData = input("<<")
        udpsocket.sendto(sendData.encode("gb2312"),(sendIp,sendPort))
        #print(">>")

def recvInfo():
    while True:
        recvData = udpsocket.recvfrom(1024)
        ip =  recvData[1]
        print("%s:%s"%(str(ip[0]),str(recvData[0].decode("gb2312"))))
        print(">>",end="")

udpsocket = None
sendIp = ""
sendPort = 0

def main():
    global udpsocket
    global sendIp
    global sendPort
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    sendIp = input("请输入对方ip:")
    sendPort = int(input("请输入端口号："))
    ts = Thread(target=sendInfo)
    tr = Thread(target=recvInfo)
    ts.start()
    tr.start()
    ts.join()
    tr.join()

if __name__ == "__main__":
    main()

