# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb  # 导入数据库模块
from news.items import CnblogspiderItem  #从item倒入CnblogspiderItem
from twisted.enterprise import adbapi	# 导入adbapi
from MySQLdb.cursors import DictCursor
from scrapy.pipelines.images import ImagesPipeline  #导入ImagesPipeline图片管道
from scrapy.exporters import CsvItemExporter  # 定义导出数据的组件为Exporter，以CSV格式输出
class NewsPipeline(object):
    def process_item(self, item, spider):
        return item
class CsvNewsPipeline(object):
    def __init__(self):
        self.file = open("news.csv",'wb')	# 保存数据到news.csv文件
        self.exporter = CsvItemExporter(self.file,fields_to_export=['title','content', "create_date", 'front_image_url'])	# 设置4个字段
        self.exporter.start_exporting()
    def process_item(self, item, spider):	# 每个item被spider yield时都会调用。该方法现在返回一个Item
        self.exporter.export_item(item)
        return item
    def spider_closed(self,spider):	#在spider关闭时（数据爬取后）调用该函数，关闭news.csv文件
        self.exporter.finish_exporting()
        self.file.close()
class MysqlNewsPipeline(object):
    def __init__(self):
        # 链接mysql数据库
        self.conn = MySQLdb.connect("localhost","root","root","blog",charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()
     #数据同步插入到mysql数据库
    def process_item(self, item, spider):
       # sql语句
        insert_sql = """
            insert into  news(title,content,front_image_url,create_date) values(%s,%s,%s,%s)  
        """
        #从item获得数据
        params = list()
        params.append(item.get("title",""))
        params.append(item.get("content", ""))
        params.append(item.get("front_image_url", ""))
        params.append(item.get("create_date", ""))
        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql,tuple(params))
        # 提交，保存到数据库
        self.conn.commit()
        return item
#mysql 异步导入数据
class MysqlYbNewsPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool
    @classmethod
    def from_settings(cls,settings):
        # 数据库配置文件从setting里读，数据库建立连接
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=DictCursor,
            use_unicode=True,
        )
        # 连接数据池ConnectionPool，使用MySQLdb连接
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        # 返回实例化参数
        return cls(dbpool)
    def process_item(self, item, spider):
        """
            使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)    # 指定操作方法和操作数据
        query.addErrback(self.handle_error, item, spider)   # 添加异常处理
    def handle_error(self, failure, item, spider):
        if failure:
            print(failure)  # 打印错误信息
    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
                    insert into  news(title,content,front_image_url,create_date) values(%s,%s,%s,%s)  
                """
        params = list()
        params.append(item.get("title", ""))
        params.append(item.get("content", ""))
        params.append(item.get("front_image_url", ""))
        params.append(item.get("create_date", ""))
        cursor.execute(insert_sql, tuple(params))
#存储本地图片路径
class NewsImagePipeline(ImagesPipeline):
    def item_completed(self,results,item,info):
        if "front_image_url" in item:
            image_file_path=""
            for ok,value in results:
                image_file_path = value["path"] # 将路径保存在item中返回
            item["front_image_path"] = image_file_path
        return item
