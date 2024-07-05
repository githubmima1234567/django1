
import urllib.parse
import urllib.request
import requests
url = "https://www.zhenai.com/api/search/getConditionData.do "

headers = {
"Host": "www.zhenai.com",
"Connection": "keep-alive",
"Content-Length": "271",
"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
"Accept": "application/json, text/plain, */*",
"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
"sec-ch-ua-mobile": "?0",
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
"sec-ch-ua-platform": "\"Windows\"",
"Origin": 'https://www.zhenai.com',
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
# "Referer": "https://www.zhenai.com/n/search",
# Accept-Encoding: gzip, deflate, br, zstd
# Accept-Language: zh-CN,zh;q=0.9
"Cookie": "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016",
}
formdata = {
"page":"1",
"pageSize":"20",
"ageBegin":"29",
"ageEnd":"43",
"workCity":"10115001",
"heightBegin":"-1",
"heightEnd":"-1",
"multiEducation":"-1",
"salaryBegin":"103",
"salaryEnd":"-1",
"body":"-1",
"_":"1714794419990",
"ua":"h5/1.0.0/1/0/0/0/901045/0//0/0/dbbb0be5-e271-4dc5-a867-bba857687a37/0/0/1297809052",
}
data = urllib.parse.urlencode(formdata)
my_edata = data.encode('ascii')
response = requests.post(url,headers=headers)

html = response.json()
print(html)