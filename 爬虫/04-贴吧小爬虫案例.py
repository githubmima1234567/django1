from urllib import request,parse
from lxml import etree
def loadPage(fullurl,filename):
    """
    作用：根据url发送请求，获取服务器响应，
    url:需要爬取的url地址
    """
    ua_header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
    user_agent = {'User-Agent':ua_header}
    # request1 = request.add_header('User-Agent',ua_header)
    request1 = request.Request(fullurl, headers=user_agent)
    response = request.urlopen(request1)
    print("正在下载:"+filename)
    html = response.read()

    print("下载已完成！")
    return html

def writePage(html,filename):
    """
    作用：将响应的html内容写入到本地
    html:服务器响应的内容
    """
    with open(filename,'wb') as f :
        f.write(html)
        print("*************************************")

def tiebaSpider(url,beginPage,endPage):
    """
    作用：贴吧爬虫调度器，负责组合处理每个页面的url
    url:贴吧url的前部分
    beginPage:起始页
    endPage:结束页
    """
    for page in range(beginPage,endPage+1):
        pn = str((page-1)*50)
        filename = "第"+str(page)+"页.html"
        fullurl = url +"&pn="+pn
        # print(fullurl)
        html= loadPage(fullurl,filename)
        print("正在保存："+filename)
        writePage(html,filename)
    print("已全部保存完成！")

if __name__ =="__main__":
    kw = input("请输入关键字：")
    key = parse.urlencode({"kw": kw})
    beginPage =int( input("请输入起始页："))
    endPage =int(input("请输入结束页："))
    url = "https://tieba.baidu.com/f?"
    full_url = url + key
    tiebaSpider(full_url,beginPage,endPage)


