#coding=utf-8
import unittest
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
	#构造测试集
    suite = unittest.TestSuite()
    suite.addTest(UnitCase('testfirst'))
    suite.addTest(UnitCase('testsecond'))
    suite.addTest(UnitCase('testthird'))
#执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
