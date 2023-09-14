from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time

proxy_address = "127.0.0.1"
proxy_port = 9090
user = "qq97770"
pwd = "wmf521"

class taozi:
    def __init__(self,proxy_address = proxy_address,proxy_port = proxy_port):
        # 创建Chrome WebDriver选项
        chrome_options = webdriver.ChromeOptions()
        # 设置代理服务器地址和端口
        # 将代理设置添加到Chrome选项中
        chrome_options.add_argument(f'--proxy-server={proxy_address}:{proxy_port}')
        # 创建Chrome WebDriver实例
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(30)

    def login(self):
        # 访问一个网站
        self.driver.get("https://uu1idi.vip/#/setting")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div[4]/ul/li[3]/div/div/img').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH,'//body/ul/div/div[2]').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH,'//div[@id="tab-account"]').click()
        self.driver.implicitly_wait(30)
        username = self.driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='phone']//input")
        password = self.driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='pwd']//input")
        self.driver.implicitly_wait(30)
        username.send_keys(user)
        password.send_keys(pwd)
        time.sleep(1)
        # 执行登录操作
        self.driver.find_element(By.XPATH, "//div[@class='smsWithAccount']//button").click()


if __name__ == "__main__":
    dom = taozi()
    dom.login()
    dom.driver.quit()