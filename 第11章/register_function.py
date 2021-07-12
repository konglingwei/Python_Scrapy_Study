#coding=utf-8
from selenium import webdriver
import time
import random
import base64
import json
import requests
from io import BytesIO
from sys import version_info
from PIL import Image
from find_element import FindElement
class RegisterFunction(object):
    #定义构造函数
    def __init__(self,url):
        self.driver = self.get_driver(url)
    #获取driver，并打开url
    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver
    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)
    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    # 获取随机数用户名
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
        return user_info
    # 获取随机数邮箱
    def get_range_email(self):
        user_email = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8)) + "@163.com"
        return user_email
    # 验证码读取
    def base64_api(self,uname, pwd, img):
        img = img.convert('RGB')
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        if version_info.major >= 3:
            b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
        else:
            b64 = str(base64.b64encode(buffered.getvalue()))
        data = {"username": uname, "password": pwd, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            return result["message"]
        return ""
    # 获取图片
    def get_range_img(self,filename,image_add):
        #截屏处理
        self.driver.save_screenshot(filename)
        code_element = self.get_user_element("code_image")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(filename)
        # 按一定的坐标裁剪
        img = im.crop((left, top, right, height))
        img.save(image_add)
        return image_add
    # 解析图片获取验证码
    def code_online(self,image_adds):
        img_path = image_adds
        img = Image.open(img_path)
        result = self.base64_api(uname='qingying', pwd='linda1221', img=img)
        print(result)
        return result
    def main(self):
        user_name = self.get_range_user()
        user_email = self.get_range_email()
        user_password = "666666"
        # 定义文件下载位置及名称
        filename = "E:/Linda/python37/test/ceshi/capacha.png"
        # 定义图片地址及名称
        image_add = "E:/Linda/python37/test/ceshi/capacha2.png"
        image_adds = self.get_range_img(filename,image_add)
        code_text = self.code_online(image_adds)
        self.send_user_info('user_email',user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('password', user_password)
        self.send_user_info('code_text', code_text)
        # self.send_user_info('code_text', '11111')
        time.sleep(5)
        self.get_user_element('register_button').click()
        code_error = self.get_user_element("code_text_error")
        if code_error == None:
            print('注册成功')
        else:
            #验证码获取失败，截屏处理
            self.driver.save_screenshot("E:/Linda/python37/test/ceshi/code_error.png")
            print('验证码错误，注册失败')
        time.sleep(5)
        self.driver.close()
if __name__=='__main__':
    url = 'https://www.qingyingtech.com/register.php'
    #实例化
    register_function = RegisterFunction(url)
    #运行主程序
    register_function.main()
