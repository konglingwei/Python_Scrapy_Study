# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib import parse
from baidu.items import BaiduItem
class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/']
    def parse(self, response):
        kw= '柯南'
        keys = parse.urlencode({'kw': kw})  # 转换为url编码
        key_url = self.start_urls[0] + 'f?' + keys
        yield Request(url=key_url,callback=self.parse_detail)
    def parse_detail(self,response):
        print(response.url)
        baidu_item = BaiduItem()
        before = response.xpath('//*[@id="thread_list"]/li')
        for be in before:
            #获取标题名
            title = be.xpath('.//div[1]/div[1]/a/text()').extract_first("")
            baidu_item['title'] = title
            #获取回复
            reply = be.xpath('.//span[@title="回复"]/text()').extract_first("")
            baidu_item['reply'] = reply
            #获取作者名
            author = be.xpath('.//div[1]/div[2]/span[1]/span[1]/a/text()').extract_first("")
            baidu_item['author'] = author
            yield baidu_item

