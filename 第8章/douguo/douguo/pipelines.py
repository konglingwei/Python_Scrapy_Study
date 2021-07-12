# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#导入DouguoItem类里的数据格式
from douguo.items import DouguoItem
#导入csv模块
from scrapy.exporters import CsvItemExporter

class DouguoPipeline(object):
    def process_item(self, item, spider):
        return item
class CsvDouguoPipeline(object):
    def __init__(self):
        # 新建douguo.csv文件，定义能够写入数据
        self.file = open("douguo.csv",'wb')
       # 定义保存的字段
        self.exporter = CsvItemExporter(self.file,fields_to_export=['dish_name','author', "cook_story", 'cook_time','cook_difficult','rate','peoples'])
        self.exporter.start_exporting()
   # 从item存入数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    # 关闭douguo.csv数据文件
    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
