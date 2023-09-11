import time;
from datetime import datetime

middletime = int(time.time())

local = time.localtime()

struct = time.asctime(local)

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('日期：',date)
date1 = time.strftime("%Y-%m-%d ", time.localtime())
print('日期2', date1)

print('middletime:',middletime)

print('local:',local)

print('struct:',struct)

print('时间戳:',middletime)