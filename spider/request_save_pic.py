import requests
import time

url = 'https://t7.baidu.com/it/u=1819248061,230866778&fm=193&f=GIF'

headers = {'User-Agent':'Mozilla/4.0'}
html = requests.get(url=url,headers=headers).content
#以二进制的方式下载图片
filename = int(time.time())

with open('./pic/{}.jpg'.format(filename),'wb') as f:
    f.write(html)