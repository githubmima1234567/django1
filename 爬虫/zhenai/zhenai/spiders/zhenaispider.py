from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhenai.items import ZhenaiItem

class ZhenaispiderSpider(CrawlSpider):
    name = "zhenaispider"
    allowed_domains = ["zhenai.com","album.zhenai.com"]
    start_urls = ["https://www.zhenai.com/zhenghun/wuhan/nan",]
    # "https://www.zhenai.com/zhenghun/wuhan/nan",
    #第一级匹配规则：武汉男性的每一页链接匹配规则,如果callback为None，follow 默认设置为True ，否则默认为False。
    page_links = LinkExtractor(allow=(r"zhenai.com/zhenghun/wuhan/nan/\d+"))
    # #第二级匹配规则：每个男性个人主页的匹配规则,profile：个人简介
    profile_links = LinkExtractor(allow=(r"album.zhenai.com/u/\d+"))
    rules = (
        Rule(page_links,),
        Rule(profile_links, callback="parse_item"),
    )

    def start_requests(self):
        cookies = "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        print(cookies)
        url = self.start_urls[0]
        yield scrapy.Request(
            url=url,
            cookies=cookies,
            )

    def parse_item(self, response):
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
#     def get_username(self,response):
#         # print("get_username++++++++++++++++++++++++++++++==")
#         # html = response.body.decode("utf-8")
#         # print(html)
#         username = response.xpath('//div[@class="name"]/h1/text()').extract()
#         print(username)
#         return username
#     def get_age(self,response):
#         age1 = response.xpath('//div[@class="des des_ip f-cl"]/text()').extract()
#         print(age1)
#         age = response.xpath('//div[@class="des des_ip f-cl"]/text()').extract().split('|')[1]
#
#         return age
#     def get_zhenai_id(self,response):
#         zhenai_id = response.xpath('//div[@class="id id_ip"]/text()').extract().split(':')[1]
#         return zhenai_id
#     def get_header_url(self,response):
#         header_url = response.xpath('//div[@class="top f-cl"]/div[@class="logo f-fl"]/@style[1]').extract().split('"')[1]
#         return header_url
#     def get_images_url(self,response):
#         images_url = response.xpath('//div[@class="photoBox"]/div/@href').extract()
#         return images_url
#     def get_content(self,response):
#         content = response.xpath('//div[@class="m-content-box m-des"]/span/text()').extract()
#         return content
#     def get_personal_data(self,response):
#         personal_data = response.xpath('//div[@class="m-content-box"]/div[@class="purple-btns"]/div[@class="m-btn purple"]/text()').extract()
#         return personal_data
#     def get_hobby(self,response):
#         hobby = response.xpath('//div[@class="item f-fl"]').extract()
#         return hobby
#     def get_m_select(self,response):
#         m_select = response.xpath('//div[@class="m-btn"]').extract()
#         return m_select

#
# https://album.zhenai.com/api/profile/getObjectProfile.do?
# objectID=1712139573
# &_=1715726196302&
# ua=h5%2F1.0.0%2F1%2F0%2F0%2F0%2F0%2F0%2F%2F0%2F0%2Fe4b4cc3b-b31a-47c3-abfc-a735d0e2f558%2F0%2F0%2F365986633&data=eyJ2IjoiSEJOTWgrMTM3Ym9qMkJQL0NaZS93Zz09Iiwib3MiOiJ3ZWIiLCJpdCI6MzE1LCJ0IjoicnNhK0RhUSs1eHl6aG5YNGdlYVVyQWVBRVpuaDlISTlNeTRGSEJkSVprU2wvY0pJQlNackUzZzB1WlVxOW8yNEZVL0tZMkVnL0l1OUw4ZXlkQy9TaFE9PSJ9&
# MmEwMD=5aeu6TVsV_UqOWdeEAM0nsh3lZTptitR.TpfoeYoSu3F_.VvGHPiM06S82luhkoaOGipq6NxMfp.r1rqISx0vPtH9PgeauxeDqNCCL28HETPv52YxKDnjQlLURheNTLvgU1qONs8hEy60kXXtQP8NyiXubHIW0aWFGJP5UFjmp32q3c_3YE.E6TFvQhclwSdpDyqJJgO4SaQhqaqh49K2R2v3IQyINvOPY2zxTN9l8hbgRK4FToTFYPgXuCu7vPieaxKPw9hz8sstkXgRcD4wgx5557hlZ.4X._G46pI70x1C7FM6W9rD4FhiLX6pFIP5
# #
#
#
#
# {
#     "data": {
#         "age": 67,
#         "avatarPhotoID": 435190761,
#         "avatarPraiseCount": 0,
#         "avatarPraised": false,
#         "avatarURL": "https://photo.zastatic.com/images/photo/428035/1712139573/4793394252534114709.jpg",
#         "basicInfo": [
#             "离异",
#             "67岁",
#             "双子座(05.21-06.21)",
#             "178cm",
#             "89kg",
#             "工作地:南京江宁区",
#             "月收入:3-5千",
#             "自由职业",
#             "中专"
#         ],
#         "deliverLove": {
#             "show": false
#         },
#         "detailInfo": [
#             "汉族",
#             "籍贯:江苏南京",
#             "不吸烟",
#             "不喝酒",
#             "和家人同住",
#             "未买车",
#             "有孩子但不在身边",
#             "是否想要孩子:视情况而定",
#             "何时结婚:时机成熟就结婚"
#         ],
#         "educationString": "中专",
#         "emotionStatus": 0,
#         "gender": 0,
#         "genderString": "男士",
#         "hasIntroduce": true,
#         "hasSendMail": false,
#         "heightString": "178cm",
#         "hideVerifyModule": false,
#         "introduceContent": "希望在对的时间遇到对的缘分，由相识到相知相亲相爱。",
#         "introducePraiseCount": 0,
#         "ipAreaDesc": "IP属地：江苏",
#         "isActive": false,
#         "isFollowing": false,
#         "isInBlackList": false,
#         "isOfflineSuperRecUser": false,
#         "isRecentlyActive": false,
#         "isStar": false,
#         "isSuperVip": false,
#         "isZhenaiMail": false,
#         "lastLoginTimeString": "",
#         "liveAudienceCount": 0,
#         "liveType": 0,
#         "lookMe": false,
#         "marriageString": "离异",
#         "matchingDegree": "98.4",
#         "memberID": 1712139573,
#         "momentCount": 7,
#         "nickname": "康无为2890",
#         "objectAgeString": "57-71岁",
#         "objectChildrenString": "未填写",
#         "objectEducationString": "中专",
#         "objectHeightString": "158cm以上",
#         "objectInfo": [
#             "57-71岁",
#             "158cm以上",
#             "工作地:江苏南京",
#             "中专",
#             "不要吸烟"
#         ],
#         "objectMarriageString": "未填写",
#         "objectSalaryString": "未填写",
#         "objectWantChildrenString": "未填写",
#         "objectWorkCityString": "江苏南京",
#         "occupation": "自由职业",
#         "onlive": 0,
#         "photoCount": 1,
#         "photos": [
#             {
#                 "createTime": "2024-01-24 08:54:42",
#                 "isAvatar": true,
#                 "photoID": 435190761,
#                 "photoType": 1,
#                 "photoURL": "https://photo.zastatic.com/images/photo/428035/1712139573/4793394252534114709.jpg",
#                 "praiseCount": 0,
#                 "praised": false,
#                 "verified": true
#             }
#         ],
#         "praisedIntroduce": false,
#         "previewPhotoURL": "",
#         "pycreditCertify": false,
#         "recommendUpgrade2": false,
#         "recommendUpgrade3": false,
#         "salaryString": "3001-5000元",
#         "showHighVipPic": false,
#         "showValidateIDCardFlag": false,
#         "superRecClickTip": "将在24小时内推荐给大量心仪异性",
#         "superRecGuideTip": "",
#         "superRecommend": false,
#         "totalPhotoCount": 1,
#         "validateEducation": false,
#         "validateFace": false,
#         "validateIDCard": false,
#         "videoCount": 0,
#         "videoID": 0,
#         "workCity": 10118025,
#         "workCityString": "南京",
#         "workProvinceCityString": "南京江宁区"
#     },
#     "errorCode": "",
#     "errorMessage": "",
#     "isError": false
# }