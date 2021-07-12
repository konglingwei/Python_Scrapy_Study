from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(__file__)) #定位到该项目douban下
execute(["scrapy","crawl","movie"])  #movie为自己的爬虫名
