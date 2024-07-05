from typing import Any

import scrapy
from scrapy.http import Response
import json
import jsonpath
import time
# import chardet
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    # now_stamp = int(time.time())
    timestamp= str(int(time.time() * 1000))
    print(timestamp)
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp='
    timestamp = timestamp+'&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex='
    index = 1
    start_urls = [url+timestamp+str(index)+"&pageSize=10"]
    def parse(self, response: Response, **kwargs: Any) -> Any:
        # 把json格式的数据转换为python格式，data是列表

        item_list = json.loads(response.text)["Data"]["Posts"]
        print(item_list)
        # print(item_list)
        # print(type(item_list))
        for job in item_list:
            print(job)
            print(type(job))
            item = TencentItem()
            item["RecruitPostName"] = job["RecruitPostName"]
            item["CountryName"] = job["CountryName"]
            item["LocationName"] = job["LocationName"]
            item["BGName"] = job["BGName"]
            item["CategoryName"] = job["CategoryName"]
            item["Responsibility"] = job["Responsibility"]
            item["LastUpdateTime"] = job["LastUpdateTime"]
            item["RequireWorkYearsName"] = job["RequireWorkYearsName"]
            yield item
        if self.index < 286:
            self.index += 1
        yield scrapy.Request(self.url +self.timestamp+ str(self.index) + "&pageSize=10", callback=self.parse)
