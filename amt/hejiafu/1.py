# from datetime import time
import time
import logging
import json
import datetime
from datetime import date, timedelta
from bs4 import BeautifulSoup
# from datetime import date, timedelta
# 时间转换
import logging
# html = b'<form id="formsubmit" name="formsubmit" action="https://wdc.watsonsvip.com.cn/supplyreport/account/tokenLogin" method="post"> <input type="hidden" name="sign" value="e4e40a8e8ed3beb1c1b4aba11d1a35f42669c89415390d5485a1352df2a4b541"> <input type="hidden" name="timestamp" value="1722575175092"> <input type="hidden" name="token" value="328930803570674329811846f">  <input type="hidden" name="refer" value="supplierportal"> <input type="hidden" name="outter" value="true"></form><script>document.forms[\'formsubmit\'].submit();</script>'
#
# soup = BeautifulSoup(html, 'html.parser')
#
# sign_input = soup.find('input', {'name': 'sign'})
# sign_value = sign_input['value']
#
# timestamp_input = soup.find('input', {'name': 'timestamp'})
# timestamp_value = timestamp_input['value']
#
# token_input = soup.find('input', {'name': 'token'})
# token_value = token_input['value']
#
# print("sign 值:", sign_value)
# print("timestamp 值:", timestamp_value)
# print("token 值:", token_value)
import base64
#
# str = [c_id,mdfd,wlms,ykmx,spbm,ddlx,cglx,o_dhr,o_dhrq,jglx,shck,
# shr,r_dhr,r_dhrq,ht,lxcz,qxrq,dhcz,dhdh,lxdh,lxr,pszxck,yyzt,
# yysj,dyzt,lrr,lrsj,yydh,qrzt,checker,shsj,shdz,bz,factorycode,
# uuid,retailer_id,download_time,]
#
import urllib.parse

# encoded_string ='eyJVbmlxdWVLZXkiOiJFbmpveVNDTTQw5YWx566h5bqT5a2YIiwiTWV0aG9kTmFtZSI6IkdldE9yZGVyQnlSZWNTdGF0dXNMaXN0IiwiVXNlck5vIjoiMDAwMDAzIiwiQ2xpZW50VGltZSI6IjIwMjQtMDgtMDlUMDM6Mjc6NTUuODE1WiIsIk9iamVjdERhdGEiOnsic1Byb3ZpZGVyTm8iOiIwMDAwMDMiLCJzU3RvcmVJZCI6IiIsIklkIjoiIiwiZFN0IjoiMjAyNC0wNy0wOSIsImRFbiI6IjIwMjQtMDgtMDkiLCJzU0NNU3RhdHVzIjoiIiwic1R5cGUiOiIiLCJzQ29uTm8iOiIiLCJzU3RhdHVzIjoi5bCa5pyq5pS26LSnIiwic0V4dGVuZCI6IiIsIlRhZyI6IiIsIkN1cnJlbnRQYWdlIjoxLCJQYWdlU2l6ZSI6MTAwfSwiVGFnIjpudWxsLCJUb2tlbiI6ImhEK2NWUVBiQ2c1Nk1ra25vZ2tCMnZZc3ppV09aYmFTIn0='
# decoded_string = urllib.parse.unquote(encoded_string)
# print(decoded_string)

data ='eyJVbmlxdWVLZXkiOiJFbmpveVNDTTQw5YWx566h5bqT5a2YIiwiTWV0aG9kTmFtZSI6IkdldFJlY0JpbGxEZXRhaWwiLCJVc2VyTm8iOiIwMDAwMDMiLCJDbGllbnRUaW1lIjoiMjAyNC0wOC0wOVQwODoyNDo0OC4xNzVaIiwiT2JqZWN0RGF0YSI6eyJJZCI6IlBPMjQwNzMwMDEyMSJ9LCJUYWciOm51bGwsIlRva2VuIjoiaEQrY1ZRUGJDZzVtN2c0ak1WY05KaEtaVTErV1FTMVgifQ=='
decoded_data = base64.b64decode(data).decode('utf-8')
print(decoded_data)

# str = '[020401]'
#
# print(str[1:5])
# input_string = str.strip('[]')
# print(input_string[:4])
# import random
import base64
#
# re = {"ObjectData": [], "UniqueKey": 'null', }
# print(re["ObjectData"])
# {'ObjectData': None, 'UniqueKey': None, 'MethodName': None, 'SourceMethodName': None, 'Tag': None, 'UserState': None, 'Exception': {'HasException': True, 'ExceptionType': 0, 'Code': 'TokenExpired', 'Message': '身份验证失败!', 'StackTrace': None, 'LogErrorCode': None}, 'HasException': True}

# import re
#
# def convert_value(value):
#     sub_str = re.compile(',', re.IGNORECASE)  # 创建正则表达式对象，不区分大小写，全局查找
#     result = (str(value)).replace(',', '')  # 把 ',' 替换为空字符串
#     return int(result)
# convert_value()
# # from datetime import datetime
# # import pytz
# r = "^([0-1][0-9]|2[0-3]|[0-9])"


# now = datetime.now(pytz.utc)
# formatted_now = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
# print(formatted_now)
# data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRetList","UserNo":"000003","ClientTime":"2024-08-07T03:31:14.313Z","ObjectData":{"sProviderNo":"000003","sStoreId":"","dSt":"2024-07-07","dEn":"2024-08-07","Id":"","sPayStatus":"","sType":"","sTitle":"","Tag":""},"Tag":"null","Token":"hD+cVQPbCg7yr4zGPkrgD6DenI1e37TC"}
# data_str = json.dumps(data)
# encoded_data = base64.b64encode(data_str.encode()).decode()
# print(encoded_data)

# str = '?,?,?'
# new_str = str.replace('?', '%s')
# print(new_str)

# def generate_uuid():
#     uuid_template = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
#     uuid = ""
#     for char in uuid_template:
#         if char == 'x':
#             random_num = random.randint(0, 15)
#             uuid += format(random_num, 'x')
#         elif char == 'y':
#             random_num = random.randint(0, 15)
#             random_num = (3 & random_num) | 8
#             uuid += format(random_num, 'x')
#         else:
#             uuid += char
#     print(uuid)
#     return uuid
# generate_uuid()
# print(len([202431, '滴露', 'DETTOL', '2', 'Personal Care', '2003', 'Bath / Deo / Talc', '2', 'Hand Liquid Soap', 1055275101, '上海曼伦商贸有限公司', '100014865', '滴露健康抑菌洗手液滋润倍护500毫升', '6974352530413', 'N', 'N', '东区', 'HB-HN-SD', '河南', 9891, 'KS莴笋美团', 'Y', 9891, 'KS莴笋美团', 4039, 'HB淇滨万达广场', 1, 17.28, 19.53, 'SPT_1055275101_1', '20240805-19:43:40.579101', '鹤壁', 'rb', '1055275101']))
# cookies = [{'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': True, 'name': 'MatrixGateWay_SESSION_ID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '83C3AD87A28B1574B9AEFEBF1D41319F'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': True, 'name': 'Matrix_SESSION_ID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0d701fa4-3b77-4737-9fee-db5851e91c6a'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'uc_access_token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ac0e2494-a847-4b05-94df-cdcc8bb5561d'}, {'domain': '.watsonsvip.com.cn', 'httpOnly': False, 'name': 'token_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.6692248003029969'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'accId_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '41396166'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'token_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.09206991464700909'}, {'domain': '.watsonsvip.com.cn', 'httpOnly': False, 'name': 'accId_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '41396166'}, {'domain': '.watsonsvip.com.cn', 'expiry': 1722997587, 'httpOnly': True, 'name': 'UC_SSO_TOKEN', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '9104b2a5da6e5db968b2b3607f404fbc5d7bed20c40f0f51129237d2a76027c8-6c0623b6-7b41-45c0-a365-ddd723aa0512'}, {'domain': 'wdc.watsonsvip.com.cn', 'expiry': 1722912987, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '707c9fcc17229111873651024e2e8614ee830c862b55e11c711cd41f2835f2'}]
#
# cookie_pairs = [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
# print(cookie_pairs)

# def convert_cookies_to_expected_format(cookies):
#     cookie_pairs = [f"{cookie['name']}={cookie['value']}" for cookie in cookies]
#     cookies = '; '.join(cookie_pairs)
#     print(cookies)
#     # return f"Cookie: {'; '.join(cookie_pairs)}"
#
# cookies =[{'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': True, 'name': 'MatrixGateWay_SESSION_ID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '38F7882CEB527E53B7D784574C318F67'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': True, 'name': 'Matrix_SESSION_ID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '6d6c0d0e-67a6-4242-a2ef-64fee19323dd'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'uc_access_token', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'cc5b3303-a06e-49f2-abe7-aa8a277bc26f'}, {'domain': '.watsonsvip.com.cn', 'httpOnly': False, 'name': 'token_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.6462977218863513'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'accId_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '41396166'}, {'domain': 'wdc.watsonsvip.com.cn', 'httpOnly': False, 'name': 'token_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '0.6375353184658927'}, {'domain': '.watsonsvip.com.cn', 'httpOnly': False, 'name': 'accId_matrix', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '41396166'}, {'domain': '.watsonsvip.com.cn', 'expiry': 1723017897, 'httpOnly': True, 'name': 'UC_SSO_TOKEN', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '9104b2a5da6e5db968b2b3607f404fbc5d7bed20c40f0f51129237d2a76027c8-6c0623b6-7b41-45c0-a365-ddd723aa0512'}, {'domain': 'wdc.watsonsvip.com.cn', 'expiry': 1722933297, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '2f624a5c17229314976722807e56ca0602ef42110d82dad1a0f08c6bd9f075'}]
#
# convert_cookies_to_expected_format(cookies)
# 创建一个文件处理器
# file_handler = logging.FileHandler('./app.log')
# # 创建一个控制台处理器
# console_handler = logging.StreamHandler()

# 配置日志格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)

# # 获取根日志记录器
# logger = logging.getLogger()
# # 添加处理器
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
#
# # 设置日志级别
# logger.setLevel(logging.INFO)


# level=logging.INFO：设置日志级别为 INFO，这意味着只会记录 INFO 级别及以上（如 WARNING、ERROR、CRITICAL）的日志消息。
# filemode="a"：指定文件的打开模式为追加模式（"append"），新的日志消息会追加到已有文件的末尾。
# filename=rukudan_log+"{}.log".format(t)：设置日志文件的名称，其中 rukudan_log 可能是一个基础名称，{}.log.format(t) 表示使用变量 t 的值来进一步补充文件名。
# format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'：定义了日志消息的格式。%(asctime)s 表示记录日志的时间，%(filename)s 表示文件名，[line:%(lineno)d] 表示所在行号，%(levelname)s 表示日志级别，%(message)s 表示实际的日志消息。
#
# logger.info('This is an info message')
# logger.info('这是日志输出')

#
# timestamp = 1721649600000  #时间戳
# shiji_daohuo_dates = time.localtime(int(timestamp) / 1000)
# print(shiji_daohuo_dates)
# print(time.strftime("%Y-%m-%d %H:%M:%S", shiji_daohuo_dates))
# # cost_unit_pur = '7726'

# # 20231018
# # ["202430", "202429", "202428"]
# print(date.strftime(date.today() + timedelta(days=-1), '%Y%m%d'))
# a = [202430, '薇婷', 'VEET', '3', 'Skincare', '3002', 'Hand/Body/Depilatory', '7', 'Hair Remover', 1055275101, '上海曼伦商贸有限公司', '101375545', '薇婷净纯脱毛膏滋润型（干性肌肤适用）50ml', '6932740902150', 'Y', 'Y', '北区', 'BJ-XJ', '新疆', 3820, 'YL奎屯友好时尚', 'N', 3820, 'YL奎屯友好时尚', 3820, 'YL奎屯友好时尚', 2, 61.95, 70.0, 'SPT_1055275101_1', '20240801-21:19:53.207933', '奎屯', '1055275101', '1722518393207']
#
# print(len(a))
import datetime

import datetime

# def get_latest_week_of_year():
#     today = datetime.date.today()
#     start_of_year = datetime.date(today.year, 1, 1)
#     days_since_start = (today - start_of_year).days
#     week_number = int(days_since_start / 7)
#     return f"{today.year}{week_number:02}"
#
# print(get_latest_week_of_year())

# time.sleep(2)
# dropdown = self.driver.find_element(By.CLASS_NAME, "lego-container__menus-item-title")
#
# actions = ActionChains(self.driver)
# actions.move_to_element(dropdown).perform()
#
# option = self.driver.find_element(By.XPATH, '//*[@id="preview-framework"]/div/div[1]/div/div[2]/div/div[2]/div/div[1]')
#
# actions.move_to_element(option).perform()
# week =  self.driver.find_element(By.XPATH, '//*[@id="preview-framework"]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[1]')
#
# actions.move_to_element(week).perform()
# week.click()
