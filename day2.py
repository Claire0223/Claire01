#coding=utf-8

#运算符

'''
#将华氏温度转为摄氏温度
#F=1.8C+32
f=float(input('请输入华氏温度:\n'))
c=(f-32)/1.8
print('%.1f 华氏度=%.1f摄氏度'%(f,c))




#输入圆的半径，计算周长和面积
import math
radius=float(input('请输入半径：\n'))
perimeter=2*math.pi*radius
area=math.pi*radius*radius
print('周长为%.2f,面积为%.2f'%(perimeter,area))
'''

#输入的年份是否为闰年
year=int(input('请输入年份:\n'))
if (year % 4==0 and year %100 !=0 or year %400==0):
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)