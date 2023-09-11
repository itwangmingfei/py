import os

abspath = os.path.abspath('img')

print("获取绝对路径：{}".format(abspath))

#返回 文件夹下对应的数据信息
for root, dirs, files in os.walk(abspath):
    print(files)

 