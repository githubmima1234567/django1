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
        next_page = self.driver.find_element(By.CLASS_NAME,'DyListCover-intro')


        next_page.click()
        time.sleep(1)

        self.driver.save_screenshot("douyu1.png")
        #
        # self.driver.find_element_by_class_name("dy-Pagination-item").click()
        # self.driver.implicitly_wait(5)
        # self.driver.save_screenshot("douyu2.png")
        # self.driver.find_element_by_css_selector('.dy-Pagination-next.xh-highlight').click()

    def tearDown(self):       # print("当前网站直播人数：",self.num)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()