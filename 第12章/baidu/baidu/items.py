# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class BaiduItem(scrapy.Item):
    #定义文章标题
    title = scrapy.Field()
    #定义作者
    author = scrapy.Field()
    #定义回复数
    reply = scrapy.Field()

