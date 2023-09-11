import requests


###############################get
url = 'http://baidu.com'
response = requests.get(url)
print(response)

data = {
    'name': '编程帮',
    'url': "www.biancheng.net"
}
response = requests.get('http://httpbin.org/get', params=data)

print(response.text)


###################################post
url = 'https://fanyi.baidu.com'
data = {'from': 'zh',
        'to': 'en',
        'query': '编程帮www.biancheng.net你好'
        }
response = requests.post(url, data=data)
print(response)


#############################get 
response = requests.get('http://www.baidu.com')

print('获取网页编码') 
print(response.encoding)

print('设置网页编码')
response.encoding="utf-8"    #更改为utf-8编码

print('打印状态码')
print(response.status_code)  # 打印状态码

print('打印请求url')
print(response.url)          # 打印请求url

print('打印头信息')
print(response.headers)      # 打印头信息
print('打印cookie信息')
print(response.cookies)      # 打印cookie信息

print('以字符串形式打印网页源码')
print(response.text)  #以字符串形式打印网页源码

print('以字节流形式打印')
print(response.content) #以字节流形式打印