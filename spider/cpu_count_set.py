# 获取cpu 个数
from multiprocessing import cpu_count,Pool
import time
import threading

lock = threading.Lock()     # 全局资源锁

def urls_crawler(url):
    try:
        with lock:
            print("获取地址：",url)

            
    except Exception as e:
        print(e)
 
if __name__ == "__main__":
    urls = ['http://mmjpg.com/mm/{cnt}'.format(cnt=cnt)
            for cnt in range(1, 50)]
    pool = Pool(processes=cpu_count())
    try: 
        pool.map(urls_crawler, urls)
    except Exception:
        time.sleep(30) 
        pool.map(urls_crawler, urls)
  