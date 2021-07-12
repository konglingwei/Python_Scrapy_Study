import scrapy
#引入items
from douban.items import DoubanItem
class MovieSpider(scrapy.Spider):
    #爬虫名
    name = 'movie'
    #允许的域名
    allowed_domains = ['movie.douban.com/top250']
    #入口url
    start_urls = ['https://movie.douban.com/top250']
    #解析start_urls的内容，默认的解析方法
    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        #循环电影的条目
        for i_item in movie_list:
            #item文件导进来
            douban_item = DoubanItem()
            #在当前xpath进一步细分,需要加一个点. 并解析到它第一个数据extract_first("")
            douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first("")
            douban_item['movie_name'] = i_item.xpath(".//div[@class='hd']//span[1][@class='title']/text()").extract_first("")
            douban_item['star'] = i_item.xpath(".//div[@class='star']/span[2]/text()").extract_first("")
            # 获取电影的介绍
            count = i_item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for i_count in count:
                # 去掉字符串的空格
                count_s = "".join(i_count.split())
                douban_item['movie_introduce'] = count_s
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first("")
            douban_item['describe'] = i_item.xpath(".//div[@class='bd']//span[@class='inq']/text()").extract_first("")
            # 将数据yield到piplines里去（在那里进行数据的清洗和存储）
            yield douban_item
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        #查询下一页是否有链接则取，无链接就不取
        if next_link:
            next_link = next_link[0]
            # 通过循环的方式将待爬取的url添加到scrapy中
            # 回调自己,使用Request的参数dont_filter=True,这样request的地址和allow_domain里面的冲突而不会被过滤
            yield scrapy.Request("https://movie.douban.com/top250" + next_link,callback=self.parse,dont_filter=True)
