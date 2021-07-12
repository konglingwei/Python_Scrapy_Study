# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanItem(scrapy.Item):
    #电影序号
    serial_number = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #电影的介绍
    movie_introduce = scrapy.Field()
    #电影星级
    star = scrapy.Field()
    #电影的评论数
    evaluate = scrapy.Field()
    #电影的描述
    describe = scrapy.Field()

