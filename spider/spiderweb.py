from urllib import request
from fake_useragent import UserAgent

picurl = 'http://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/400'

ua = UserAgent()

head = ua.random
print(picurl) 
print(head)

headers = {'User-Agent':head}

req = request.Request(url=picurl,headers=headers)
res = request.urlopen(req)
html = res.read().decode("utf-8")

filename =  'a.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)