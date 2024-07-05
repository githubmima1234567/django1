
import requests
import json
import execjs
import time

# qq音乐的sign是消息摘要加密算法
t1 = str(int(time.time()*1000))
print(t1)
url = 'https://u6.y.qq.com/cgi-bin/musics.fcg?'
# _=1718328149086&sign=zzb6d67fa03e1yiqlwt3o5i2lgxld3mw0017f400

headers = {
'Host': 'u6.y.qq.com',
'Connection': 'keep-alive',
'Content-Length': '1279',
'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
'Accept': 'application/json',
'Content-Type': 'application/x-www-form-urlencoded',
'sec-ch-ua-mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
'sec-ch-ua-platform': '"Windows"',
'Origin': 'https://y.qq.com',
'Sec-Fetch-Site': 'same-site',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://y.qq.com/',
# 'Accept-Encoding: gzip, deflate, br, zstd
'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cookie': 'pgv_pvid=5041743610; fqm_pvqid=f675ece1-19c8-4733-9f32-dd1bc2969036; ts_uid=5594447288; RK=7Gfk/GByZ9; ptcz=379344e52d9d989c45d7e992914a53784b1ea0e718c6794e151816b883ff3b22; euin=NKS5oic57ivF; psrf_qqopenid=12B58DC26579A2156E0797DCA8A2943C; psrf_qqaccess_token=0009C237B6FDCE5805F6C214E0545A9F; wxrefresh_token=; psrf_access_token_expiresAt=1726040650; tmeLoginType=2; psrf_qqrefresh_token=C0D3A4EC020329E55047C6372839FDC5; wxunionid=; psrf_qqunionid=22E9CB8B97733BF2D957878AF55F7B69; psrf_musickey_createtime=1718264650; music_ignore_pskey=202306271436Hn@vBj; uin=971381748; qm_keyst=Q_H_L_63k3NT1laHjSaNOqpzRsDNUL7i7-BEzLphpRURJGybvM56RpmnmXegXxI7QtiXqCRv4jI2PQrjQ; qqmusic_key=Q_H_L_63k3NT1laHjSaNOqpzRsDNUL7i7-BEzLphpRURJGybvM56RpmnmXegXxI7QtiXqCRv4jI2PQrjQ; wxopenid=; fqm_sessionid=9202942d-2b72-409e-8228-740dc2463617; pgv_info=ssid=s254169265; ts_last=y.qq.com/n/ryqq/player',
# {"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":626428183,"g_tk":626428183},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001QJyJ32zybEe"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001QJyJ32zybEe","songID":247347346}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"247347346","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"0049MVh824D7bM"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"3131153292","songmid":["001QJyJ32zybEe"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02061u18bu37wpHO.mp3"]}}}
}
cookies = {
'pgv_pvid':'5041743610',
'fqm_pvqid':'f675ece1-19c8-4733-9f32-dd1bc2969036',
'ts_uid':'5594447288',
'RK':'7Gfk/GByZ9',
'ptcz':'379344e52d9d989c45d7e992914a53784b1ea0e718c6794e151816b883ff3b22',
'euin':'NKS5oic57ivF',
'psrf_qqopenid':'12B58DC26579A2156E0797DCA8A2943C',
'psrf_qqaccess_token':'0009C237B6FDCE5805F6C214E0545A9F',
'wxrefresh_token':'',
'psrf_access_token_expiresAt':'1726040650',
'tmeLoginType':'2',
'psrf_qqrefresh_token':'C0D3A4EC020329E55047C6372839FDC5',
'wxunionid':'',
'psrf_qqunionid':'22E9CB8B97733BF2D957878AF55F7B69',
'psrf_musickey_createtime':'1718264650',
'music_ignore_pskey':'202306271436Hn@vBj',
'uin':'971381748',
'qm_keyst':'Q_H_L_63k3NT1laHjSaNOqpzRsDNUL7i7-BEzLphpRURJGybvM56RpmnmXegXxI7QtiXqCRv4jI2PQrjQ',
'qqmusic_key':'Q_H_L_63k3NT1laHjSaNOqpzRsDNUL7i7-BEzLphpRURJGybvM56RpmnmXegXxI7QtiXqCRv4jI2PQrjQ',
'wxopenid':'',
'fqm_sessionid':'9202942d-2b72-409e-8228-740dc2463617',
'pgv_info':'ssid=s254169265',
'ts_last':'y.qq.com/n/ryqq/player',
}
# data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":1033948989,"g_tk":1033948989},"req_1":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["002G0sJY2wThyx","003S1hgM2asCye"}},"req_2":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["003S1hgM2asCye"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"003S1hgM2asCye","songID":102174489}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102174489","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003c616O2Zlswm"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7292601882","songmid":["003S1hgM2asCye"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02061Ia7kn1GYOS9.mp3"]}}}'
# data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":1033948989,"g_tk":1033948989},"req_1":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["002G0sJY2wThyx","003S1hgM2asCye"}},"req_2":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["003S1hgM2asCye"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"003S1hgM2asCye","songID":102174489}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102174489","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003c616O2Zlswm"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7292601882","songmid":["003S1hgM2asCye"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":"M800"}}}'

# data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":0,"g_tk_new_20200303":5381,"g_tk":5381},"req_1":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["002G0sJY2wThyx","003S1hgM2asCye"]}},"req_2":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"002G0sJY2wThyx","songID":7168586}},"req_3":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"7168586","biz_sub_type":0}]}},"req_4":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"000cFPKx3ZGzks"}},"req_5":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1864347631","songmid":["002G0sJY2wThyx"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}}}'  #
data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1033948989,"g_tk":1033948989},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["003S1hgM2asCye"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"003S1hgM2asCye","songID":102174489}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102174489","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003c616O2Zlswm"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7292601882","songmid":["003S1hgM2asCye"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20"}}}'

with open("./qqmusic.js", 'r') as f:
    js_code1 = f.read()
    # 通过execjs.compile()进行编译js文件内容
js = execjs.compile(js_code1)
# 调用js文件传参
#'h'是js中的function方法名，en_data是传参
sign1 = js.call('main123',data)
print(sign1)
params = {
    '_':t1,
    'sign':sign1
}
response = requests.post(url,params=params,cookies=cookies,headers=headers,data=data.encode()).json()
print(response)
# purl = response.xpath
# https://ws6.stream.qqmusic.qq.com/C400000ME7es0ihTlN.m4a?guid=1864347631&vkey=0E3B51A16509A6C3860719B34DF4BABC358348AC771A7F103945CADCD7F35276E206E50F8B6FE0A36569FAB0F3355AA2513A9C765D490AA5&uin=971381748&fromtag=120032

# 搁浅VIP{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1365295831,"g_tk":1365295831},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001Bbywq2gicae"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001Bbywq2gicae","songID":102065750}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102065750","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003DFRzD192KKD"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"72203580","songmid":["001Bbywq2gicae"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02062VCVkH3Hm4wk.mp3"]}}}
# 一起VIP{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1033948989,"g_tk":1033948989},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["003S1hgM2asCye"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"003S1hgM2asCye","songID":102174489}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"102174489","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"003c616O2Zlswm"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7292601882","songmid":["003S1hgM2asCye"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02061Ia7kn1GYOS9.mp3"]}}}'
# 屋顶非V{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1365295831,"g_tk":1365295831},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001wXiwd0eRSes"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001wXiwd0eRSes","songID":4758516}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"4758516","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"002GJDhP0ZluDv"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"5448814160","songmid":["001wXiwd0eRSes"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20"}}}
# 喜欢你非{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1365295831,"g_tk":1365295831},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["002G0sJY2wThyx"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"002G0sJY2wThyx","songID":7168586}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"7168586","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"000cFPKx3ZGzks"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"7802538560","songmid":["002G0sJY2wThyx"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20"}}}
# 喜欢你vip {"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":971381748,"g_tk_new_20200303":1365295831,"g_tk":1365295831},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001mbYZr3QR68r"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001mbYZr3QR68r","songID":7096775}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"7096775","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"001oHxZZ1pAQn4"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"2851021096","songmid":["001mbYZr3QR68r"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02061Gtd9U3PDjbz.mp3"]}}}
# "req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["971381748"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["971381748"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001mbYZr3QR68r"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001mbYZr3QR68r","songID":7096775}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"7096775","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"001oHxZZ1pAQn4"}},"req_8":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"2851021096","songmid":["001mbYZr3QR68r"],"songtype":[0],"uin":"971381748","loginflag":1,"platform":"20","filename":["RS02061Gtd9U3PDjbz.mp3"]}}}