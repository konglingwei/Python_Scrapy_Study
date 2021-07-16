# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import redis,re
class MasterredisPipeline(object):
    def process_item(self, item, spider):
        return item

class MasterPipeline(object):
    def __init__(self,host,port,password):
        #连接redis数据库
        self.r = redis.Redis(host=host, port=port,decode_responses=True)
        # self.r = redis.Redis(host=host, port=port, password=password,decode_responses=True)
        # self.r = redis.Redis(host='127.0.0.1', port=6379, password='klw120110119',decode_responses=True)
        # self.r = redis.Redis(host='localhost', port=6379, password='klw120110119', decode_responses=True)
    @classmethod
    def from_crawler(cls,crawler):
        '''注入实例化对象（传入参数）'''
        return cls(
            host = crawler.settings.get("REDIS_HOST"),
            port = crawler.settings.get("REDIS_PORT"),
            password = crawler.settings.get("REDIS_PASSWORD"),
        )
    def process_item(self, item, spider):
        #使用正则判断url地址是否有效，并写入redis。
        print("konglw")
        print(item)
        if re.search('/list/unsolved?',item['url']):
            self.r.lpush('questionspider:start_urls', item['url'])
            # self.r.lpush('konglw:start_urls', item['url'])
        else:
            self.r.lpush('questionspider:no_urls', item['url'])
