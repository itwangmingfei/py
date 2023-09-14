from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
import random
import re
from Taozi_cms import taozi

class taozidetail:
    def __init__(self, dom = taozi()):         
        self.driver = dom.driver
    
    def run(self,video_id):
        video_id = str(video_id)
        url = 'https://uu1idi.vip/#/detail?id='+ str(video_id)
        window_before = self.driver.window_handles[0]
        js = 'window.open("' + url + '")'
        self.driver.execute_script(js)        
        # 切换新窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 执行页面刷新
        self.driver.refresh()        
        print("handle跳转{0} = {1}".format(window_before,self.driver.window_handles[1]))
        time.sleep(12)
        # 向下滚动500像素
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        # 滚动到底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 标题
        title = self.driver.find_element(By.XPATH, "//body/div[@id='app']/section[@class='el-container is-vertical']/main[@class='el-main']/div[@class='detail']/div[@class='box']/div[@class='maxWidth el-row']/div/div[@class='operation']/ul[@class='operation-bottom']/li[1]").text
        # 类型
        typeinfo = self.driver.find_element(By.XPATH,"//body/div[@id='app']/section[@class='el-container is-vertical']/main[@class='el-main']/div[@class='detail']/div[@class='box']/div[@class='maxWidth el-row']/div/div[@class='operation']/ul[@class='operation-bottom']/li[2]").text
        # 简介
        content =  self.driver.find_element(By.XPATH,"//body/div[@id='app']/section[@class='el-container is-vertical']/main[@class='el-main']/div[@class='detail']/div[@class='box']/div[@class='maxWidth el-row']/div/div[@class='operation']/ul[@class='operation-bottom']/li[4]").text
        # 播放量
        looknums = self.driver.find_element(By.XPATH,"//body/div[@id='app']/section[@class='el-container is-vertical']/main[@class='el-main']/div[@class='detail']/div[@class='box']/div[@class='maxWidth el-row']/div/div[@class='operation']/ul[@class='operation-bottom']/li[3]/span[1]").text

        print(f"获取视频名称:{title} 获取视频类型：{typeinfo} 获取简介：{content} 获取播放量：{looknums}")
        ajax_requests = self.driver.requests
        for request in ajax_requests:
            if request.response:
                _url = request.url
                if re.search(r'index\.m3u8', _url):
                    print("获取视频地址：",_url)
        self.driver.close()
        self.driver.switch_to.window(window_before)
        videoinfo = {"title":title,'type':typeinfo,'des':content,'loocnums':looknums}
        return videoinfo

if __name__ == "__main__":
    tdom_dr = taozi()
    tdom_dr.login()
    tdom = taozidetail(tdom_dr)
    title = tdom.run(102191)
    print(title)
    
    while 1:
        time.sleep(5000)