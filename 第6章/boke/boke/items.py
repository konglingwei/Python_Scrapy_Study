# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BokeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BokeItem(scrapy.Item):
    titleid = scrapy.Field()  #文章id
    title = scrapy.Field()  #文章标题
    url = scrapy.Field()    #文章链接地址
    datetime = scrapy.Field()   #文章发表时间
    content = scrapy.Field()    #文章内容
    hits = scrapy.Field()   #文章浏览数
