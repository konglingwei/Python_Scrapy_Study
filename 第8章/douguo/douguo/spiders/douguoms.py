# -*- coding: utf-8 -*-
import scrapy
# 导入json模块
import json
import time
from urllib import parse
from douguo.items import DouguoItem
class DouguoSpider(scrapy.Spider):
    name = 'douguo'
    allowed_domains = ['api.douguo.net']
    start_urls = ['http://api.douguo.net/']
    # 获取http://api.douguo.net/recipe/flatcatalogs信息
    def start_requests(self):
        url_no1 = 'http://api.douguo.net/recipe/flatcatalogs'
        data = {
            "client":"4",
            "_vs":"2305",
            "sign_ran":"b103409281b81561400c949067802643",
            "code":"de36699c41aefda2",
        }
		#定义URL按照POST方法提交
        yield scrapy.FormRequest(url=url_no1, formdata=data, callback=self.parse)
    # 查询做过最多的菜谱
    def parse(self, response):
        print('url:',response.url) #http://api.douguo.net/recipe/flatcatalogs
        print("konglw response.text")
        print(response.text)
        url_search = '/recipe/v2/search/0/20'
        print("konglw response.body")
        print(response.body.decode())
        node_list = json.loads(response.body.decode())["result"]["cs"]
        print("node_list")
        print(node_list)
        if not node_list:
            return
        else:
            for node in node_list:
                for index in node['cs']:
                    for last in index['cs']:
                        # 输入http://api.douguo.net/recipe/v2/search/0/20的Post发送的数据
                        data2 = {
                            "client": "4",
                            "keyword": last["name"],
                            "order":"3",
                            "_vs":"11104",
                            "type":"0",
                            "auto_play_mode":"2",
                            "sign_ran":"8684b7e782350b7f4afe1c10d5bd084b",
                            "code":"8b016ce8f25a621a",
                        }
                        time.sleep(5)
					#定义URL按照POST方法提交
                        yield scrapy.FormRequest(url=parse.urljoin(response.url,url_search),formdata=data2, meta={"data2":last["name"]},callback=self.caipu_list)
    # 查询豆果美食具体信息
    def caipu_list(self,response):
        douguo_item = DouguoItem()
        # 获取返回的json数据
        print("konglw response.body.decode() 2")
        print(response.body.decode())
        url_searchs = json.loads(response.body.decode())['result']['list']
        print("konglw url_searchs")
        print(url_searchs)
        name = response.meta.get("data2", "")
        print("konglw name")
        print(name)
        if name=='土豆':
            for neirong in url_searchs:
                try:
                    nr = neirong['r']
                    douguo_item['author'] = nr['an']
                    douguo_item['dish_name'] = nr['n']
                    douguo_item['cook_story'] = nr['cookstory']
                    douguo_item['cook_time'] = nr['cook_time']
                    douguo_item['cook_difficult'] = nr['cook_difficulty']
                    douguo_item['rate'] = nr['rate']
                    douguo_item['peoples'] = nr['recommendation_tag']
                    yield douguo_item
                except:
                    # 若菜谱信息读取不到，则为广告
                    print("广告")
        else:
            return

