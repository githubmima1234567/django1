import socket, sys
dest = ('<broadcast>', 2425) 
# 创建udp套接字 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1) 
# 以⼴播的形式发送数据到本⽹络的所有电脑中 
s.sendto("Hi".encode("utf-8"), dest) 
print ("等待对⽅回复（按ctrl+c退出）" )
while True: 
	(buf, address) = s.recvfrom(2048) 
	print ("Received from %s: %s" % (address, buf))