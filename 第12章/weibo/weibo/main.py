from scrapy.cmdline import execute
import sys
import os
def start_scrapy():
    sys.path.append(os.path.dirname(__file__))
    execute(["scrapy","crawl","keys"])
if __name__ == '__main__':
    start_scrapy()
