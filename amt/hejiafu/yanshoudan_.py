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
from config.sql_order import yanshoudan_result
from login import Moban

path = os.path.dirname(os.path.abspath(__file__))

yanshoudan_log = path + '/log/yanshoudan/'
order_xls_name = path + '/order_xls/'


class tongyong_order(Moban):
    def moban_xiazai(self, username, password, factorycode, client_id):
        # try:

            start_date = date.strftime(date.today() + timedelta(days=-30), '%Y-%m-%d')
            end_date = date.strftime(date.today() + timedelta(days=0), '%Y-%m-%d')

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Cookie': 'ASP.NET_SessionId=hii3mtpe4qbvuhhbmaditjye; .ASPXAUTH=7B1EF5AF2C6C67DC417D6513CC1B1BB7049E29C40009CE0B85446DE9A4429021CE7EFA281C4B82DBA1A1E2CC5D33AC47162C268AE51C42F66DFF6A924AB8A512A1581E9824758B4BA384B1C7C7A1C5CA5E53B6CA090B28D928A78FF35300EAD8',
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

            HJF_swjsysd_note = []
            HJF_swjsysd_detail_header = []
            HJF_swjsysd_detail_body = []


            data ={"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRecByPayStatusList","UserNo":username,
                   "ClientTime":formatted_now,"ObjectData":{"sProviderNo":factorycode,"sStoreId":"",
                "Id":"","dSt":start_date,"dEn":end_date,"sType":"","sConNo":"","sPayStatus":"尚未结算",
                    "sExtend":"","Tag":"","CurrentPage":1,"PageSize":100},"Tag":'null',"Token":self.token}

            # print(data)
            data_str = json.dumps(data)
            encoded_data = base64.b64encode(data_str.encode()).decode()

            url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
            response = self.session.post(url, headers=headers,data=encoded_data).json()
            # print(response)

            if response['ObjectData']['tb_o_rec'] == []:
                add_log(username, factorycode, client_id, "HJF", "验收单",
                            "本次下载共0条", "成功")
                print("本次下载共0条")
                # return True

            else:
                # 要判断总共多少页并循环
                page_num = int(response['ObjectData']['dtTotalPage'][0]['totalPageCount'])
                # print(page_num)
                for i in range(1,page_num+1):
                    data = {"UniqueKey": "EnjoySCM40共管库存", "MethodName": "GetRecByPayStatusList", "UserNo": username,
                            "ClientTime": formatted_now, "ObjectData": {"sProviderNo": factorycode, "sStoreId": "",
                                                                        "Id": "", "dSt": start_date, "dEn": end_date,
                                                                        "sType": "", "sConNo": "", "sPayStatus": "尚未结算",
                                                                        "sExtend": "", "Tag": "", "CurrentPage": i,
                                                                        "PageSize": 100}, "Tag": 'null', "Token": self.token}
                    data_str = json.dumps(data)
                    encoded_data = base64.b64encode(data_str.encode()).decode()
                    # print(encoded_data)

                    response = self.session.post(url, headers=headers, data=encoded_data).json()
                    rowss = response['ObjectData']['tb_o_rec']
                    if type(rowss) == dict:
                        rows = []
                        rows.append(rowss)
                    else:
                        rows = rowss

                    for row in rows:
                        # 尚未结算验收单列表
                        swjsysd_note = []
                        # 序号
                        c_sort = row.get('c_sort')
                        swjsysd_note.append(c_sort)
                        #订单号
                        c_id = row.get('c_id')
                        swjsysd_note.append(c_id)
                        #分店编码
                        c_delivery_store_id = row.get('store_id')
                        swjsysd_note.append(c_delivery_store_id)
                        #分店名称
                        c_delivery_store_sname = row.get('c_store_sname')
                        swjsysd_note.append(c_delivery_store_sname)
                        #物流模式
                        c_delivery_type = row.get('c_delivery_type')
                        swjsysd_note.append(c_delivery_type)
                        #越库类型
                        yueku_type = row.get('c_storage_mode')
                        swjsysd_note.append(yueku_type)
                        #单据状态
                        c_rec_status = row.get('c_rec_status')
                        swjsysd_note.append(c_rec_status)
                        #打印状态
                        c_print_status = row.get('c_print_status')
                        if "000003" in c_print_status:
                            dyzt = '已打印'
                        else:
                            dyzt = '尚未打印'
                        swjsysd_note.append(dyzt)
                        #进价总额
                        c_at_order = row.get('c_at_in')
                        print(c_at_order)
                        swjsysd_note.append(c_at_order)
                        #结算价总额（含税）
                        c_at_in = row.get('c_at_pay')
                        swjsysd_note.append(c_at_in)
                        #不含税总额
                        c_a_in = row.get('c_a_in')
                        swjsysd_note.append(c_a_in)
                        #税额 "13.00%299.30"
                        se = row.get('c_tax_str').split('%')[1].split(';')[0]
                        swjsysd_note.append(se)
                        #生成订单
                        scdd = ''
                        swjsysd_note.append(scdd)
                        #订单反馈单
                        ddfkd = ''
                        swjsysd_note.append(ddfkd)
                        #订单反馈单号
                        ddfkdh = row.get('c_feedback_id')
                        swjsysd_note.append(ddfkdh)
                        #收货审核时间
                        c_rec_au_dt = row.get('c_rec_au_dt')
                        swjsysd_note.append(c_rec_au_dt)
                        #备注
                        c_note = row.get('c_note')
                        swjsysd_note.append(c_note)


                        # 验货人--详情头
                        c_rec_userno = row.get('c_rec_userno')
                        # 部门编码
                        c_adno = row.get('c_adno')
                        #验货顺序号
                        c_rec_no = row.get('c_rec_no')
                        c_rec_store_id = row.get('c_rec_store_id')
                        #供应商编码
                        # swjsysd_note.append(factorycode)
                        print(swjsysd_note)
                        #uuid

                        #client_id
                        #下载时间

                        HJF_swjsysd_note.append(swjsysd_note)


                        # 尚未结算验收单详情单头

                        data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRecBillDetail","UserNo":username,"ClientTime":formatted_now,"ObjectData":{"Id":c_id},"Tag":'null',"Token":self.token}
                        # print(data)
                        data_str = json.dumps(data)
                        encoded_data = base64.b64encode(data_str.encode()).decode()
                        # print(encoded_data)
                        url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
                        response = self.session.post(url, headers=headers,data=encoded_data).json()
                        # print(response)
                        row = response['ObjectData']['tb_o_rec'][0]
                        print('尚未结算验收单详情单头')
                        # print(row)
                        # 尚未结算验收单详情单头
                        swjsysd_detail_header = []
                        #单据号
                        swjsysd_detail_header.append(c_id)
                        #部门编码
                        c_adno = row.get('c_adno')
                        swjsysd_detail_header.append(c_adno)
                        #目的机构编码
                        c_rec_store_id = row.get('c_rec_store_id')
                        swjsysd_detail_header.append(c_rec_store_id)
                        #目的机构名称
                        swjsysd_detail_header.append(c_delivery_store_sname)
                        #收货仓库
                        c_rec_site = row.get('c_rec_site')
                        swjsysd_detail_header.append(c_rec_site)
                        #验货人
                        c_rec_userno = row.get('c_rec_userno')
                        swjsysd_detail_header.append(c_rec_userno)
                        #收货顺序号
                        c_rec_no = row.get('c_rec_no')
                        swjsysd_detail_header.append(c_rec_no)
                        #收货机构
                        c_rec_store_id = row.get('c_rec_store_id')
                        swjsysd_detail_header.append(c_rec_store_id)
                        #采购类型
                        c_type = row.get('c_type')
                        swjsysd_detail_header.append(c_type)
                        #联系人
                        c_link_man = row.get('c_link_man')
                        swjsysd_detail_header.append(c_link_man)
                        #订货人
                        c_order_userno = row.get('c_order_userno')
                        swjsysd_detail_header.append(c_order_userno)
                        # 供应商
                        c_provider = row.get('c_provider')
                        swjsysd_detail_header.append(c_provider)
                        # 合同
                        c_con_no = row.get('c_con_no')
                        swjsysd_detail_header.append(c_con_no)
                        # 电话
                        c_link_tele = row.get('c_link_tele')
                        swjsysd_detail_header.append(c_link_tele)
                        # 验货录入人
                        c_mk_usernor = row.get('c_mk_usernor')
                        swjsysd_detail_header.append(c_mk_usernor)
                        # 验货时间c_rec_dt
                        c_rec_dt = row.get('c_rec_dt')
                        swjsysd_detail_header.append(c_rec_dt)
                        # 验货审核人
                        c_rec_au_userno = row.get('c_rec_au_userno')
                        swjsysd_detail_header.append(c_rec_au_userno)
                        # 验货审核时间
                        c_rec_au_dt = row.get('c_rec_au_dt')
                        swjsysd_detail_header.append(c_rec_au_dt)
                        # 录入时间
                        lrsj = row.get('c_mk_dtr')
                        swjsysd_detail_header.append(lrsj)
                        # 第二验货人
                        c_check_userno = row.get('c_rec_userno2')
                        swjsysd_detail_header.append(c_check_userno)
                        # 打印状态
                        print_status = row.get('c_print_status')
                        if print_status == '':
                            dyzt = '尚未打印'
                        else:
                            dyzt = '已打印'
                        swjsysd_detail_header.append(dyzt)
                        # 其他物品
                        qtwp = ''
                        swjsysd_detail_header.append(qtwp)
                        #备注
                        c_note = row.get('c_note')
                        swjsysd_detail_header.append(c_note)
                        #供应商编码
                        # yyzt = ''
                        # swjsysd_detail_header.append(factorycode)
                        # uuid
                        # print(swjsysd_detail_header)
                        #下载时间
                        #clien_id
                        HJF_swjsysd_detail_header.append(swjsysd_detail_header)

                        rowss = response['ObjectData']['tb_o_recg']
                        # print(rowss)
                        # print(type(rows))
                        if type(rowss) == dict:
                            rows = []
                            rows.append(rowss)
                        else:
                            rows = rowss

                        print(rows)
                        for row in rows:
                            print(row)
                            # 尚未结算验收单详情身
                            swjsysd_detail_body = []
                            #商品编码
                            c_gcode = row.get('c_gcode')
                            swjsysd_detail_body.append(c_gcode)
                            #商品名称
                            c_gname = row.get('c_gname')
                            swjsysd_detail_body.append(c_gname)
                            # 主条码
                            c_barcode = row.get('c_barcode')
                            swjsysd_detail_body.append(c_barcode)
                            # 规格
                            c_model = row.get('c_model')
                            swjsysd_detail_body.append(c_model)
                            # 单位
                            c_basic_unit = row.get('c_basic_unit')
                            swjsysd_detail_body.append(c_basic_unit)
                            # 订货数量
                            c_order_n = row.get('c_order_n')
                            swjsysd_detail_body.append(c_order_n)
                            # 赠品订货数量
                            c_order_free_n = row.get('c_order_free_n')
                            swjsysd_detail_body.append(c_order_free_n)
                            # 订货总量
                            dhzl = c_order_n+c_order_free_n
                            swjsysd_detail_body.append(dhzl)
                            # 收货数量
                            c_rec_n = row.get('c_rec_n')
                            swjsysd_detail_body.append(c_rec_n)
                            # 收货数量赠品
                            c_rec_free_n = row.get('c_rec_free_n')
                            swjsysd_detail_body.append(c_rec_free_n)
                            # 包装含量
                            c_content = row.get('c_content')
                            swjsysd_detail_body.append(c_content)
                            # 税率
                            c_tax_rate = row.get('c_tax_rate')
                            swjsysd_detail_body.append(c_tax_rate)
                            # 结算税率
                            c_tax_rate_pay = row.get('c_tax_rate_pay')
                            swjsysd_detail_body.append(c_tax_rate_pay)
                            # 进货价格（含税）
                            c_pt_in = row.get('c_pt_in')
                            swjsysd_detail_body.append(c_pt_in)
                            # 结算（含税） c_pt_pay
                            c_pt_pay = row.get('c_pt_pay')
                            swjsysd_detail_body.append(c_pt_pay)
                            # 进货金额（含税）
                            c_at_in = row.get('c_at_in')
                            swjsysd_detail_body.append(c_at_in)
                            # 结算价金额（含税）
                            c_at_pay = row.get('c_at_pay')
                            swjsysd_detail_body.append(c_at_pay)
                            # 不含税总额
                            c_aet_cost = row.get('c_a_in')
                            swjsysd_detail_body.append(c_aet_cost)
                            # 税额
                            se = c_at_pay - c_aet_cost
                            swjsysd_detail_body.append(se)
                            # 单据号
                            swjsysd_detail_body.append(c_id)
                            # 目的机构编码
                            # dhje = ''
                            swjsysd_detail_body.append(c_rec_store_id)
                            # 供应商编码
                            # swjsysd_detail_body.append(factorycode)
                            print("****************************")
                            print(swjsysd_detail_body)
                            # uuid
                            # 下载时间
                            # client_id
                            HJF_swjsysd_detail_body.append(swjsysd_detail_body)

            #已结算验收单
            data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRecByPayStatusList","UserNo":username,"ClientTime":formatted_now,"ObjectData":{"sProviderNo":factorycode,"sStoreId":"","Id":"","dSt":start_date,"dEn":end_date,"sType":"","sConNo":"","sPayStatus":"已结算","sExtend":"","Tag":"","CurrentPage":1,"PageSize":100},"Tag":'null',"Token":self.token}
            data_str = json.dumps(data)
            encoded_data = base64.b64encode(data_str.encode()).decode()
            res = self.session.post('https://www.crtc-jmfws.com:8003/Enjoy/Service/',headers=headers, data=encoded_data).json()
            # print(res)

            HJF_yjsysd_list = []
            HJF_yjsysd_detail_header = []
            HJF_yjsysd_detail_body = []

            if res['ObjectData']['tb_o_rec'] == []:
                add_log(username, factorycode, client_id, "HJF", "已结算验收单",
                        "本次下载共0条", "成功")
                # print("本次下载共0条")
                return True
            else:

                    # 要判断总共多少页并循环
                page_num = int(res['ObjectData']['dtTotalPage'][0]['totalPageCount'])
                # print(page_num)
                for i in range(1, page_num + 1):
                    data = {"UniqueKey": "EnjoySCM40共管库存", "MethodName": "GetRecByPayStatusList", "UserNo": username,
                            "ClientTime": formatted_now,
                            "ObjectData": {"sProviderNo": factorycode, "sStoreId": "", "Id": "", "dSt": start_date,
                                           "dEn": end_date, "sType": "", "sConNo": "", "sPayStatus": "已结算",
                                           "sExtend": "", "Tag": "", "CurrentPage": i, "PageSize": 100}, "Tag": 'null',
                            "Token": self.token}

                    data_str = json.dumps(data)
                    encoded_data = base64.b64encode(data_str.encode()).decode()
                    # print(encoded_data)
                    url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
                    response = self.session.post(url, headers=headers, data=encoded_data).json()
                    rowss = response['ObjectData']['tb_o_rec']
                    if type(rowss) == dict:
                        rows = []
                        rows.append(rowss)
                    else:
                        rows = rowss

                    for row in rows:
                        yjsysd_list = []
                        # 序号
                        c_sort = row.get('c_sort')
                        yjsysd_list.append(c_sort)
                        # 订单号
                        c_id = row.get('c_id')
                        yjsysd_list.append(c_id)
                        # 分店编码
                        c_de_store_id = row.get('store_id')
                        yjsysd_list.append(c_de_store_id)
                        # 分店名称
                        c_de_store_sname = row.get('c_store_sname')
                        yjsysd_list.append(c_de_store_sname)
                        # 物流模式
                        c_delivery_type = row.get('c_delivery_type')
                        yjsysd_list.append(c_delivery_type)
                        # 越库类型
                        yklx = row.get('c_storage_mode')
                        yjsysd_list.append(yklx)
                        # 单据状态
                        c_rec_status = row.get('c_rec_status')
                        yjsysd_list.append(c_rec_status)
                        # 打印状态
                        c_print_status = row.get('c_print_status')
                        if "000003" in c_print_status:
                            dyzt = '已打印'
                        else:
                            dyzt = '尚未打印'
                        yjsysd_list.append(dyzt)
                        # 进价总额
                        c_at_in = row.get('c_at_in')
                        yjsysd_list.append(c_at_in)
                        # 结算价总额(含税)
                        c_at_pay = row.get('c_at_pay')
                        yjsysd_list.append(c_at_pay)
                        # 不含税总额
                        c_a_in = row.get('c_a_in')
                        yjsysd_list.append(c_a_in)
                        # 税额 "c_tax_str":"13.00%184.72;
                        c_tax_str = row.get('c_tax_str').split('%')[1]
                        c_tax_str = c_tax_str.replace(';','')
                        yjsysd_list.append(c_tax_str)
                        # 结算分区
                        c_settle_region = row.get('c_settle_region')
                        yjsysd_list.append(c_settle_region)
                        # 收货审核时间
                        c_rec_dt = row.get('c_rec_au_dt')
                        yjsysd_list.append(c_rec_dt)
                        # 备注
                        c_note = row.get('c_note')
                        yjsysd_list.append(c_note)
                        # 供应商编码
                        # uuid
                        HJF_yjsysd_list.append(yjsysd_list)

                        data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetRecBillDetail","UserNo":username,"ClientTime":formatted_now,"ObjectData":{"Id":c_id},"Tag":'null',"Token":self.token}
                        data_str = json.dumps(data)
                        encoded_data = base64.b64encode(data_str.encode()).decode()
                        response = self.session.post(url, headers=headers, data=encoded_data).json()
                        # print(response)
                        row = response['ObjectData']['tb_o_rec'][0]
                        print('已结算验收单详情单头')
                        # print(row)
                        # 已结算验收单详情单头
                        yjsysd_detail_header = []
                        # 单据号
                        yjsysd_detail_header.append(c_id)
                        # 部门编码
                        c_adno = row.get('c_adno')
                        yjsysd_detail_header.append(c_adno)
                        # 目的机构编码
                        c_rec_store_id = row.get('c_rec_store_id')
                        yjsysd_detail_header.append(c_rec_store_id)
                        # 目的机构名称
                        c_delivery_store_sname = row.get('c_delivery_store_sname')
                        yjsysd_detail_header.append(c_delivery_store_sname)
                        # 收货仓库
                        c_rec_site = row.get('c_rec_site')
                        yjsysd_detail_header.append(c_rec_site)
                        # 验货人
                        c_rec_userno = row.get('c_rec_userno')
                        yjsysd_detail_header.append(c_rec_userno)
                        # 收货顺序号
                        c_rec_no = row.get('c_rec_no')
                        yjsysd_detail_header.append(c_rec_no)
                        # 收货机构
                        c_rec_store_id = row.get('c_rec_store_id')
                        yjsysd_detail_header.append(c_rec_store_id)
                        # 采购类型
                        c_type = row.get('c_type')
                        yjsysd_detail_header.append(c_type)
                        # 联系人
                        c_link_man = row.get('c_link_man')
                        yjsysd_detail_header.append(c_link_man)
                        # 订货人
                        c_order_userno = row.get('c_order_userno')
                        yjsysd_detail_header.append(c_order_userno)
                        # 供应商
                        c_provider = row.get('c_provider')
                        yjsysd_detail_header.append(c_provider)
                        # 合同
                        c_con_no = row.get('c_con_no')
                        yjsysd_detail_header.append(c_con_no)
                        # 电话
                        c_link_tele = row.get('c_link_tele')
                        yjsysd_detail_header.append(c_link_tele)
                        # 验货录入人
                        c_mk_usernor = row.get('c_mk_usernor')
                        yjsysd_detail_header.append(c_mk_usernor)
                        # 验货时间
                        c_rec_dt = row.get('c_rec_dt')
                        yjsysd_detail_header.append(c_rec_dt)
                        # 验货审核人
                        c_rec_au_userno = row.get('c_rec_au_userno')
                        yjsysd_detail_header.append(c_rec_au_userno)
                        # 验货审核时间
                        c_rec_au_dt = row.get('c_rec_au_dt')
                        yjsysd_detail_header.append(c_rec_au_dt)
                        # 录入时间
                        lrsj = row.get('c_mk_dtr')
                        yjsysd_detail_header.append(lrsj)
                        # 第二验货人
                        c_check_userno = row.get('c_rec_userno2')
                        yjsysd_detail_header.append(c_check_userno)
                        # 打印状态
                        print_status = row.get('c_print_status')
                        if print_status == '':
                            dyzt = '尚未打印'
                        else:
                            dyzt = '已打印'
                        yjsysd_detail_header.append(dyzt)
                        # 其他物品
                        qtwp = ''
                        yjsysd_detail_header.append(qtwp)
                        # 备注
                        c_note = row.get('c_note')
                        yjsysd_detail_header.append(c_note)
                        # 供应商编码
                        # yyzt = ''
                        # yjsysd_detail_header.append(factorycode)
                        # uuid
                        print(yjsysd_detail_header)
                        # 下载时间
                        # clien_id
                        HJF_yjsysd_detail_header.append(yjsysd_detail_header)

                        rowss = response['ObjectData']['tb_o_recg']
                        print(rowss)
                        if type(rowss) == dict:
                            rows = []
                            rows.append(rowss)
                        else:
                            rows = rowss
                        # print(row)
                        for row in rows:
                            print("**********已结算验收单详情身************")
                            print(row)
                            # 已结算验收单详情身
                            yjsysd_detail_body = []
                            # 商品编码
                            c_gcode = row.get('c_gcode')
                            yjsysd_detail_body.append(c_gcode)
                            # 商品名称
                            c_gname = row.get('c_gname')
                            yjsysd_detail_body.append(c_gname)
                            # 主条码
                            c_barcode = row.get('c_barcode')
                            yjsysd_detail_body.append(c_barcode)
                            # 规格
                            c_model = row.get('c_model')
                            yjsysd_detail_body.append(c_model)
                            # 单位
                            c_basic_unit = row.get('c_basic_unit')
                            yjsysd_detail_body.append(c_basic_unit)
                            # 订货数量
                            c_order_n = row.get('c_order_n')
                            yjsysd_detail_body.append(c_order_n)
                            # 赠品订货数量
                            c_order_free_n = row.get('c_order_free_n')
                            yjsysd_detail_body.append(c_order_free_n)
                            # 订货总量
                            dhzl = c_order_n + c_order_free_n
                            yjsysd_detail_body.append(dhzl)
                            # 收货数量
                            c_rec_n = row.get('c_rec_n')
                            yjsysd_detail_body.append(c_rec_n)
                            # 收货数量赠品
                            c_rec_free_n = row.get('c_rec_free_n')
                            yjsysd_detail_body.append(c_rec_free_n)
                            # 包装含量
                            c_content = row.get('c_content')
                            yjsysd_detail_body.append(c_content)
                            # 税率
                            c_tax_rate = row.get('c_tax_rate')
                            yjsysd_detail_body.append(c_tax_rate)
                            # 结算税率
                            c_tax_rate_pay = row.get('c_tax_rate_pay')
                            yjsysd_detail_body.append(c_tax_rate_pay)
                            # 进货价格（含税）
                            c_pt_in = row.get('c_pt_in')
                            yjsysd_detail_body.append(c_pt_in)
                            # 结算（含税）
                            c_pt_pay = row.get('c_pt_pay')
                            yjsysd_detail_body.append(c_pt_pay)
                            # 进货金额（含税）
                            c_at_in = row.get('c_at_in')
                            yjsysd_detail_body.append(c_at_in)
                            # 结算价金额（含税）
                            c_at_pay = row.get('c_at_pay')
                            yjsysd_detail_body.append(c_at_pay)
                            # 不含税总额
                            c_aet_cost = row.get('c_aet_cost')
                            yjsysd_detail_body.append(c_aet_cost)
                            # 税额
                            se = c_at_pay - c_aet_cost
                            yjsysd_detail_body.append(se)
                            # 单据号
                            yjsysd_detail_body.append(c_id)
                            # 目的机构编码
                            # dhje = ''
                            yjsysd_detail_body.append(c_rec_store_id)
                            # 供应商编码
                            # yjsysd_detail_body.append(factorycode)

                            # uuid
                            # 下载时间
                            # client_id
                            HJF_yjsysd_detail_body.append(yjsysd_detail_body)

            logging.info("合家福军民 验收单长度：{}".format(len(HJF_swjsysd_note)+len(HJF_yjsysd_list)))


            result = yanshoudan_result(HJF_swjsysd_note,HJF_swjsysd_detail_header,HJF_swjsysd_detail_body,HJF_yjsysd_list,HJF_yjsysd_detail_header,HJF_yjsysd_detail_body,client_id,factorycode)
            logging.info("下载条数：{}".format(len(HJF_swjsysd_note)+len(HJF_yjsysd_list)))
            if not result:
                add_log(username, factorycode, client_id, "HJF", "验收单", "入库意外失败", "错误")

            add_log(username, factorycode, client_id, "HJF", "验收单",
                    "本次下载共{}条".format(len(HJF_swjsysd_note)+len(HJF_yjsysd_list)), "成功")
            return True
        # except Exception as e:
        #     logging.info("验收单入库 下载失败：{}".format(e))
        #     return False


if __name__ == '__main__':
    t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logging.basicConfig(level=logging.INFO,
                        filemode="a",
                        filename=yanshoudan_log+"{}.log".format(t),
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s', )



    systemname = "HJF"
    Status = "1"
    data_name = "Receive"
    data_status = "1"
    username = "000003"
    password = '20110721'
    factorycode = "000003"
    client_id = "1006"
    accounts = account_infos(systemname, Status, data_name, data_status, username, factorycode, client_id)
    logging.info("合家福军民 长度为：{}".format(len(accounts)))
    moban_name = "验收单"
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
    #         result = tongyong_class._login(username, password, factorycode, client_id)
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
    tongyong_class._login(username, password, factorycode, '')
    tongyong_class.moban_xiazai(username, password, factorycode, client_id)
"""

0 8-20/1 * * * python3 /home/leili/zhuozhan/order_.py &
30 08,20 * * * python3 /home/leili/aoqile/shouhuodan.py
00 08-20 * * * python3 /home/leili/aoqile/order.py

"""