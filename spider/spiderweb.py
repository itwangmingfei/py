from urllib import request,parse
# 1.拼url地址
url = 'http://www.baidu.com/s?wd={}'
word = input('请输入搜索内容:')
params = parse.quote(word)
full_url = url.format(params)
# 2.发请求保存到本地
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
req = request.Request(url=full_url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
# 3.保存文件至当前目录
filename = word + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)