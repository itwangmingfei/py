from datetime import datetime, timedelta

today = datetime.now()
one_day = timedelta(days=1)
tomorrow = today + one_day

print("今天:", today)
print("明天:", tomorrow)


date_str = "2023-09-15 14:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

print("解析的日期:", date_obj)


# 时间处理 逻辑
current_datetime = datetime.now()
today_start = current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
# 时间戳
today_time = int(today_start.timestamp())

print("今天的开始时间:", today_start)
print('今日时间戳',today_time)

# 执行时间运算 中间件
one_day = timedelta(days=-1)

print(one_day)

# 获取新时间   运算
get_day = today_start + one_day

print("获取的新时间 {}".format(get_day))