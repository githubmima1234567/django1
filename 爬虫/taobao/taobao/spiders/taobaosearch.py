from typing import Any

import scrapy
import time
import execjs
from scrapy.http import Response


class TaobaosearchSpider(scrapy.Spider):
    name = "taobaosearch"
    allowed_domains = ["h5api.m.taobao.com"]
    start_urls = ["https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?"]


    def start_requests(self):
        t1 = str(int(time.time() * 1000))
        headers = {
            # 'Accept':' */*',
            # Accept-Encoding: gzip, deflate, br, zstd
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'thw=cn; cna=k9wLHsdsmQkCAXWaOo3XwbR8; lgc=%5Cu6881%5Cu4E16%5Cu71D522; tracknick=%5Cu6881%5Cu4E16%5Cu71D522; havana_lgc2_0=eyJoaWQiOjEwNDkwNDYxMjUsInNnIjoiOWYyZjI3MTMzYmMxMzIyMDI0YzA1ZWU4ODhlOGI3MDQiLCJzaXRlIjowLCJ0b2tlbiI6IjFfSlVXUkhQdGtLYzg4SnNNc2I0TWp3In0; _hvn_lgc_=0; havana_lgc_exp=1714419481223; cookie3_bak=124f57c288c5bad2b4c798b39e0c0e2e; wk_cookie2=1579cd594858f06ec40a27cc7a6c1abc; wk_unb=UoH7Ik2T6S1FrQ%3D%3D; env_bak=FM%2Bgzadehc%2BvwAnw5RSVYJsCf77Vs1vmgK7rxMXUp9H9; mt=ci=241_1; xlly_s=1; sgcookie=E100U0Jsk9oVDzTWJ4iiR%2B1bdPvbE2q1j%2BtKOyJwhzbDi6%2FQqkxhV%2BQVU6flstnwJR8NRwgTf3ofR6mFSQwHsBXdfjOgpyNBk3Pqu5%2BCf2Wb3tQ%3D; cookie3_bak_exp=1715761347791; dnk=%5Cu6881%5Cu4E16%5Cu71D522; _samesite_flag_=true; 3PcFlag=1715681362625; unb=1049046125; uc1=cookie14=UoYfpCGFNewrYw%3D%3D&cookie21=Vq8l%2BKCLj6Hk37282g%3D%3D&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=false&pas=0&cookie15=VFC%2FuZ9ayeYq2g%3D%3D; uc3=id2=UoH7Ik2T6S1FrQ%3D%3D&nk2=okgRRKY1CXg%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dD3eMy0uYLWeULAwU%3D; csg=12d6b0a3; cancelledSubSites=empty; t=896570f7865b77ff4bd32634fbd07bfe; cookie17=UoH7Ik2T6S1FrQ%3D%3D; skt=1b639d032697ead7; cookie2=124f57c288c5bad2b4c798b39e0c0e2e; existShop=MTcxNTY4MTM2OQ%3D%3D; uc4=id4=0%40UOnkRkT9LKXypO5WyFo2EzPkdupN&nk4=0%40oErx3ZTIogErAuFUa2jAfhR5Uw%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=259; _nk_=%5Cu6881%5Cu4E16%5Cu71D522; cookie1=AiSnZHwY7wDKodXwKzTDYtgCCfCsX88FlJkWy4zjD%2Bg%3D; _tb_token_=e3efeebee1536; mtop_partitioned_detect=1; _m_h5_tk=0ae14fdec5652d841fab183c083c2dc0_1715700628423; _m_h5_tk_enc=76de6796a6636b5c61d0ea882874a0a2; tfstk=ftLK9aZlFAD3itikRBiMUui2rNcgyedEKpRbrTX3Vdp9NO4oTwmPyLB9U9jhR94RyQpyELdrT_6WFLBkxc0DTB7PPxX-oqAUgVYoMLICP1w6__B5FJ3G8X_PPxDgjzsEkaJD8e2r2GGOZ_e7OL6Q5P6NZk6WF9s_CsCVPT95Pfe1Gsf7Ak1S5NGWrcBzAt4JS6k9YPyIqh-HW6IsjI61C9hlwMdytOFQOFUVvtOCBzMDwH8ceO8jIcdwEH9h_L3xBNOXXw1pFqZcChd68ibxckpfSTIfMpcu41KJNE7Fk7gB6wBdceIIrr9X6QtcXFcjuwQCd3beZSHH6epHTFduNl_d-hIvJZg4dTxMMUCJzYu9HBtXF3IzOEYYlWwcH_qI6fEz4M1GOEJPLLkWsU1Onff34uStb1Bm6fEz4M1N6tcgKurPXc5..; isg=BOHhx_H1I_OM7o_40TvI5yIC8K37jlWAemMn3EO0Mehpqgl8h9pyUGusDd4sP-24',
            'Host': 'h5api.m.taobao.com',
            'Referer': 'https://s.taobao.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sec-ch-ua': '\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        # url = 'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?'
        params2 = {
            "jsv": "2.6.2",
            "appKey": "12574478",
            "t": t1,
            # sign: f209cf4e106f5fd3bc06120397380f16
            "api": "mtop.relationrecommend.wirelessrecommend.recommend",
            "v": "2.0",
            "type": "jsonp",
            "dataType": "jsonp",
            "callback": "mtopjsonp7",
        }
        data1 = {"appId": "34385",
                 "params": "{\"device\":\"HMA-AL00\",\"isBeta\":\"false\",\"grayHair\":\"false\",\"from\":\"nt_history\",\"brand\":\"HUAWEI\",\"info\":\"wifi\",\"index\":\"4\",\"rainbow\":\"\",\"schemaType\":\"auction\",\"elderHome\":\"false\",\"isEnterSrpSearch\":\"true\",\"newSearch\":\"false\",\"network\":\"wifi\",\"subtype\":\"\",\"hasPreposeFilter\":\"false\",\"prepositionVersion\":\"v2\",\"client_os\":\"Android\",\"gpsEnabled\":\"false\",\"searchDoorFrom\":\"srp\",\"debug_rerankNewOpenCard\":\"false\",\"homePageVersion\":\"v7\",\"searchElderHomeOpen\":\"false\",\"search_action\":\"initiative\",\"sugg\":\"_4_1\",\"sversion\":\"13.6\",\"style\":\"list\",\"ttid\":\"600000@taobao_pc_10.7.0\",\"needTabs\":\"true\",\"areaCode\":\"CN\",\"vm\":\"nw\",\"countryNum\":\"156\",\"m\":\"pc\",\"page\":1,\"n\":48,\"q\":\"python\",\"tab\":\"all\",\"pageSize\":48,\"totalPage\":100,\"totalResults\":4800,\"sourceS\":\"0\",\"sort\":\"_coefp\",\"bcoffset\":\"\",\"ntoffset\":\"\",\"filterTag\":\"\",\"service\":\"\",\"prop\":\"\",\"loc\":\"\",\"start_price\":null,\"end_price\":null,\"startPrice\":null,\"endPrice\":null,\"itemIds\":null,\"p4pIds\":null,\"categoryp\":\"\"}"}
        token = '0ae14fdec5652d841fab183c083c2dc0';
        en_data = token + "&" + t1 + "&" + params2['appKey'] + "&" + str(data1)
        with open("taobao.js", 'r') as f:
            js_code1 = f.read()
            # 通过execjs.compile()进行编译js文件内容
        js = execjs.compile(js_code1)
        # 调用js文件传参
        # 'h'是js中的function方法名，en_data是传参
        sign = js.call('u', en_data)
        params2['sign'] = sign
        params2['data'] = str(data1)
        print("sign:" + sign)
        print(params2)

        cookies = "thw=cn; cna=k9wLHsdsmQkCAXWaOo3XwbR8; lgc=%5Cu6881%5Cu4E16%5Cu71D522; tracknick=%5Cu6881%5Cu4E16%5Cu71D522; _hvn_lgc_=0; wk_cookie2=1579cd594858f06ec40a27cc7a6c1abc; wk_unb=UoH7Ik2T6S1FrQ%3D%3D; mt=ci=241_1; dnk=%5Cu6881%5Cu4E16%5Cu71D522; t=896570f7865b77ff4bd32634fbd07bfe; mtop_partitioned_detect=1; _m_h5_tk=7cf75a5f8d5211e102ec4c5081359db2_1716029888287; _m_h5_tk_enc=08387a50dd2508b9de4048e0d424b048; xlly_s=1; _samesite_flag_=true; 3PcFlag=1716020169328; cookie2=26bdd10fb01baeb22cb6ac1b9911aa3d; _tb_token_=e54db66e33363; sgcookie=E100LfkioGV1lmGJYuNfE35NNfQ6V51WOdjQsAsK3NM6y4lRQ4WpCwlAwDdBRYwTzk3WE8TrcOsoysuokWgK%2FT5dVwHttF3z3I97Mg49BvrRuWA%3D; cookie3_bak=26bdd10fb01baeb22cb6ac1b9911aa3d; cookie3_bak_exp=1716279373376; havana_lgc2_0=eyJoaWQiOjEwNDkwNDYxMjUsInNnIjoiYTQ5MzJhM2E1MWMwZGZjYzQ3YTA0OWE0NGU1ZDcwZmYiLCJzaXRlIjowLCJ0b2tlbiI6IjF0SEpfUE9Xb3YtVzA0bGk3b0xDajVnIn0; havana_lgc_exp=1715206238793; unb=1049046125; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie14=UoYfp3RLia%2F5jQ%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&existShop=false&cookie21=UIHiLt3xTwwM1Oej1w%3D%3D; uc3=nk2=okgRRKY1CXg%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dD3eM2mDz7ALJNbZQ%3D&id2=UoH7Ik2T6S1FrQ%3D%3D; csg=6c9c0f1e; cancelledSubSites=empty; env_bak=FM%2Bgzadehc%2BvwAnw5RSVYJsCf77Vs1vmgK7rxMXUp9H9; cookie17=UoH7Ik2T6S1FrQ%3D%3D; skt=3e779a3451627013; existShop=MTcxNjAyMDE3Mw%3D%3D; uc4=nk4=0%40oErx3ZTIogErAuFUaJyJVMCQxA%3D%3D&id4=0%40UOnkRkT9LKXypO5WyFo1qryD72gh; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; sg=259; _nk_=%5Cu6881%5Cu4E16%5Cu71D522; cookie1=AiSnZHwY7wDKodXwKzTDYtgCCfCsX88FlJkWy4zjD%2Bg%3D; tfstk=fNqI679y2BAQ8EysZ2BZf51HS5i7OWs2OLM8n8KeeDnKwPw0NXWl-DzsN5Fs9HWh-4h7tD3u8blEN0wuGO5V0iy3K00RgsS4QErIW0cR40dQpDvK2s5VbFJt-6o8z7De1fgtsYMpp4F-XVHEd0HKJvBs6YMDyBF-2OwtsvHpwHLdXCHmhjQMAAWIsJ1zxun3oQP8pftbIlMKOe2K13K8fy3IMgG623EsdR0K88-fzjUmTqlu6G-IVRH7GxNB61i8CkqjWkCMVSN_kcZilLBsYk2Lk4EAZUFjA7gYvV9JVJe3ScMTDT8m_lGUwkgO3ngrXouxvP7GT4oIh7E3OLt8MRy4xVq5GChu8xmtd7IA1goD0jZaRU9so3MsgO66rUu_7QVZ17rQy2HiQ_W1CEyoJADsgO66rU0KIAyPCOT4E; isg=BFNTh8cSMTLkUP2Sl_0a3Qzs4td9COfKpP31tgVwr3KphHMmjdh3GrHSvvTqIT_Ci.m "
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        # print(cookies)
        url = self.start_urls[0]
        yield scrapy.Request(
            url=url+str(params2),
            headers=headers,
            cookies=cookies,
            method='GET',
            callback=self.parse
        )

    def parse(self, response: Response, **kwargs: Any) -> Any:
        print(response.body.decode("utf-8"))