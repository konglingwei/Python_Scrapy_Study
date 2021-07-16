#导入定义好的数据格式
from slaveredis.items import AskquestionItem
from scrapy_redis.spiders import RedisSpider
import time
class SlaveSpider(RedisSpider):
    #定义爬虫名
    name = 'slave'
    # allowed_domains = ['q.cnblogs.com']
   #定义redis键值
    redis_key = 'questionspider:start_urls'
    # redis_key = 'konglw:start_urls'
    # def __init__(self, *args, **kwargs):
    #     # 定义允许的 domains list.
    #     domain = kwargs.pop('domain', '')
    #     print("konglw :"+domain)
    #     print(domain)
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(SlaveSpider, self).__init__(*args, **kwargs)
    #按照规则爬取
    def parse(self, response):
        # print(response.text)
        ask_item = AskquestionItem()
        try:
            post_nodes = response.xpath("//*[@id='main']//div[@class='one_entity']")
            for post_node in post_nodes:
                # 标题
                title = post_node.xpath('.//h2[@class="news_entry"]/a/text()').extract_first("")
                ask_item['title'] = title.strip()
                # 作者
                author = post_node.xpath('.//div[@class="news_footer_user"]//a[@class="news_contributor"]/text()').extract_first("")
                ask_item['author'] = author.strip()
                # 浏览量
                reading = post_node.xpath('.//div[@class="news_footer_user"]/text()').extract()[4]
                ask_item['reading'] = reading.strip()
                # 回答数
                ask = post_node.xpath('.//div[@class="news_footer_user"]/a[@class="question-answer-count"]/text()').extract_first("")
                ask_item['ask'] = ask.strip()
                # 发表时间
                datetime = post_node.xpath('.//div[@class="news_footer_user"]/span/@title').extract_first("")
                ask_item['datetime'] = datetime
                yield ask_item
            time.sleep(5)
        except:
            return
