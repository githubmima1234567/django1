# -*- coding:utf-8 -*-
import json
import logging
import os
import random
import re
import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from tuling_dama import base64_api
from seleniumwire import request
import requests
from io import BytesIO
from lxml.html.formfill import _select
from urllib import parse
# from selenium import webdriver.requests
from config.ip_chaxun import select_ip, updata_ip
from config.sql_log import save_log, add_log
import uuid
import urllib3
import base64
from selenium.webdriver.common.by import By
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
path = os.path.dirname(os.path.abspath(__file__))
yanzhengma = path + '/yanzhengma/'


class Moban():
    def __init__(self):
        self.session = requests.session()
        # self.session.verify = False
        # self.session.keep_alive = False
        self.session.timeout = (5, 10)

        # self.driver = webdriver.Chrome()
    def get_imgcode(self,guid):
        url = f'https://www.crtc-jmfws.com:8003/Authentication/GenerateCheckCode/{guid}'
        response = requests.get(url)
        with open('img.jpg', 'wb') as f:
           f.write(response.content)
        img_path = 'img.jpg'
        res = base64_api(uname='amtdata', pwd='ll931126', img=img_path, typeid=1)
        return res

    def _login(self, username, password, factorycode, client_id):
        try:
            guid = uuid.uuid4()
            code = self.get_imgcode(guid)
            # print(code)
            username_b64 = base64.b64encode(username.encode('utf-8')).decode('utf-8')
            password_b64 = base64.b64encode(password.encode('utf-8')).decode('utf-8')
            headers = {

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',

            }
            data = {
                'ClientType': 'Web',
                'ProviderNo':f'{username_b64}' ,
                'Password': f'{password_b64}',
                'IdentityFlag': f'{guid}',
                'IdentityCode': f'{code}',
            }
            # print(data)

            url = 'https://www.crtc-jmfws.com:8003/Authentication/Login'
            res = self.session.post(url,headers=headers, data=data).json()
            # print(res)

            if res.get("UserName") == username:
                logging.info('登录成功')
                self.token = res['Token']
                # print('登录成功')
                return True
            if res.get("Msg") == "验证码不正确!":
                logging.info('验证码不正确')
                return 401
            elif res.get("Msg") == '连续登陆错误次数1次，超过10次后暂时无法登陆!':
                logging.info('密码错误')
                return 401
            elif res.get('Msg') == '供应商不存在！':
                logging.info('供应商不存在')
                return 401
            elif res.get('Msg') == '验证码已过期！':
                logging.info('验证码已过期！')
                return 401
            else:
                logging.info('登录失败')
                return False
        except Exception as e:
            logging.info("意外失败：{}".format(e))
            return False


if __name__ == '__main__':
    # Moban().login('2004591','123456','2004591','KA230220000101',"moban_name")
    # Moban().login('15957','1595','2004591','KA230220000101')
    Moban()._login('000003','20110721')

    # pass
"""
132061,132061,123456	
700429,700429,700429


INSERT INTO cass_db_gyb.dbo.new_gongyingbao_order_body
(serial_number, operation, bu, bu_name, commodity_id, commodity_bar_code, commodity_name, box_qty, order_qty, ruku_qty, affirm_qty, affirm_price, produced_date, daoqi_date, no_tax_price, commodity_spc, sell_unit, commodity_gongenng, baozhuang_qty, order_status, chandi, order_id, supplier_id, download_time, retailer_id)
VALUES('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');


"""

