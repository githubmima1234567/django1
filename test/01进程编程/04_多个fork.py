import os

ret = os.fork()
if ret == 0:
	print("*********1*****")
else:
	print("*********2*****")
	ret = os.fork()
	if ret == 0:
		print("*********1*****")
	else:
		print("*********2*****")
