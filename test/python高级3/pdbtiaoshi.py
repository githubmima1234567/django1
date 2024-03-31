#coding=utf-8
import pdb 
def combline(s1,s2):
    s3 = s1 + s2 + s1
    s3 = '"' + s3 + '"'
    return s3

a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = combline(a,b)
print(final)

