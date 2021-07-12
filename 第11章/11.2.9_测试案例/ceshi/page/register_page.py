#coding=utf-8
#page层
from base.find_element import FindElement
class RegisterPage(object):
    #定义构造方法
    def __init__(self,driver):
        self.find_e = FindElement(driver)
    def get_email_element(self):
        return self.find_e.get_element("user_email")
    def get_name_element(self):
        return self.find_e.get_element("user_name")
    #获取密码元素
    def get_password_element(self):
        return self.find_e.get_element("password")
    #获取验证码元素
    def get_code_element(self):
        return self.find_e.get_element("code_text")
    #获取注册按钮元素
    def get_button_element(self):
        return self.find_e.get_element("register_button")
    #获取邮箱错误元素
    def get_email_error_element(self):
        return self.find_e.get_element("user_email_error")
    #获取用户名错误元素
    def get_name_error_element(self):
        return self.find_e.get_element("user_name_error")
    #获取密码错误元素
    def get_password_error_element(self):
        return self.find_e.get_element("user_password_error")
    #获取验证码错误元素
    def get_code_error_element(self):
        return self.find_e.get_element("code_text_error")
