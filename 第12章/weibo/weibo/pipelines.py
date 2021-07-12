# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from weibo.items import WeiboItem
from weibo.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
from scrapy.exporters import CsvItemExporter


class WeiboPipeline(object):
    def process_item(self, item, spider):
        return item
class AskPipeline(object):
    def __init__(self):
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
        if isinstance(item, WeiboItem):
            data = dict(item)
            self.post.insert(data)
        return item
class CsvAskPipeline(object):
    def __init__(self):
        # 新建weibo.csv文件，定义能够写入数据
        self.file = open("weibo.csv",'wb')
       # 定义保存的字段
        self.exporter = CsvItemExporter(self.file,fields_to_export=['title','content', "pinglun", 'zhuanfa','hot','datetime'])
        self.exporter.start_exporting()
   # 从item存入数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    # 关闭cnask.csv数据文件
    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
