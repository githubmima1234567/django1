import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
class Douban(unittest.TestCase):
    """
       # 如果iframe有name或id的话，直接使用switch_to_frame("name值")
        # 或switch_to_frame("id值")。
        # driver.switch_to_frame('x-URS-iframe')  # 需先跳转到iframe框架
        # username = driver.find_element_by_name('email')
        # username.clear()
        #
        # 如果iframe没有name或id的话，则可以通过下面的方式定位：
        # # 先定位到iframe
        # elementi = driver.find_element_by_class_name('APP-editor-iframe')
        # # 再将定位对象传给switch_to_frame()方法
        # driver.switch_to_frame(elementi)

    """
    def setUp(self):
        self.driver = webdriver.Chrome()
    def testDouban(self):
        url = 'https://www.douban.com/'
        self.driver.get(url)
        time.sleep(2)
        # self.driver.save_screenshot('douban.png')
        # 切换iframe
        login_frame = self.driver.find_element(By.XPATH,'//div/div/div/iframe')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element(By.CLASS_NAME,'account-tab-account').click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'account-form-input').send_keys('18824620119')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'password').send_keys('18824620119@')
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'btn-account ').click()
        time.sleep(9)
        self.driver.save_screenshot('baidu.png')
        with open('douban.html','w',encoding = 'UTF-8') as f:
            f.write(self.driver.page_source)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()



