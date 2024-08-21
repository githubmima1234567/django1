import json
import logging
import time
import pymssql

import requests

from config.settings import DAEUNFA_SQL


class SQL_SERVERS(object):
    def __init__(self):
        self.logger = logging.getLogger('Sql_Servers')

    def conn(self, **kwargs):
        while True:
            try:

                connection = pymssql.connect(host=kwargs['host'],
                                             port=kwargs['port'],
                                             user=kwargs['user'],
                                             password=kwargs['password'],
                                             database=kwargs['db'],
                                             charset=kwargs['charset'],
                                             )
                return connection
            except Exception as e:
                self.logger.error("链接sql_server出错,kwargs:{},error_msg:{}".format(kwargs, e))
                time.sleep(3)
                continue


def save_result(account_note, account_detail):
    connection = SQL_SERVERS().conn(**DAEUNFA_SQL)
    supplier_name = account_note['factorycode'] + " " + account_note['supplier']
    pay_date = account_note['pay_data']
    bank_acc = account_note['bank_acc']
    pay_type = account_note['pay_type']
    sum_amount = account_note['sum_amount']
    account_date = account_note['account_data']
    supplier_id = account_note['factorycode']
    try:
        with connection.cursor() as cursor:
            import datetime
            download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
            insert_sql = "insert into {} (supplier_name, pay_date, bank_acc,pay_type,sum_amount,account_date,download_time,retailer_id,supplier_id) values(%s, %s, %s, %s, %s,%s,%s,%s,%s)".format(
                ACCOUNT_NOTE)

            cursor.execute(insert_sql, (
                supplier_name, pay_date, bank_acc, pay_type, sum_amount, account_date, download_time, "1005",
                supplier_id))
        connection.commit()
        logging.info("保存数据成功。")
        return True
    except Exception as e:
        logging.warning("保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()


def ip_select():
    connection = SQL_SERVERS().conn(**DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            select_sql = "select * FROM dbo.amt_proxy_ip ORDER BY amt_proxy_ip.update_time DESC"
            cursor.execute(select_sql)
            ruslts = cursor.fetchone()
        connection.commit()
        logging.info("查询数据成功。")
        return ruslts
    except Exception as e:
        logging.warning("查询数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()


def get_proxy_sql():
    while True:
        try:
            proxys = ip_select()
            ip = proxys[0] + ":" + proxys[1]
            proxies = {
                "http": "socks5h://" + ip,
                "https": "socks5h://" + ip,
            }
            logging.info(proxies)
            return proxies
        except Exception as e:
            logging.info("代理拿不到")
            time.sleep(5)


if __name__ == '__main__':
    get_proxy_sql()
