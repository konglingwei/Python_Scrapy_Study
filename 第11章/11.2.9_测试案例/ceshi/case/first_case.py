#coding=utf-8
import sys
#添加当前工程目录
sys.path.append('所在的目录')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import HTMLTestRunner

class FirstCase(unittest.TestCase):
    file_name = "所在的目录/ceshi/image/capacha2.png"
    def setUp(self):
        self.driver = webdriver.Chrome("所在的目录/chromedriver.exe")
        self.driver.get("https://www.qingyingtech.com/register.php")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(3)
        #拿到case和错误信息
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "\\report\\" + case_name +'.png')
                self.driver.save_screenshot(file_path)
        print('这是后置case')
        time.sleep(3)
        self.driver.close()
    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user111','11111',self.file_name)
        return self.assertFalse(email_error,'测试邮箱')
        #通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_username_error('k','mjgted','666@ss.com',self.file_name)
        self.assertFalse(username_error,'测试用户名')
    def test_login_password_error(self):
        password_error = self.login.login_password_error('22','1k','1111@qq.com',self.file_name)
        self.assertFalse(password_error,'测试密码')
    def test_login_code_error(self):
        code_error = self.login.login_code_error('2586s','few','mjdr@163.com',self.file_name)
        self.assertFalse(code_error,'测试code')
    def test_login_success(self):
        success = self.login.user_base('kdsa','jjausa','dadwe@163.com',self.file_name)
        self.assertFalse(success,'测试点击注册')
        # if self.login.register_succes() == True:
        #     print("注册成功")

# def main():
#     #实例化FirstCase
#     first = FirstCase()
#     first.test_login_code_error()
#     first.test_login_email_error()
#     first.test_login_password_error()
#     first.test_login_username_error()
#     first.test_login_success()

if __name__ == '__main__':
    # 获取当前工程目录
    file_path = os.path.join(os.getcwd() + "\\report\\" + "first_case.html")
    #以读写的模式打开file_path
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_password_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_success'))
     #unittest.main()
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description="Register Test Report",verbosity=2)
    runner.run(suite)
    # unittest.TextTestRunner().run(suite)
