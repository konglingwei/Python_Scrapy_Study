from lxml import etree
import requests
res = requests.get('https://news.cnblogs.com/')
res.encoding = 'utf-8'
html_data = res.text
html = etree.HTML(html_data)
result = html.xpath('//*[@id="entry_654172"]/div[2]/h2/a/text()')[0]
print(result)
