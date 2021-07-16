# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#导入mongodb模块
import pymongo
import json
# 爬虫数据保存在csv中 方法2
from scrapy.exporters import CsvItemExporter  # 导入cvs模块
# from laveredis.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
# from laveredis.items import AskquestionItem
class SlaveredisPipeline(object):
    def process_item(self, item, spider):
        return item
class SlavePipeline(object):
    # def __init__(self):
    #     host = mongo_host
    #     port = mongo_port
    #     dbname = mongo_db_name
    #     dbcollection = mongo_db_collection
    #     # 进行mongdb的链接
    #     client = pymongo.MongoClient(host=host, port=port)
    #     mydb = client[dbname]
    #     self.post = mydb[dbcollection]
    # def process_item(self, item, spider):
        # print(item)
        # 数据的插入，data转换成字典(dict)
        # if isinstance(item, AskquestionItem):
        #     data = dict(item)
        #     self.post.insert(data)
        # return item

#-------------------------------------------------------------------
    # def __init__(self):
    #     self.file = open('questions.json', 'wb')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item)) + "\n"
    #     self.file.write(line.encode('utf-8'))
    #     return item
# -------------------------------------------------------------------
    def __init__(self):
        # 新建toutiao.cvs文件，定义能够写入数据
        self.file = open("questions2.csv", 'wb')
        # 定义保存字段 title, author, reading, ask,datetime
        self.exporter = CsvItemExporter(self.file,fields_to_export=['title', 'author', 'reading', 'ask','datetime'])
        self.exporter.start_exporting()

    # 从item存入数据
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # questions.cvs数据文件
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

# -------------------------------------------------------------------
#     def __init__(self):
#         # connection database
#         self.connect = pymysql.connect(host='localhost', user='root', passwd='klw120110119',
#                                        db='slave', charset='utf8')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
#         # get cursor
#         self.cursor = self.connect.cursor()
#         print("连接数据库成功")
#
#     def process_item(self, item, spider):
#         print(item)
#         # sql语句 ['rank', 'title', 'link', 'star','rate','quote']
#         insert_sql = """ insert into question_table(title, author, reading, ask,datetime) VALUES (%s,%s,%s,%s,%s) """
#         # 执行插入数据到数据库操作
#         self.cursor.execute(insert_sql, (item['title'], item['author'], item['reading'],item['ask'],item['datetime']))
#         # 提交，不进行提交无法保存到数据库
#         self.connect.commit()
#         return item
#
#     def close_spider(self, spider):
#         # 关闭游标和连接
#         self.cursor.close()
#         self.connect.close()


import pymysql
from twisted.enterprise import adbapi

# 异步更新操作
class AncyLvyouPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor,  # 指定cursor类型
            charset = 'utf8'
        )

        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql',**adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常
        return item

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """ insert into question_table(title, author, reading, ask,datetime) VALUES (%s,%s,%s,%s,%s) """
        cursor.execute(insert_sql, (item['title'], item['author'], item['reading'],item['ask'],item['datetime']))


    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)

#--------------------------------------------------------------------------------
#爬虫数据保存在mysql中 同步操作
import pymysql

class LvyouPipeline(object):
    def __init__(self):
        # connection database
        self.connect = pymysql.connect(host='localhost', user='root', passwd='klw120110119',
                                       db='slave', charset='utf8')  # 后面三个依次是数据库连接名、数据库密码、数据库名称
        # get cursor
        self.cursor = self.connect.cursor()
        print("连接数据库成功")

    def process_item(self, item, spider):
        print(item)
        # sql语句 ['rank', 'title', 'link', 'star','rate','quote']
        insert_sql = """ insert into question_table(title, author, reading, ask,datetime) VALUES (%s,%s,%s,%s,%s) """
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['title'], item['author'], item['reading'],item['ask'],item['datetime']))
        # 提交，不进行提交无法保存到数据库
        self.connect.commit()
        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.connect.close()