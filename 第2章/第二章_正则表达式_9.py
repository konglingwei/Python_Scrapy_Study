import re  #re是专门用于正则表达式的模块（python内嵌的包）
char =  " 欢迎回来"
regex_str = " (欢\w+来)"
result = re.match(regex_str,char)   # 使用match方法进行匹配操作
if result:
    print(result.group(1))
else:
    print('匹配不成功')
