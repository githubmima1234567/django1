import re
# . 匹配任意1个字符（除了\n）
result = re.match(".","a").group()
print(result)
result = re.match(".","\n")
print(result)

# \d 匹配数字，即0-9
result = re.match(r"\d","2").group()
print(result)
# 报错 " invalid escape sequence ‘\d’ " (无效的转义字符’\d’)。
# 原因是Python 3将字符串文字解释为Unicode字符串，因此 \d 被视为转义的Unicode字符。解决办法有两种。
# 1.在字符串字面值中使用两个反斜线,2.可以预先在正则表达式前添加 r
result = re.match(r"\d","w")
print(result)

# \D 匹配非数字，即不是数字
result = re.match(r"\D","w").group()
print(result)
result = re.match(r"\D","3")
print(result)

# \s 匹配空白,即空格，tab键\n、\r
result = re.match(r"\s","\n").group() #返回一个空行
print(result)
result = re.match(r"\s","\a")
print(result)

# \S 匹配非空白
result = re.match(r"\s","\na").group()
print(result)
result = re.match(r"\s","\n")
print(result)

# \w 匹配单词字符，即a-z、A-Z，0-9、-
result = re.match(r"\w","77")
print(result)
result = re.match(r"\w","\n")
print(result)

# \W 匹配非单词字符
result = re.match(r"\W","77")
print(result)
result = re.match(r"\W","\n")
print(result)

# [] 匹配[]中例举的字符
result = re.match(r"1[135]","13")
print(result)
result = re.match(r"1[135]","8")
print(result)