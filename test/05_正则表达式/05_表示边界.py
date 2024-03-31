import re

# ^ 匹配字符串开头
result = re.match("^name","name is liangshiyan")
print(result)

# $ 匹配字符串结尾
result = re.match(".*yan$","is yan")
print(result)

# \b 匹配一个单词的边界
result = re.match(r".+er\b\s\w","howevyer ih")
print(result)

# \B 匹配非单词边界
result = re.match(r".+am\B.+","liang name yan").group()
print(result)