import os


def make_dir(Path,folder_name):
    """
    新建套图文件夹并切换到该目录下
    """
    path = os.path.join(Path, folder_name)
    # 如果目录已经存在就不用再次爬取了，去重，提高效率。存在返回 False，否则反之
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
        os.chdir(path)
        return path
    print("Folder has existed!")
    return Path+'/'+folder_name

def delete_empty_dir(save_dir):
    print(save_dir)
    """
    如果程序半路中断的话，可能存在已经新建好文件夹但是仍没有下载的图片的
    情况但此时文件夹已经存在所以会忽略该套图的下载，此时要删除空文件夹
    """
    if os.path.exists(save_dir):
        if os.path.isdir(save_dir):
            for d in os.listdir(save_dir):
                path = os.path.join(save_dir, d)     # 组装下一级地址
                if os.path.isdir(path):
                    delete_empty_dir(path)      # 递归删除空文件夹
        if not os.listdir(save_dir):
            os.rmdir(save_dir)
            print("remove the empty dir: {}".format(save_dir))
    else:
        print("Please start your performance!")     # 请开始你的表演

################################
path = "./img"

 
for d in os.listdir(path):
    print('获取文件目录：{}'.format(d))

folder_name = "aa"

filepath = make_dir(path,folder_name)

print("检测文件：{}".format(os.path.isdir(filepath)))

filename = os.path.join(filepath,'b.log') 

print("检测文件log：{}".format(os.path.isdir(filename)))


print("获取文件路径",filename)


with open(filename,'w') as f:
    f.write('vvvvv')

# 执行数据删除
delete_empty_dir(filepath)