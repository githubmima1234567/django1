#coding=utf-8
import os
# 添加系统环境变量
os.environ.update({'APP_HOME': 'liangshiyan'})
# 获取系统环境变量
app_home = os.environ.get('APP_HOME')
#删除系统环境变量
os.environ.pop('APP_HOME')
print(app_home)
print(os.environ.keys())