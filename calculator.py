def cal(a,b,opertn):
    return {
        '+':a+b,
        '/':a/b,
        '-':a-b,
        '*':a*b
    }.get(opertn)


index1 = int(input('输入第一值:'))
opertn = input('操作类型:')
index2 = int(input('输入第二个数值:'))

result = cal(index1,index2,opertn)

print('获取结果{0}{1}{2} = {3}'.format(index1,opertn,index2,result))