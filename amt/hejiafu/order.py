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
from config.sql_order import order_result
from login import Moban

path = os.path.dirname(os.path.abspath(__file__))

order_log = path + '/log/order/'
order_xls_name = path + '/order_xls/'


class tongyong_order(Moban):
    def moban_xiazai(self, username, password, factorycode, client_id):
        # try:

            start_date = date.strftime(date.today() + timedelta(days=-30), '%Y-%m-%d')
            end_date = date.strftime(date.today() + timedelta(days=0), '%Y-%m-%d')
            print(end_date)

            url = 'https://oapi.sanjiang.com/api/scm-order/purchase/getPurchaseByPage'

            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Origin": "https://scm_new.sanjiang.com",
                "Pragma": "no-cache",
                "Referer": "https://scm_new.sanjiang.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "sec-ch-ua-mobile": "?0",
                "token": "0c9ad555-0001-45d2-9c1f-06a625403d74",
                "token-type": "pc"
            }

            params = {
                "venderId": "61025",
                "date\\[\\]": "2024-8-21",
                "startDate": "2024-08-07",
                "endDate": "2024-08-21",
                "pageNumber": "1",
                "pageSize": "10",
                "total": "54",
                "mVenderId": "61025"
            }

            # 发送GET请求
            response = requests.get(url, headers=headers, params=params)

            print(response.text)


            # now = datetime.now(pytz.utc)
            # formatted_now = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            #
            # HJF_order_note = []
            # HJF_order_details_header = []
            # HJF_order_details_body = []
            # HJF_order_print_header = []
            # HJF_order_print_body = []
            #
            # data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetOrderByRecStatusList","UserNo":username,
            #         "ClientTime":formatted_now,"ObjectData":{"sProviderNo":factorycode,"sStoreId":"","Id":"",
            #         "dSt":start_date,"dEn":end_date,"sSCMStatus":"","sType":"","sConNo":"","sStatus":"尚未收货",
            #         "sExtend":"","Tag":"","CurrentPage":1,"PageSize":100},"Tag":'null',"Token":self.token}
            #
            # # print(data)
            # data_str = json.dumps(data)
            # encoded_data = base64.b64encode(data_str.encode()).decode()
            # # print(encoded_data)
            # url = 'https://www.crtc-jmfws.com:8003/Enjoy/Service/'
            # response = self.session.post(url, headers=headers,data=encoded_data).json()
            # # print(response)
            #
            # if response['ObjectData']['tb_o_i'] == []:
            #     add_log(username, factorycode, client_id, "HJF", "订单",
            #                 "本次下载共0条", "成功")
            #     print("本次下载共0条")
            #     return True
            #
            # rowss = response['ObjectData']['tb_o_i']
            # if type(rowss) == dict:
            #     rows = []
            #     rows.append(rowss)
            # else:
            #     rows = rowss
            #
            # for row in rows:
            #     #订单列表
            #     order_note = []
            #     # 序号
            #     c_sort = row.get('c_sort')
            #     order_note.append(c_sort)
            #     #订单号
            #     c_id = row.get('c_id')
            #     order_note.append(c_id)
            #     #分店编码
            #     c_delivery_store_id = row.get('store_id')
            #     order_note.append(c_delivery_store_id)
            #     #分店名称
            #     c_delivery_store_sname = row.get('c_store_sname')
            #     order_note.append(c_delivery_store_sname)
            #     #物流模式
            #     c_delivery_type = row.get('c_delivery_type')
            #     order_note.append(c_delivery_type)
            #     #越库类型
            #     yueku_type = row.get('c_storage_mode')
            #     order_note.append(yueku_type)
            #     #结算分区
            #     jsfq = row.get('c_settle_region')
            #     order_note.append(jsfq)
            #     #确认状态
            #     queren_statu = row.get('c_scm_status')
            #     order_note.append(queren_statu)
            #     #订单状态
            #     c_rec_status = row.get('c_order_status')
            #     order_note.append(c_rec_status)
            #     #预约状态
            #     yuyue = row.get('c_booking_status')
            #     order_note.append(yuyue)
            #     #订货总额
            #     c_at_order = row.get('c_at_order')
            #     order_note.append(c_at_order)
            #     #打印状态
            #     dayin_status = row.get('c_print_status')
            #     order_note.append(dayin_status)
            #     #订单反馈单
            #     ddfkd = ''
            #     order_note.append(ddfkd)
            #     #订单反馈单号
            #     ddfkdh = row.get('c_feedback_id')
            #     order_note.append(ddfkdh)
            #     #预约送货时间
            #     yyshsj = row.get('c_booking_dt')
            #     order_note.append(yyshsj)
            #     #期望送货日期
            #     qwshrq = row.get('c_order_de_dt')
            #     order_note.append(qwshrq)
            #     #取消日期
            #     qxrq = row.get('c_cancel_dt')
            #     order_note.append(qxrq)
            #     #录入时间
            #     lrsj = row.get('c_mk_dto')
            #     order_note.append(lrsj)
            #     #审核时间
            #     c_rec_au_dt = row.get('c_order_au_dt')
            #     order_note.append(c_rec_au_dt)
            #     #备注
            #     c_note = row.get('c_note')
            #     order_note.append(c_note)
            #     #供应商编码
            #     order_note.append(factorycode)
            #     #uuid
            #     #client_id
            #     #下载时间
            #     # print("order_note")
            #     print(order_note)
            #     HJF_order_note.append(order_note)
            #
            #
            #
            #     headers = {
            #         'Accept': 'application/json, text/javascript, */*; q=0.01',
            #         'Accept-Language': 'zh-CN,zh;q=0.9',
            #         'Cache-Control': 'no-cache',
            #         'Connection': 'keep-alive',
            #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #         # 'Cookie': 'ASP.NET_SessionId=544qdoi2yo0ye4qmolaozh3o; .ASPXAUTH=19A99D29D8203D8029E8FC5497125B6B9CE5DBED940412B0EB8F413F02E8ED0CDCFF7ADF8797F4C1880618F48F1414368C5F556899D7BF5AA1A0F8678A463BBC79FB763673955A8557E0B0E32F1E78EB15810A7EA52193BF57A31CE15FD69C9A',
            #         'Origin': 'https://www.crtc-jmfws.com:8003',
            #         'Pragma': 'no-cache',
            #         'Referer': 'https://www.crtc-jmfws.com:8003/index.html',
            #         'Sec-Fetch-Dest': 'empty',
            #         'Sec-Fetch-Mode': 'cors',
            #         'Sec-Fetch-Site': 'same-origin',
            #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            #         'X-Requested-With': 'XMLHttpRequest',
            #         'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            #         'sec-ch-ua-mobile': '?0',
            #         'sec-ch-ua-platform': '"Windows"',
            #     }
            #
            #     data = {"UniqueKey":"EnjoySCM40共管库存","MethodName":"GetOrderDetail","UserNo":username,
            #             "ClientTime":formatted_now,"ObjectData":{"Id":c_id},
            #             "Tag":'null',"Token":self.token}
            #     # print(data)
            #     data_str = json.dumps(data)
            #     encoded_data = base64.b64encode(data_str.encode()).decode()
            #
            #     response = self.session.post('https://www.crtc-jmfws.com:8003/Enjoy/Service/',headers=headers, data=encoded_data).json()
            #     # print(response)
            #     item = response['ObjectData']['tb_o_i'][0]
            #     #订单详情单头
            #     order_detail_header = []
            #     #单据号
            #     order_detail_header.append(c_id)
            #     #目的分店
            #     mdfd = item.get('c_delivery_store_id')
            #     order_detail_header.append(mdfd)
            #     #物流模式
            #     wlms = item.get('c_delivery_type')
            #     order_detail_header.append(wlms)
            #     #越库类型
            #     ykmx = item.get('c_storage_mode')
            #     order_detail_header.append(ykmx)
            #     #商品部门
            #     spbm_1 = item.get('c_adno')
            #     order_detail_header.append(spbm_1)
            #     #订单类型
            #     ddlx = item.get('c_order_type')
            #     order_detail_header.append(ddlx)
            #     #采购类型
            #     cglx= item.get('c_type')
            #     order_detail_header.append(cglx)
            #     #订货人
            #     o_dhr = item.get('c_mk_usernoo')
            #     order_detail_header.append(o_dhr)
            #     #订货日期
            #     o_dhrq = item.get('c_order_dt')
            #     order_detail_header.append(o_dhrq)
            #     #价格类型
            #     jglx = item.get('c_order_p_type')
            #     order_detail_header.append(jglx)
            #     # 收货仓库
            #     shck = item.get('c_dc_site')
            #     order_detail_header.append(shck)
            #     # 收货人
            #     shr = item.get('c_rec_username')
            #     order_detail_header.append(shr)
            #     # 到货日期
            #     r_dhrq = item.get('c_order_de_dt')
            #     order_detail_header.append(r_dhrq)
            #     # 合同
            #     ht = item.get('c_con_no')
            #     order_detail_header.append(ht)
            #     # 联系传真
            #     lxcz = item.get('c_link_fax')
            #     order_detail_header.append(lxcz)
            #     # 取消日期
            #     qxrq = item.get('c_cancel_dt')
            #     order_detail_header.append(qxrq)
            #     # 订货传真
            #     dhcz = item.get('c_order_fax')
            #     order_detail_header.append(dhcz)
            #     # 订货电话
            #     dhdh = item.get('c_order_tele')
            #     order_detail_header.append(dhdh)
            #     # 联系电话
            #     lxdh = item.get('c_link_tele')
            #     order_detail_header.append(lxdh)
            #     # 联系人
            #     lxr = item.get('c_link_man')
            #     order_detail_header.append(lxr)
            #     #配送中心仓库
            #     pszxck = item.get('c_dc_site')
            #     order_detail_header.append(pszxck)
            #     #预约状态
            #     yyzt = item.get('c_booking_status')
            #     order_detail_header.append(yyzt)
            #     # 预约时间
            #     yysj = item.get('c_booking_dt')
            #     order_detail_header.append(yysj)
            #     # 打印状态
            #     order_detail_header.append(dayin_status)
            #     # 录入人
            #     lrr = item.get('c_mk_usernoo')
            #     order_detail_header.append(lrr)
            #     # 录入时间
            #     lrsj = item.get('c_mk_dto')
            #     order_detail_header.append(lrsj)
            #     # 预约电话
            #     yydh = item.get('c_deal_tele')
            #     order_detail_header.append(yydh)
            #     # 确认状态
            #     qrzt = item.get('c_scm_status')
            #     order_detail_header.append(qrzt)
            #     # 审核人
            #     checker = item.get('c_mk_usernoo')
            #     order_detail_header.append(checker)
            #     # 审核时间
            #     shsj = item.get('c_mk_dtr')
            #     order_detail_header.append(shsj)
            #     # 送货地址
            #     shdz = item.get('c_rec_address')
            #     order_detail_header.append(shdz)
            #     # 备注
            #     bz = item.get('c_note')
            #     order_detail_header.append(bz)
            #     # 供应商编码
            #     order_detail_header.append(factorycode)
            #     # uuid
            #     #下载时间
            #     #clien_id
            #
            #     HJF_order_details_header.append(order_detail_header)
            #     #供应商名称
            #     c_provider = item.get('c_provider')
            #     c_pname = item.get('c_pname')
            #     #制单人
            #     c_mk_usernameo = item.get('c_mk_usernameo')
            #
            #     rowss = response['ObjectData']['tb_o_ig']
            #     print(rowss)
            #     # print(type(rowss))
            #     if type(rowss) == dict:
            #         rows = []
            #         rows.append(rowss)
            #     else:
            #         rows = rowss
            #     for item in rows:
            #         #订单详情单身
            #         order_detail_body = []
            #         #序号
            #         xuhao = item.get('c_ig_sort')
            #         order_detail_body.append(xuhao)
            #         #商品编码
            #         spbm = item.get('c_gcode')
            #         order_detail_body.append(spbm)
            #         # 主条码
            #         ztm = item.get('c_barcode')
            #         order_detail_body.append(ztm)
            #         # 商品名称
            #         spmc = item.get('c_gname')
            #         order_detail_body.append(spmc)
            #         # 订货数量
            #         dhsl = item.get('c_order_n')
            #         order_detail_body.append(dhsl)
            #         # 订货包装量
            #         dhbzl = item.get('c_order_pack')
            #         order_detail_body.append(dhbzl)
            #         # 订货赠品数量
            #         dhzpsl = item.get('c_order_free_n')
            #         order_detail_body.append(dhzpsl)
            #         # 赠品包装量
            #         zpbzl = item.get('c_order_free_pack')
            #         order_detail_body.append(zpbzl)
            #         # 单位
            #         dw = item.get('c_basic_unit')
            #         order_detail_body.append(dw)
            #         # 规格
            #         gg = item.get('c_model')
            #         order_detail_body.append(gg)
            #         # 多条码
            #         dtm = item.get('c_barcode_ig')
            #         order_detail_body.append(dtm)
            #         # 生产日期
            #         scrq = item.get('c_produce_dt')
            #         order_detail_body.append(scrq)
            #         # 合同进货（含税）
            #         htjh = item.get('c_pt_in_con')
            #         order_detail_body.append(htjh)
            #         # 进货价格（含税）
            #         jhjg = item.get('c_pt_in')
            #         order_detail_body.append(jhjg)
            #         # 结算价格（含税）
            #         jsjg = item.get('c_pt_pay')
            #         order_detail_body.append(jsjg)
            #         # 进项税率
            #         jxsl = item.get('c_tax_rate')
            #         order_detail_body.append(jxsl)
            #         # 包装含量
            #         bzhl = item.get('c_content')
            #         order_detail_body.append(bzhl)
            #         # 总计
            #         zj = dhbzl*bzhl
            #         order_detail_body.append(zj)
            #         # 订货金额（含税进价）
            #         o_dhje = item.get('c_at_in')
            #         order_detail_body.append(o_dhje)
            #         # 订货金额（含税结算价）
            #         dhje = item.get('c_at_pay')
            #         order_detail_body.append(dhje)
            #         # 备注
            #         bz = item.get('c_note')
            #         order_detail_body.append(bz)
            #         # 单据号
            #         djh = c_id
            #         order_detail_body.append(djh)
            #         # 目的分店
            #         # mdfd = mdfd
            #         order_detail_body.append(mdfd)
            #         # 供应商编码
            #         order_detail_body.append(factorycode)
            #         # uuid
            #         # retailer_id
            #         # 下载时间
            #         HJF_order_details_body.append(order_detail_body)
            #
            #     data = response['ObjectData']['tb_o_ig_sum'][0]
            #     print(data)
            #     #订单打印单头
            #     order_print_header = []
            #     #收货机构
            #     # shjg = c_delivery_store_id
            #     order_print_header.append(c_delivery_store_id)
            #     #收货机构名称
            #     # shjgmc = ''
            #     order_print_header.append(c_delivery_store_sname)
            #     # 单据号
            #     # djh = ''
            #     order_print_header.append(c_id)
            #     # 订货日期
            #     order_print_header.append(o_dhrq)
            #     # 商品部门
            #     order_print_header.append(spbm_1)
            #     # 物流模式
            #     order_print_header.append(wlms)
            #     # 到货日期
            #     order_print_header.append(r_dhrq)
            #     # 供应商
            #     # gys = c_provider
            #     order_print_header.append(c_provider)
            #     # 供应商名称
            #     # c_pname = c_pname
            #     order_print_header.append(c_pname)
            #     # 合同
            #     order_print_header.append(ht)
            #     # 取消日期
            #     order_print_header.append(qxrq)
            #     # 联系人
            #     order_print_header.append(lxr)
            #     # 联系电话
            #     order_print_header.append(lxdh)
            #     # 合计订货数量
            #     hjdhsl = data.get('c_rec_n_sum')
            #     order_print_header.append(hjdhsl)
            #     # 合计订货件数
            #     hjdhjs = data.get('c_order_pack_sum')
            #     order_print_header.append(hjdhjs)
            #     # 合计订货金额（含税进价）
            #     hjdhje = data.get('c_at_in')
            #     order_print_header.append(hjdhje)
            #     # 收货人
            #     order_print_header.append(shr)
            #     # 制单人
            #     # zdr = c_mk_usernameo
            #     order_print_header.append(c_mk_usernameo)
            #     # 供应商编码
            #     order_print_header.append(factorycode)
            #     # uuid
            #     #下载时间
            #     #client_id
            #
            #     HJF_order_print_header.append(order_print_header)
            #
            #     rowss = response['ObjectData']['ds3']
            #     if type(rowss) == dict:
            #         rows = []
            #         rows.append(rowss)
            #     else:
            #         rows = rowss
            #     for row in rows:
            #         #订单打印单身
            #         order_print_body = []
            #         #商品编码
            #         spbm = row.get('c_gcode')
            #         order_print_body.append(spbm)
            #         # 条码
            #         tm = row.get('c_barcode')
            #         order_print_body.append(tm)
            #         # 商品名称
            #         spmc  = row.get('c_gname')
            #         order_print_body.append(spmc)
            #         # 规格
            #         gg = row.get('c_model')
            #         order_print_body.append(gg)
            #         # 包装含量
            #         bzhl = row.get('c_content')
            #         order_print_body.append(bzhl)
            #
            #         # 零售价
            #         lsj = row.get('c_price')
            #         order_print_body.append(lsj)
            #         # 进货单位
            #         jhdw = row.get('c_basic_unit')
            #         order_print_body.append(jhdw)
            #         # 订货数量
            #         dhsl = row.get('c_order_n')
            #         order_print_body.append(dhsl)
            #         # 订货件数
            #         dhjs = row.get('c_order_pack')
            #         order_print_body.append(dhjs)
            #         # 订货价格
            #         dhjg = row.get('c_pt_in_order')
            #         order_print_body.append(dhjg)
            #         # 订货金额（含税进价）
            #         dhje_hs = row.get('c_at_in')
            #         order_print_body.append(dhje_hs)
            #         #订货金额（不含税进价）
            #         dhje_bhs = row.get('c_aet_cost')
            #         order_print_body.append(dhje_bhs)
            #         #收货机构
            #         order_print_body.append(c_delivery_store_id)
            #         # 单据号
            #         order_print_body.append(c_id)
            #         # 供应商编码
            #         order_print_body.append(factorycode)
            #         # uuid
            #         # 下载时间
            #         # client_id
            #         HJF_order_print_body.append(order_print_body)
            #
            #
            # logging.info("合家福军民 订单长度：{}".format(len(HJF_order_note)))
            # result = order_result(HJF_order_note,HJF_order_details_header,HJF_order_details_body,HJF_order_print_header,HJF_order_print_body,factorycode,client_id)
            # logging.info("下载条数：{}".format(len(HJF_order_note)))
            # if not result:
            #     add_log(username, factorycode, client_id, "HJF", "订单", "入库意外失败", "错误")
            #
            # add_log(username, factorycode, client_id, "HJF", "订单",
            #         "本次下载共{}条".format(len(HJF_order_note)), "成功")
            # return True
        # except Exception as e:
            # logging.info("进货入库 下载失败：{}".format(e))
            # return False


if __name__ == '__main__':
    t = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logging.basicConfig(level=logging.INFO,
                        filemode="a",
                        filename=order_log+"{}.log".format(t),
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s', )



    systemname = "HJF"
    Status = "1"
    data_name = "Order"
    data_status = "1"
    username = "000003"
    password = '20110721'
    factorycode = "000003"
    client_id = ""
    # accounts = account_infos(systemname, Status, data_name, data_status, username, factorycode, client_id)
    # logging.info("奥乐奇 长度为：{}".format(len(accounts)))
    # moban_name = "订单"
    # for account in accounts:
    #     count = 0
    #     while True:
    #         count +=1
    #         logging.info("第{}次登录 奥乐奇".format(count))
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
    tongyong_class._login(username, password, factorycode, '')
    tongyong_class.moban_xiazai(username, password, factorycode, '')
"""
订单下载日期范围近7天。每天早上8点至20点每个小时执行一次。
退单下载日期范围近10天。每天早上8点晚上20点各执行一次。
验收单下载日期范围近10天。每天早上8点和晚上20点各执行一次。

0 8-20 * * * python3 /home/lsy/hejiafu/order.py 
0 08,20 * * * python3 /home/lsy/hejiafu/shouhuodan.py
0 08,20 * * * python3 /home/lsy/hejiafu/return.py

"""