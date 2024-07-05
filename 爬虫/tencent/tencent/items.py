# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    RecruitPostName = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    BGName = scrapy.Field()
    CategoryName = scrapy.Field()
    Responsibility = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    RequireWorkYearsName = scrapy.Field()



