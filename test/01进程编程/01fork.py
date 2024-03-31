import os
import time

ret = os.fork()
print(ret)
if ret>0:
      print("父进程为：%s"%os.getpid())
else:
         print("子进程pid:%s,父进程pid：%s"%(os.getpid(),os.getppid()))



    
