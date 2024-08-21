# 联众打吗平台
import json
import logging
import time

import requests


RECOGNIZE_USERNAME = "AmtData"  # 打码用户名
RECOGNIZE_PASSWORD = "Amt@2020"

TOKEB = "281611d85d7c9b4e2077fac883b9e6b5"  # 打码用户名

DAEUNFA_SQL = {
    'host': 'rm-uf6x86bp5vnl4fg336o.sqlserver.rds.aliyuncs.com',
    'port': 3433,
    'user': 'amt',
    'password': 'Amt2017@',
    'db': 'cass_db_yf',
    'charset': 'utf8'
}


# NEW_DAEUNFA_SQL = {
#     'host': 'rm-uf6rmw924l4fpab0txo.sqlserver.rds.aliyuncs.com,1433',
#     'port': 1433,
#     'user': 'amt',
#     'password': 'Amt@2020',
#     'db': 'cass_db_HJF',
#     'charset': 'utf8'
# }

NEW_DAEUNFA_SQL = {
    'DRIVER':'{SQL Server};',
    'SERVER': 'rm-uf6rmw924l4fpab0txo.sqlserver.rds.aliyuncs.com,1433;',
    'UID': 'amt;',
    'PWD': 'Amt@2020;',
    'DATABASE': 'cass_db_HJF;',
}



ACCOUNT_TABLE = "dbo.account_info"

DIAOBA_TABLE = "dbo.cxzy_diaobo_note"
SELL_TABLE = "dbo.cxzy_sell_note"
KUCUN_TABLE = "dbo.cxzy_inventory_note"
JINHUO_RUKU_TABLE = "dbo.cxzy_jinhuo_ruku_note"


ORDER_NOTE_TABLE = "dbo.HJF_order_list"
ORDER_HEADER_TABLE = "dbo.HJF_order_detail_header"
ORDER_BODY_TABLE = "dbo.HJF_order_detail_body"
ORDER_PRINT_HEADER_TABLE = "dbo.HJF_order_print_header"
ORDER_PRINT_BODY_TABLE = "dbo.HJF_order_print_body"

SWJSYSD_TABLE = "dbo.HJF_swjsysd_list"
SWJSYSD_HEADER_TABLE = "dbo.HJF_swjsysd_detail_header"
SWJSYSD_BODY_TABLE = "dbo.HJF_swjsysd_detail_body"
YJSYSD_TABLE = "dbo.HJF_yjsysd_list"
YJSYSD_HEADER_TABLE = "dbo.HJF_yjsysd_detail_header"
YJSYSD_BODY_TABLE = "dbo.HJF_yjsysd_detail_body"

RETURN_TABLE = "dbo.HJF_return_list"
RETURN_HEADER_TABLE = "dbo.HJF_return_details_header"
RETURN_BODY_TABLE = "dbo.HJF_return_details_body"
RETURN_PRINT_HEADER_TABLE = "dbo.HJF_return_print_header"
RETURN_PRINT_BODY_TABLE = "dbo.HJF_return_print_body"


