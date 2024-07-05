# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
import codecs
class SinaPipeline:
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrls[7:-6].replace('/','_')
        filename += ".txt"

        fp = codecs.open(item['subFilename']+'/'+filename, 'wb',encoding="utf-8")
        fp.write(item['content'])
        fp.close()

        return item