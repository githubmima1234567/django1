#coding=utf-8
from lxml import etree
from urllib import request,parse
from lxml import html
# import xml.etree.ElementTree as ET
#贴吧id
# //div[@class="threadlist_lz clearfix"]/div/a[@class="j_th_tit"]/@href
#图片地址
# //img[@class="BDE_Image"]/@src


def loadPage(url):
    """
    作用：根据url发送请求，返回服务响应信息
    url：需要爬取的url地址
    """
    # headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    # print(url)
    ua_header = 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'
    user_agent = {'User-Agent': ua_header}
    request1 = request.Request(url,headers=user_agent)
    # html = request.urlopen(request1).read().decode('utf-8')
    html = request.urlopen(request1).read()
    # print(html.encode('utf-8'))
    with open('tiebatupian.txt','wb') as f:
        f.write(html)
    with open('tiebatupian.txt', 'rb') as f:
        html1 = f.read().decode('utf-8')
        # print(html1)
    content = etree.HTML(html1)
    link_list = content.xpath('//a[@class="j_th_tit "]/@href')
    for link in link_list:
        fulllink = "https://tieba.baidu.com" + link
        # print(fulllink)
        loadImage(fulllink)

def loadImage(fulllink):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    request1 = request.Request(fulllink, headers=headers)
    response = request.urlopen(request1)
    html = response.read()
    # with open('tiebatupianurl.txt','wb') as f:
    #     f.write(html)
    # print(html)
    # with open('tiebatupianurl.txt', 'rb') as f:
    #     html1 = f.read().decode('utf-8')
    # print(html1)
    content = etree.HTML(html)
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # print(link_list)
    for link in link_list:
        print(link)
        writeImage(link)


def writeImage(link):
    """
    将图片存到本地
    link:图片链接
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    request1 = request.Request(link, headers=headers)
    image = request.urlopen(request1).read()
    filename = link[-10:]+'.jpg'
    with open(filename,'wb') as f:
        f.write(image)

def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn = str((page-1)*50)
        fullurl = url+"&pn="+pn
        loadPage(fullurl)

# https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=200
if __name__ =="__main__":
    kw = input("请输入关键字：")
    key = parse.urlencode({"kw":kw})
    beginPage =input("请输入起始页：")
    endPage = input("请输入终止页：")
    url = "https://tieba.baidu.com/f?"
    full_url = url +key
    loadPage(full_url)
