#coding:utf-8
import socket
import re

from multiprocessing import Process

HTML_ROOT_DIR = "./html"

class Server_Http(object):
    def __init__(self):
        # 创建服务socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        while True:
            # 接收新客户端的socket
            client_socket, client_addres = self.server_socket.accept()
            print("%s:%s 用户已连接" % client_addres)
            client_process = Process(target=self.handle_client, args=(client_socket,))
            client_process.start()
            client_socket.close()
    def handle_client(self,client_socket):
        """处理客户信息并响应"""
        # 接收客户端的信息
        request_data = client_socket.recv(1024)
        print(request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)
        request_start_line = request_lines[0]
        # 解析客户发送的数据
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        if "/" == file_name:
            file_name = "/index.html"
        try:
            # 打开文件
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: My server\r\n"
            response_boby = "the file is not found"
        else:
            contentdata = file.read()
            file.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: My server\r\n"
            response_boby = contentdata.decode("utf-8")
        response = response_start_line + response_header + "\r\n" + response_boby
        print(response)
        # 发送响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端socket
        client_socket.close()
    def bind(self,port):
        # 对服务socket进行绑定
        self.server_socket.bind(("", port))
    def listen(self,num):
        # 对服务socket进行监听
        self.server_socket.listen(num)


def main():
    serversocket = Server_Http()
    serversocket.bind(8000)
    serversocket.listen(12)
    serversocket.start()

if __name__ == "__main__":
    main()



