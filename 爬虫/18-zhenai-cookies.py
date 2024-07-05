
import requests

headers = {
"Host": "album.zhenai.com",
"Connection": "keep-alive",
"sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\",\"Not-A.Brand\";v=\"99\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "\"Windows\"",
"Upgrade-Insecure-Requests": "1",
"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Dest": "document",
"Referer": "https://album.zhenai.com/u/1781372408",
# Accept-Encoding: gzip, deflate, br, zstd"
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; FSSBBIl1UgzbN7NO=5n4VRu2_0N5UH6gUjlaH.hFdOSDIszz5zY5cWKVYSZrZRWg7lD9BnKnVMgo8N4NmXWbH5RUhDayR0fJUoljlrRA; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; _exid=Qevzv4P2atJTz4O2Sm5qyX8c7q4K9IH0ccl3NGe14QkKW9MqN6XGg2azgL0onm%2BWA5zCAoEQRqAn22UmNLsEOw%3D%3D; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2FE%2BTlUaovMO6p%2FNp7wKZ%2FxGL9nPY07SP215a3fjwch5Y%3D; lrt=1715049726250; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225,1714916243,1715049726; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1715049726; FSSBBIl1UgzbN7NP=5RObXaC3y..3qqqDHVYtzDqzQb5eXlkFG6qM2WLMBl8vPJeXihRXeE7QckPYWC49KNkBXKZWiqZaq49yXAz82eoPWMqFK1LCbthcwLVDXxJ3Zy1wf85IvMiUYl1ukWgsv5ZLoGzBBI6gv8gHIkikZfPbjdcG69Iv9WtwxLkA9f4J.rGtMijqb_h5GrD1tOvnDpjJKI__4NiHqhFZP5mAmECPKiwRkYHORiHxEAFLxF_W4rAvtcA55xO5h5m9WZtlVQ",
}
sessions = requests.Session()
sessions.headers[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
cookies = "sid=89048270-cecf-4d5a-a066-f44f00057abf; bdVid=8383750066493410530; ec=esPVDWND-1714623179219-e4bf5f1bb3a37-779144053; recommendId=ZaMainpageTa-0001-online_xgb-0.0.1-za_user_profile-0.0.1; notificationPreAuthorizeSwitch=7491; loginRegisterSwitchType=1; login_health=15e4d5db1230971a6273f5e864fd9164574821996072fb298a567fe3bd24e2165a767c815a39ec044e5128f43b8b1386a03d423d2c4208e585b4247bc603d3b9; _pc_login_validate_isUnconnectByAdmin=; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714623185,1714787225; __channelId=901045%2C0; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1650634300%22; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1714794298; _efmdata=GSVnrz1fEOY65%2FVfv7ldOwLrVLN3%2BBmO7Y0sNcb2OHaAta9Qga%2FuMdWjftvc5od%2F8noi%2FFcnvF0OhduLsZ%2BG%2BkHr1QBs8MNKztBGxXXpPN8%3D; _exid=L1hw2B1%2FvFBfdYq%2FvNAaneyepMBLdqqATkqt1CecdTA2kc%2FcOj4Hr3NWsehqM8XoT%2BgWI3MZLy9lcZKeV5YMKg%3D%3D; token=1650634300.1714794417822.f5e2b68945951c1887d7c28c7746ee0e; refreshToken=1650634300.1714880817822.96bc17c8e54d374e7e23b4aa893d9244; lrt=1714794418016"
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
response1 = sessions.get('https://album.zhenai.com/u/1781372408', headers = headers).text
print(response1)