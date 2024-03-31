import os
import time
g_num = 100
print (g_num)
ret = os.fork()
if ret>0:
      g_num = g_num+1
      print("**********父**********%d"%g_num)
else:
      g_num= g_num+2
      print("****1******%d"%g_num)

print("全局变量：%d"%g_num)
