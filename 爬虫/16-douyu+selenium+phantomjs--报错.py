import time
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

class douyu(unittest.TestCase):
    #初始化方法
    def setUp(self):
        self.num =0
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\18824\Documents\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        # self.driver.find_element(By.CLASS_NAME,'Header-menu-link')
        # time.sleep(2)
        # self.driver.save_screenshot('douyu.png')
        while True:
        # while self.num<=61:
            html = self.driver.page_source.encode('utf-8')
            soup = bs(self.driver.page_source,"lxml")

            with open("aa.txt",'wb') as f:
                f.write(html)
            names = soup.findAll("h3",{"class":"DyListCover-intro"})
            numbers = soup.findAll("span",{"class":"DyListCover-hot"})

            for name,number in zip(names,numbers):
                print("房间名："+name.get_text().strip()+",观众人数："+number.get_text().strip())
                self.num +=1
            #如果在页面源码里找到“下一页”为隐藏的标签，就退出循环
            print(self.driver.page_source.find("dy-Pagination-item-custom"))
            if self.driver.page_source.find("dy-Pagination-item-custom") !=-1:
                break
            #一直点击下一页
            # self.driver.find_element_by_css_selector('.dy-Pagination-next.xh-highlight').click()

            # self.driver.implicitly_wait(10)
            # self.driver.find_element(By.CLASS_NAME,'ListFooter-btn-input').send_keys(self.num)

            self.driver.find_element(By.XPATH, '//div[@class=" dy-Pagination-next"]/span').click()
            time.sleep(1)
    def tearDown(self):
        print("当前网站直播人数：",self.num)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()