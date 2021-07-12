##coding=utf-8
#导入unittest
import unittest
# 测试方法继承自unittest.TestCase
class Count(unittest.TestCase):
# 计算减法
    def minus(self,a,b):
        subtraction = a - b
        return subtraction
    def setUp(self):
        print("测试开始")
    def minus(self):
        s = self.minus(14,4)
        # 这里的比较,如果是10就是我们的预期结果，否则为 Fail。
        text = self.assertEqual(s,10,msg='不想等')
        if text == None:
            print('相等')
    def tearDown(self):
        print("测试结束")
if __name__ == '__main__':
    unittest.main()
