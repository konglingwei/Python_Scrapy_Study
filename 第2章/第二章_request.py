import requests
r = requests.get('http://localhost/insert.php') #通过requests建立请求
code = r.status_code  #获取状态值
print('code: ',code)
print(r.text)
