# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#CsvItemExporter用来保存Item数据为csv文件
from scrapy.exporters import CsvItemExporter

class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item
class CsvExporterPipeline(object):
    def __init__(self):
	# 创建接收文件，初始化exporter属性
        self.file = open("movie.csv",'wb')  # movie.csv为将要写入的文件名
        self.exporter = CsvItemExporter(self.file,fields_to_export=['serial_number','movie_name', "movie_introduce", 'star','evaluate','describe'])  # fields_to_export 里放入Items字段列表
        self.exporter.start_exporting()  #启动start_exporting()，接收Item
    def process_item(self, item, spider):
        self.exporter.export_item(item)  #从items.py里传入Item值
        return item
    def spider_closed(self,spider):
        self.exporter.finish_exporting()  # 结束exporter的exporting
        self.file.close()  #关闭文件
