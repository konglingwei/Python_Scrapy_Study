from scrapy.cmdline import execute  # 导入cmd模块
# 导入系统模块
import sys
import os
def start_scrapy():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 定义运行爬虫命令
    execute(["scrapy","crawl","toutiao"])
if __name__ == '__main__':
    start_scrapy()
