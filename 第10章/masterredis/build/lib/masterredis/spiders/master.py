from scrapy.spiders import CrawlSpider,Rule
from scrapy import Request
from masterredis.items import MasterredisItem
from scrapy.linkextractors import LinkExtractor
from urllib import parse
class QuestionSpider(CrawlSpider):

    name = 'question'
    allowed_domains = ['q.cnblogs.com']
    start_urls = ["https://q.cnblogs.com"]

    # 定义提取url地址规则
    # 一个Rule一条规则，LinkExtractor表示链接提取器，提取url地址
    # allow，提取的url,url不完整，但是crawlspider会帮我们补全，然后再请求
    # callback 提取出来的url地址的response会交给callback处理
    # follow 当前url地址的响应是否重新将过rules来提取url地址
    rules = (
        # Rule(LinkExtractor(allow=r'/list/unsolved'), callback='parse_item',follow=True),
        Rule(LinkExtractor(allow=('https://q.cnblogs.com/list/unsolved\?page=\d',)), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        item = MasterredisItem()
        no1 = response.url
        item['url'] = no1
        yield item
        # print(response.url)
        # next_url = response.xpath("//div[@id='pager']/a[last()]/text()").extract_first("")
        # if next_url == "Next >":
        #     next_url = response.xpath("//div[@id='pager']/a[last()]/@href").extract_first("")
        #     item['url'] = self.start_urls[0] + next_url
        #     yield Request(url=parse.urljoin(response.url, next_url), meta={"item": item},callback=self.parsenums,dont_filter=True)
        # else:
        #     return

    def parsenums(self, response):
        item = response.meta.get("item", "")
        yield item
        # 提取下一页并交给scrapy进行下载
        next_url = response.xpath("//div[@id='pager']/a[last()]/text()").extract_first("")
        if next_url == "Next >":
            next_url = response.xpath("//div[@id='pager']/a[last()]/@href").extract_first("")
            item['url'] = self.start_urls[0] + next_url
            yield Request(url=parse.urljoin(response.url, next_url), meta={"item": item},callback=self.parsenums,dont_filter=True)
        else:
            return

