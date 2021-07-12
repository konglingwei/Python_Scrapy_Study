from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>Test BeautifulSoup</title></head>
<body>
<p class="title"><b>Test BeautifulSoup</b></p>
<p class="test">Well come to Qingying!
<a href="https://www.qingyimgtech.com/top" id="link1">Top</a>,
<a href="https://ewww.qingyimgtech.com/middle" id="link2">Middle</a> and
<a href="https://www.qingyimgtech.com/bottom" id="link3">Bottom</a>;
</p>
<p class="other">...</p>
"""
soup = BeautifulSoup(html_doc,'html.parser')
links = soup.find_all('a')
print('获取所有的链接：')
for link in links:
    print(link.name,link['href'],link.get_text())
print('获取Middle的链接，正则匹配:')
link_node = soup.find('a',href=re.compile(r"tom"))
print(link_node.name,link_node['href'],link_node.get_text())
print('获取p段落的文字，class="title"的文字')
p_node = soup.find('p',class_="title")
print(p_node.name,p_node.get_text())
