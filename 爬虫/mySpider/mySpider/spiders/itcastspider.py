from typing import Any

import scrapy
from scrapy.http import Response
from mySpider.items import ItcastItem


#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    name = "itcast"
    #允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    start_urls = ["https://www.itheima.com/teacher.html#"]
    def parse(self, response: Response, **kwargs: Any) -> Any:
        # with open("teather.html",'wb') as f:
        #     f.write(response.body)
        response_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []
        #遍历根节点集合
        for each in response_list:
            #name,extract()将匹配出来的结果转换为Unicode字符串
            #不加extract()结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()
            item = ItcastItem()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item
            # teacherItem.append(item)
            # print(item)
        # return teacherItem