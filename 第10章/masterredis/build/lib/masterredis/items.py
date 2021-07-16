# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class MasterredisItem(scrapy.Item):
    # 定义url地址存储
    url = scrapy.Field()

class AskquestionItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    reading = scrapy.Field()
    ask = scrapy.Field()
    datetime = scrapy.Field()

