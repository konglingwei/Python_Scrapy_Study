#coding=utf-8
import unittest
import os
#导入生成web测试报告模块
import HTMLTestRunner
#继承TestCase类
class DemoCase(unittest.TestCase):
    def setUp(self):
        print('这是case的前置条件')
    def tearDown(self):
        print('这是case的后置条件')
    def testfirst(self):
        print('This is first case')
    def testsecond(self):
        print('This is second case')
    def testthird(self):
        print('This is third case')
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "\\test_case.html")
    # 以读写的模式打开file_path
    file = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(DemoCase('testfirst'))
    suite.addTest(DemoCase('testsecond'))
    suite.addTest(DemoCase('testthird'))
    # 执行测试
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="This is test report", description="Register Test Report",verbosity=2)
    runner.run(suite)
