import pymysql

from config import db_api,db_source

class DB:
    def __init__(self) -> None:
        pass

    def apimodel(self,sql):
         # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
        db = pymysql.connect(
            user= db_api['user'],  # 用户名
            password= db_api['password'],  # 密码：这里一定要注意123456是字符串形式
            host= db_api['host'],  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
            database= db_api['database'],  # 数据库的名字
            port= db_api['port'],  # 指定端口号，范围在0-65535
            charset='utf8mb4',  # 数据库的编码方式
        )
        cursor = db.cursor()
        try:
            num = cursor.execute(sql)
            result = {'num':num,'cursor':cursor}
            db.commit()
        except Exception as e:
            print(e)
            # 回滚
            db.rollback()
        # 最后我们关闭这个数据库的连接
        db.close()
        
        return result

    def sourceModel(self,sql):
         # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
        db = pymysql.connect(
            user= db_source['user'],  # 用户名
            password= db_source['password'],  # 密码：这里一定要注意123456是字符串形式
            host= db_source['host'],  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
            database= db_source['database'],  # 数据库的名字
            port= db_source['port'],  # 指定端口号，范围在0-65535
            charset='utf8mb4',  # 数据库的编码方式
        )
        cursor = db.cursor()
        try:
            num = cursor.execute(sql)
            result = {'num':num,'cursor':cursor}
            db.commit()
        except Exception as e:
            print(e)
            # 回滚
            db.rollback()
        # 最后我们关闭这个数据库的连接
        db.close()   
        return result


# sql = "select * from ms_video limit 2"
# mysql = model()
# res = mysql.sourceModel(sql)
# print(res['cursor'].fetchone())