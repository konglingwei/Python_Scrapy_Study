# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy import Request
import re
from weibo.items import WeiboItem
class KeysSpider(scrapy.Spider):
    name = 'keys'
    allowed_domains = ['www.weibo.com']
    start_urls = ['https://www.weibo.com/']
    def parse(self, response):
        # 实例化driver
        driver = webdriver.Chrome(executable_path="E:\Python\chromedriver_win32 (1)\chromedriver.exe")
        driver.get(self.start_urls[0])
        time.sleep(3)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(20)
        print(driver.title)
        driver.find_element_by_name("username").send_keys("孔令威")
        driver.find_element_by_name("password").send_keys("1516156161611")
        # driver.find_element_by_css_selector("#loginname").send_keys("用户名")
        # driver.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("密码")
        driver.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()
        time.sleep(5)
        keys = '科比'
        driver.find_element_by_css_selector(".gn_search_v2 input[node-type='searchInput']").send_keys(keys)
        time.sleep(5)
        driver.find_element_by_css_selector(".gn_search_v2 a[node-type='searchSubmit']").click()
        time.sleep(20)
        urls = driver.find_elements_by_xpath("//*[@class='m-page']//ul/li/a") #有误
        for last in urls:
            # 提取下一页并交给scrapy进行下载
            hh = last.get_attribute('href')
            jk = Request(hh, callback=self.nexttext,meta = {'driver':driver},dont_filter=True)
            yield jk
    def nexttext(self,response):
        weibo_item = WeiboItem()
        # 获取driver
        drivers = response.meta['driver']
        last = response.url
        print('response.url: ',last)
        drivers.get(last)
        time.sleep(3)
        # 最大化窗口
        drivers.maximize_window()
        time.sleep(20)
        urlss = drivers.find_elements_by_xpath("//*[@class='m-page']//a")
        lasts = urlss[-1].get_attribute('href')
        print('urlss:', lasts)
        urls = drivers.find_elements_by_xpath("//*[@class='m-page']//a")
        last = urls[-1].get_attribute('href')
        kk = drivers.find_elements_by_xpath("//*[@class='s-scroll']/li/a")
        print('dangqian:', kk[-1].get_attribute('href'))
        ss = kk[-1].get_attribute('href')
        gg = re.findall(r".*page=(.+)", ss)
        print(gg[0])
        now = drivers.find_element_by_xpath("//*[@class='list']//a[@class='pagenum']").text
        print(now)
        a = now.split()  # split依照空格把字符串分为一个列表
        direcor = a[0]
        dd = re.findall(r"第(.+?)页", direcor)
        print('dd: ', dd[0])
        length = len(urls) - 2
        lastno2 = urls[-1].get_attribute('href')
        print(lastno2)
        if int(dd[0]) <= 5:
            print('ddd: ',dd[0])
            texte = drivers.find_elements_by_xpath("//*[@class='card-wrap']")
            for msge in texte:
                # 获取博主id
                try:
                    nre = msge.find_element_by_xpath(".//div[@class='content']/div[@class='info']//div/a[@class='name']").text
                    weibo_item['title'] = nre.strip()
                    time.sleep(1)
                except Exception as e:
                    print(e)
                # 获取文章
                try:
                    content = msge.find_element_by_xpath(".//div[@class='content']//p[@node-type='feed_list_content']").text
                    weibo_item['content'] = content.strip()
                except Exception as e:
                    print(e)
                # 获取评论
                try:
                    pinglun = msge.find_element_by_xpath(".//div[@class='card-act']//li[3]").text
                    weibo_item['pinglun'] = pinglun.strip()
                except Exception as e:
                    print(e)
                # 获取转发数
                try:
                    zhuanfa = msge.find_element_by_xpath(".//div[@class='card-act']//li[2]").text
                    weibo_item['zhuanfa'] = zhuanfa.strip()
                except Exception as e:
                    print(e)
                # 获取点赞数
                try:
                    hot = msge.find_element_by_xpath(".//div[@class='card-act']//li[4]").text
                    weibo_item['hot'] = hot.strip()
                except Exception as e:
                    print(e)
                # 获取时间
                try:
                    datetime = msge.find_element_by_xpath(".//div[@class='content']/p[@class='from']/a[@target='_blank']").text
                    weibo_item['datetime'] = datetime.strip()
                except Exception as e:
                    print(e)
                time.sleep(5)
                print('weibo_item_no2: ', weibo_item)
                yield weibo_item
        else:
            return

