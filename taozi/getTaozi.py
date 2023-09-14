from browsermobproxy import Server

import json
import time
import re
import urllib
import requests
import sys
import pymysql
from selenium.webdriver.common.by import By
import random
from seleniumwire import webdriver as wiredriver

import  traceback
class updatem3u8Url:
    def __init__(self):
        self.web = 1
        chrome_options = wiredriver.ChromeOptions()

        chrome_options = {
            'proxy': {
                'http': 'http://localhost:10809',  # 用你的实际代理地址和端口替换
                'https': 'https://localhost:10809',  # 同样用实际地址和端口替换
                'no_proxy': 'localhost,127.0.0.1'  # 可选，指定不使用代理的地址
            }
        }


        self.driver = wiredriver.Chrome(options=chrome_options)
        # chrome_options.add_argument('--proxy-server=system')
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.login()

    def login(self):



            self.driver.get("https://uu1idi.vip/#/setting")
            self.driver.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div[4]/ul/li[3]/div/div/img').click()
            self.driver.find_element(By.XPATH,'//*[@id="tab-account"]').click()
            time.sleep(1)
            # self.driver.find_element(By.XPATH,
            #                          "//ul[@class='el-dropdown-menu el-popper']//div[@style='font-size: 14px; cursor: pointer;']").click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, "//div[@id='tab-account']").click()
            # time.sleep(1)
            username = self.driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='phone']//input")
            password = self.driver.find_element(By.XPATH, "//div[@id='pane-account']//div[@class='pwd']//input")
            username.send_keys("zhutousan")
            password.send_keys("zhutousan")
            #
            self.driver.find_element(By.XPATH, "//div[@class='smsWithAccount']//button").click()

    def mysql_db(self, sql):
        # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
        db = pymysql.connect(
            user='api_api',  # 用户名
            password='JNjALHPJz87SpfSn',  # 密码：这里一定要注意123456是字符串形式
            host='18.162.149.234',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
            database='api_api',  # 数据库的名字
            port=3306,  # 指定端口号，范围在0-65535
            charset='utf8mb4',  # 数据库的编码方式
        )
        cursor = db.cursor()

        res = cursor.execute(sql)
        print('-------------db save result-------------')
        print(res)
        db.commit()

        # 最后我们关闭这个数据库的连接
        db.close()

    def run(self, video_id):


        video_id = str(video_id)
        url = 'https://uu1idi.vip/#/detail?id='+ str(video_id)



        window_before = self.driver.window_handles[0]
        js = 'window.open("' + url + '")'
        self.driver.execute_script(js)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        ajax_requests = self.driver.requests
        for request in ajax_requests:
            print(request)
            if request.response:
                _url = request.url

                matchObj = re.match(r'.*?index.m3u8', _url, re.M | re.I)
                if matchObj:
                    print(_url)

        # driver.close()
        time.sleep(random.randint(10, 15))
        # result = self.proxy.har
        # for entry in result['log']['entries']:
        #     _url = entry['request']['url']
        #     matchObj = re.match(r'.*?index.m3u8', _url, re.M | re.I)
        #     if matchObj:
        #         sql = "update ms_video set url='%s',download_url='%s',origin_url ='%s',url_status=1 where video_id ='%s'" % (_url, _url, _url,video_id)
        #         print(sql)
        #         self.mysql_db(sql)
        self.driver.switch_to.window(window_before)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



def do_db(sql):
    # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
    db = pymysql.connect(
        user='api_api',  # 用户名
        password='JNjALHPJz87SpfSn',  # 密码：这里一定要注意123456是字符串形式
        host='18.162.149.234',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
        database='api_api',  # 数据库的名字
        port=3306,  # 指定端口号，范围在0-65535
        charset='utf8mb4',  # 数据库的编码方式
    )
    cursor = db.cursor()
    try:
        num = cursor.execute(sql)
        result = {'num':num,'cursor':cursor}
        db.commit()
        return result
    except Exception as e:
        print(e)
        # 回滚
        db.rollback()
    # 最后我们关闭这个数据库的连接
    db.close()


while(True):

        # sql = "select video_id from ms_video where origin=2 and url_status=0"
        #
        try:
        # res = do_db(sql)
            res = [150871]
            obj = updatem3u8Url()
            for item in res:
                obj.run(item)

        except Exception as e:
            print(e)
            traceback.print_exc()

            time.sleep(1000)


        time.sleep(10000)