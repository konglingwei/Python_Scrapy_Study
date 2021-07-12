# -*- coding: utf-8 -*-
import scrapy
import re
from boke.items import BokeItem
from urllib import parse
from scrapy import Request

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.leibotech.com']
    start_urls = ['http://www.leibotech.com/itjs/']
    def parse(self, response):
        # 获取文章列表
        blog_list = response.xpath('//*[@id="main"]//div[@class="entry clearfix"]')
        for i_blog in blog_list:
            # 获取文章详情的url
            url = i_blog.xpath('.//h1/a/@href').extract_first("")
            post_url = str(url)
            details_url = parse.urljoin('http://www.leibotech.com',post_url)
            yield Request(url=details_url, callback=self.parse_detail)

    def parse_detail(self,response):
        #通过正则表达式提取文章id
        martch_re = re.match(".*?(\d+)", response.url)
        # 将item文件导进来
        boke_item = BokeItem()
        if martch_re:
            post_id = martch_re.group(1)
            boke_item['titleid'] = post_id
            #提取文章标题
            boke_item['title'] = response.xpath('//*[@class="entry clearfix"]/h1/a/text()').extract_first("")
            boke_item['url'] = response.url
            #提取文章发表日期
            date = response.xpath('//*[@class="entry clearfix"]//div[@class="post-meta"]').extract_first("")
            # 通过正则表达式格式化日期
            pattern = re.compile(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}')
            riqi= pattern.findall(date)
            boke_item['datetime'] = riqi[0]
            # 用正则获取浏览量
            martch_re = re.compile(r"浏览:\s\d+")
            hh = martch_re.findall(date)
            hits = re.findall('\d+',hh[0])
            boke_item['hits'] = hits[0]
            #获取文章内容
            content = response.xpath('//*[@class="entry clearfix"]//div[@class="entry-content"]').extract_first("")
            boke_item['content'] = content
            yield boke_item

