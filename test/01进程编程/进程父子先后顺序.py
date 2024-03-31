import os
import time

ret = os.fork()
print(ret)
if ret>0:
      print("**********父**********")
else:
      print("****1******")
      time.sleep(1)
      print("****2******")

print ("****over****")
