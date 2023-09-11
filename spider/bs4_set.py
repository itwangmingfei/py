#coding:utf8
html_doc = """
<html><head><title>"c语言中文网"</title></head>
<body>
<p class="title"><b>c.biancheng.net</b></p>
<p class="website">一个学习编程的网站
<a href="http://c.biancheng.net/python/" id="link1">python教程</a>
<a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
#prettify()用于格式化输出html/xml文档
#print(soup('a'))

#print(soup.find('a'))

#print(soup.findAll('p'))

#print(soup.findAll('a'))

for tag in soup.find_all('a'):
    datainfo = tag.attrs
    href = datainfo['href']
    id = datainfo['id']
    print("获取数据a标签数据 id:{0}  url：{1}".format(id,href))
