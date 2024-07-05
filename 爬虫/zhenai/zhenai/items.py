# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhenaiItem(scrapy.Item):
    #用户名
    username = scrapy.Field()
    #年龄
    age = scrapy.Field()
    #ID
    zhenai_id = scrapy.Field()
    #头像图片的链接
    header_url = scrapy.Field()
    #相册图片的链接
    images_url= scrapy.Field()
    #内心独白
    content = scrapy.Field()
    #个人资料
    personal_data =scrapy.Field()
    #兴趣爱好
    hobby = scrapy.Field()
    #择偶条件
    m_select = scrapy.Field()


