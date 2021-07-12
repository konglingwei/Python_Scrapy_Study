import re   #re是专门用于正则表达式的模块（python内嵌的包）
char =  " doooocddaddadpylina45678"
regex_str = " .*([abcd]dpylina45678).*"
result = re.match(regex_str,char)  # 使用match方法进行匹配操作
if result:
    print(result.group(1))
else:
    print('匹配不成功')
regex_str = ".*(a[0-9]{3}).*"
result = re.match(regex_str,char)  # 使用match方法进行匹配操作
if result:
    print("设置区间：",result.group(1))
else:
    print('匹配不成功')
