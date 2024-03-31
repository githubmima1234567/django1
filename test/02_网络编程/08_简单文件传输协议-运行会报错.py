from socket import *
import struct
#从键盘获取要下载的文件名称
#客户端发送请求下载数据
#服务答应请求返回数据
#保存

def main():
    #0. 获取要下载的文件名字:
    filename = input("请输入要下载的文件名称：")
    #1.创建socket
    udpsocket = socket(AF_INET,SOCK_DGRAM)
    sendData = struct.pack("!H8sb5sb",1,filename.encode("utf-8"),0,"octet".encode("utf-8"),0)
    #2. 发送下载文件的请求
    udpsocket.sendto(sendData,("192.168.10.9",69))

    file = open(filename,'w')
    num = 0
    flag = True #表示能够下载数据，即不擅长，如果是false那么就删除
    while True:
        #3. 接收服务发送回来的应答数据
        recvInfo = udpsocket.recvfrom(1024)
        recvData,recvAddr = recvInfo
        opNum = struct.unpack("!H", recvData[:2])#操作码
        print (opNum)
        packetNum = struct.unpack("!H", recvData[2:4])#块编号从1开始
        print(packetNum[0])

        if len(recvData)<516:
            break
        # if 如果服务器发送过来的是文件的内容的话:
        elif opNum[0] == 3:#因为opNum此时是一个元组(3,)，所以需要使用下标来提取某个数据
            num += 1#计算出这次应该接收到的文件的序号值，应该是上一次接收到的值的基础上+1
            # 如果一个下载的文件特别大，即接收到的数据包编号超过了2个字节的大小
            # 那么会从0继续开始，所以这里需要判断，如果超过了65535 那么就改为0
            if num == 65535:
                num = 0
            if num == packetNum[0]:
                file.write(recvData[4:])
                num = packetNum[0]
            #整理ACK包
            ackData = struct.pack("!H",4,packetNum[0])
            udpsocket.sendto(ackData,"192.168.10.9",69)
            # udpsocket.close()
        elif opNum[0] == 5:
            print ("sorry,没有文件")
            flag = False
        
    if flag == True:
        file.close()

    else:
        os.unlink(filename)#如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除





if __name__ == "__main__":
    main()