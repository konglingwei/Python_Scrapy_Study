from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor,build_opener
# --------------------获取cookie---------------------------
# 生成一个管理cookie的对象
cookie_obj = CookieJar()
# 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
cookie_handler = HTTPCookieProcessor(cookie_obj)
#创建一个opener
opener = build_opener(cookie_handler)
response = opener.open('http://localhost/Post.php')
print(response)
#打印cookie
for cookie in cookie_obj:
    print('keys:',cookie.name)
    print('values:',cookie.value)
