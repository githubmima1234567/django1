import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread

"""
 建立driver的花销较大，尽量创建一次，多次使用， 并发的话不能共用一个driver，必须重新创建
使用技巧总结：创建多个线程，个数最好和cpu个数相同，
多线程原理：
1、利用同一个浏览器打开多页面、相当于打开一个线程、提高爬虫速度
2、同时打开多个浏览器，相关于打开多个线程。多线程提高爬虫速度
3、对于一个账号不能同时登录的网站不可用多线程开多个浏览器，除非有多个账号
"""
def process():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    url = 'https://e.etc-parts.com/#/login'
    driver.get(url)
    # 最大化浏览器窗口
    driver.maximize_window()
    # driver.set_window_size(1280, 720)  # 自定义窗口大小：
    driver.find_element(By.NAME,"loginName").send_keys("17606600836")
    driver.find_element(By.NAME, "password").send_keys("HongKong717")

    driver.find_element(By.CLASS_NAME,'el-button').click()
    # 关闭广告
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, 'el-dialog__headerbtn'))).click()
    #进入到首页
    #点击关键子搜索
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,  "//div[@class='search-engine-box']/ul[@class='search-type']/li[5]"))).click()
    # keys = ["奔驰", "宝马", "奥迪"]
    # for item in keys:
    #搜索输入框输入

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CLASS_NAME, 'el-input__inner'))).send_keys("奔驰")

    # self.driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys(item)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, "//div[@class='el-input-group__append']/div"))).click()
    time.sleep(1)
    # 跳转到新窗口,切换到商品列表窗口
    handle = driver.window_handles # 获取句柄，得到的是一个列表
    # print(handle)
    # print(self.driver.title)
    driver._switch_to.window(handle[-1])  # 切换至最新句柄
    print(driver.title)
    time.sleep(3)
    # self.driver.save_screenshot('./商品列表.png')
    n = 1
    while True:
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ETC_num = soup.find_all("span", {"class": "e-text-link"})
        # time.sleep(3)
        #获取一页的ETC总数量
        num = len(ETC_num)
        print("一页的ETC总数量:" + str(num))
        print("****************************第%d页******************************************************" %n)
        try:
            for i in range(1,num+1):
                print(i)
                data = {}
                # 点击ETC号
                ETC_btn =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='list-body']/div[%d]/div/div/div/div/div/div/span[@class='e-text-link']" %i)))
                driver.execute_script("arguments[0].click();", ETC_btn)
                #切换到最新商品详情窗口
                handle = driver.window_handles
                driver._switch_to.window(handle[-1])
                time.sleep(2)
                # self.driver.save_screenshot('./商品详情.png')
                html = driver.page_source
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
                # print(list)
                car_list = []
                for item in list:
                    car_list.append(item.get_text())
                print(car_list)

                data["适用车型"] = car_list
                #点击对应OE号
                btn_next = driver.find_element(By.ID, 'tab-exchangeOE')
                driver.execute_script("arguments[0].click();", btn_next)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                driver.save_screenshot('./商品详情2.png')
                list_OE = soup.select("div[class='cell']")
                # print(list_OE)
                print("对应OE号:")
                OE_list = []
                for item in list_OE:
                    OE_list.append(item.get_text())

                OE_list = OE_list[3:-1]
                print(OE_list)
                data["对应OE号"] = OE_list
                #点击对应品牌件号
                tab_item = driver.find_element(By.ID, 'tab-exchangePartBrand')
                driver.execute_script("arguments[0].click();", tab_item)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                driver.save_screenshot('./商品详情3.png')
                list_pinpai = soup.select("tr[class='el-table__row']")
                print("对应品牌件号:")
                # print(list_pinpai)
                jianhao_list = []
                for item in list_pinpai:
                    jianhao_list.append(item.get_text())
                print(jianhao_list)

                data["对应品牌件号"] = jianhao_list
                if len(jianhao_list)&len(OE_list)&len(car_list) !=0:
                    with open('./data.txt','a+',encoding = 'UTF-8') as f:
                       f.write(str(data)+'\n')
                #关闭商品详情页回到商品列表页
                handle = driver.window_handles
                driver.switch_to.window(handle[-1])
                self.driver.close()
                handle = driver.window_handles
                # print(handle)
                driver._switch_to.window(handle[-1])
                # time.sleep(1)
                # print(self.driver.title)
            #点击下一页按钮
            btn_next = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'btn-next')))
            # btn_next = self.driver.find_element(By.CLASS_NAME, 'btn-next')
            if btn_next.is_enabled():
                driver.execute_script("arguments[0].click();", btn_next)
                time.sleep(3)
                html = driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                ETC_num = soup.find_all("span", {"class": "e-text-link"})
                # time.sleep(3)
                # 获取一页的ETC总数量
                num = len(ETC_num)
                n += 1
            else:
                print("这是最后一页，下一页按钮不可点击")
                break
                ac = driver.find_element_by_xpath('element')
                ActionChains(driver).move_to_element(ac).perform()
        except IndexError:
            # 防止IndexError
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            ETC = soup.find_all("span", {"class": "e-text-link"})
            # time.sleep(3)
            # 获取一页的ETC总数量
            num = len(ETC)
    print("爬虫结束！")
    driver.quit()

def main():
        # 开启4个进程，传入爬取的页码范围
        thead_list = []
        t1 = Thread(target=process,)
        t1.start()
        t2 = Thread(target=process,)
        t2.start()
        t3 = Thread(target=process,)
        t3.start()
        t4 = Thread(target=process,)
        t4.start()
        thead_list.append(t1)
        thead_list.append(t2)
        thead_list.append(t3)
        thead_list.append(t4)
        for t in thead_list:
            t.join()


if __name__ == "__main__":
    main()


