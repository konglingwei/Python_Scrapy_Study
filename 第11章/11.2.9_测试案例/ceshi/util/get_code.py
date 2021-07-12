#coding=utf-8
from PIL import Image
import base64
import json
import time
import requests
from io import BytesIO
from sys import version_info
from util.ShowapiRequest import ShowapiRequest
class GetCode:
    def __init__(self,driver):
        self.driver = driver
        # 定义文件下载位置及名称
        filename = "所在的目录/ceshi/capacha.png"
        # 定义图片地址及名称
        image_add = "所在的目录/ceshi/capacha2.png"
        self.image_add = image_add
    # 获取图片
    def get_range_img(self,filename):
        self.driver.save_screenshot(filename)
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(filename)
        # 按一定的坐标裁剪
        img = im.crop((left, top, right, height))
        img.save(self.image_add)
        time.sleep(2)
        return self.image_add
    # 验证码读取
    def base64_api(self, uname, pwd, img):
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
    # 解析图片获取验证码
    def code_online(self,filename):
        image_adds = self.get_range_img(filename)
        img_path = image_adds
        img = Image.open(img_path)
        result = self.base64_api(uname='qingying', pwd='linda1221', img=img)
        time.sleep(2)
        return result

