# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import base64

from scrapy import signals
import random
from .settings import USER_AGENTS
from .settings import PROXIES

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

#随机的User-Agent
class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        print(useragent)
        request.headers.setdefault("User-Agent",useragent)
        # return None

class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        print(proxy)

        if proxy["user_passwd"] is None:
            request.meta['proxy']= "http://" + proxy['ip_port']
        else:
            base64_userpasswd = base64.b64encode(proxy['user_passwd'].encode('utf-8'))
            request.headers['Proxy-Authorization'] = 'Basic' + base64_userpasswd.decode('utf-8')
            request.meta['proxy'] = "http://" + proxy['ip_port']

