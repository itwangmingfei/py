from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
# 创建Chrome WebDriver选项
chrome_options = webdriver.ChromeOptions()

# 设置代理服务器地址和端口
proxy_address = "127.0.0.1"  # 代理服务器的地址
proxy_port = 9090  # 代理服务器的端口

# 将代理设置添加到Chrome选项中
chrome_options.add_argument(f'--proxy-server={proxy_address}:{proxy_port}')
chrome_options.add_argument('--ignore-certificate-errors')

# 创建Chrome WebDriver实例
driver = webdriver.Chrome(options=chrome_options)

# 访问一个网站
log = driver.get("http://baidu.com")
time.sleep(5)
 
i = 1
while(True):
    i = i+1
    if i > 500:
        break
    time.sleep(2)
    print(i)