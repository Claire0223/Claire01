#coding=utf-8
'''
#寻找所有的水仙花
#水仙花：一个三位数，它的每个位上的数字的3次幂之和等于它本身
#pow(x,y) 返回x的y次方
import math
list=[]
for i in range(100,1000):
    a=int(i/100)
    b=int(i%100/10)
    c=int(i%10)
    num=math.pow(a,3)+math.pow(b,3)+math.pow(c,3)
    if num==i:
        list.append(i)
print('一共%d朵水仙花'%len(list))
print(list)


#寻找完美数
list=[]
for i in range(1,1001):
    k=0
    for j in range(1,i):
        if(i%j==0):
            k+=j
    if i==k:
        list.append(i)
print (list)


'''
#craps赌博游戏
#玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，
# 则玩家输庄家胜。若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
import random
x=random.randint(1,7)
y=random.randint(1,7)
first=x+y
if first==7 or first==11:
    print('玩家获胜。')
    print(x,y,first)
elif first==2 or first==3 or first==12:
        print('庄家获胜。')
        print(x, y, first)
else:
    while True:
        x = random.randint(1, 7)
        y = random.randint(1, 7)
        sum = x + y
        if sum==first:
            print('玩家获胜。')
            print(x, y, first,sum)
            break
        else :
            if sum==7:
                print('庄家获胜')
                print(x, y, first,sum)
                break
            else:
                continue






