# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#导入mongodb模块
import pymongo
from laveredis.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
from laveredis.items import AskquestionItem
class SlaveredisPipeline(object):
    def process_item(self, item, spider):
        return item
class SlavePipeline(object):
   def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        dbcollection = mongo_db_collection
        # 进行mongdb的链接
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[dbcollection]
    def process_item(self, item, spider):
        # 数据的插入，data转换成字典(dict)
        if isinstance(item, AskquestionItem):
            data = dict(item)
            self.post.insert(data)
        return item
