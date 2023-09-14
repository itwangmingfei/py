import oss2
from config import ossconfig


access_key_id = ossconfig['access_key_id']
access_key_secret = ossconfig['access_key_secret']
endpoint = ossconfig['endpoint']
bucket_name = ossconfig['bucket_name']

class oss_upload:    
    def __init__(self,access_key_id=access_key_id,access_key_secret=access_key_secret,endpoint=endpoint,bucket_name=bucket_name):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret 
        self.endpoint = endpoint 
        self.bucket_name = bucket_name

    def upload_oss(self,local_file_path, oss_file_key):        
        # 创建 OSS 客户端
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(self.auth, endpoint, self.bucket_name)
        print(bucket)
        res = bucket.put_object_from_file(oss_file_key, local_file_path)
        return res


# oss = oss_upload()
# oss.upload_oss(1,2)