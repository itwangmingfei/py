from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse,parse_qs
import json
from Taozi_cms import taozi


class actory:
    def __init__(self, dom = taozi()):
        self.driver = dom.driver  

    def get_actor(self):
        driver = self.driver
        # 访问一个网站
        driver.get("https://uu1idi.vip/#/actor")

        # 执行页面刷新
        driver.refresh()
        time.sleep(5)
        # 获取所有自模块
        driver.implicitly_wait(10)

        div_card_info =  driver.find_elements(By.CSS_SELECTOR, "div.card")
        returndata = []
        for index,div_card in  enumerate(div_card_info,start=1):
            print(index)
            div_elements = div_card.find_elements(By.CSS_SELECTOR, "div.card-item")
            # 一个模块滚动一下
            for image_elements in div_elements:  

                imginfo = image_elements.find_element(By.TAG_NAME,'img')
                img = imginfo.get_attribute('src')
                txtinfo = image_elements.find_element(By.TAG_NAME,'p').text
                # 点击图片获取类型ID
                time.sleep(1)
                imginfo.click()
                time.sleep(1)
                # 获取跳转域名地址
                current_url = driver.current_url
                # 替换特殊符号
                url  = current_url.replace('#',"a")
                parsed_url = urlparse(url)
                # 转数组
                query_parameters = parse_qs(parsed_url.query) 
                if 'id' in query_parameters:
                    id_value = query_parameters['id'][0]
        
                # 返回主页面
                driver.back()
                gedata = {"img":img,"lable":txtinfo,"class_id":id_value}
                print(gedata)
                returndata.append(gedata)
            # 滚动div
            driver.execute_script("arguments[0].scrollTop = 0;", div_elements)
        return returndata

if __name__ == "__main__":
    taozidom = taozi()
    dom = actory(taozidom)
    
    returndata = dom.get_actor()    
    d = [{"img": info['img'],"lable":info['lable'],"class_id":info['class_id'] } for info in returndata ]
    with open("actor.json", "w+") as f:
        json.dump(d, f)
