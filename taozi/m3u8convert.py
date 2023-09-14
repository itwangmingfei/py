import requests
import oss2
import os
def upload_oss(local_file_path, oss_file_key):
    # 配置 OSS 访问信息
    access_key_id = 'LTAI5tJCtijofrY86ykuXfsC'
    access_key_secret = '6ETOgPXiCrnjQsegu0FaLQdyKhpgAn'
    endpoint = 'oss-cn-hongkong.aliyuncs.com'
    bucket_name = 'dfqapp'

    # 创建 OSS 客户端
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    bucket.put_object_from_file(oss_file_key, local_file_path)
def getM3u8(url, video_id):
    response = requests.get(url)
    print(url)
    parts = url.split("/")
    pre = "/".join(parts[:-1])


    if response.status_code == 200:
        m3u8_content = response.text
    else:
        raise Exception(f"Failed to download M3U8 file. Status code: {response.status_code}")

    ts_urls = []
    lines = m3u8_content.splitlines()
    new_lines = []
    for line in lines:
        if line.find("encryption.key") != -1:
            line = line.replace("encryption.key", pre+"/encryption.key")
        if line.endswith('.ts'):
            # 提取TS片段URL
            line = pre+'/'+line
            ts_urls.append(line)

        new_lines.append(line)



    m3u8_content = '\n'.join(new_lines)
    #print(m3u8_content)
    newpath = os.path.abspath("m3u8")

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    new_m3u8_file = os.path.join(newpath, 'short_pilot.m3u8')
    print(new_m3u8_file)
    
    with open(new_m3u8_file, 'w') as f:
        f.write(m3u8_content)

    oss_file_key = f'longvideo/temp/{video_id}.m3u8'
    # upload_oss(new_m3u8_file, oss_file_key)
    return 'https://dfqapp.oss-cn-hongkong.aliyuncs.com/' + oss_file_key


res = getM3u8('https://uu.uqjh4.shop/hubal3asstd/vod/20220815/video/WH0P0V390A0944412723_eab8e27d5879471b9a9016d09fecdd34.mp4/index.m3u8', 't111881')
print(res)