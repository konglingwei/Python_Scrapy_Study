#coding=utf-8
from util.read_ini import ReadIni
#封装类
class FindElement(object):
    #定义构造函数
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        #实例化ReadIni
        read_ini=ReadIni()
        data=read_ini.get_value(key)
        #定位方式
        by = data.split('>')[0]
        #定位值
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None