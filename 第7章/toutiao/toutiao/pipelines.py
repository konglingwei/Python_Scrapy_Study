# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from news.items import ToutiaoItem
import pymongo
from news.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
from scrapy.exporters import CsvItemExporter  #导入csv模块

class ToutiaoPipeline(object):
    def process_item(self, item, spider):
        return item
class NewsPipeline(object):
    def __init__(self):
        # 定义mongdb的链接
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        dbcollection = mongo_db_collection
        # 拿mongdb的链接
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[dbcollection]
    def process_item(self, item, spider):
        # 数据的插入，data转换成字典(dict)
        if isinstance(item, ToutiaoItem):
            data = dict(item)
            self.post.insert(data)
        return item
#保存数据到news.csv文件
class CsvNewsPipeline(object):
    def __init__(self):
        # 新建news.csv文件，定义能够写入数据
        self.file = open("news.csv",'wb')
       # 定义保存的字段
        self.exporter = CsvItemExporter(self.file,fields_to_export=['title','content', "create_date", 'front_image_url'])
        self.exporter.start_exporting()
   # 从item存入数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    # 关闭news.csv数据文件
    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
