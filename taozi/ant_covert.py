import os
import re
import requests
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import os
import time

import requests
import re
import mysql.connector
import threading

import oss2
import concurrent.futures
import os
import pymysql
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor


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
        header_for_taozi = {
            'Host': 'tigers.mcszzw.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19',
            'sec-ch-ua-platform': '',
            'Accept': '*/*',
            'Origin': 'https://vyf2ll7bqgrdyi.xyz',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://vyf2ll7bqgrdyi.xyz/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        if(origin=='taozi'):
            self.header = header_for_taozi
        else:
            self.header = []
        print(self.header)
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

        print(ts_url)

        response = requests.get(ts_url,headers= self.header,timeout=5)

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

        # for ts_url in ts_urls:
        #     self.download_ts_file(ts_url, save_path)
        # 并发下载 TS 文件
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for ts_url in ts_urls:
                executor.submit(self.download_ts_file, ts_url, save_path)

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


        ts_count_to_extract = 6
        ts_urls = []
        lines = m3u8_content.splitlines()
        new_lines = []
        for line in lines:
            if line.endswith('.ts'):
                # 提取TS片段UR
                ts_urls.append(line)
                if len(ts_urls)== ts_count_to_extract:
                    break
            new_lines.append(line)
        new_lines.append('#EXT-X-ENDLIST')
        m3u8_content = '\n'.join(new_lines)
        new_m3u8_file = self.path+'/pilot.m3u8'
        with open(new_m3u8_file, 'w') as f:
            f.write(m3u8_content)


access_key_id = 'LTAI5tJCtijofrY86ykuXfsC'
access_key_secret = '6ETOgPXiCrnjQsegu0FaLQdyKhpgAn'
endpoint = 'oss-cn-hongkong.aliyuncs.com'
bucket_name = 'dfqapp'

auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, 'https://' + endpoint, bucket_name)
def upload_file(file_path,remote_path):
    # try:
    #     file_name = file_path.split('/')[-1]  # 获取文件名
    #     with open(file_path, 'rb') as file:
    #         bucket.put_object(file_name, file)
    #     print(f"文件 {file_name} 上传成功！")
    # except oss2.exceptions.OssError as e:
    #     print(f"文件上传失败：{e}")


    local_file_path = file_path
    # oss_file_key = 'shortvideo/temp/'+file_name
    oss_file_key = remote_path
    print(oss_file_key)

    # 如果需要设置文件权限，可以使用以下参数
    # headers = {'x-oss-object-acl': 'public-read'}
    # #执行上传
    print(local_file_path)
    bucket.put_object_from_file(oss_file_key, local_file_path)

# 设置M3U8文件的URL和保存目录
save_dir = "C:/long/"
while(True):

    select_query = "SELECT pilot_url,video_id from ms_video where origin='ant' limit 3,1"
    res = do_db(select_query)
    result = res['cursor'].fetchall()

    for row in result:
        print(row[0])

        url = row[0]
        url ='https://dfqapp.oss-cn-hongkong.aliyuncs.com/'+url
        response = requests.get(url)

        if response.status_code == 200:
            m3u8_content = response.text
            print(m3u8_content)



            # 在这里进行您的修改，例如替换字符串
            modified_m3u8_content = m3u8_content.replace('https://td3.bmyy.work', 'https://t15.shnhyl.com.cn')
            #remote_path = row[0].replace('https://dfqapp.oss-cn-hongkong.aliyuncs.com/', '')

            remote_path = row[0][1:]
            print(remote_path)


            # 保存修改后的文件
            file_name ="C:/m3u8/"+row[1]+'.m3u8'
            with open(file_name, 'w') as f:
                f.write(modified_m3u8_content)
                upload_file(file_name,remote_path)

            print("M3U8文件已下载并修改完成。")
        else:
            print(f'下载失败，状态码：{response.status_code}')
        time.sleep(1000)
        #DownloadTSFile(row[0], save_dir,row[1])
    time.sleep(100)