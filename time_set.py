import time;


middletime = time.time()

local = time.localtime()

struct = time.asctime(local)

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print('日期：',date)

print('middletime:',middletime)

print('local:',local)

print('struct:',struct)
