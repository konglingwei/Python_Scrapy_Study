# -*- coding: utf-8 -*-
import scrapy
import re   # 导入正则表达式re模块
from news.items import CnblogspiderItem

class NewsSpider(scrapy.Spider):   # 爬虫类名为NewsSpider
    name = 'news'   # 爬虫名为news
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['https://news.cnblogs.com']   #开始爬取的网页地址
    custom_settings = {
        'ITEM_PIPELINES': {'douban.pipelines.BlogPipeline': 5},
    }

    # 解析start_urls的内容，默认的解析方法
    def parse(self, response):
        blog_list = response.xpath('//*[@id="news_list"]/div[@class="news_block"]') # 获取爬取第一页的爬取新闻列表
        for i_blog in blog_list:
            # 将item文件导进来
            article_item = CnblogspiderItem()
            title = i_blog.xpath('.//div[2]/h2/a/text()').extract()     # 获取新闻标题名
            str = ','.join(title)
            article_item['title'] = str
            content = i_blog.xpath('.//div[2]/div[1]/text()').extract()  # 获取新闻内容
            for i_count in content:
                # 去掉字符串的空格
                count_s = "".join(i_count.split())
                article_item['content'] = count_s
            create_date = i_blog.xpath(".//div[@class='entry_footer']/span[@class='gray']/text()").extract_first("")    # 获取发表时间
            # 通过正则表达式格式化日期
            martch_re = re.match(".*?(\d+.*)", create_date)
            if martch_re:
                article_item['create_date'] = martch_re.group(1)
            image_urls = i_blog.xpath('.//div[@class="entry_summary"]/a/img/@src').extract_first("")    # 获取图片地址
            # 判断获取到的图片地址，根据情况整理出完整的图片url
            if 'images0.cnblogs.com' in image_urls:
                img_url = 'https:'+image_urls
            elif 'images2015.cnblogs.com' in image_urls:
                img_url = 'https:' + image_urls
            else:
                img_url = image_urls
            article_item['front_image_url'] = img_url
            yield article_item 	# article_item 数据先返回到ItemPipeline
