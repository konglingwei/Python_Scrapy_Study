# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouguoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class DouguoItem(scrapy.Item):
    author = scrapy.Field() # 作者
    dish_name = scrapy.Field() # 菜名
    rate = scrapy.Field() # 星级
    peoples = scrapy.Field() # 做过的人数
    cook_story = scrapy.Field() #烹饪故事
    cook_time = scrapy.Field() # 烹饪时间
    cook_difficult = scrapy.Field() # 烹饪难度
