from bs4 import BeautifulSoup  #导入Beautiful Soup
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
beautifulobj = BeautifulSoup(html_doc,'lxml')  #指定lxml解析器解析
print(beautifulobj.prettify()) #打按照lxml格式打印
