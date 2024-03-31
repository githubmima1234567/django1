#coding:utf-8
import socket
import re
import sys
#需要在配置文件中配置文件名和模块
from multiprocessing import Process
HTML_ROOT_DIR = "./html"

class Server_Http(object):
    def __init__(self,Aplication):
        # 创建服务socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = Aplication

    def start(self):
        while True:
            # 接收新客户端的socket
            client_socket, client_addres = self.server_socket.accept()
            print("%s:%s 用户已连接" % client_addres)
            client_process = Process(target=self.handle_client, args=(client_socket,))
            client_process.start()
            client_socket.close()
    def start_response(self,status,headers):
        """status = "200 OK", response_headers = [("Content-Type",'text/plain')]"""
        response_headers = "HTTP/1.1 "+status+"\r\n"
        for header in headers:
            response_headers += "%s:%s\r\n"%header
            self.response_headers = response_headers
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
        # GET / HTTP/1.1
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)
        environ = {
            "PATH_INFO":file_name,
            "METHOD":method
        }
        response_boby = self.app(environ,self.start_response)
        response = self.response_headers + "\r\n" + response_boby
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
    if len(sys.argv) < 2:
        sys.exit("python MyWebFremWork.py Module:app")
    module_name,app_name = sys.argv[1].split(":")
    #module_name = MyWebFrameWork,app_name = app
    m = __import__(module_name)
    app = getattr(m,app_name)
    serversocket = Server_Http(app)
    serversocket.bind(8000)
    serversocket.listen(12)
    serversocket.start()

if __name__ == "__main__":
    main()



