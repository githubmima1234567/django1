import urllib.request
import  random
import urllib.parse

ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

user_agent = random.choice(ua_list)
print(user_agent)
# ua_headers = {'User-agent':ua_list1}

url = "https://www.baidu.com/s?"

request = urllib.request.Request(url)

request.add_header("User-Agent",user_agent)
# get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他的必须小写
# print(request.get_header("User-agent"))

#编码
wd = {'wd':'传智播客'}
print(urllib.parse.urlencode(wd))
#解码
wd1 = '%e4%bc%a0%e6%99%ba%e6%92%ad%e5%ae%a2'
print(urllib.parse.unquote(wd1))