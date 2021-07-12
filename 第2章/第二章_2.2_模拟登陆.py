import requests   #导入requests模块
from jsonpath import jsonpath  #导入jsonpath模块
login_api = ' http://localhost/user/login?sid='
login_username = 'linda'
login_params = {'verifyCode': 'abcde', 'password': '123456', 'email': login_username}
s = requests.Session()  #建立requests.Session()请求
r = s.post(login_api, data=login_params)  #发送头信息
sid = jsonpath(r.json(), '$..sid')[0]   #使用jsonpath解析获取到的json数据
user_detail_api = ' http://localhost/user/1?sid=%s' %sid  #在url里加入sid
result = s.get(user_detail_api)
print(result.text)
