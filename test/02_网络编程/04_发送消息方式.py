from socket import *

def main():
        udpsocket = socket(AF_INET, SOCK_DGRAM)
        addrdata = input("请输入ip地址：")
        port =int( input("请输入端口："))
        senddata =input("请输入发送消息：")
        udpsocket.sendto(senddata.encode("gb2312"),(addrdata,port))


if __name__ == "__main__":
   main()
