# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZhenaiPipeline:
    def process_item(self, item, spider):
        data = json.dumps(dict(item),ensure_ascii=False)
        with open("zhenai.json","wb") as f:
            f.write(data.encode("utf-8"))
        return item
