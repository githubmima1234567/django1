from multiprocessing import Process
import time
def test():
    for i in range(5):
        time.sleep(1)
        print("11111111111")
        
P = Process(target=test)
P.start()
