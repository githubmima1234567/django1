# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunPipeline:
    def __init__(self):
        self.filename = open("sun.json","wb")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False,)+"\n"
        self.filename.write(content.encode("utf-8"))
        return item
    def close_spider(self):
        self.filename.close()