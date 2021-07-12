# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WeiboItem(scrapy.Item):
    # 定义博主名
    title = scrapy.Field()
    #定义文章内容
    content = scrapy.Field()
    #定义评论数
    pinglun = scrapy.Field()
    #定义转发数
    zhuanfa = scrapy.Field()
    #定义点赞数
    hot = scrapy.Field()
    #定义发表时间
    datetime = scrapy.Field()
