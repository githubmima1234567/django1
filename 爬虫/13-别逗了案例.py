#coding=utf-8
import urllib
from urllib import request
from lxml import etree

class BiedouleSpider(object):
    def __init__(self):
        self.page = 1
        self.switch = True
    def loadPage(self):
        print("正在下载数据")
        url = "https://www.biedoul.com/wenzi/"+str(self.page)+"/"
        print(url)
        headers = {"User-Agent":'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0'}
        request1 =urllib.request.Request(url,headers=headers)
        response= request.urlopen(request1)
        html =  response.read().decode('utf-8')
        html1 = html.lower()
        # print(html)
        # with open('111.txt','a') as f:
        #     f.write(html)
        self.dealPage(html1)

    def dealPage(self,html1):
        print("****************")
        html = etree.HTML(html1)
        node_list = html.xpath('//dl[contains(@id,"xh_")]')
        # print(node_list)
        for node in node_list:
            title =node.xpath('./span/dd/a/strong/text()')
            # < DD > < p >
            content = node.xpath('./dd/p/text()')
            print(title)
            print(content)

    def writePage(self,html):
        print("正在写入数据")
        with open("duanzi.txt",'a') as f:
            f.write(html)

    def starWork(self):
        while self.switch:
            self.loadPage()
            command = input("如果继续爬，请按enter键（退出请输入quit)")
            if command == "quit":
                self.switch=False
            self.page +=1
        print("谢谢使用！")

if __name__=="__main__":
    biedoule = BiedouleSpider()
    biedoule.loadPage()
    biedoule.starWork()


