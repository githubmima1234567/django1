
import requests

headers = {
# "Host": "user.qzone.qq.com",
# "Connection": "keep-alive",
# "Cache-Control": "max-age=0",
# "sec-ch-ua": "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
# "sec-ch-ua-mobile": "?0",
# "sec-ch-ua-platform": "\"Windows\"",
# "Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
# "Sec-Fetch-Site": "same-site",
# "Sec-Fetch-Mode": "navigate",
# "Sec-Fetch-User": "?1",
# "Sec-Fetch-Dest": "document",
# "Referer": "https://qzs.qzone.qq.com/",
# "Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "971381748_todaycount=0; 971381748_totalcount=25276; pac_uid=0_928b6ddd40b71; iip=0; _qimei_uuid42=17c030b040c100cbafe2267c12cded46b1df0277a4; _qimei_fingerprint=2af7e4984dc243ba320ccbe4663fe0a5; _qimei_q36=; _qimei_h38=716d5c8aafe2267c12cded460200000c617c03; zzpaneluin=; zzpanelkey=; _qpsvr_localtk=0.039393084456412764; pgv_pvid=816857663; pgv_info=ssid=s2779887902; RK=4Gfs6GBic/; ptcz=570b1aeca5313143635986ab8fa422310a2996a580925071d37c45144a1a5c3d; Loading=Yes; qz_screen=1440x900; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; QZ_FE_WEBP_SUPPORT=1; __Q_w_s__QZN_TodoMsgCnt=1; rv2=80D8F7E5BEA55BA0531755B1CC858EEE8523E90A0A4267063F; property20=EA7905338668669DA434D7472BFC4BA18A6D99D54ED0F362C8E96F3DA8EE0639BA37E2E4B30B7878; uin=o0971381748; skey=@TlrKBzR2u; p_uin=o0971381748; pt4_token=uXtlhHHHWf9tbDAwDDcBnQ-GdRhWKueaH4rjPQ4p990_; p_skey=zuV*2YoT-ccfpPcAqPzY8htG2Mt7NWjDN0QqisF9icg_; qzmusicplayer=qzone_player_971381748_1714377787143; cpu_performance_v8=72",
# "If-Modified-Since": "Mon, 29 Apr 2024 01:53:08 GMT",
}


url = 'https://user.qzone.qq.com/971381748/infocenter?_t_=0.8480688236276015'
html = requests.get(url, headers = headers).text
print(html)