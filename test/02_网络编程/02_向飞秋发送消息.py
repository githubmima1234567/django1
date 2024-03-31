from multiprocessing import Process
from socket import *

def test():
    while True:
        udpsocket = socket(AF_INET, SOCK_DGRAM)
        udpsocket.sendto(b"1:1238605487:mengxiang:YAN:32:hello",("192.168.10.9",2425))


for i in range(2):
    p = Process(target=test)
    p.start()

