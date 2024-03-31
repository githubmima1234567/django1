#coding:utf-8
import socket

from multiprocessing import Process

HTML_ROOT_DIR = ""
def handle(client_socket):
    """处理客户信息并响应"""
    # 接收客户端的信息
    client_data = client_socket.recv(1024)
    print(client_data)

    # 构造响应数据
    response_start_line = "http/1.1 200 OK\r\n"
    response_header = "server: my server\r\n"
    response_boby = "I miss you!"
    response = response_start_line+response_header+"\r\n"+response_boby
    client_socket.send(bytes(response,"utf-8"))
    client_socket.close()
if __name__ == "__main__":
    # 创建服务socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 对服务socket进行绑定
    server_socket.bind(("",8000))
    # 对服务socket进行监听
    server_socket.listen(12)
    while True:
        # 接收新客户端的socket
        client_socket,client_addres = server_socket.accept()
        print("%s:%s 用户已连接"%client_addres)
        client_process = Process(target=handle,args=(client_socket,))
        client_process.start()
        client_socket.close()

