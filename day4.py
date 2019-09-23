#coding=utf-8
'''
#判断是否为素数
import math
num=int(input('请输入一个大于1的正整数:\n'))
if num <= 1:
    print('输入的数字应大于1！')
else:
    end=int(math.sqrt(num))
    flag=True
    for x in range(2,end+1):
        if num%x==0:
            flag=False
            break
    if flag:
        print('%d是素数'%num)
    else:
        print('%d不是素数'%num)




#打印三角形图案-打印各种三角形图案
#左对齐，右对齐，居中
row=int(input('输入行数:\n'))
for i in range(row):
    for j in range(row):
        if j<row-i-1:
            print(' ',end='')
        else:
            print('*',end="")
    print()

for i in range(row):
    for x in range(i+1):
        print('*',end="")
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
'''
#猜数字
import random
num=random.randint(1,101)
time=0
while True:
    guess=int(input('请输入你猜测的数字:\n'))
    time = time + 1

    if guess>num:
        print('猜错啦！你输入的数字大了一点点哦。')

    elif guess<num:
        print('猜错啦！你输入的数字小了一点点哦。')

    else:
        print('你猜中啦！')
        break
print('你总共猜了%d次'%time)
if time>7:
    print('智商该充值啦！')
else:
    print('棒棒哒~')


