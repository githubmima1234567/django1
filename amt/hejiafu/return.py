# -*- coding:utf-8 -*-

import base64
import json
import logging
import os
import re
import time
import urllib
from urllib import parse

import requests
import xlrd
from lxml import etree
from datetime import date, timedelta
from datetime import datetime
import pytz

from config.sql_account_flask import account_infos
from config.sql_log import add_log
from config.sql_order import return_result
from login import Moban

path = os.path.dirname(os.path.abspath(__file__))

return_log = path + '/log/return/'
order_xls_name = path + '/order_xls/'


class tongyong_order(Moban):
    def moban_xiazai(self, username, password, factorycode, client_id):
        try:

            start_date = date.strftime(date.today() + timedelta(days=-60), '%Y-%m-%d')
            end_date = date.strftime(date.today() + timedelta(days=0), '%Y-%m-%d')

            headers = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        # 'Cookie': 'ASP.NET_SessionId=hii3mtpe4qbvuhhbmaditjye; .ASPXAUTH=0F7AEEFE3966E500BDD8927CBD36A7D6C2F85024DECDBD6303F9A894BAFDFD534850CC5C75D2E315E20C4017C2605825AD02A0D73031E44CD4007A7525D9DE22F62983A80B43CB3BDB6B9036327B94ABBAF8BB1A5B1BABF0E36F9437531FF837',
                        'Origin': 'https://www.crtc-jmfws.com:8003',
                        'Pragma': 'no-cache',
                        'Referer': 'https://www.crtc-jmfws.com:8003/index.html',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest',
                        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                    }
            now = datetime.now(pytz.utc)
            formatted_now = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            # print(formatted_now)

            HJF_return_note = []
            HJF_return_details_header = []
            HJF_return_details_body = []
            HJF_return_printheader = []
            HJF_return_printbody = []

            sPayStatus = ["尚未结算","已结算"]
            for item in sPayStatus:
                data = {"UniqueKey": "EnjoySCM40共管库存", "MethodName": "GetRetList", "UserNo": username,
                        "ClientTime":formatted_now,
                        "ObjectData": {"sProviderNo": factorycode, "sStoreId": "", "dSt": start_date, "dEn": end_date,
                                       "Id": "", "sPayStatus": item, "sType": "", "sTitle": "", "Tag": ""}, "Tag": "null",
                        "Token": self.token}
                print(data)
                data_str = json.dumps(data)
                encoded_data = base64.b64encode(data_str.encode()).decode()
                # print(encoded_data)
                url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
                response = requests.post(url, headers=headers,data=encoded_data).json()
                print(response)
                if response['ObjectData'] == []:
                    add_log(username, factorycode, client_id, "HJF", "退单",
                                "本次下载共0条", "成功")
                    print("本次下载共0条")
                    # return True
                else:
                    rowss = response['ObjectData']

                    if type(rowss) == dict:
                        rows = []
                        rows.append(rowss)
                    else:
                        rows = rowss

                    for row in rows:
                        return_note = []
                        # 序号
                        row_number = row.get('row_number')
                        return_note.append(row_number)
                        #订单号
                        c_id = row.get('c_id')
                        return_note.append(c_id)
                        # 退货机构
                        c_rec_store_id = row.get('c_rec_store_id')
                        tuihuojigou = c_rec_store_id.split('[')[1].split(']')[0]
                        return_note.append(tuihuojigou)
                        # 退货机构名称
                        c_rec_store_id = row.get('c_rec_store_id')
                        tuihuojigou_name = c_rec_store_id.split('[')[1].split(']')[1]
                        return_note.append(tuihuojigou_name)
                        #退货部门
                        c_adno = row.get('c_adno')
                        return_note.append(c_adno)
                        # 退货金额 c_at_pay和这个字段一样，不知道是哪个
                        c_at_in = row.get('c_at_in')
                        return_note.append(c_at_in)
                        # 采购类型
                        c_type = row.get('c_type')
                        return_note.append(c_type)
                        #确认状态
                        status = row.get('c_scm_status')
                        if status is None:
                            c_scm_status = '尚未确认'
                        else:
                            c_scm_status = status
                        return_note.append(c_scm_status)
                        # 打印状态
                        dayin_status = row.get('c_print_status')
                        if dayin_status =='':
                            dayin = '尚未打印'
                        else:
                            dayin = '已打印'
                        return_note.append(dayin)
                        #审核人
                        c_rec_au_userno = row.get('c_rec_au_userno')
                        return_note.append(c_rec_au_userno)
                        #审核时间
                        c_rec_au_dt = row.get('c_rec_au_dt')
                        return_note.append(c_rec_au_dt)
                        # 录入人
                        c_mk_usernoo = row.get('c_mk_usernoo')
                        return_note.append(c_mk_usernoo)
                        #录入时间
                        c_mk_dtr = row.get('c_mk_dto')
                        return_note.append(c_mk_dtr)
                        #备注
                        c_note = row.get('c_note')
                        return_note.append(c_note)
                        print(return_note)
                        HJF_return_note.append(return_note)

                        #     #供应商编码
                        #     #uuid
                        #     #client_id
                        #     #下载时间
                        #
                        headers = {
                            'Accept': 'application/json, text/javascript, */*; q=0.01',
                            'Accept-Language': 'zh-CN,zh;q=0.9',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            # 'Cookie': 'ASP.NET_SessionId=hii3mtpe4qbvuhhbmaditjye; .ASPXAUTH=DC4320524798F07A339E10146E1A9C6ABF46BFC1FD9CEE816DE0BC3CE3BBADA543338184E8625A6F832499FF596189257344F0868275B18FE968B5EA056E2720E5C82A6A263E0CA1C39EA0F26C40BF43AC2C294A284A82666903C932D2C5C60F',
                            'Origin': 'https://www.crtc-jmfws.com:8003',
                            'Pragma': 'no-cache',
                            'Referer': 'https://www.crtc-jmfws.com:8003/index.html',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                            'X-Requested-With': 'XMLHttpRequest',
                            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                        }
                        data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRetDetail","UserNo":"000003","ClientTime":formatted_now,"ObjectData":{"Id":c_id},"Tag":"null","Token":self.token}

                        data_str = json.dumps(data)
                        encoded_data = base64.b64encode(data_str.encode()).decode()
                        url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
                        response = self.session.post(url, headers=headers, data=encoded_data).json()
                        # print(response)

                        # 退单详情单头
                        item = response['ObjectData']['ret_header'][0]
                        # print(data)
                        # if type(data) == dict:
                        #     rows = []
                        #     rows.append(data)
                        # else:
                        #     rows = data
                        # for item in rows:
                        # 退单详情单头
                        return_details_hearder = []
                        #订单号
                        # c_id = item.get('c_id')
                        return_details_hearder.append(c_id)
                        #退货机构
                        # c_rec_store_id = item.get('c_rec_store_id')
                        return_details_hearder.append(tuihuojigou)
                        # 退货机构名称
                        return_details_hearder.append(tuihuojigou_name)
                        # 合同
                        c_con_no = item.get('c_con_no')
                        return_details_hearder.append(c_con_no)
                        # 退货金额
                        c_at_pay = item.get('c_at_pay')
                        return_details_hearder.append(c_at_pay)
                        # 采购方式
                        c_type = item.get('c_type')
                        return_details_hearder.append(c_type)
                        # 物流方式
                        c_delivery_type = item.get('c_delivery_type')
                        return_details_hearder.append(c_delivery_type)
                        # 审核日期
                        c_rec_au_dt = item.get('c_rec_au_dt')
                        return_details_hearder.append(c_rec_au_dt)
                        # 退货原因
                        c_reason_i = item.get('c_reason_i')
                        return_details_hearder.append(c_reason_i)
                        #供应商名称--打印头需要
                        c_partner_name = item.get('c_partner_name')


                        # 退单打印头

                        return_print_header = []
                        # 供应商编号
                        return_print_header.append(factorycode)
                        # 退货单号
                        return_print_header.append(c_id)
                        # 供应商名称
                        return_print_header.append(c_partner_name)
                        # 分店名称编码
                        return_print_header.append(tuihuojigou)
                        # 分店名称
                        return_print_header.append(tuihuojigou_name)
                        # 结算方式c_type
                        return_print_header.append(c_type)
                        # 合计金额
                        return_print_header.append(c_at_in)
                        # 合同编号
                        return_print_header.append(c_con_no)
                        # 退货日期
                        return_print_header.append(c_mk_dtr)
                        # 备注
                        return_print_header.append(c_note)
                        # 供应商编码
                        # return_print_header.append(factorycode)
                        # uuid
                        # client_id
                        # 下载时间
                        HJF_return_printheader.append(return_print_header)



                        #供应商编码
                        # return_details_hearder.append(factorycode)
                        HJF_return_details_header.append(return_details_hearder)
                        #uuid
                        #client_id
                        #下载时间

                        #退单详情单身
                        ret_line = response['ObjectData']['ret_line']
                        if type(ret_line) == dict:
                            rows = []
                            rows.append(ret_line)
                        else:
                            rows = ret_line
                        for item in rows:
                            return_details_body = []
                            # 序号
                            c_orig_sort = item.get('c_orig_sort')
                            return_details_body.append(c_orig_sort)
                            # 主条码
                            c_barcode = item.get('c_barcode')
                            return_details_body.append(c_barcode)
                            # 商品名称
                            c_gname = item.get('c_gname')
                            return_details_body.append(c_gname)
                            # 规格
                            c_model = item.get('c_model')
                            return_details_body.append(c_model)
                            # 单位
                            c_unit = item.get('c_unit')
                            return_details_body.append(c_unit)
                            # 申请数量
                            c_order_n = item.get('c_order_n')
                            return_details_body.append(c_order_n)
                            # 申请赠品数量
                            c_order_free_n = item.get('c_order_free_n')
                            return_details_body.append(c_order_free_n)
                            # 实退数量
                            c_rec_n = item.get('c_rec_n')
                            return_details_body.append(c_rec_n)
                            # 实退赠品数量
                            c_rec_free_n = item.get('c_rec_free_n')
                            return_details_body.append(c_rec_free_n)
                            # 结算价
                            c_pt_fall = item.get('c_pt_fall')
                            return_details_body.append(c_pt_fall)
                            # 退货金额
                            c_at_pay = item.get('c_at_pay')
                            return_details_body.append(c_at_pay)
                            # 订单号
                            return_details_body.append(c_id)
                            # 退货机构
                            return_details_body.append(tuihuojigou)
                            # 供应商编码
                            # return_details_body.append(factorycode)

                            # 商品编码--打印身需要
                            c_gcode = item.get('c_gcode')
                            # 商品条形码--打印身需要
                            c_barcode_ig = item.get('c_barcode_ig')
                            # 税率--打印身需要
                            c_tax_rate = item.get('c_tax_rate')
                            HJF_return_details_body.append(return_details_body)
                            # uuid
                            # client_id
                            # 下载时间

                            # 退单打印身
                            return_print_body = []
                            # 商品编码
                            return_print_body.append(c_gcode)
                            # 商品条码
                            return_print_body.append(c_barcode_ig)
                            # 商品名称
                            return_print_body.append(c_gname)
                            # 规格
                            return_print_body.append(c_model)
                            # 单位
                            return_print_body.append(c_unit)
                            # 税率
                            return_print_body.append(c_tax_rate)
                            # 退货数量
                            return_print_body.append(c_rec_n)
                            # 进价（含税）
                            return_print_body.append(c_pt_fall)
                            # 退货金额（含税）
                            return_print_body.append(c_at_pay)
                            # 供应商编号
                            return_print_body.append(factorycode)
                            # 退货单号
                            return_print_body.append(c_id)
                            # 分店名称编码
                            return_print_body.append(tuihuojigou)
                            # uuid
                            # client_id
                            # 下载时间
                            HJF_return_printbody.append(return_print_body)




            logging.info("合家福军民 退单长度：{}".format(len(HJF_return_note)))

            result = return_result(HJF_return_note,HJF_return_details_header,HJF_return_details_body,HJF_return_printheader,HJF_return_printbody,factorycode,client_id)

            logging.info("下载条数：{}".format(len(HJF_return_note)))
            if not result:
                add_log(username, factorycode, client_id, "HJF", "退单", "入库意外失败", "错误")

            add_log(username, factorycode, client_id, "HJF", "退单",
                    "本次下载共{}条".format(len(HJF_return_note)), "成功")
            return True
        except Exception as e:
            logging.info("进货入库 下载失败：{}".format(e))
            return False


if __name__ == '__main__':
    t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logging.basicConfig(level=logging.INFO,
                        filemode="a",
                        # filename=return_log+"{}.log".format(t),
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s', )



    systemname = "HJF"
    Status = "1"
    data_name = "Return"
    data_status = "1"
    username = "000003"
    password = '20110721'
    factorycode = "000003"
    client_id = "1006"
    # accounts = account_infos(systemname, Status, data_name, data_status, username, factorycode, client_id)
    # logging.info("合家福军民 长度为：{}".format(len(accounts)))
    # moban_name = "退单"
    # for account in accounts:
    #     count = 0
    #     while True:
    #         count +=1
    #         logging.info("第{}次登录 合家福军民".format(count))
    #
    #         if count == 6:
    #             add_log(username, factorycode, client_id, systemname, moban_name, "意外失败", "错误")
    #             break
    #         username = account.get('username')
    #         password = account.get('password')
    #         factorycode = account.get('factorycode')
    #         client_id = account.get('client_id')
    #         logging.info("卓展 账号为：'{}','{}','{}','{}'".format(username,password,factorycode,client_id))
    #         tongyong_class = tongyong_order()
    #         result = tongyong_class.login(username, password, factorycode, client_id)
    #         if result == 401:
    #             add_log(username, factorycode, client_id,systemname,moban_name, "用户名/密码错误", "错误")
    #             break
    #         if not result:
    #             continue
    #         result = tongyong_class.moban_xiazai(username, password, factorycode, client_id)
    #         if not result:
    #             continue
    #         break

    tongyong_class = tongyong_order()
    tongyong_class._login(username, password, '', '')
    tongyong_class.moban_xiazai(username, password, factorycode, client_id)
"""

0 8-20/1 * * * python3 /home/leili/zhuozhan/order_.py &
30 08,20 * * * python3 /home/leili/aoqile/shouhuodan.py
00 08-20 * * * python3 /home/leili/aoqile/order.py

"""