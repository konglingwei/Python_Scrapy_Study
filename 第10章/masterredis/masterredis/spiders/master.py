from scrapy.spiders import CrawlSpider,Rule
from scrapy import Request
from masterredis.items import MasterredisItem
from scrapy.linkextractors import LinkExtractor
from urllib import parse
class QuestionSpider(CrawlSpider):
    name = 'question'
    allowed_domains = ['q.cnblogs.com']
    start_urls = ['https://q.cnblogs.com']
    #Rule是在定义抽取链接的规则
    rules = (
        Rule(LinkExtractor(allow=('https://q.cnblogs.com/list/unsolved?page=[1-160]',)), callback='parse_item',
             follow=True),
    )
    def parse_item(self, response):
        item = MasterredisItem()
        no1 = response.url + '/list/unsolved?page=1'
        item['url'] = no1
        print(item)
        yield item
        next_url = response.xpath("//div[@id='pager']/a[last()]/text()").extract_first("")
        if next_url == "Next >":
            next_url = response.xpath("//div[@id='pager']/a[last()]/@href").extract_first("")
            item['url'] = response.url + next_url
            print(item)
            yield Request(url=parse.urljoin(response.url, next_url), meta={"item": item},callback=self.parsenums,dont_filter=True)
        else:
            return
    def parsenums(self, response):
        print(response.url)
        item= response.meta.get("item", "")
        yield item
        # 提取下一页并交给scrapy进行下载
        next_url = response.xpath("//div[@id='pager']/a[last()]/text()").extract_first("")
        print('next2:', next_url)
        if next_url == "Next >":
            next_url = response.xpath("//div[@id='pager']/a[last()]/@href").extract_first("")
            item['url'] = response.url + next_url
            print('next: ',item)
            yield Request(url=parse.urljoin(response.url, next_url), meta={"item": item},callback=self.parsenums,dont_filter=True)
        else:
            return

