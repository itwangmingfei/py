import os
import re
import requests
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import os
import time

import requests
import re

import threading

import oss2
import concurrent.futures
import os
import pymysql
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import requests
import random
def getIp():
    url = 'https://ip.hj10.com/ip.txt'

    response = requests.get(url)

    if response.status_code == 200:
        # 获取响应内容并打印
        ip_port_str = response.text
        ip_port_str = ip_port_str.rstrip('\n')
        ip_port_list = ip_port_str.split('\n')

        ip = random.choice(ip_port_list)
        return ip

    else:
        print(f'请求失败，状态码：{response.status_code}')

headers = {
            'Accept': '*/*',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,de;q=0.7,fr;q=0.6,es;q=0.5,ar;q=0.4,zh-TW;q=0.3',
            'Connection': 'keep-alive',
            'Origin': 'null',
            'Referer': 'https://livepush.io/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }


headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]


def get_url(url):
    print(url)
    proxy = {
        'http': 'http://'+getIp(),  # 如果您的代理是HTTP代理
        #'https': 'https://'+getIp(),  # 如果您的代理是HTTPS代理
    }
    headers = random.choice(headers_list)
    try:

        response = requests.get(url, headers=headers, timeout=10,verify=False,proxies=proxy)  # 超时设置为10秒
    except:
        for i in range(4):  # 循环去请求网站
            response = requests.get(url, headers=headers, timeout=20,verify=False,proxies=proxy)
            if response.status_code == 200:
                break
    html_str = response
    return html_str


def do_db(sql):
    # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
    db = pymysql.connect(
        user='source',  # 用户名
        password='87758258',  # 密码：这里一定要注意123456是字符串形式
        host='16.162.114.9',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
        database='source',  # 数据库的名字
        port=3306,  # 指定端口号，范围在0-65535
        charset='utf8mb4',  # 数据库的编码方式
    )

    cursor = db.cursor()
    try:
        num = cursor.execute(sql)
        result = {'num': num, 'cursor': cursor}
        db.commit()
        print(result)
        return result
    except Exception as e:
        print(e)
        # 回滚
        db.rollback()
    # 最后我们关闭这个数据库的连接
    db.close()
class DownloadTSFile:

    def __init__(self, m3u8_url, save_dir,origin):


        pattern = r'/([a-zA-Z0-9]+)\.m3u8$'
        match1 = re.search(pattern, m3u8_url)
        video_id = match1.group(1)
        self.origin = origin
        self.video_id = video_id
        self.path = save_dir + video_id
        self.m3u8_url = m3u8_url
        save_dir = os.path.join(save_dir, video_id)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        self.download_ts_files(m3u8_url, save_dir, 1)
        self.download_key_file(m3u8_url)
        self.convert_m3u8(m3u8_url)


    def download_ts_file(self, ts_url, save_path):



        # proxy = {
        #     'http': 'http://'+getIp(),  # 如果您的代理是HTTP代理
        #     #'https': 'https://'+getIp(),  # 如果您的代理是HTTPS代理
        # }
        # print(proxy)


        #response = requests.get(ts_url, headers=headers, verify=False)

        response = get_url(ts_url)
        # seconds = random.randint(1, 10)
        time.sleep(3)
        print(response.status_code)



        if response.status_code==200:
            ts_filename = os.path.basename(ts_url)
            ts_filepath = os.path.join(save_path, ts_filename)

            with open(ts_filepath, 'wb') as f:
                f.write(response.content)

    def download_key_file(self,m3u8_url):
        resp = requests.get(m3u8_url, timeout=(3, 7))
        uri_pattern = r'URI="([^"]+)"'
        uri_match = re.search(uri_pattern, resp.text)

        if uri_match:
            key_uri = uri_match.group(1)
            print(key_uri)
            key_file_name = key_uri.split('/')[-1]
            # resp = requests.get(key_uri, timeout=(3, 7))
            # with open(self.path+'/key.php', 'w', encoding='utf-8') as f:
            #     f.write(resp.text)
            with urllib.request.urlopen(key_uri) as response:
                # 读取文件内容
                file_content = response.read()
                print(file_content)
                # 保存文件
                with open(self.path + f'/{key_file_name}', 'wb') as file:
                    file.write(file_content)
        else:
            print("URI not found in the M3U8 file.")
    def download_ts_files(self, m3u8_url, save_path, max_workers=1):
        # 发送HTTP请求获取M3U8文件内容



        # 获取 M3U8 文件内容
        response = requests.get(m3u8_url)
        m3u8_content = response.text

        # 解析出 TS 文件链接
        ts_urls = []
        lines = m3u8_content.split('\n')
        for line in lines:
            line = line.strip()
            if line.endswith('.ts'):
                ts_urls.append(line)
        print(ts_urls)
        # for ts_url in ts_urls:
        #     self.download_ts_file(ts_url, save_path)
        # 并发下载 TS 文件

        for ts_url in ts_urls:
            self.download_ts_file(ts_url, save_path)

        print('TS 文件下载完成！')

    def convert_m3u8(self, url):
        m3u8_path = self.path + '/' + self.video_id + '.m3u8'
        print(url)
        resp = requests.get(url, timeout=(3, 7))
        content = resp.text
        pattern = r'URI="([^"]+)"'
        match = re.search(pattern, content)

        # 检查是否找到匹配
        if match:
            first_match = match.group(1)
            key_file_name = first_match.split('/')[-1]
            print(key_file_name)
            content = re.sub(r'URI="([^"]+)"', f'URI="{key_file_name}"', content)
        else:
            print("未找到匹配项")


        lines = content.split('\n')
        filtered_lines = []
        for line in lines:
            line = line.replace("\r", "")
            if line.strip().endswith('.ts'):
                line_parts = line.split("/")
                ts_url = line_parts[-1]
                filtered_lines.append(ts_url)
            else:
                filtered_lines.append(line)

        output_text = '\n'.join(filtered_lines)
        with open(m3u8_path, 'w') as f:
            f.write(output_text)
        self.download_pilot_file(output_text)


    def download_pilot_file(self,m3u8_content):

        lines = m3u8_content.splitlines()
        new_lines = []
        duration = 0
        for line in lines:
            if line.startswith('#EXTINF'):
                # 提取TS片段UR
                duration_str = line.split(':')[1].split(',')[0]
                duration += int(float(duration_str))
                if (duration > 30):
                    break
            new_lines.append(line)
        new_lines.append('#EXT-X-ENDLIST')
        m3u8_content = '\n'.join(new_lines)
        new_m3u8_file = self.path+'/pilot.m3u8'
        with open(new_m3u8_file, 'w') as f:
            f.write(m3u8_content)




# 设置M3U8文件的URL和保存目录
# save_dir = "C:/ant/"
#
# url = 'https://dfqapp.oss-cn-hongkong.aliyuncs.com/longvideo/temp/antzrLvYERYylnvqda.m3u8'
# #url = 'https://dfqapp.oss-cn-hongkong.aliyuncs.com//short/9ZE/antDqm6ErOVJyqM9ZE/pilot.m3u8'
# DownloadTSFile(url, save_dir, 'ant')

save_dir = "C:/ant/"
while(True):

    select_query = "SELECT url,origin from ms_video where origin='ant' and url like '%/temp/%' order by id desc"
    res = do_db(select_query)
    result = res['cursor'].fetchall()

    for row in result:
        print(row[0])
        DownloadTSFile(row[0], save_dir,row[1])
    time.sleep(1)

