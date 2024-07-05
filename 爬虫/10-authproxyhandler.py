#coding=utf-8
from urllib import request
import os

#把用户和密码存到环境变量中
os.environ.update({"proxyuser":"111"})
os.environ.update({"proxypasswd":"111"})

#从环境变量中获取用户和密码
proxyuser = os.environ.get()
proxypasswd = os.environ.get()

authproxyhandler = request.ProxyHandler({"http":proxyuser+":"+proxypasswd+"@114.215.104.49:16816"})

opener = request.build_opener(authproxyhandler)

request = request.Request("http://www.baidu.com/")

response = opener.open(request)