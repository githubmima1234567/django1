from typing import Any
from zhenai.items import ZhenaiItem
import scrapy
from scrapy.http import Response


class ZhenaiSpider(scrapy.Spider):
    name = "zhenaispider"
    allowed_domains = ["zhenai.com","album.zhenai.com"]
    url = 'https://www.zhenai.com/zhenghun/wuhan/nan/'
    # url = "https://album.zhenai.com/u/1781372408"
    offset = 1
    start_urls = [url + str(offset)]

    def start_requests(self):

        cookies = "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # print(cookies)
        url = self.start_urls[0]
        yield scrapy.Request(
            url=url,
            cookies=cookies,
            callback=self.parse
            )


    def parse(self, response: Response, **kwargs: Any) -> Any:
        """
        构造url,
        """
        print(response.body.decode("utf-8"))
        cookies = "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        links = response.xpath('//div/div[@class="photo"]/a/@href').extract()
        print(links)
        for link in links:
            # print(link)
            yield  scrapy.Request(link,callback=self.parse_item,cookies=cookies)

        if self.offset <=4 :#100
            self.offset += 1
            # 发送请求放到请求队列里，调用self.parse处理response
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse,cookies=cookies)

    def parse_item(self, response: Response, **kwargs: Any) -> Any:
        print("===========" + response.url)
        print(response.text)
        print(response.body.decode("utf-8"))
        item = ZhenaiItem()
        item["username"] = self.get_username(response)
        # 年龄
        item["age"] = self.get_age(response)
        # ID
        item["zhenai_id"] = self.get_zhenai_id(response)
        # 头像图片的链接
        item["header_url"] = self.get_header_url(response)
        # 相册图片的链接
        item["images_url"] = self.get_images_url(response)
        # 内心独白
        item["content"] = self.get_content(response)
        # 个人资料
        item["personal_data"] = self.get_personal_data(response)
        # 兴趣爱好
        item["hobby"] = self.get_hobby(response)
        # 择偶条件
        item["m_select"] = self.get_m_select(response)
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        yield item
    def get_username(self,response):
        # print("get_username++++++++++++++++++++++++++++++==")
        # html = response.body.decode("utf-8")
        # print(html)
        username = response.xpath('//div[@class="name"]/h1/text()').extract()
        print(username)
        return username
    def get_age(self,response):
        age1 = response.xpath('//div[@class="des des_ip f-cl"]/text()').extract()
        print(age1)
        age = response.xpath('//div[@class="des des_ip f-cl"]/text()').extract().split('|')[1]
        return age
    def get_zhenai_id(self,response):
        zhenai_id = response.xpath('//div[@class="id id_ip"]/text()').extract().split(':')[1]
        return zhenai_id
    def get_header_url(self,response):
        header_url = response.xpath('//div[@class="top f-cl"]/div[@class="logo f-fl"]/@style[1]').extract().split('"')[1]
        return header_url
    def get_images_url(self,response):
        images_url = response.xpath('//div[@class="photoBox"]/div/@href').extract()
        return images_url
    def get_content(self,response):
        content = response.xpath('//div[@class="m-content-box m-des"]/span/text()').extract()
        return content
    def get_personal_data(self,response):
        personal_data = response.xpath('//div[@class="m-content-box"]/div[@class="purple-btns"]/div[@class="m-btn purple"]/text()').extract()
        return personal_data
    def get_hobby(self,response):
        hobby = response.xpath('//div[@class="item f-fl"]').extract()
        return hobby
    def get_m_select(self,response):
        m_select = response.xpath('//div[@class="m-btn"]').extract()
        return m_select


