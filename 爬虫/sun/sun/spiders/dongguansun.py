from typing import Any

import scrapy
from scrapy.http import Response
from sun.items import SunItem

class DongguansunSpider(scrapy.Spider):
    name = "dongguansun"
    allowed_domains = ["wz.sun0769.com"]
    url = 'https://wz.sun0769.com/political/index/politicsNewest?id=1&page='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        links = response.xpath('//ul[@class="title-state-ul"]/li/span/a[@class="color-hover"]/@href').extract()
        print(links)
        for link in links:
            link = 'https://wz.sun0769.com'+link
            print(link)
            yield  scrapy.Request(link,callback=self.parse_item)

        if self.offset <=50 :#100
            self.offset += 1
            # 发送请求放到请求队列里，调用self.parse处理response
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response: Response, **kwargs: Any) -> Any:
        item = SunItem()
        item["title"] = response.xpath('//div/p[@class="focus-details"]/text()').extract()[0]
        a= response.xpath('//span[@class="fl"][4]/text()').extract()[0] #编号：454368
        item['number'] = a.split("：")[-1]
        print(item['number'])
        i = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]
        item["content"] = i.replace('\r','').replace('\n','')
        yield item

