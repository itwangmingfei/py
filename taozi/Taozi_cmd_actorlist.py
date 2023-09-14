import time
from Taozi_cms import taozi
from selenium.webdriver.common.by import By
from util_page import pageutil

class actorlist:
    def __init__(self,dom = taozi()):
        self.driver = dom.driver       
    def getpagecount(self):
        # 分页采集视频播放地址
        pageutilmodel = pageutil()
        # 获取分类对应视频页码数量   
        driver = self.driver
        pageinfo = driver.find_element(By.XPATH,"/html[@class=' ']/body/div[@id='app']/section[@class='el-container is-vertical']/main[@class='el-main']/div[@class='actorDetail']/div[@class='maxWidth']/div[@class='el-pagination is-background']")

        page = pageinfo.find_elements(By.CSS_SELECTOR,"li.number")
        endpage = 0
        for index, event in enumerate( page ,start= 1):
            endpage = event.text
        print(f"共计获取页码数量：{endpage}")

        # 循环页码 开始页码为2
        middlenums = 1
        pageindex = 1 

        for i in range(int(endpage)):
            # 获取页面数据信息
            returndata = self.getactorlist()
            print(returndata)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 翻页处理
            if middlenums == 1:
                middlenums = middlenums +1
                continue

            pageindex = int(pageutilmodel.getpageindex(int(endpage),int(middlenums),int(pageindex)))
            time.sleep(1)
            pageevent = pageinfo.find_element(By.XPATH,"//li[@class='number'][{0}]".format(pageindex))
            print(f"共计页码{endpage},当前页码：{middlenums} 索引页码：{pageindex} 返回当前页码{pageevent.text}")    
            print(f'获取初始化索引：{pageindex} ')
            time.sleep(1)
            pageevent.click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(1)
            middlenums = middlenums +1

        return endpage

    def getactor(self,actorid):
        # 初始化方法
        self.actorid = actorid
        driver = self.driver
        driver.get(f"https://uu1idi.vip/#/actorDetail?id={str(actorid)}")
        # 标记开始页面
        self.homeHandel = driver.window_handles[0]
        self.driver.maximize_window()
        time.sleep(5)
        
        driver.implicitly_wait(30)
        return 
    def getactorlist(self):
        # 获取一页对应视频访问地址
        driver = self.driver
        time.sleep(2)
        divcard = driver.find_elements(By.CSS_SELECTOR,"div.card")
        # 获取视频数量展示
        divcount = len(divcard)
        print(f"获取视频数量{divcount}")
        videinfo = []
        for index,card in enumerate( divcard,start= 1):
            
            # 点击图片打开一个新页面
            imgevent = card.find_element(By.TAG_NAME,'img')
            imgevent.click()
            driver.switch_to.window(driver.window_handles[1])
            # 获取演员对应的视频id
            url = driver.current_url
            driver.close()
            # 返回主页面
            driver.switch_to.window(self.homeHandel)
            info = {'actorid':self.actorid,'url':url}
            print(f"第 {index} 个 {url}")
            videinfo.append(info)
        return videinfo

if __name__ == "__main__":
    actorlistdom = actorlist()
    # 初始化
    actorlistdom.getactor(40446)
    # 执行分野获取数据
    actorlistdom.getpagecount()


