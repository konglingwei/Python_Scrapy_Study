#coding=utf-8
#业务层
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
    # 在构造方法中实例初始化
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    #封装公用的
    def user_base(self,name,password,email,filename):
        self.register_h.send_user_name(name)
        self.register_h.send_user_email(email)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(filename)
        self.register_h.click_register_button()
    #判断注册是否成功
    def register_succes(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False
    #封装login函数,执行操作
    # def login(self,email,name,password,code):
    #     if self.register_h.get_user_text('请输入一个正确的邮箱地址'):
    #         print('邮箱检验成功')
    #         return True
    #     elif self.register_h.get_user_text('最少要输入 5 个字符'):
    #         print('密码检验成功')
    #         return True
    #检验用户名
    def login_username_error(self,email,name,password,filename):
        self.user_base(email,name,password,filename)
        if self.register_h.get_user_text('user_name_error', '最少要输入 2 个字符') == None:
            print('用户名检验不成功')
            return True
        else:
            return False
    #检验密码
    def login_password_error(self,email,name,password,filename):
        self.user_base(email,name,password,filename)
        if self.register_h.get_user_text('user_password_error', '最少要输入 5 个字符') == None:
            print('密码检验不成功')
            return True
        else:
            return False
    #检验邮箱
    def login_email_error(self,email,name,password,filename):
        self.user_base(email,name,password,filename)
        if self.register_h.get_user_text('user_email_error','请输入一个正确的邮箱地址！')  == None:
            print('邮箱检验不成功')
            return True
        else:
            return False
    #检验验证码
    def login_code_error(self,email,name,password,filename):
        self.user_base(email,name,password,filename)
        if self.register_h.get_user_text('code_text_error', '验证码错误！') == None:
            print('验证码检验不成功')
            return True
        else:
            return False