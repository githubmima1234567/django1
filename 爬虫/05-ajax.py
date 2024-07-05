from urllib import parse,request

def movieSpider():

    #从fiddler中获取url
    url = "https://movie.douban.com/j/chart/top_list?"
    # https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20
    formdata  = {
    "type":"11",
    "interval_id":"100:90",
    "action":"",
    "start":"20",
    "limit":"20"
    }
    #对post数据进行转码
    data = parse.urlencode(formdata).encode('utf-8')
    hearder= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
    request1 = request.Request(url,data=data,headers=hearder)
    response= request.urlopen(request1)
    html = response.read()
    loadPage(html)
def loadPage(html):
    with open("movie.json","wb") as f:
        f.write(html)

if __name__ =="__main__":
    movieSpider()