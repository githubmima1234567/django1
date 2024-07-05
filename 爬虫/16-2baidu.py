import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(executable_path=r'C:\Users\18824\Documents\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    def testBaidu(self):
        url = 'https://www.baidu.com/'
        self.driver.get(url)
        self.driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('美女')
        # self.driver.find_element(By.ID,'su').click()
        self.driver.find_element(By.CLASS_NAME, 's_btn').click() #class="bg s_btn"全部放会报错

        time.sleep(1)
        self.driver.save_screenshot('baidu.png')
        print(self.driver.title)
        print(self.driver.get_cookies())
        print(self.driver.page_source)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()