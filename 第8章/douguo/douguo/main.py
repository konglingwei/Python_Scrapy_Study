from scrapy.cmdline import execute
import sys
import os
def start_scrapy():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(["scrapy","crawl","douguo"])
if __name__ == '__main__':
    start_scrapy()
