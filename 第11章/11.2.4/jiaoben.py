#coding=utf-8
import time
import random
from PIL import Image
from selenium import webdriver
import json
import requests
import base64
from io import BytesIO
from sys import version_info
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# 实例化driver
driver = webdriver.Chrome()
# driver初始化
def driver_init():
    driver.get("https://www.qingyingtech.com/register.php")
    #最大化窗口
    driver.maximize_window()
    time.sleep(5)
#封装定位元素,，获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element
#获取随机数用户名
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',8))
    return user_info
#获取随机数邮箱
def get_range_email():
    user_email = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',8)) + "@163.com"
    return user_email
#验证码读取
def base64_api(uname, pwd,  img):
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
#获取图片
def get_range_img():
    # 定义文件下载位置及名称
    filename = "E:/Linda/python37/test/ceshi/capacha.png"
    # 定义图片地址及名称
    image_add = "E:/Linda/python37/test/ceshi/capacha2.png"
    driver.save_screenshot(filename)
    code_element = driver.find_element_by_id("getcode_num")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(filename)
    # 按一定的坐标裁剪
    img = im.crop((left, top, right, height))
    img.save(image_add)
    return image_add
#解析图片获取验证码
def code_online(image_add):
    img_path = image_add
    img = Image.open(img_path)
    result = base64_api(uname='qingying', pwd='linda1221', img=img)
    print(result)
    return result

#运行主程序
def run_main():
    user_name = get_range_user()
    user_email = get_range_email()
    user_password = "666666"
    driver_init()
    try:
        locator = (By.CLASS_NAME, "input")
        # 判断传入的元素是否可见
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
        print("网页正确")
        get_element("register_nickname").send_keys(user_name)
        get_element("register_email").send_keys(user_email)
        get_element("register_password").send_keys(user_password)
        image_add = get_range_img()
        text = code_online(image_add)
        get_element("validate").send_keys(text)
        time.sleep(3)
        get_element("submit").click()
        time.sleep(3)
        driver.close()
    except:
        print("网页错误")
        time.sleep(2)
        driver.close()
#调用主程序
run_main()
