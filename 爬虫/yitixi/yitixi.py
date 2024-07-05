import requests
import json

"""
确定目标
发送请求
解析数据
保存数据
"""
headers = {
    'Host': 'gateway.etc-parts.com',
    'Connection': 'keep-alive',
    'Content-Length': '400',
    # 'sec-ch-ua': '\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"',
    'x-page-code': 'M1634261022396W83BO',
    'sec-ch-ua-mobile': '?0',
    'x-uid': '990306821417865216',
    # 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOiIyMDI0LTA1LTIxIDE4OjU3OjI1IiwiZXhwIjoiMjAyNC0wNS0yMiAwMjo1NzoyNSIsImV4cFNlY29uZHMiOm51bGwsInN1YiI6ImVtYWxsVXNlciIsImNsaWVudCI6InBjIiwidXNlciI6eyJ1c2VySWQiOjk5MDMwNjgyMTQxNzg2NTIxNiwidXNlcm5hbWUiOm51bGwsIm1vYmlsZSI6bnVsbCwib3BlbkFwaVVzZXJUeXBlIjpudWxsfSwiZXhwaXJlZCI6ZmFsc2UsImR1cmF0aW9uIjoyODgwMCwiZXhwaXJlZEhhbGYiOmZhbHNlLCJtaW5pQXBwRW1hbGxVc2VyIjpmYWxzZSwibWluaUFwcFN1cHBsaWVyVXNlciI6ZmFsc2UsIm1pbmlBcHBHYXJhZ2VVc2VyIjpmYWxzZSwiYXBwVXNlciI6ZmFsc2UsInRhc2tTZXJ2aWNlIjpmYWxzZSwiYW5vbnltb3VzIjpmYWxzZSwib3BlbkFwaVVzZXIiOmZhbHNlLCJvZFNhbGVzIjpmYWxzZSwib2RPcGVyIjpmYWxzZX0.K2Oz0zY2mlbBbueQDBZ7Qr949nSTPwCcuUDXHEebDKA',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'x-page-url': '/goodsList',
    'isPrompt': 'false',
    # 'x-auth-sign': '1eaf439cf5f81796f00e12b0bfaff735',
    # 'x-request-id': '04a02cf2cf195c4763c828ac479e197f',
    'sec-ch-ua-platform': '\"Windows\"',
    'Origin': 'https://e.etc-parts.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://e.etc-parts.com/',
    # Accept-Encoding: gzip, deflate, br, zstd
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2218f99e2dcfca6-0c709574cc3cf68-26001d51-1296000-18f99e2dcfd1090%22%7D; acw_tc=2f624a0d17162890399851378e1c75df5bde8636f293c594398c8cc347a574; ssxmod_itna=YqIx2CIxyAGHD8QtIx7uDGqY5DQFIjQ5d3D/QDf2xiNDnD8x7YDvCGhRSCKSKbMmOhoGeADxb5TzW8DOTGIWUu0D5DU4i8DCwGcdtDee=D5xGoDPxDeDAeKiTDY4Ddfh5H=DEDeKDRDWKDX6akDickDm+8dAukfrKDR65D0gbFDQKDucF5DGH5G9h3DYeDKE7COxgsH4D1eev4fxG1O40HE7k5f=g6g9r12xL4Y84OxKYDvxDkVEKDo6cpDBbkyhYNi7RDiB0t8Bi3ACD5orGP1NG3AHpPGSG5qj2ldWReWg=Di64a4D; ssxmod_itna2=YqIx2CIxyAGHD8QtIx7uDGqY5DQFIjQ5dG93HRDBT247phxyWaY7qH4cyh=HeadGgT5G8KS8whbDKLw3DLxijt4D',
}

headers['x-auth-sign'] = 1
headers['x-request-id'] = 1
headers['Authorization']= 1
headers['sec-ch-ua'] = 1

url = 'https://gateway.etc-parts.com/web-emall/home/moduleProductInfoSearch'

datas = {
    "pageSize": "20",
    "pageNum": "1",
    "vinCode": "",
    "partBrandCode": "[]",
    "seriesCodeList": "[\"130\",\"140\",\"100\"]",
    "searchName": "",
    "priceSort": "",
    "levelCode": "306",
    "brandList": "[]",
    "modelList":"[]",
    "hasStock": "true",
    "newProductIdentity": "false",
    "commodityId": "",
    "commodityLibraryId": "840643219464523776",
    "moduleId": "989972392329752576",
    "vehicleIds": "[]",
    "seriesName": "",
    "vehicleBrandNameCnOfficial": "",
    "vehicleModel": "",
    "simplifiedEngineDesc": ""
}

# {"pageSize":20,"pageNum":1,"vinCode":"","partBrandCode":[],"seriesCodeList":["130","140","100"],"searchName":"","priceSort":"","levelCode":"1","brandList":[],"modelList":[],"hasStock":true,"newProductIdentity":false,"commodityId":"","commodityLibraryId":"840643219464523776","moduleId":"989972392329752576","vehicleIds":[],"seriesName":"","vehicleBrandNameCnOfficial":"","vehicleModel":"","simplifiedEngineDesc":""}
json_data = json.dumps({"pageSize":"20","pageNum":"1","vinCode":"","partBrandCode":"[]","seriesCodeList":"[\"130\",\"100\",\"903\"]","searchName":"","priceSort":"","levelCode":"1","brandList":"[]","modelList":"[]","hasStock":"true","newProductIdentity":"false","commodityId":"","commodityLibraryId":"840643219464523776","moduleId":"989972392329752576","vehicleIds":[],"seriesName":"","vehicleBrandNameCnOfficial":"","vehicleModel":"","simplifiedEngineDesc":""})
response = requests.post(url,json=json_data,headers=headers)
print(response.content.decode())
# 保存response文件
with open("goods.txt", "wb") as f:
    f.write(response.content)

