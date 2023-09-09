
def checkNumber(number):
    if number%2 == 0 :
        print('可以被2整除')
    else:
        print('不可以整除')


input = int(input('请输入一个数字:'))

checkNumber(input)