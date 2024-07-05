import json
from typing import Any

import scrapy
from scrapy.http import Response

from douyu.items import DouyuItem

class DouyumeinvSpider(scrapy.Spider):
    name = "douyumeinv"
    allowed_domains = ["douyu.com"]
    start_urls = ["https://www.douyu.com/japi/weblist/apinc/recLabelList"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        # html = response.text
        # print(html)
        content_list = json.loads(response.text)["data"]["list"]
        for content in content_list:
            # print(content)
            item = DouyuItem()
            item["nn"] = content["room"]["nn"]
            item["imageLink"] = content["room"]["avatar"]
            yield item