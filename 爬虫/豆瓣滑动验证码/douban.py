import requests
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2


def identify_gap(bg, tp, out):
    '''
    bg: 背景图片
    tp: 缺口图片
    out:输出图片
    '''
    # 读取背景图片和缺口图片，以灰度模式加载图片
    bg_img = cv2.imread(bg,0)  # 背景图片
    tp_img = cv2.imread(tp,0)  # 缺口图片
    # 转换为灰度图像
    gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    # 创建二值化掩码，只保留指定范围内的灰度
    mask = cv2.inRange(gray, 100, 200)
    # 找到轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 创建一个副本用于绘制
    img_with_contours = bg_img.copy()
    # 绘制轮廓
    for contour in contours:
        # 用绿色线条绘制
        cv2.drawContours(img_with_contours, [contour], -1, (0, 255, 0), 1)
        # 找到最大的轮廓，并计算其外接矩形
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        # 获得外接矩形
        x, y, w, h = cv2.boundingRect(max_contour)
        # 用绿色矩形标记
        cv2.rectangle(img_with_contours, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # # 识别图片边缘
    # bg_edge = cv2.Canny(bg_img, 100, 200)
    # tp_edge = cv2.Canny(tp_img, 100, 200)
    #
    # # 转换图片格式,背景图片灰度处理
    # bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    # tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    #
    # # 模板匹配TM_CCOEFF_NORMED 归一化相关匹配法，缺口匹配
    # res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    # lo = cv2.minMaxLoc(res)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    #
    # # 绘制方框
    # th, tw = tp_pic.shape[:2]
    # tl = max_loc  # 左上角点的坐标
    # br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    # cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    # cv2.imwrite(out, bg_img)  # 保存在本地
    #
    # # 返回缺口的X坐标
    # return lo[3][0]
def get_tracks(distance, rate=0.6, t=0.2, v=0):
    """
    将distance分割成小段的距离
    :param distance: 总距离
    :param rate: 加速减速的临界比例
    :param a1: 加速度
    :param a2: 减速度
    :param t: 单位时间
    :param t: 初始速度
    :return: 小段的距离集合
    """
    tracks = []
    # 加速减速的临界值
    mid = rate * distance
    # 当前位移
    s = 0
    # 循环
    while s < distance:
        # 初始速度
        v0 = v
        if s < mid:
            a = 20
        else:
            a = -3
        # 计算当前t时间段走的距离
        s0 = v0 * t + 0.5 * a * t * t
        # 计算当前速度
        v = v0 + a * t
        # 四舍五入距离，因为像素没有小数
        tracks.append(round(s0))
        # 计算当前距离
        s += s0

    return tracks


def slide(driver):
    """滑动验证码"""
    # 切换iframe
    driver.switch_to_frame("tcaptcha_iframe_dy")
    #获取验证码背景图url,隐式等待
    backgroup_img_url = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.ID, 'slideBg'))).value_of_css_property(
        "background-image").split('"')[1]
    # print(backgroup_img_url)
    backgroup_img = requests.get(backgroup_img_url).content
    with open('./backgroup_img.png', 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        f.write(backgroup_img)
    #获取碎片图片url
    slider_img_url = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='tc-opera']/div[7]"))).value_of_css_property(
        "background-image").split('"')[1]
    # print(slider_img_url)
    slider_img = requests.get(slider_img_url).content
    with open('./slider_img.png', 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        f.write(slider_img)
    file = "./img.png"

    x = identify_gap('./backgroup_img.png', './slider_img.png', file)
    print(x)
    # # img = imread("./backgroup_img.png",0)
    # # 以灰度图的形式读取图像
    # lena = cv2.imread("./backgroup_img.png",0)
    # slider_pic = cv2.imread('./slider_img.png', 0)
    #
    # #展示图片
    # cv2.imshow("image", slider_pic)
    # cv2.imshow("image", lena)
    # # 注意：在调用显示图像的API后，要调用cv.waitKey()
    # # 给图像绘制留下时间，否则窗口会出现无响应情况，并且图像无法显示出来。
    # cv2.waitKey(0)
    # # 获取缺口图数组的形状 -->缺口图的宽和高
    # width, height = slider_pic.shape[::-1]
    # print(width)
    # print(height)
    # # 保存图像
    # cv2.imwrite('./huiduimge.png', lena)
    # # 图像模糊原理为卷积，根据模糊核的size执行平均操作，常用于图像滤波效果，减少噪点。
    # img_blur = cv2.blur(lena, (8, 8))
    # ret, img_bin = cv2.threshold(img_blur, 180, 255, cv2.THRESH_BINARY)
    # cv2.imshow('img_bin', img_bin)


    block = driver.find_element_by_xpath('//*[@id="tcOperation"]/div[6]') # *匹配任何元素节点
    # 找到刷新
    reload = driver.find_element_by_xpath('//*[@id="reload"]/img')
    while True:
        # 摁下滑块

        ActionChains(driver).click_and_hold(block).perform()
        # 移动
        ActionChains(driver).move_by_offset(187, 0).perform()  #怎么来180？
        # 获取位移
        tracks = get_tracks(30) #30怎么来？
        # 循环
        for track in tracks:
            # 移动
            ActionChains(driver).move_by_offset(track, 0).perform()
        # 释放
        ActionChains(driver).release().perform()
        # 停一下
        time.sleep(2)
        # 判断刷新按钮是否存在，存在则循环识别验证码

        #判断失效，重新设置
        if driver.find_element_by_xpath('//*[@id="reload"]/img').is_enabled():
            print("失败...再来一次...")
            # 单击刷新按钮刷新
            reload.click()
            driver.switch_to_frame("tcaptcha_iframe_dy")
            block = driver.find_element_by_xpath('//*[@id="tcOperation"]/div[6]')
            # 停一下
            time.sleep(2)
        else:
            break

def main():
    """主程序"""
    url = "https://www.douban.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    #切换iframe
    login_frame = driver.find_element_by_xpath('//div/div/div/iframe')
    driver.switch_to.frame(login_frame)
    # 点击密码登录按钮
    driver.find_element_by_class_name('account-tab-account').click()
    #输入登录账号和密码
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("18824620119")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("18824620119@")
    #点击登录豆瓣按钮
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    # 停一下，等待滑块验证码出现
    time.sleep(2)

    # 滑动验证码
    slide(driver)

    print("成功")
    driver.quit()


if __name__ == '__main__':
    main()


# def get_element_slide_distance(self, slider_ele, background_ele, correct=0):模块图像识别
# 图片url地址：
# target_link = driver.find_element(By.CLASS_NAME, "yidun_bg-img").get_attribute('src')
#https://turing.captcha.qcloud.com/cap_union_new_getcapbysig?img_index=1&image=0279050000696f180000000bbb8669432c50&sess=s0TPwGwcYzNVxTWpPTQW2P7VZa4WTg-fluYQC7_hG7TTyoIDrPijoAxdvb4l2d7OyZ3jtDteOB_Wm-ONtkUt61wo7A_-IsspFyir7KvbIKIzJo56O27rV1hHwbKlEb7-E7B3RNPgItw_wDGqWpjV53ju5M45N6qArPhAogHKbbWAqCSpzgbkulqV2i4yOMlRyx_r-BWlvaWLU7joyF7IAHUAex9DJFKCCXgR5WCXFc6zmTrmcymqRgtP8lks-ZGy51fDUYw9wA5jJOKLIPOBTq6X_gDuR6AwhSoFNrAg2lvhojfvosxVyXH6nz3ppSEwvvdnF-HPlINu5S9e2qKXEP4_VMt83ethQJM-h2B_R0EEorLmZhkw5MDA



# var url=$(obj).css('background-image');
# url = url.split("(")[1].split(")")[0];
# 刷新一次