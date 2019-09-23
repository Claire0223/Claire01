#coding=utf-8

#分支结构
'''
#英制单位与公制单位互换【1英寸=2.54厘米】
value=float(input('请输入长度:\n'))
unit=input('请输入单位:\n')
if unit=='厘米' or unit=='cm':
    print('%.2f厘米=%.2f英寸'%(value,value/2.54))
elif unit=='英寸' or unit=='in':
    print('%.2f英寸=%.2f厘米'%(value,2.54*value))
else:
    print('请输入正确的长度单位！')

#掷骰子决定做什么
from random import randint
face =randint(1,6)
if face ==1:
    result='买菜'
elif face ==2:
    result='做饭'
elif face==3:
    result='扫地'
elif face==4:
    result='洗碗'
elif face==5:
    result='拖地'
else:
    result='铺床单'
print (result)
'''



#输入三条边长如果能构成三角形就计算周长和面积
import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    area=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('这是三角形,其周长为%.2f,面积为%.2f'%(p,area))
else:
    print('这不是三角形!!')


