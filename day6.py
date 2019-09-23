#coding=utf-8
#函数与模块的使用

#实现计算求最大公约数和最小公倍数的函数
def gcd(x,y):
    if x>y:
        (x,y)=(y,x)
    else:
        (x,y)
    for factor in range(x,0,-1):
        if x % factor==0 and y % factor ==0:
            return factor

def lcm(a,b):
    return a*b//gcd(a,b)

test=gcd(6,8)
print(test)
test1=lcm(6,8)
print(test1)


