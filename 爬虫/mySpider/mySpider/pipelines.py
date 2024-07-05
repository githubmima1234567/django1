# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ItcastPipeline(object):
    #可选，作为类的初始化方法
    def __init__(self):
        #创建一个文件
        self.filename = open("teacher.json","wb")

       #必须写的，用来处理item数据
    def process_item(self,item, spider):
        #实现python类型转化为json字符串，返回一个str对象 把一个Python对象编码转换成Json字符串
        jsontext = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.filename.write(jsontext.encode("utf-8"))
        return item
        #可选，结束时调用这个方法
    def close_spider(self,spider):
        self.filename.close()