import json
import logging
import time
import pymssql

import requests

DAEUNFA_SQL = {
    'host': '101.132.15.241',
    'port': 3433,
    'user': 'amt',
    'password': 'Amt2017@',
    'db': 'cass_db_yf',
    'charset': 'utf8'
}

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


def save_result(ip, port):
    connection = SQL_SERVERS().conn(**DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            import datetime
            download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
            insert_sql = "insert into dbo.amt_proxy_ip (ip, port, update_time) values(%s, %s, %s)"
            cursor.execute(insert_sql, (ip, port, download_time))
        connection.commit()
        logging.info("保存数据成功。")
        return True
    except Exception as e:
        logging.warning("保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()


def get_proxy():
    i = 0
    while True:
        try:
            i += 1
            if i == 4:
                logging.info("代理拿不到")
                return False
            url = 'http://webapi.http.zhimacangku.com/getip_3h?num=1&type=2&pro=&city=0&yys=100017&port=2&time=3&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions='
            proxys = requests.get(url, timeout=10)
            proxys_dict = json.loads(proxys.text)
            if not proxys_dict:
                continue
            proxys = proxys_dict["data"][0]
            ip = proxys["ip"]
            prot = proxys["port"]
            logging.info("ip: {},port: {}".format(ip, prot))
            save_result(ip, prot)
            return True
        except Exception as e:
            logging.info("代理拿不到:{}".format(e))
            time.sleep(5)


if __name__ == '__main__':
    get_proxy()
