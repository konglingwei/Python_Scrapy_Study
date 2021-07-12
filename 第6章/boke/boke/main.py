from scrapy.cmdline import execute
import sys
import os
def start_scrapy():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    #定义运行爬虫命令
    execute(["scrapy","crawl","news"])
if __name__ == '__main__':
#运行爬虫
    start_scrapy()
