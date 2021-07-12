# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CnblogspiderItem(scrapy.Item):  # scrapy.Item是基类
    # scrapy.Field用来描述自定义数据里包含哪些字段信息
    title = scrapy.Field()  # 文章标题
    content = scrapy.Field()  # 文章内容
    front_image_url = scrapy.Field() # 图片地址
    create_date = scrapy.Field()  # 文章创建时间


