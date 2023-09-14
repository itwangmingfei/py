import pymysql
def do_db(sql):
    # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
    # db = pymysql.connect(
    #     user='api_api',  # 用户名
    #     password='JNjALHPJz87SpfSn#',  # 密码：这里一定要注意123456是字符串形式
    #     host='52.192.56.159',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
    #     database='api_api',  # 数据库的名字
    #     port=6734,  # 指定端口号，范围在0-65535
    #     charset='utf8mb4',  # 数据库的编码方式
    # )
    db = pymysql.connect(
        user='api_api',  # 用户名
        password='JNjALHPJz87SpfSn',  # 密码：这里一定要注意123456是字符串形式
        host='16.162.114.9',  # 指定访问的服务器，本地服务器指定“localhost”，远程服务器指定服务器的ip地址
        database='api_api',  # 数据库的名字
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
def do_db2(sql):
    # 接着我们获取 cursor 来操作我们的 avIdol 这个数据库
    db = pymysql.connect(
        user='source',  # 用户名
        password='jj',  # 密码：这里一定要注意123456是字符串形式
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

sql = "select video_id,url from ms_video where url like '%/longvideo/%' and origin='lutube'"
res = do_db(sql)

if(res['num']>1):
    for row in res['cursor']:
        print(row[0])
        sql2 = f"select video_id,url from ms_video where video_id='{row[0]}'"
        print(sql2)
        res2 = do_db2(sql2)
        if(res2['num']>=1):
            row = res2['cursor'].fetchone()
            video_id = row[0]
            url = row[1]
            update_sql = f"update ms_video set url='{url}' where video_id = '{video_id}';"
            with open('C:/video_long.sql', "a", encoding="utf-8") as file:
                file.write(update_sql + "\n")
        else:
            with open('C:/error_long.txt', "a", encoding="utf-8") as file:
                file.write(sql2 + "\n")
            print('not found')