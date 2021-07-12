#coding=utf-8
import unittest
import os
import HTMLTestRunner
#继承TestCase类
class DemoCase(unittest.TestCase):
    def setUp(self):
        print('这是case的前置条件')
    def tearDown(self):
        print('这是case的后置条件')
    def count(self,a,b):
        num = a + b
        return num
    def input(self):
        d = int(input("请输入一个数字："))
        return d
    def testfirst(self):
        first = self.count(6,5)
        #测试不相等则通过
        return self.assertNotEqual(first,12, '相等')
    def testsecond(self):
        second = self.count(6, 5)
        # 测试相等则通过
        return self.assertEqual(second, 11, '不相等')
    def testthird(self):
        third = self.input()
        # 测试输入a是否是6则通过
        return self.assertIs(third,6, '不是')
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
