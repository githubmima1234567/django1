from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from biedoule.items import BiedouleItem
class BiedoulespiderSpider(CrawlSpider):
    name = "biedoulespider"
    allowed_domains = ["biedoul.com"]
    start_urls = ["https://www.biedoul.com/wenzi/1"]
    pagelink = LinkExtractor(allow=(r"/wenzi/\d+"))
    rules = [
        Rule(pagelink,callback="biedoulparse",follow=True)
    ]

    def biedoulparse(self, response: Response, **kwargs: Any) -> Any:
        for each in response.xpath('//dl[contains(@id,"xh_")]'):
            item = BiedouleItem()
            item['title'] = each.xpath('./span/dd/a/strong/text()').extract()
            # print("**********************")
            # print(item['title'] )
            item['content'] = each.xpath('./dd/p/text()').extract()
            # print("**********************")
            # print(item['content'] )
            yield item










