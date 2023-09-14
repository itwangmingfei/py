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
log = driver.get("https://uu1idi.vip/#/setting")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div[4]/ul/li[3]/div/div/img').click()
time.sleep(4)
driver.find_element(By.XPATH,'//body/ul/div/div[2]').click()

time.sleep(2)
driver.find_element(By.XPATH,'//div[@id="tab-account"]').click()
time.sleep(2)
username = driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='phone']//input")
password = driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='pwd']//input")
username.send_keys("qq97770")
password.send_keys("wmf521")
#
driver.find_element(By.XPATH, "//div[@class='smsWithAccount']//button").click()
# 进行其他操作...

# 关闭WebDriver
##driver.quit()
i = 1
while(True):
    i = i+1
    if i > 500:
        break
    time.sleep(2)
    print(i)