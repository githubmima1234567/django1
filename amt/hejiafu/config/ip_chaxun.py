# -*- coding:utf-8 -*-
import logging
import requests
import sys
import os
p = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(p)


# 查询 ip
def select_ip():
    try:
        url = "http://101.132.157.102:6001/ip_chaxun"
        accounts = requests.request("get", url, timeout=30).json()
        if accounts['code'] == "200":
            return accounts['data']
        if accounts['code'] == "201":
            logging.info("意外失败 可能是没有钱了")
            return False
        else:
            logging.info("意外失败 可能是没有钱了")
            return False
    except Exception as e:
        logging.info("ip 查询账号失败：{}".format(e))
        return False


# 更新 ip
def updata_ip():
    try:
        url = "http://101.132.157.102:6001/ip_updata"
        accounts = requests.request("get", url, timeout=30).json()
        if accounts['code'] == 113:
            logging.info("没有添加白名单")
            return False
        if accounts['code'] == 201:
            logging.info("意外失败 可能是没有钱了")
            return False
        return accounts['data']
    except Exception as e:
        logging.info("ip更新失败：{}".format(e))
        return False


if __name__ == '__main__':
    """
       ip会没半个小时自动更新
       这个ip更新是手动更新
    """

    print(updata_ip())
    # print("qqqqqqqqq")
    print(select_ip())
