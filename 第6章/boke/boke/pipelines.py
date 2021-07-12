# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb  # 链接mysql数据库


class BokePipeline(object):
    def process_item(self, item, spider):
        return item

    class MysqlNewsPipeline(object):
        def __init__(self):
            self.conn = MySQLdb.connect("localhost", "root", "root", "boke", charset="utf8", use_unicode=True)
            self.cursor = self.conn.cursor()

        def process_item(self, item, spider):
            # 使用sql insert语句
            insert_sql = """
                insert into  news(titleid,title,content,url,datetime,hits) values(%s,%s,%s,%s,%s,%s)  
            """
            params = list()
            params.append(item.get("titleid", ""))
            params.append(item.get("title", ""))
            params.append(item.get("content", ""))
            params.append(item.get("url", ""))
            params.append(item.get("datetime", ""))
            params.append(item.get("hits", 0))
            # 把数据插入数据表
            self.cursor.execute(insert_sql, tuple(params))
            self.conn.commit()
            return item
