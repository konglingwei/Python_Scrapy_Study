import re   #re是专门用于正则表达式的模块（python内嵌的包）
char =  "linda1234"
regex_str = "^l"
#使用match方法进行匹配操作，基本参数为：a=re.match(pattern,string,flags=0)
# pattern为匹配规则模式，string是要匹配的字符串。
result = re.match(regex_str,char)   # 使用match方法进行匹配操作
if result:
    print(result.group())
else:
    print('匹配不成功')
