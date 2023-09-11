# 通过cpu处个数
from multiprocessing import cpu_count,Pool
import time
import threading

lock = threading.Lock()     # 全局资源锁

def urls_crawler(url):
    """
        处理数据信息
    """
    try:
        with lock:
                    
            print("获取地址：",url)
            
    except Exception as e:
        print(e)
 
if __name__ == "__main__":

    url = 'http://mmjpg.com/mm/{cnt}'

    urls = [url.format(cnt=cnt)
            for cnt in range(1, 50)]
    pool = Pool(processes=cpu_count())
    try: 
        pool.map(urls_crawler, urls)
    except Exception:
        time.sleep(30) 
        pool.map(urls_crawler, urls)
  