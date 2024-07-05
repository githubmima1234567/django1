#coding=utf-8
from urllib import request
import urllib
import ssl
# 表示忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

proxyswitch = True

httpproxy_handler = request.ProxyHandler({"http":"117.57.117.20:8089"})

nullproxy_handler = request.ProxyHandler({})

if proxyswitch:
    opener = request.build_opener(httpproxy_handler)
else:
    opener = request.build_opener(nullproxy_handler)

#设置opener为全局变量
request.install_opener(opener)

request = request.Request("http://www.baidu.com/")
response = urllib.request.urlopen(request,context = context)
print(response.read().decode("utf-8"))