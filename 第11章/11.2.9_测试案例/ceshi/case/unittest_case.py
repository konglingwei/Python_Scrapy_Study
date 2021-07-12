#coding=utf-8
import unittest
import os
import HTMLTestRunner
#继承TestCase类
class UnitCase(unittest.TestCase):
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
    file_path = os.path.join(os.getcwd()  + "test_case.html")
    print(file_path)
    # 以读写的模式打开file_path
    file = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(UnitCase('testfirst'))
    # suite.addTest(UnitCase('testsecond'))
    # suite.addTest(UnitCase('testthird'))
    # unittest.main()
    # 执行测试
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title="This is test report", description="Register Test Report",verbosity=2)
    runner.run(suite)