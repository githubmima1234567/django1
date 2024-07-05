import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from lxml import etree

class yitixi(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def testyitixi(self):
        self.driver.implicitly_wait(3)
        url = 'https://e.etc-parts.com/#/login'
        self.driver.get(url)
        # 最大化浏览器窗口
        self.driver.maximize_window()
        # driver.set_window_size(1280, 720)  # 自定义窗口大小：
        self.driver.find_element(By.NAME,"loginName").send_keys("17606600836")
        self.driver.find_element(By.NAME, "password").send_keys("HongKong717")

        self.driver.find_element(By.CLASS_NAME,'el-button').click()


        time.sleep(3)
        # 关闭广告
        self.driver.find_element(By.CLASS_NAME,'el-dialog__headerbtn').click()
        #进入到首页
        #点击关键子搜索
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class='search-engine-box']/ul[@class='search-type']/li[5]").click()
        time.sleep(1)
        #搜索输入框输入
        self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys("奔驰")
        self.driver.find_element(By.XPATH, "//div[@class='el-input-group__append']/div").click()
        time.sleep(1)

        # 跳转到新窗口,切换到商品列表窗口
        handle = self.driver.window_handles # 获取句柄，得到的是一个列表
        # print(handle)
        # print(self.driver.title)
        self.driver._switch_to.window(handle[-1])  # 切换至最新句柄
        # print("************************************************************")
        # print(self.driver.title)
        # print("************************************************************")
        time.sleep(2)
        self.driver.save_screenshot('./商品列表.png')

        #点击ETC号
        for n in range(1, 79):
            if n == 1:

                print("在第一页")

                for i in range(1,2):#21
                    data = {}
                    self.driver.find_element(By.XPATH,"//div[@class='list-body']/div[%d]/div/div/div/div/div/div/span[@class='e-text-link']" %i).click()
                    #切换到最新商品详情窗口
                    handle = self.driver.window_handles
                    self.driver._switch_to.window(handle[-1])
                    time.sleep(2)
                    # print(self.driver.title)

                    # self.driver.save_screenshot('./商品详情.png')
                    # time.sleep(2)
                    html = self.driver.page_source

                    soup = BeautifulSoup(html,'lxml')
                    price = soup.select('.price-current')[0].get_text()
                    data["价格"]=price
                    #价格
                    print(soup.select('.price-current')[0].get_text())
                    #ETC号
                    ETC = soup.select('.item-row span')[1].get_text()
                    data["ETC"]=ETC
                    print(soup.select('.item-row span')[1].get_text())
                    #名称
                    name = soup.select('.item-row span')[3].get_text()
                    data["名称"] = name
                    print(soup.select('.item-row span')[3].get_text())
                    list = soup.select('div[class="cell el-tooltip"]')
                    print("适用车型:")
                    car_list = []
                    for item in list:
                        car_list.append(item.get_text())
                    print(car_list)
                    data["适用车型"]=car_list

                    #点击对应OE号
                    btn_next = self.driver.find_element(By.ID, 'tab-exchangeOE')
                    self.driver.execute_script("arguments[0].click();", btn_next)
                    html = self.driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    self.driver.save_screenshot('./商品详情2.png')
                    list_OE = soup.select("div[class='cell']")
                    print("对应OE号:")
                    OE_list = []
                    for item in list_OE:
                        OE_list.append(item.get_text())
                        # print(item.get_text())
                    print(OE_list)
                    data["对应OE号"] = OE_list
                    #点击对应品牌件号
                    tab_item = self.driver.find_element(By.ID, 'tab-exchangePartBrand')
                    self.driver.execute_script("arguments[0].click();", tab_item)
                    html = self.driver.page_source
                    soup = BeautifulSoup(html, 'lxml')
                    self.driver.save_screenshot('./商品详情3.png')
                    list_pinpai = soup.select("tr[class='el-table__row']")
                    print("对应品牌件号:")
                    jianhao_list = []
                    for item in list_pinpai:
                        jianhao_list.append(item.get_text())
                    print(jianhao_list)
                    data["对应品牌件号"] = jianhao_list
                    with open('./data.txt','a+',encoding = 'UTF-8') as f:
                       f.write(str(data)+'\n')

                    handle = self.driver.window_handles
                    # print(handle)
                    self.driver.switch_to.window(handle[-1])
                    # print(self.driver.title)
                    time.sleep(2)
                    self.driver.close()
                    time.sleep(2)
                    handle = self.driver.window_handles
                    # print(handle)
                    self.driver._switch_to.window(handle[-1])
                    time.sleep(1)
                    # print("*****************************88")
                    # print(self.driver.title)
            else:

                data = {}
                n += 1
                print("准备进入第%d页" % n)
                btn_next = self.driver.find_element(By.CLASS_NAME, 'btn-next')
                if btn_next.is_enabled():
                    self.driver.execute_script("arguments[0].click();", btn_next)
                    time.sleep(2)
                    for i in range(1, 21):
                        time.sleep(2)
                        # self.driver.find_element(By.XPATH,
                        #                          "//div[@class='list-body']/div[%d]/div/div/div/div/div/div/span[@class='e-text-link']" % i).click()
                        self.driver.find_element(By.XPATH,
                                                 "//div[@class='list-body']/div[%d]/div/div/div/div/div/div/span[@class='e-text-link']" % i).click()

                        # 切换到最新商品详情窗口
                        handle = self.driver.window_handles
                        self.driver._switch_to.window(handle[-1])
                        time.sleep(2)
                        # print(self.driver.title)

                        self.driver.save_screenshot('./商品详情.png')
                        # time.sleep(2)
                        html = self.driver.page_source

                        soup = BeautifulSoup(html, 'lxml')
                        # print("____________________________________________-")
                        # 价格

                        price = soup.select('.price-current')[0].get_text()
                        print(price)
                        data["价格"] = price
                        # # ETC号

                        ETC = soup.select('.item-row span')[1].get_text()
                        print(ETC)
                        data["ETC"] = ETC
                        # #名称

                        name = soup.select('.item-row span')[3].get_text()
                        print(name)
                        data["名称"] = name
                        # print("____________________________________________")
                        list = soup.select('div[class="cell el-tooltip"]')
                        print("使用车型")
                        car_list = []
                        for item in list:
                            car_list.append(item.get_text())
                        print(car_list)
                        data["适用车型"] = car_list
                        # 点击对应OE号
                        time.sleep(1)
                        btn_next = self.driver.find_element(By.ID, 'tab-exchangeOE')
                        self.driver.execute_script("arguments[0].click();", btn_next)
                        html = self.driver.page_source
                        soup = BeautifulSoup(html, 'lxml')
                        self.driver.save_screenshot('./商品详情2.png')
                        list_OE = soup.select(('div[class="cell"]'))
                        print("对应OE号:")
                        OE_list = []
                        for item in list_OE:
                            OE_list.append(item.get_text())
                            # print(item.get_text())
                        print(OE_list)
                        data["对应OE号"] = OE_list

                        # 点击对应品牌件号
                        self.driver.execute_script('window.scrollTo(800,0);')
                        tab_item = self.driver.find_element(By.ID, 'tab-exchangePartBrand')
                        self.driver.execute_script("arguments[0].click();", tab_item)
                        html = self.driver.page_source
                        soup = BeautifulSoup(html, 'lxml')
                        self.driver.save_screenshot('./商品详情3.png')
                        list_pinpai = soup.select("tr[class='el-table__row']")
                        print("对应品牌件号:")
                        jianhao_list = []
                        for item in list_pinpai:
                            jianhao_list.append(item.get_text())
                        print(jianhao_list)
                        data["对应品牌件号"] = jianhao_list
                        with open('./data.txt','a+',encoding = 'UTF-8') as f:
                           f.write(str(data)+'\n')
                        handle = self.driver.window_handles
                        # print(handle)
                        self.driver.switch_to.window(handle[-1])
                        # print(self.driver.title)
                        time.sleep(2)
                        self.driver.close()
                        time.sleep(2)
                        handle = self.driver.window_handles
                        # print(handle)
                        self.driver._switch_to.window(handle[-1])
                        time.sleep(2)
                        # print("*****************************88")
                        # print(self.driver.title)
                        n+=1
                else:
                    print("这是最后一页，下一页按钮不可点击")

    def tearDown(self):
        #关闭所有窗口
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()


# try:
#     driver.find_element_by_xpath('//*[@id="IBMAccessibleItemComponents-next" and not(@aria-disabled)]').click()
# except NoSuchElementException:
#     break

# try:
#         next = driver.find_element_by_xpath('//*[@id="IBMAccessibleItemComponents-next"]')
#         if (next.is_enabled()):
#             next.click()
#         else:
#             break
#     except NoSuchElementException:
#         break

#进入到79页
        # self.driver.find_element(By.XPATH,"//ul[@class='el-pager']/li[8]").click()
        # time.sleep(2)
        # btn_next = self.driver.find_element(By.CLASS_NAME, 'btn-next')
        # print("按钮是否可用："+str(btn_next.is_enabled()))