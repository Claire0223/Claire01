#-*-coding:utf-8 -*-
'''class HobbyClass:
    def __init__(self,name,hobby):
        self.name=name
        self.hobby=hobby

    def Hobby(self):
        print ('%s,%s'%(self.name,self.hobby))

xiaoming=HobbyClass('小明','唱歌跳舞蹦沙卡拉卡')
xiaoming.Hobby()
xiaohong=HobbyClass('小红','抽烟喝酒纹身')
xiaohong.Hobby()'''
class Person:
    def __init__(self,name,sex,age,baseFi):
        self.name=name
        self.sex=sex
        self.age=age
        self.baseFi=baseFi

    def baseMessage(self):
        print ('%s,%s,%d,初始战斗力是%d'%(self.name,self.sex,self.age,self.baseFi))

    def grassFi(self):
        fight=self.baseFi-200
        print ('%s目前的战斗力是%d'%(self.name,fight))

    def practice(self):
        fight=self.baseFi+100
        print ('%s目前的战斗力是%d'%(self.name,fight))

    def incest(self):
        fight=self.baseFi-500
        print('%s目前的战斗力是%d'%(self.name,fight))

x1=Person('明世隐','男',12,3000)
x2=Person('公孙离','女',11,3500)
x3=Person('奕星','女',12,3500)
x4=Person('裴擒虎','男',11,4000)
x1.baseMessage()
x2.grassFi()
x3.practice()
x4.incest()

