import json
import jsonpath
from urllib import request

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
request1 = request.Request(url,headers=headers)
response = request.urlopen(request1)
#取出json里面的内容，返回格式是字符串
html = response.read()
# print(html.decode("utf-8"))
#把json形式的字符串转换成python形式的unicode字符串(utf-8)
unicodestr = json.loads(html)
print(unicodestr)
# python形式的列表
city_list = jsonpath.jsonpath(unicodestr,"$..name")
for item in city_list:
    print(item)
#dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
#禁用ascii编码格式，返回的Unicode字符串，方便使用
array = json.dumps(city_list,ensure_ascii=False).encode("utf-8")
with open("lagoucity.json",'wb') as f:
    f.write(array)