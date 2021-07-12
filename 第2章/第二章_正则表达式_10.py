import re  #re是专门用于正则表达式的模块（python内嵌的包）
char =  " 小明出生于2005年"
regex_str = " .*?(\d+)年"
result = re.match(regex_str,char)   # 使用match方法进行匹配操作
if result:
    print(result.group(1))
else:
    print('匹配不成功')
