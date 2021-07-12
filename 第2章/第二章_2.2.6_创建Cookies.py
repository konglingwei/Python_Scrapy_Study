from urllib import request
from urllib import parse
from http.cookiejar import LWPCookieJar,CookieJar
# 创建cookie管理
cookie_obj = LWPCookieJar(filename='cookies.txt')
handler = request.HTTPCookieProcessor(cookie_obj)
opener = request.build_opener(handler)
response = opener.open('http://localhost/Post.php')
cookie_obj.save(ignore_expires=True,ignore_discard=True)
#打印cookie
for cookie in cookie_obj:
    print('key:',cookie.name)
    print('value:',cookie.value)
