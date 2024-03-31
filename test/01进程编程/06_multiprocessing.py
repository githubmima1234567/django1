import time
from multiprocessing import Process
def test():
    while True:
        print("*****1*****")
        time.sleep(1)
P = Process(target=test)
P.start()

while True:
    print("****mian***")
    time.sleep(1)
