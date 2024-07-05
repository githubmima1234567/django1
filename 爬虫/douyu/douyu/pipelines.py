# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import  get_project_settings
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):
    #获取settings文件里设置的图片位置变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        # for images_url in item["imageLink"]:
        images_url = item["imageLink"]
        # print(images_url)
        yield scrapy.Request(images_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        # print(image_path)
        # python是跨平台的。在Windows上，文件的路径分隔符是'\'，在Linux上是'/'。
        # 为了让代码在不同的平台上都能运行，那么路径应该写'\'还是'/'呢？
        # 使用os.sep的话，就不用考虑这个了，os.sep根据你所处的平台，自动采用相应的分隔符号
        # old_name = self.IMAGES_STORE + os.sep +image_path[0]
        # new_name = self.IMAGES_STORE +os.sep + image_path[0].split(os.sep)[0]+os.sep+item["rn"]+'.jpg'
        os.rename(self.IMAGES_STORE +"\\" + image_path[0],self.IMAGES_STORE + "\\" + item["nn"] +".jpg")
        # os.rename(old_name,new_name)
        # item["imagePath"] =new_name
        item["imagePath"] = self.IMAGES_STORE + "\\" + item["nn"] + ".jpg"
        # self.IMAGES_STORE + "/" + item["rn"]
        return item