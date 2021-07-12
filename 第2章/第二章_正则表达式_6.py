import re  #re是专门用于正则表达式的模块（python内嵌的包）
char = "doooocddadpylina456"
regex_str = ".*(d.{2}d).*"
result = re.match(regex_str,char)  # 使用match方法进行匹配操作
if result:
    print("限定中间字符出现N次：",result.group(1))
else:
    print('匹配不成功')
regex_str = ".*(d.{3,}d).*"
result = re.match(regex_str,char)
if result:
    print("限定中间字符出现N次以上：",result.group(1))
else:
    print('匹配不成功')
regex_str = ".*(d.{3,6}d).*"
result = re.match(regex_str,char)  # 使用match方法进行匹配操作
if result:
    print("限定中间字符出现最少3次，最多6次：",result.group(1))
else:
    print('匹配不成功')
