from multiprocessing import Pool
import os

def worker(num):
    for i in range(5):
        print("PID是：%s,num:%s"%(os.getpid(),num))


pool = Pool(3)
for i in range(10):
    pool.apply_async(worker,(i,))

pool.close()#关闭进程池
pool.join()#默认不会等待子进程结束
