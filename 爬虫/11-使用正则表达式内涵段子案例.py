#coding=utf-8
import urllib
from urllib import request
import re

class BiedouleSpider(object):
    def __init__(self):
        self.page = 1
        self.switch = True
    def loadPage(self):
        print("正在下载数据")
        url = "https://www.biedoul.com/wenzi/"+str(self.page)+"/"
        # print(url)
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
        request1 =urllib.request.Request(url,headers=headers)
        response= request.urlopen(request1)
        html =  response.read().decode('utf-8')
        self.dealPage(html)

    def dealPage(self,html):
        pattern = re.compile('<DL\\sclass="xhlist".*?>(.*?)</DL>',re.S)
        # print(pattern)
        content_list = re.findall(pattern,html)
        # print(content_list)
        for content in content_list:
            content = content.replace("&rdquo;","").replace("<br />","")
            self.writePage(content)

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


