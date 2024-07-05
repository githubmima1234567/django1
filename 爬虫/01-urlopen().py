
import urllib.request

ua_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}
page = urllib.request.Request("https://www.baidu.com/",headers = ua_headers)

response = urllib.request.urlopen(page)

# print(response.read().decode('utf-8')) #返回网页信息
print (response.geturl())  #返回url
print (response.getcode())  #返回状态码
print (response.info())  #返回服务器响应的http报头信息
