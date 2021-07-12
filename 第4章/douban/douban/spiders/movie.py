# -*- coding: utf-8 -*-
import scrapy
#引入items
from douban.items import DoubanItem
class MovieSpider(scrapy.Spider):
    #爬虫名
    name = 'movie'
    #允许的域名
    allowed_domains = ['movie.douban.com/top250']
    #入口url
    start_urls = ['https://movie.douban.com/top250']
    #解析start_urls的内容，默认的解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")[0:3]
        #循环电影的条目前3条
        for i_item in movie_list:
            #item文件导进来
            douban_item = DoubanItem()
            #在当前xpath进一步细分,需要加一个点. 并解析到它第一个数据extract_first("")
			# #获取电影序号
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first("")
			#获取电影名称
            douban_item['movie_name'] = i_item.xpath(".//div[@class='hd']//span[1][@class='title']/text()").extract_first("")
            #获取电影的介绍
            count = i_item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for i_count in count:
                count_s = "".join(i_count.split())  # 去掉字符串的空格
                douban_item['movie_introduce'] = count_s
			#获取电影星级
            douban_item['star'] = i_item.xpath(".//div[@class='star']/span[2]/text()").extract_first("")
			#获取电影的评论数
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first("")
			#获取电影的描述
            douban_item['describe'] = i_item.xpath(".//div[@class='bd']//span[@class='inq']/text()").extract_first("")
            print(douban_item)  #打印douban_item数据
			# 将数据yield到piplines里去（在那里进行数据的清洗和存储）
            yield douban_item
