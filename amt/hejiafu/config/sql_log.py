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


def save_log(account_log):
    connection = SQL_SERVERS().conn(**DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            import datetime
            download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
            insert_sql = "insert into {} (client_id,systemname,username,factorycode,log_type,data_type,monitor_type,log_summary,download_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)".format("dbo.amt_log")

            cursor.execute(insert_sql, (account_log[0],account_log[1],account_log[2],account_log[3],account_log[4],account_log[5],account_log[6],account_log[7], download_time))


        connection.commit()
        logging.info("保存数据成功。")
        return True
    except Exception as e:
        logging.warning("保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()



def add_log(username,systemname,client_id,BusinessApp,BusinessType,BusinessData,CreateUserId):
    try:
        url = "http://amtlog.amt-data.cn:8057/Log/AddLog"
        import datetime
        download_time = datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S.%f')
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "App": "前端采集",
            "BusinessApp": BusinessApp,
            "ProgramApp": "Saas",
            "LogType": "BusinessLog",
            "ChainId": "",
            "ParentChainId": "",
            "BusinessType": BusinessType,
            "BusinessId1": client_id,
            "BusinessId2": username,
            "BusinessId3": systemname,
            "BusinessDateTime": download_time,
            "BusinessData": BusinessData,
            "CreateTime": download_time,
            "CreateUserId": CreateUserId,
            "CreateUserName": "l",
        }
        web = requests.post(url, data=json.dumps(data), headers=headers, timeout=20).json()
        if web['isSuccess'] is True:
            logging.info("日志保存成功")
        else:
            logging.info("日志保存失败")
    except Exception as e:
        logging.info("日志保存失败: {}".format(e))


if __name__ == '__main__':
    a = ["xtl","huarun","121762481112","1762481112","错误","网站登录","T","aaa"]
    save_log(a)
