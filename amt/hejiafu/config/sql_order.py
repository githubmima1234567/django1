# -*- coding:utf-8 -*-
import logging
import time

from config.Sql_servers import SQL_SERVERS
from config.settings import (NEW_DAEUNFA_SQL,ORDER_NOTE_TABLE,ORDER_HEADER_TABLE,ORDER_BODY_TABLE,
                                     ORDER_PRINT_HEADER_TABLE,ORDER_PRINT_BODY_TABLE,SWJSYSD_TABLE,SWJSYSD_HEADER_TABLE,
                                     SWJSYSD_BODY_TABLE,YJSYSD_TABLE,YJSYSD_HEADER_TABLE,YJSYSD_BODY_TABLE,RETURN_TABLE,
                                     RETURN_HEADER_TABLE,RETURN_BODY_TABLE,RETURN_PRINT_HEADER_TABLE,RETURN_PRINT_BODY_TABLE)


import datetime

def order_result(HJF_order_note,HJF_order_details_header,HJF_order_details_body,HJF_order_print_header,HJF_order_print_body, factorycode,client_id):
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    if not connection:
        return False
    try:
        with connection.cursor() as cursor:

            uuid = str(int(time.time() * 1000))
            if HJF_order_note:

                for account in HJF_order_note:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = "insert into {} (c_sort,c_id,c_delivery_store_id,c_delivery_store_sname,c_delivery_type,yueku_type,"\
                                            "jsfq,queren_statu,c_rec_status,yuyue,c_at_order,dayin_status,ddfkd,ddfkdh,"\
                                            "yyshsj,qwshrq,qxrq,lrsj,c_rec_au_dt,c_note,uuid,retailer_id,download_time,factorycode) values("\
                                         " ?, ?, ?, ?, ?, ?, ?, ?, ?," \
                                                 " ?, ?, ?, ?, ?,?, ?, ?, ?, ?," \
                                         " ?, ?, ?, ?, ?)".format(ORDER_NOTE_TABLE) #24
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9],account[10],account[11],account[12],
                    account[13],account[14],account[15],account[16],account[17],account[18],account[19],
                    uuid,client_id,download_time,account[20]))

            if HJF_order_details_header:

                for account in HJF_order_details_header:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = "insert into {} (c_id,mdfd,wlms,ykmx,spbm,ddlx,cglx,o_dhr,o_dhrq,jglx,shck,"\
                                "shr,r_dhrq,ht,lxcz,qxrq,dhcz,dhdh,lxdh,lxr,pszxck,yyzt,"\
                                "yysj,dyzt,lrr,lrsj,yydh,qrzt,checker,shsj,shdz,bz,factorycode,"\
                                "uuid,retailer_id,download_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?,?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?)".format(
                        ORDER_HEADER_TABLE) #36
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],account[9],account[10],account[11],account[12],
                    account[13],account[14],account[15],account[16],account[17],account[18],
                    account[19],account[20],account[21],account[22],account[23],account[24],account[25],account[26],account[27],account[28],
                    account[29],account[30],account[31],account[32],uuid,client_id,download_time))
            if HJF_order_details_body:

                for account in HJF_order_details_body:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = "insert into {} (xuhao,spbm,ztm,spmc,dhsl,dhbzl,dhzpsl,zpbzl,dw,gg,dtm,scrq,"\
                                            "htjh,jhjg,jsjg,jxsl,bzhl,zj,o_dhje,dhje,bz,djh,mdfd,factorycode,"\
                                            "uuid,retailer_id,download_time) values(?, ?, ?, ?, ?,?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?, ?, ?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?, ?, ?, ?)".format(
                        ORDER_BODY_TABLE) #27
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9], account[10], account[11],account[12],account[13],account[14],account[15],account[16],account[17],account[18],
                    account[19],account[20],account[21],account[22],account[23],uuid,client_id,download_time))
            if HJF_order_print_header:

                for account in HJF_order_print_header:
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = "insert into {} (shjg,shjgmc,djh,o_dhrq,spbm,wlms,r_dhrq,gys,gysmc,ht,qxrq,"\
                            "lxr,lxdh,hjdhsl,hjdhjs,hjdhje,shr,zdr,factorycode,uuid,retailer_id,download_time) values(?,"\
                                 " ?, ?, ?,?, ?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?, ?, ?, ?, ?,?, ?," \
                                 " ?, ?)".format(
                        ORDER_PRINT_HEADER_TABLE)#22
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],account[9],account[10],account[11],account[12],
                    account[13],account[14],account[15],account[16],account[17],account[18],uuid,client_id,download_time))
            if HJF_order_print_body:

                for account in HJF_order_print_body:
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (spbm,tm,spmc,gg,bzhl,lsj,jhdw,dhsl,dhjs,dhjg,dhje_hs,dhje_bhs,shjg,c_id,factorycode,"\
                                  "uuid,retailer_id,download_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"\
                                 "?, ?, ?, ?, ?, ?, ?, ?)".format(
                        ORDER_PRINT_BODY_TABLE))
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],account[9],account[10],account[11],account[12],
                    account[13],uuid,factorycode, download_time,"1006"))
        connection.commit()
        logging.info("订单 保存数据成功。")
        return True
    except Exception as e:
        logging.warning("订单 保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()

def return_result(HJF_return_note,HJF_return_details_header,HJF_return_details_body,HJF_return_printheader,HJF_return_printbody,factorycode,client_id):
    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    if not connection:
        return False
    try:
        with connection.cursor() as cursor:

            uuid = str(int(time.time() * 1000))
            if HJF_return_note:

                for account in HJF_return_note:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (serial_number, order_number, return_institution, return_institution_name, "
                                  "return_department, return_amount, purchase_type, confirm_status, print_status, auditor, "
                                  "audit_time, entry_person, entry_time, remarks, supplier_code, uuid, client_id, "
                                  "download_time) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(RETURN_TABLE))
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9],account[10],account[11],account[12],
                    account[13],factorycode,uuid,client_id,download_time))

            if HJF_return_details_header:

                for account in HJF_return_details_header:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (order_number,return_institution,return_institution_name,contract,"
                                  "return_amount,purchase_method,logistics_method,audit_date,return_reason,"
                                  "supplier_code,uuid,client_id,download_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"\
                                 " ?, ?, ?)".format(
                        RETURN_HEADER_TABLE))
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],factorycode,uuid,client_id,download_time))
            if HJF_return_details_body:

                for account in HJF_return_details_body:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (serial_number,main_barcode,goods_name,specification,unit,"
                                  "application_quantity,application_gift_quantity,actual_return_quantity,"
                                  "actual_return_gift_quantity,settlement_price,return_amount,order_number,"
                                  "return_institution,supplier_code,uuid,client_id,download_time) "
                                  "values(?, ?, ?, ?, ?,?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?)".format(
                        RETURN_BODY_TABLE))
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9], account[10], account[11],account[12],factorycode,uuid,client_id,download_time))
            if HJF_return_printheader:

                for account in HJF_return_printheader:
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (supplier_code,return_order_number,supplier_name,branch_name_code,"
                                  "branch_name,settlement_method,total_amount,contract_number,return_date,"
                                  "remarks,supplier_id,uuid,client_id,download_time) values(?,"\
                                 " ?, ?, ?,?, ?, ?, ?, ?, ?," \
                                 " ?, ?, ?, ?)".format(
                        RETURN_PRINT_HEADER_TABLE))
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],account[9],factorycode,uuid,client_id,download_time))
            if HJF_return_printbody:

                for account in HJF_return_printbody:
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (goods_code,goods_barcode,goods_name,specification,unit,"
                                  "tax_rate,return_quantity,purchase_price_including_tax,return_amount_including_tax,"
                                  "supplier_code,return_order_number,branch_name_code,supplier_id,uuid,"
                                  "client_id,download_time) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"\
                                 "?, ?, ?, ?, ?, ?)".format(
                        RETURN_PRINT_BODY_TABLE))
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6],
                    account[7], account[8],account[9],account[10],account[11],factorycode,uuid,client_id,download_time))
        connection.commit()
        logging.info("退单 保存数据成功。")
        return True
    except Exception as e:
        logging.warning("退单 保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()
def yanshoudan_result(HJF_swjsysd_note, HJF_swjsysd_detail_header, HJF_swjsysd_detail_body, HJF_yjsysd_list,
                          HJF_yjsysd_detail_header, HJF_yjsysd_detail_body, client_id, factorycode):

    connection = SQL_SERVERS().conn(**NEW_DAEUNFA_SQL)
    if not connection:
        return False
    try:
        with connection.cursor() as cursor:
            uuid = str(int(time.time() * 1000))
            if HJF_swjsysd_note:

                for account in HJF_swjsysd_note:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (c_sort,c_id, c_delivery_store_id, c_delivery_store_sname, c_delivery_type, yueku_type, "
                                  "c_rec_status, dyzt, c_at_order, c_at_in, c_a_in, se, scdd, ddfkd, ddfkdh, c_rec_au_dt, "
                                  "c_note, factorycode, uuid, client_id, download_time) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(SWJSYSD_TABLE))
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9],account[10],account[11],account[12],
                    account[13],account[14],account[15],account[16],factorycode,uuid,client_id,download_time))
                    # print(insert_sql)
            if HJF_swjsysd_detail_header:

                for account in HJF_swjsysd_detail_header:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (c_id,department_code, destination_institution_code, destination_institution_name,"
                                  " receiving_warehouse, inspector, receiving_sequence, receiving_institution, purchase_type, "
                                  "contact_person, orderer, supplier, contract, phone_number, inspection_entry, inspection_time,"
                                  " inspection_audit, inspection_audit_time, entry_time, c_check_userno, print_status,"
                                  " other_items, remarks, supplier_code, client_id, download_time, uuid) "
                                  "values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(SWJSYSD_HEADER_TABLE))
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],account[9],account[10],account[11],account[12],
                    account[13],account[14],account[15],account[16],account[17],account[18],
                    account[19],account[20],account[21],account[22],factorycode,client_id, download_time, uuid))
            if HJF_swjsysd_detail_body:

                for account in HJF_swjsysd_detail_body:
                    # print(account)
                    download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                    insert_sql = ("insert into {} (goods_code, goods_name, main_barcode, specification, unit, dhsl, "
                                  "gift_order_quantity, order_total_quantity, receiving_quantity, receiving_quantity_gift, "
                                  "packaging_content, tax_rate, settlement_tax_rate, purchase_price_in_tax, "
                                  "settlement_price_in_tax, purchase_amount_in_tax, set_price_amount_in_tax, "
                                  "bhsze, tax_amount, document_number, destination_institution_code, supplier_code,"
                                  " uuid, client_id, download_time) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(
                        SWJSYSD_BODY_TABLE))
                    # print(insert_sql)
                    cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7], account[8],
                    account[9], account[10], account[11],account[12],account[13],account[14],account[15],account[16],account[17],account[18],
                    account[19],account[20],factorycode, uuid,client_id,download_time))
        if HJF_yjsysd_list:

            for account in HJF_yjsysd_list:
                download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                insert_sql = ("insert into {} (serial_number, order_number, branch_code, branch_name, logistics_mode, cross_dock_type, "
                              "document_status, print_status, purchase_price_total, settlement_price_total_tax, total_excluding_tax, "
                              "tax_amount, settlement_zone, receiving_audit_time, remarks, supplier_code, uuid, client_id,"
                              " download_time) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(
                    YJSYSD_TABLE))
                cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7],
                    account[8],
                    account[9], account[10], account[11], account[12],
                    account[13], account[14],factorycode,uuid, client_id,download_time))
        if HJF_yjsysd_detail_header:

            for account in HJF_yjsysd_detail_header:
                # print(account)
                download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                insert_sql = ("insert into {} (document_number, department_code, destination_institution_code, "
                              "destination_institution_name, receiving_warehouse, inspector, receiving_sequence_number, "
                              "receiving_institution, purchase_type, contact_person, order_person, supplier, "
                              "contract,phone,inspection_entry, inspection_time, inspection_audit, inspection_audit_time, "
                              "entry_time, second_inspection, print_status, other_items, remarks, "
                              "supplier_code, uuid,client_id, download_time) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(
                    YJSYSD_HEADER_TABLE))
                # print(insert_sql)
                cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7],
                    account[8], account[9], account[10], account[11], account[12],
                    account[13], account[14], account[15], account[16], account[17], account[18],
                    account[19], account[20], account[21], account[22],
                    factorycode,uuid,client_id,download_time))
        if HJF_yjsysd_detail_body:

            for account in HJF_yjsysd_detail_body:
                download_time = datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
                insert_sql = ("insert into {} (goods_code, goods_name, main_barcode, specification,unit,order_quantity,"
                              " gift_order_quantity, total_order_quantity, receiving_quantity, receiving_gift_quantity,"
                              " packaging_content, tax_rate, settlement_tax_rate, purchase_price_including_tax,"
                              " settlement_price_including_tax, purchase_amount_including_tax,"
                              "settlement_price_amount_including_tax,bhsze,tax_amount, document_number, "
                              "destination_institution_code,supplier_code,uuid,client_id, download_time)"
                              " values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(YJSYSD_BODY_TABLE))
                # print(insert_sql)
                cursor.execute(insert_sql, (
                    account[0], account[1], account[2], account[3], account[4], account[5], account[6], account[7],
                    account[8], account[9], account[10], account[11], account[12], account[13], account[14], account[15],
                    account[16], account[17], account[18],account[19], account[20],factorycode,uuid,client_id, download_time))

        connection.commit()
        logging.info("验收单 保存数据成功。")
        return True
    except Exception as e:
        logging.warning("验收单 保存数据失败,message:[{}]".format(e))
        return False
    finally:
        connection.close()




"""
INSERT INTO cass_db_aldi.dbo.aldi_order_body_print_body

VALUES('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '');

"""


if __name__ == '__main__':
    pass
