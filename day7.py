#coding=utf-8
#在屏幕上显示跑马灯文字
'''
import os
import time
def main():
    content='好好学习，天天向上!'
    while True:
        os.system('cls')#清屏
        print(content)
        content=content[1:]+content[0]#将字符串中第一个元素移到了最后一个
        time.sleep(0.5) #滚动速度
if __name__=='__main__':#类的检测方法
    main()


#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random
import string
def generate_code():
    long = int(input('请输入验证码的长度:\n'))
    str=''
    for i in range(long):
        str=str+random.choice(string.ascii_letters + string.digits)
    print (str)
    return str

def time():
    strx=generate_code()#获取generate_code里面的str
    num=0
    letter=0
    for i in strx:
        if i in string.ascii_letters:
            letter += 1
        else :
                num += 1
    print ('一共有%d个数字'%num)
    print('一共有%d个英文字符' % letter)
time()



#设计一个函数返回给定文件名的后缀名。
def get_filename(filename,has_dot=False):
    pos=filename.rfind('.',0)
#返回的后缀名是否需要带点
    if 0<pos<len(filename)-1:
       """三元运算:
            如果条件为真，返回真，否则返回假
            condition_is_true if condition else condition_is_false
            ==>is_fat=True
            ==>state='fat' if is_fat else "not fat"
        """
        index=pos if has_dot else pos+1  #位置索引//
        return filename[index:]
    else:
        return 'nothing'
x=get_filename('xyq.tag.gz')
print (x)




#计算指定的年月日是这一年的第几天
#判断是否是闰年
#月份划分天数
def is_leap_year(year):
    #闰年
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
def which_day(year,month,date):
    day_of_month=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
    type=is_leap_year(year)
    days=day_of_month[1] if type else day_of_month[0]
    totle=0
    for x in range(month-1):
        totle+=days[x]
    return totle+date

year=int(input('请输入年份:'))
month = int(input('请输入月份:'))
date = int(input('请输入第几天:'))
result=which_day(year,month,date)
print('这是%d年的第%d天'%(year,result))
'''


#双色球选号




#约瑟夫环问题
"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，
由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()