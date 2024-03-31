#coding=utf-8 
import pdb 
def combine(s1,s2): 
    s3 = s1 + s2 + s1 
    s3 = '"' + s3 +'"' 
    return s3 
a = "aaaa" 
pdb.set_trace() 
b = "bbbb"
c = "eee"
final = combine(a,b) 
print (final)

