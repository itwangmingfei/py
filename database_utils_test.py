from database_utils import MySQLConnectionPool

host = "127.0.0.1"
port = 3306
user = "root"
password = "root"
database = "api_api"
mysql = MySQLConnectionPool(host,port,user,password,database)

"""
CREATE TABLE `names` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` VARCHAR(30) DEFAULT NULL COMMENT '姓名',
  `sex` VARCHAR(20) DEFAULT NULL COMMENT '性别',
  `age` int(5) DEFAULT NULL COMMENT '年龄',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='数据导入mysql';

"""

# sql = "select * from ms_member limit 1"
# getRow = mysql.select_one(sql)
# print(getRow)

# sql = "select id from ms_member limit 10"
# getlist = mysql.select_all(sql)
# print(getlist)

# mysql = MySQLConnectionPool()

# sql_insert_one = "insert into `names` (`name`, sex, age) values (%s,%s,%s)"
# mysql.insert_one(sql_insert_one, ('唐三', '男', 25))

# datas = [
#     ('戴沐白', '男', 26),
#     ('奥斯卡', '男', 26),
#     ('唐三', '男', 25),
#     ('小舞', '女', 100000),
#     ('马红俊', '男', 23),
#     ('宁荣荣', '女', 22),
#     ('朱竹清', '女', 21),
# ]
# sql_insert_all = "insert into `names` (`name`, sex, age) values (%s,%s,%s)"
# mysql.insert_all(sql_insert_all, datas)

# sql_update_one = "update `names` set age=%s where `name`=%s"
# mysql.update_one(sql_update_one, (28, '唐三'))

# sql_delete_one = 'delete from `names` where `name`=%s '
# mysql.delete_one(sql_delete_one, ('唐三',))

# sql_select_one = 'select * from `names` where `name`=%s'
# results = mysql.select_one(sql_select_one, ('小舞',))
# print(results)

# sql_select_all = 'select * from `names` where `name`=%s'
# results = mysql.select_all(sql_select_all, ('戴沐白',))
# print(results)