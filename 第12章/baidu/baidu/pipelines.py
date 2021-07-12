# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#导入csv模块
from scrapy.exporters import CsvItemExporter

class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item
class CsvBaiduPipeline(object):
    def __init__(self):
        # 新建baidu.csv文件，定义能够写入数据
        self.file = open("baidu.csv", 'wb')
        # 定义保存的字段
        self.exporter = CsvItemExporter(self.file, fields_to_export=['title', 'author', 'reply'])
        self.exporter.start_exporting()

        # 从item存入数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # 关闭baidu.csv数据文件
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
