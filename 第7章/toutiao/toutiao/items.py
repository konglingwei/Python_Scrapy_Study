# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题
    create_date = scrapy.Field()  #文章发表时间
    article_url = scrapy.Field()  #文章详情链接
    pinglun = scrapy.Field()  #评论数
    article_source = scrapy.Field() #文章来源
