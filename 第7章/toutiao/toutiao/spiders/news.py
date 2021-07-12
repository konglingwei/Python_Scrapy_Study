import scrapy
from selenium import webdriver
from scrapy import Request
from urllib import parse
# 导入Item模块
from toutiao.items import NewsItem
# 导入时间模块
import time
class NewsSpider(scrapy.Spider):
	# 定义爬虫名称
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    start_urls = ['https://www.toutiao.com']
    # 数据解析方法
    def parse(self, response):
        # 设置浏览器的无界面状态
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # 启动webdrive
        brower = webdriver.Chrome(executable_path="E:/Linda/python37/chromedriver.exe", chrome_options=options)
        brower.get(response.url)
        time.sleep(3)
        brower.maximize_window()  # 最大化窗口
        time.sleep(3)
        brower.find_element_by_link_text('科技').click()
        post_url = "/ch/news_tech/"
        time.sleep(3)
        # 下拉3次
        for i in range(3):
             # 鼠标下拉，启用script
            brower.execute_script('window.scrollTo(0,1000)')
            i+=1
            print('下拉次数：',i)
            time.sleep(5)
            brower.execute_script("window.scrollTo(0,document.body.scrollHeight-100);var lensOfPage=document.body.scrollHeight-100;return lensOfPage")
            time.sleep(5)
        yield Request(url=parse.urljoin(response.url, post_url),meta={"brower":brower},callback=self.get_info)

    # 获取页面新闻标题，详情页面链接，来源，评论，加入时间并添加到列表中
    def get_info(self,response):
        title_list = []
        toutiao_item = NewsItem()
        # 声明浏览器对象
        brower= response.meta.get("brower", "")
        # 获取页面新闻标题
        titles = brower.find_elements_by_xpath('//div[@class="title-box"]/a')
        for title in titles:
            title_list.append(title.text)
        # 计算获取到所有文章标题的条数
        lens = len(title_list)
        for i in range(lens):
            i+=1
            j = str(i)
            # 获取详情页面链接
            urls_num = brower.find_elements_by_xpath('//*[@class="wcommonFeed"]//li['+j+']//div[@class="title-box"]/a')
            for num in urls_num:
                url_num = num.get_attribute('href')
                toutiao_item['article_url']= url_num
            # 获取来源
            try:
                sources = brower.find_elements_by_xpath('//*[@class="wcommonFeed"]//li['+j+']//a[@class="lbtn source"]')
                for source in sources:
                    kk = source.text
                    ss = kk.replace(" ⋅", "")
                    toutiao_item['article_source'] = ss
            except:
                toutiao_item['article_source'] = ""
            # 获取评论
            comments = brower.find_elements_by_xpath('//*[@class="wcommonFeed"]//li['+j+']//a[@class="lbtn comment"]')
            for comment in comments:
                toutiao_item['pinglun'] = comment.text
            # 获取加入时间
            dates = brower.find_elements_by_xpath('//*[@class="wcommonFeed"]//li['+j+']//span[@class="lbtn"]')
            for times in dates:
                toutiao_item['create_date'] = times.text
            # 获取页面新闻标题
            titles2 = brower.find_elements_by_xpath('//*[@class="wcommonFeed"]//li['+j+']//div[@class="title-box"]/a')
            for title1 in titles2:
                toutiao_item['title'] = title1.text
			# 抓取的数据上传到toutiao_item
            yield toutiao_item

