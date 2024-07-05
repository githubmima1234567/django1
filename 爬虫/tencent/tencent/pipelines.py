# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
# from scrapy.conf import settings
import pymongo
from scrapy.utils.project import  get_project_settings
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import configparser
# config = configparser.ConfigParser()
class TencentPipeline(object):
    """
    mongodb中如果没有该数据库，会自动创建
    获取settings配置的数据库信息
    """
    def __init__(self):
        host = get_project_settings().get('MONGODB_HOST')
        # host = settings['MONGODB_HOST']
        port = get_project_settings().get("MONGODB_PORT")
        dbname = get_project_settings().get("MONGODB_DBNAME")
        sheetname = get_project_settings().get("MONGODB_SHEETNAME")

        #创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的集合名称
        self.sheet = mydb[sheetname]

        # self.filename = open("tencent.json","wb")
    def process_item(self, item, spider):
        # jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.filename.write(jsontext.encode("utf-8"))
        data = dict(item)
        self.sheet.insert_many([data])
        return item
    # def close_spider(self,spider):
    #     self.filename.close()
