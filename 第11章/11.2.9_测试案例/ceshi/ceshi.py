import time
import random
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import json
import requests
import base64
from io import BytesIO
from sys import version_info

# 实例化driver
driver = webdriver.Chrome()
driver.get("https://www.qingyingtech.com/register.php")
time.sleep(5)
print(driver.title)
#判断是否包含注册
print(EC.title_contains("注册"))
# 判断传入的元素是否可见
element = driver.find_element_by_class_name("input")
# EC.visibility_of_element_located(element)
locator = (By.CLASS_NAME,"input")
#判断传入的元素是否可见
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

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

driver.save_screenshot("E:/capacha.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("E:/capacha.png")
#按一定的坐标裁剪
img = im.crop((left,top,right,height))
img.save("E:/capacha2.png")

img_path = "E:/capacha2.png"
img = Image.open(img_path)
result = base64_api(uname='qingying', pwd='linda1221', img=img)
print(result)
time.sleep(2)
driver.find_element_by_id("validate").send_keys(result)

time.sleep(3)
driver.close()