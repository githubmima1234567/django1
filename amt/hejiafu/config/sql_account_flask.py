import logging

import requests
import json

"""

cd  /home/web_account_flask

101.132.157.102 服务器
screen -ls
screen -r  web_account_falsk
python3 account_flask.py


# 创建会话
screen -S web_account_falsk(会话名)

# 重启会话
screen -D -r [session-id]

screen -X -S 28508 quit
screen -X (会话名) quit
screen -wipe 685266

"""

def account_infos(systemname,Status,data_name,data_status,username,factorycode,client_id):
  try:
    url = "http://101.132.157.102:5000/account_info"

    # payload = json.dumps({
    #   "systemname": "zjhl", # 网站简称
    #   "Status": "1",        # 状态
    #   "data_name": "Sales",  # 模块名称
    #   "data_status": "1",   # 模块状态
    #   "username": "",  # 用户名
    #   "factorycode": "",    # 厂编
    #   "client_id": ""     # 品牌商编码
    # })
    payload = json.dumps({
      "systemname": systemname, # 网站简称
      "Status": Status,        # 状态
      "data_name": data_name,  # 模块名称
      "data_status": data_status,   # 模块状态
      "username": username,  # 用户名
      "factorycode": factorycode,    # 厂编
      "client_id": client_id     # 品牌商编码
    })
    headers = {
      'Content-Type': 'application/json'
    }

    accounts = requests.request("POST", url, headers=headers, data=payload).json()
    return accounts['data']
  except Exception as e:
    logging.info("查询账号失败：{}".format(e))
    return False

if __name__ == '__main__':

  accounts = account_infos("Dennis","1","Order","1","11708603","11708603","Order")
  print(accounts)