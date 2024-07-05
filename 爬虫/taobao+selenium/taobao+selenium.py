from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import  TimeoutException
import time
from selenium.webdriver import Chrome
from pyquery import PyQuery as pq
driver = Chrome()
driver.implicitly_wait(10)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => false
            })
          """
    })
url = "https://login.taobao.com/member/login.jhtml"
wait = WebDriverWait(driver, 10)
def login_taobao():
    '''
    正常的浏览器的window.navigator.webdriver为false
    selenium自动打开的浏览器的window.navigator.webdriver为true
    淘宝反爬会识别window.navigator.webdriver为true的有滑块验证码，
    所以需要设置window.navigator.webdriver为false
    '''
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, 'fm-login-id'))).send_keys('18824620119')
    driver.find_element(By.ID, 'fm-login-password').send_keys('18824620119@')
    # time.sleep(300)
    driver.find_element(By.CSS_SELECTOR, '.fm-button.fm-submit.password-login').click()

def search_taobao():
    WebDriverWait(driver,15).until(EC.visibility_of_element_located(
        (By.ID,'q'))).send_keys('儿童自行车')
    driver.find_element(By.CLASS_NAME,'btn-search').click()
def get_products():
    """提取商品列表页数据并保存"""
    html = driver.page_source
    doc = pq(html)
    items = doc('.Card--doubleCardWrapper--L2XFE73').items()
    for item in items:
        product = {'url': item.attr('href'),
                   'price': item.find('.Price--priceInt--ZlsSi_M').text(),
                   'realsales': item.find('.Price--realSales--FhTZc7U-cnt').text(),
                   'title': item.find('.Title--title--jCOPvpf').text(),
                   'shop': item.find('.ShopInfo--TextAndPic--yH0AZfx').text(),
                   'location': item.find('.Price--procity--_7Vt3mX').text()}
        print(product)
        saveDate(product)

def saveDate(data):
    with open("taobao.txt", 'a+', encoding='UTF-8') as f:
        f.write(str(data) + '\n')


def index_page(max_num):
    """
    max_num:最大页码数
    """
    n=1
    while True:
        time.sleep(5)
        print(' 正在爬取第%d页' %n)
        get_products()
        try:

            btn_next = wait.until(EC.visibility_of_element_located((By.XPATH, '//button/span[contains(text(),"下一页")]')))
            driver.execute_script("arguments[0].click();", btn_next)
            n += 1
            if n>max_num:
                print("爬完了！")
                break
        except TimeoutException:
            print("index_page TimeoutException")
def main():
    login_taobao()
    search_taobao()
    index_page(84)

if __name__ == "__main__":

    main()
