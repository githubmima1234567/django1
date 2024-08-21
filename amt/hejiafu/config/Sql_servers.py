import logging
import time
import pymssql
import pyodbc
from config.settings import NEW_DAEUNFA_SQL


class SQL_SERVERS(object):
    def __init__(self):
        self.logger = logging.getLogger('Sql_Servers')

    def conn(self, **kwargs):
        ct = 0
        while True:
            ct += 1
            if ct == 10:
                return False
            try:
                connection = pyodbc.connect(DRIVER=kwargs['DRIVER'],
                                            SERVER=kwargs['SERVER'],
                                            DATABASE=kwargs['DATABASE'],
                                            UID=kwargs['UID'],
                                            PWD=kwargs['PWD'],
                                            )

                # connection = pymssql.connect(host=kwargs['host'],
                #                              port=kwargs['port'],
                #                              user=kwargs['user'],
                #                              password=kwargs['password'],
                #                              database=kwargs['db'],
                #                              charset=kwargs['charset'],
                #                              )
                return connection
            except Exception as e:
                self.logger.error("链接sql_server出错,kwargs:{},error_msg:{}".format(kwargs, e))
                time.sleep(3)
                continue



def select_order():
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            select_sql = "select enterprise_id,username,password,factorycode,client_id,tax_rate from dbo.account_info_one where systemname =  'suguo'  and Status = '1' and [Order] = '1'"

            cursor.execute(select_sql)
            ruslts = cursor.fetchall()
        connection.commit()
        logging.info("查询订单数据成功。")
        return ruslts
    except Exception as e:
        logging.warning("查询订单数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()

def select_kucun_xiaoshou():
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            select_sql = "select enterprise_id,username,password,factorycode,client_id,tax_rate from dbo.account_info_one where systemname =  'suguo'  and Status = '1' and Sales = '1' "
            cursor.execute(select_sql)
            ruslts = cursor.fetchall()
        connection.commit()
        logging.info("查询库存销售数据成功。")
        return ruslts
    except Exception as e:
        logging.warning("查询库存销售数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()

def select_qita():
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            select_sql = "select enterprise_id,username,password,factorycode,client_id,tax_rate from dbo.account_info_one where systemname =  'suguo'  and Status = '1' and Other = '1'"
            cursor.execute(select_sql)
            ruslts = cursor.fetchall()
        connection.commit()
        logging.info("查询库存销售数据成功。")
        return ruslts
    except Exception as e:
        logging.warning("查询库存销售数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()

def select_tuihuodan():
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    try:
        with connection.cursor() as cursor:
            select_sql = "select enterprise_id,username,password,factorycode,client_id,tax_rate from dbo.account_info_one where systemname =  'suguo'  and Status = '1' and [Return] = '1' and client_id = 'KA21041300161'"
            cursor.execute(select_sql)
            ruslts = cursor.fetchall()
        connection.commit()
        logging.info("查询库存销售数据成功。")
        return ruslts
    except Exception as e:
        logging.warning("查询库存销售数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()

def create_rukudan():
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    try:
        with (connection.cursor() as cursor):
            create_sql ="select enterprise_id,username,password,factorycode,client_id,tax_rate from dbo.account_info_one where systemname =  'suguo'  and Status = '1' and Receive = '1'"
            cursor.execute(create_sql)
            ruslts = cursor.fetchall()
        connection.commit()
        logging.info("新增入库单表成功。")
        return ruslts
    except Exception as e:
        logging.warning("新增入库单表失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()




if __name__ == '__main__':
    pass
