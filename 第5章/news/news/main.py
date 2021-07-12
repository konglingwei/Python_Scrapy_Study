import time
import sched
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
#初始化sched模块的scheduler类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
scho = sched.scheduler(time.time, time.sleep)

# 被周期性调度触发的函数
def start_scrapy():
    process = CrawlerProcess(get_project_settings())
    # 添加需要执行的爬虫
    process.crawl('new')
    # 执行
    process.start()
def perform(inc):
    scho.enter(inc, 0, perform, (inc,))
    start_scrapy()   # 需要周期执行的函数

def main_scrapy():
    scho.enter(0, 0, perform, (20,))  # 每10s执行一次
    scho.run()   # 开始运行，直到计划时间队列变成空为止

if __name__ == '__main__':
    start_scrapy()
